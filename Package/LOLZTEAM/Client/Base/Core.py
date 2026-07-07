"""
API Client core
"""
import re
import time
import json
import base64
import logging
import asyncio

from typing import Union, Literal
from dataclasses import dataclass
from binascii import Error as binasciiError
from urllib.parse import parse_qs, urlparse
from curl_cffi import AsyncSession, Response
from ..Base.Wrappers import RETRY, UNIVERSAL
from importlib.metadata import version, PackageNotFoundError
from ..Base.Exceptions import BAD_TOKEN, BAD_ENDPOINT, EXPIRED_TOKEN


class APIClient:
    """
    Base API Client class
    """

    def __init__(self, base_url: str, token: str, language: str = None, logger_name: str = "APIClient", proxy: str = None, timeout: float = 90, verify: bool = True):
        self.core = self
        from ..__init__ import Antipublic  # Circular import issue
        self.settings = Settings(core=self)
        self.settings._isAntipublic = isinstance(self, Antipublic)
        self.settings.async_client = AsyncSession(timeout=timeout, verify=verify)
        self.settings.delay = AutoDelay()
        self.settings.logger = Logger(core=self, logger_name=logger_name)
        self.settings.current_loop = asyncio.get_event_loop()
        self.settings.token = token
        self.settings.language = language
        self.settings.proxy = proxy
        self.settings.base_url = base_url

        try:
            self.settings.version = version("LOLZTEAM")
        except PackageNotFoundError:
            self.settings.version = "2.2.x"
        if self.settings._isAntipublic:
            self.settings.async_client.headers.update({"x-antipublic-version": f"{self.settings.version} (API Client) pypi.org/project/LOLZTEAM/"})

        self.settings.async_client.headers.update({"User-Agent": f"Python (API Client) pypi.org/project/LOLZTEAM/ v{self.settings.version}"})

    async def __get_async_client(self: "APIClient") -> AsyncSession:
        current_loop = asyncio.get_event_loop()
        if current_loop != self.settings.current_loop:
            client_params = {
                "headers": self.settings.async_client.headers,
                "timeout": self.settings.async_client.timeout,
                "base_url": self.settings.async_client.base_url,
                "verify": self.settings.async_client.verify,  # TODO: Add verify as changeable parameter to settings?
                "proxies": self.settings.async_client.proxies
            }
            self.settings.async_client = AsyncSession(**client_params)
            self.settings.proxy = self.settings.proxy
            self.settings.current_loop = current_loop
        return self.settings.async_client

    @UNIVERSAL(batchable=True)
    @RETRY(count=25)
    async def request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ) -> Response:
        """
        Send request

        **Parameters:**
        - `method`: Request method. Example: `GET`, `POST`, `PUT`, `DELETE`
        - `endpoint`: Request endpoint. Example: `/users/items/`
        - `**kwargs`: Request parameters.

        **Example:**

        ```python
        response = client_name.request(method="GET", endpoint="/users/items/", params={"user_id": 2410024})
        print(response.json())
        ```
        """
        if not (endpoint.startswith('/') or endpoint.startswith(f"{self.settings.base_url}/")):  # Check for valid endpoint to prevent token leaks and other shit
            raise BAD_ENDPOINT(f"You can't send request to \"{endpoint}\" because it's domain is different from \"{self.settings.base_url}\"")
        parsed_url = urlparse(endpoint)
        endpoint = parsed_url.path or "/"
        bucket = None
        for _bucket in self.settings.delay.buckets._list:
            if method.upper() in _bucket.methods and re.search(_bucket.url_pattern, endpoint):
                bucket = _bucket
                break
        await self.settings.delay.asleep(bucket)  # Sleep if needed

        if not kwargs.get("params"):
            kwargs["params"] = {}
        kwargs["params"] = _NONE.TrimNONE(kwargs["params"])
        if kwargs.get("data"):
            kwargs["data"] = _NONE.TrimNONE(kwargs["data"])
        if kwargs.get("json"):
            kwargs["json"] = _NONE.TrimNONE(kwargs["json"])

        if parsed_url.query:  # Fix params collision
            parsed_params = {
                k: v[0] if len(v) == 1 and not k.endswith('[]') else v
                for k, v in parse_qs(parsed_url.query).items()
            }
            for k, v in parsed_params.items():
                if k not in kwargs["params"]:  # User params will override url params
                    kwargs["params"][k] = v

        if parsed_url.path != endpoint:
            endpoint = parsed_url.path

        for k, v in kwargs["params"].copy().items():
            if isinstance(v, (list, tuple)) and not k.endswith("[]"):  # Parse list params
                kwargs["params"][f"{k}[]"] = v
                del kwargs["params"][k]
            elif isinstance(v, dict):                                  # Parse dict params
                for kk, vv in v.items():
                    kwargs["params"][f"{k}[{kk}]"] = vv
                del kwargs["params"][k]

        if self.settings.language and not kwargs["params"].get("locale"):  # Add locale to requests
            kwargs["params"]["locale"] = self.settings.language
        client = await self.__get_async_client()

        def mask(obj, mask_: dict[str, str]):  # TODO: Implement pattern replacement instead of that shit
            if isinstance(obj, dict) and mask_:
                obj = obj.copy()
                for k, v in mask_.items():
                    if k in obj.keys():
                        obj[k] = v
            return obj

        # TODO 2.1.1: Add option to log only errors
        self.settings.logger.info(
            "\n".join(
                filter(None,
                       [
                           f"Request:  {method} {endpoint}",
                           f"Headers: {mask(obj=dict(client.headers), mask_={'authorization': 'Bearer ****************'})}",
                           f"Params: {mask(obj=kwargs.get('params', {}), mask_={'secret_answer': '********'})}",
                           f"Data: {json.dumps(mask(obj=kwargs.get('data', {}), mask_={'secret_answer': '********'}))}" if kwargs.get('data') else None,
                           f"Json: {json.dumps(mask(obj=kwargs.get('json', {}), mask_={'secret_answer': '********'}))}" if kwargs.get('json') else None,
                           #    f"File: {kwargs.get('files')}" if kwargs.get('files') else None
                       ]
                       )
            )
        )

        response = await client.request(method, endpoint, **kwargs)
        self.settings.logger.info(f"Response: {method} {endpoint} -> {response.status_code}:\n{response.text}")
        async with bucket.lock:
            new_rl = response.json().get("system_info", {}).get("rate_limit", {}).get("remaining")
            bucket.requests_remaining = new_rl if new_rl is not None else bucket.requests_remaining
        if endpoint == "/batch":
            jobs = kwargs.get("json", [])
            for job in jobs[:10]:
                job_endpoint = job.get("uri")
                job_method = job.get("method", "GET")
                if not job_endpoint:
                    continue

                parsed_job_url = urlparse(job_endpoint)
                job_path = parsed_job_url.path if parsed_job_url.path else job_endpoint
                job_bucket = None
                for bucket in self.settings.delay.buckets._list:
                    if re.search(bucket.url_pattern, job_path) and job_method in bucket.methods:
                        job_bucket = bucket
                        break
                async with job_bucket.lock:
                    if job_bucket and job_bucket.requests_remaining > 0:
                        bucket.requests_remaining -= 1
        return response


class Buckets:
    @dataclass
    class Bucket:
        requests_limit: int
        requests_remaining: int
        reset_time: int
        name: Union[str, None]
        url_pattern: Union[str, None] = None
        methods: tuple[str, ...] = ("GET", "POST", "PUT", "DELETE")
        lock: asyncio.Lock = None

    _first_reset_time = ((time.time() // 60) + 1) * 60

    # Market
    LETTERS = Bucket(requests_limit=5, requests_remaining=5, reset_time=_first_reset_time, name="letters", url_pattern=r"/letters2?$", methods=("GET"), lock=asyncio.Lock())
    EDIT = Bucket(requests_limit=1000, requests_remaining=1000, reset_time=_first_reset_time, name=None, url_pattern=r"/edit$", methods=("PUT"), lock=asyncio.Lock())
    CONFIRM_BUY = Bucket(requests_limit=1000, requests_remaining=1000, reset_time=_first_reset_time, name=None, url_pattern=r"/confirm-buy$", methods=("POST"), lock=asyncio.Lock())
    CHECK_ACCOUNT = Bucket(requests_limit=300, requests_remaining=300, reset_time=_first_reset_time, name="check-account", url_pattern=r"/(?:fast-sell|fast-buy|check-account|goods-check)$", methods=("POST"), lock=asyncio.Lock())
    SEARCH = Bucket(requests_limit=120, requests_remaining=120, reset_time=_first_reset_time, name="search", url_pattern=r"^/(?:steam|fortnite|mihoyo|riot|telegram|supercell|ea|world-of-tanks|wot-blitz|gifts|epicgames|escape-from-tarkov|socialclub|uplay|discord|tiktok|instagram|battlenet|llm|vpn|roblox|warface|minecraft|hytale)(?:/(?:params|games))?$|^/user/items$|^/[0-9]+$", methods=("GET"), lock=asyncio.Lock())
    DELETE = Bucket(requests_limit=300, requests_remaining=300, reset_time=_first_reset_time, name=None, url_pattern=r"/delete$", methods=("DELETE"), lock=asyncio.Lock())
    EMAIL_CODE = Bucket(requests_limit=300, requests_remaining=300, reset_time=_first_reset_time, name=None, url_pattern=r"/email-code$", methods=("POST"), lock=asyncio.Lock())

    # Shared Forum/market
    BATCH = Bucket(requests_limit=20, requests_remaining=20, reset_time=_first_reset_time, name="batch", url_pattern=r"^/batch$", methods=("POST",), lock=asyncio.Lock())
    GET = Bucket(requests_limit=300, requests_remaining=300, reset_time=_first_reset_time, name=None, url_pattern=r".*", methods=("GET",), lock=asyncio.Lock())
    NONGET = Bucket(requests_limit=30, requests_remaining=30, reset_time=_first_reset_time, name=None, url_pattern=r".*", methods=("POST", "PUT", "DELETE"), lock=asyncio.Lock())
    _list = [
        LETTERS,
        EDIT,
        CONFIRM_BUY,
        CHECK_ACCOUNT,
        SEARCH,
        DELETE,
        EMAIL_CODE,
        BATCH,
        GET,
        NONGET,
    ]


class AutoDelay:
    """
    Auto delay
    """

    def __init__(self, enabled: bool = True):
        self._enabled = enabled
        self.buckets = Buckets
        self.synced = False

    async def asleep(self, bucket: Buckets.Bucket):
        """
        Sleep if delay is needed
        """
        if not self._enabled:
            return
        current_time = time.time()
        
        if bucket.requests_remaining == 0:
            async with bucket.lock:
                await asyncio.sleep(bucket.reset_time - current_time)
                bucket.reset_time = ((current_time // 60) + 2) * 60
        elif current_time >= bucket.reset_time:
            async with bucket.lock:
                bucket.reset_time = ((current_time // 60) + 1) * 60
                bucket.requests_remaining = bucket.requests_limit
        return

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    @property
    def enabled(self) -> bool:
        return self._enabled

    def sync(self, client: Union["APIClient", "AutoDelay"]):
        if isinstance(client, AutoDelay):
            autodelay = client
        elif isinstance(client, APIClient):
            autodelay = client.settings.delay
        else:
            raise TypeError("Invalid client type: expected APIClient or AutoDelay")
        autodelay.buckets = self.buckets
        if not self.synced:
            self.synced = True


class Logger:
    """
    Logger
    """

    def __init__(self, core: APIClient, logger_name: str, enabled: bool = False):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        self.logger_name = logger_name
        self.core = core

        # TODO: Also may add parsing user_id from response when endpoints is /checkAccess
        if not self.core.settings._isAntipublic:
            self.file_name = f"{self.core.settings.user_id}.{self.logger_name}.log"
        else:
            self.file_name = f"{self.logger_name}.log"
        self.__enabled = enabled

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    def enable(self):
        """
        Start logging
        """
        if not self.__enabled:
            file_handler = logging.FileHandler(self.file_name, encoding="utf-8")
            file_handler.setFormatter(self.formatter)
            self.logger.addHandler(file_handler)
            self.__enabled = True
            if not self.core.settings._isAntipublic:
                self.logger.info(f"Logger started | User ID: {self.core.settings.user_id} | JTI: {self.core.settings.jti} | Scopes: {self.core.settings.scopes}")
            else:
                self.logger.info("Logger started")

    def disable(self):
        """
        Stop logging
        """
        if self.__enabled:
            if not self.core.settings._isAntipublic:
                self.logger.info(f"Logger stopped | User ID: {self.core.settings.user_id} | JTI: {self.core.settings.jti} | Scopes: {self.core.settings.scopes}")
            else:
                self.logger.info("Logger stopped")
            for handler in self.logger.handlers:
                # TODO: Try to catch exceptions when closing handler?
                handler.close()
            self.logger.handlers = []
            self.__enabled = False

    @property
    def enabled(self) -> bool:
        return self.__enabled

    def info(self, message: str):
        """
        Log info message
        """
        if self.__enabled:
            self.logger.info(message)

    def error(self, message: str):
        """
        Log error message
        """
        if self.__enabled:
            self.logger.error(message)


@dataclass
class Settings:
    """
    Settings for API Client
    """
    version: str
    """
    API Client Package Version.
    """
    _isAntipublic: str

    async_client: AsyncSession

    """
    Async curl_cffi client.
    """
    language: Literal["ru", "en"]
    """
    API response language.
    Default is same as set in web.
    """
    current_loop: asyncio.AbstractEventLoop
    """
    Current asyncio event loop.
    """
    delay: AutoDelay
    """
    Delay instance.

    Used for eeping between requests to avoid 429 status code aka rate limit.
    """
    logger: Logger
    """
    Logger. Just logger.

    He logging things if you want.
    """

    user_id: int = None
    """
    Your LZT/Antipublic user ID.
    """
    scopes: list[str] = None
    """
    Your token scopes.
    """
    jti: int = None
    """
    Your token ID.
    """
    _token: str = None
    _base_url: str = None
    _proxy: str = None

    def __init__(self, core: APIClient):
        self.core = core

    @property
    def base_url(self) -> str:
        """
        Base URL for API requests.
        """
        return self._base_url

    @base_url.setter
    def base_url(self, url: str) -> None:
        self._base_url = url
        self.async_client.base_url = url

    @property
    def proxy(self) -> dict:
        """
        Your proxy.
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy: str) -> None:
        """
        Set proxy

        ```
        client.proxy = "socks5://proxy_name:proxy_password@proxy_ip:proxy_port"
        ```
        """
        if proxy and not any(proxy.startswith(p) for p in ["http://", "https://", "socks5://", "socks5://"]):
            raise ValueError("Proxy must start with http://, https://, socks5:// or socks5h://")
        self._proxy = proxy
        self.async_client.proxies = {"all": proxy}

    @property
    def token(self) -> str:
        """
        Your LZT/Antipublic token.
        """
        return self._token

    @token.setter
    def token(self, token: str) -> None:
        self._token = token
        if self._isAntipublic:
            self.async_client.headers.update({"authorization": f"Bearer {self._token}"})
            self.user_id = None
            # TODO: Unify this shit when legacy tokens will gone. Also don't forget to edit logger stuff.
            # Legacy tokens are gone but `sub` in jwt doesn't match with lzt user_id, so ig ignore this for now. Putting random antipublic subject id will confuse users
        self.scopes = None
        self.jti = None
        self.async_client.headers.update({"authorization": f"Bearer {self._token}"})
        try:
            if "." not in self._token:
                raise BAD_TOKEN("Your token is invalid. You must check if you have pasted your token fully or create new token and use it instead (https://lolz.live/account/api).")
            payload = token.split(".")[1]
            decoded_payload: dict = json.loads(base64.b64decode(payload + "==" if payload[-2:] != "==" else payload).decode("utf-8"))
            if decoded_payload.get("exp", 9999999999) < time.time():
                raise EXPIRED_TOKEN("Your token has expired. Please get a new token here -> https://lolz.live/account/api")
            self.user_id = decoded_payload.get("sub", 0)
            self.logger.file_name = f"{self.user_id}.{self.logger.logger_name}.log"
            self.jti = decoded_payload.get("jti", 0)
            self.scopes = decoded_payload.get("scope", "").split(" ")
            self.logger.info(f"Updated Token | User ID: {self.user_id} | JTI: {self.core.settings.jti}" + (f"| Scopes: {self.core.settings.scopes}" if not self._isAntipublic else ""))
        except (binasciiError, json.JSONDecodeError) as e:
            raise BAD_TOKEN("Your token is invalid. You must check if you have pasted your token fully or create new token and use it instead (https://lolz.live/account/api).") from e


class _NONE:
    """
    None placeholder for methods and function to trim it from params
    """

    @staticmethod
    def TrimNONE(obj: Union[dict, list]) -> Union[dict, list]:
        """
        Trim NONE from any object
        """
        if isinstance(obj, dict):
            for key, value in obj.copy().items():
                if isinstance(value, _NONE):
                    obj.pop(key)
                elif isinstance(value, (dict, list)):
                    obj[key] = _NONE.TrimNONE(value)
        elif isinstance(obj, (list)):
            for value in obj.copy():
                if isinstance(value, _NONE):
                    obj.remove(value)
                elif isinstance(value, (dict, list)):
                    obj[obj.index(value)] = _NONE.TrimNONE(value)
        return obj


NONE = _NONE()

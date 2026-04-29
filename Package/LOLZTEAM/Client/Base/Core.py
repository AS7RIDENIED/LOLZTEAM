"""
API Client core
"""
import time
import json
import base64
import logging
import asyncio

from functools import wraps
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

    def __init__(self, base_url: str, token: str, language: str = None, delay_min: float = 0, logger_name: str = "APIClient", proxy: str = None, timeout: float = 90, verify: bool = True):
        self.core = self
        from ..__init__ import Antipublic  # Circular import issue
        self.settings = Settings(core=self)
        self.settings._isAntipublic = isinstance(self, Antipublic)
        self.settings.async_client = AsyncSession(timeout=timeout, verify=verify)  # TODO: Maybe replace my autoretry with this one from curl_cffi
        self.settings.delay = AutoDelay(delay_min=delay_min)
        self.settings.logger = Logger(core=self, logger_name=logger_name)
        self.settings.current_loop = asyncio.get_event_loop()
        self.settings.token = token
        self.settings.language = language
        self.settings.proxy = proxy
        self.settings.base_url = base_url

        try:
            self.settings.version = version("LOLZTEAM")
        except PackageNotFoundError:
            self.settings.version = "2.1.0"
        if self.settings._isAntipublic:
            self.settings.async_client.headers.update({"x-antipublic-version": f"{self.settings.version} (API Client) pypi.org/project/LOLZTEAM/"})

        self.settings.async_client.headers.update({"User-Agent": f"Python (API Client) pypi.org/project/LOLZTEAM/ v{self.settings.version}"})

    async def __get_async_client(self: "APIClient") -> AsyncSession:
        current_loop = asyncio.get_event_loop()
        if current_loop != self.settings.current_loop:
            try:
                await self.settings.async_client.close()
            except RuntimeError:
                pass
            client_params = {
                "headers": self.settings.async_client.headers,
                "timeout": self.settings.async_client.timeout,
                "base_url": self.settings.async_client.base_url,
                "verify": self.settings.async_client.verify,  # TODO: Add verify as changeable parameter to settings?
                "proxy": self.settings.proxy
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
        delay: float = None,
        **kwargs
    ) -> Response:
        """
        Send request

        **Parameters:**
        - `delay`: Delay in seconds.
        - `method`: Request method. Example: `GET`, `POST`, `PUT`, `DELETE`
        - `endpoint`: Request endpoint. Example: `/users/items/`
        - `**kwargs`: Request parameters.

        **Example:**

        ```python
        response = client_name.request(method="GET", endpoint="/users/items/", params={"user_id": 2410024})
        print(response.json())
        ```
        """
        if delay:
            self.settings.delay._delay = delay  # Set delay
        await self.settings.delay.asleep()  # Sleep if needed

        if not kwargs.get("params"):
            kwargs["params"] = {}
        if endpoint.startswith(self.settings.base_url.replace("prod-api.", "").replace("api.", "")):  # Remove baseurl from endpoint path
            endpoint = endpoint.replace(self.settings.base_url.replace("prod-api.", "").replace("api.", ""), "")
        if not (endpoint.startswith('/') or endpoint.startswith(f"{self.settings.base_url}/")):  # Check for valid endpoint to prevent token leaks and other shit
            raise BAD_ENDPOINT(f"You can't send request to \"{endpoint}\" because it's domain is different from \"{self.settings.base_url}\"")

        kwargs["params"] = _NONE.TrimNONE(kwargs["params"])
        if kwargs.get("data"):
            kwargs["data"] = _NONE.TrimNONE(kwargs["data"])
        if kwargs.get("json"):
            kwargs["json"] = _NONE.TrimNONE(kwargs["json"])

        parsed_url = urlparse(endpoint)
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
        self.settings.delay._last_request_time = asyncio.get_event_loop().time()
        return response


class AutoDelay:
    """
    Auto delay
    """

    def __init__(self, delay_min: float = 0, enabled: bool = True):
        self._enabled = enabled
        self._delay = 0.2
        self._delay_min = delay_min
        self._last_request_time = 0

    @UNIVERSAL()
    async def asleep(self):
        """
        Sleep if delay is needed
        """
        if not self._enabled:
            return
        loop = asyncio.get_event_loop()
        current_time = loop.time()
        time_passed = current_time - self._last_request_time
        if time_passed >= self._delay:
            return
        calculated_delay = min(self._delay - time_passed, self._delay)
        if calculated_delay < self._delay_min:
            calculated_delay = self._delay_min
        await asyncio.sleep(calculated_delay)

    @staticmethod
    def WrapperSet(seconds: float):
        """
        Decorator for setting delay on method
        """
        # TODO: Maybe delete this. There is only one method in the entire API that has a different delay.
        def decorator(func):
            @wraps(func)
            async def wrapper(self, *args, **kwargs):
                self.core.settings.delay._delay = seconds
                return await func(self, *args, **kwargs)
            return wrapper
        return decorator

    def get(self) -> float:
        """
        Get delay
        """
        return self._delay

    def set(self, delay: float) -> None:
        """
        Set custom delay

        P.s This delay will be overwrited when you run any function from API Client.
        """
        self._delay = delay

    @property
    def min(self) -> float:
        """
        Get minimal delay
        """
        return self._delay_min

    @min.setter
    def min(self, delay: float):
        """
        Set minimal delay

        P.s This delay will NOT be overwrited when you run any function from API Client BUT that's a minimal delay, so performance can be downgraded.
        """
        self._delay_min = delay

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    @property
    def enabled(self) -> bool:
        return self._enabled


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

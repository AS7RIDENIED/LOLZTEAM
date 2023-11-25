import requests
import aiohttp
import inspect


class AntipublicApi:
    def __init__(self, token: str = None, proxy_type: str = None, proxy: str = None):
        """
        :param token: Your token. You can get in there -> https://zelenka.guru/account/antipublic or in antipublic app
        :param proxy_type: Your proxy type. You can use types ( Types.Proxy.socks5 or socks4,https,http )
        :param proxy: Proxy string. Example -> ip:port or login:password@ip:port
        """
        self.base_url = "https://antipublic.one"
        if proxy_type is not None:
            proxy_type = proxy_type.upper()
            if proxy_type in ["HTTPS", "HTTP", "SOCKS4", "SOCKS5"]:
                self.__proxy_type = proxy_type
                self.__proxy = proxy
            else:
                raise Exception(f"Proxy type has invalid value. It can be only https,http,socks4 or socks5")
        else:
            self.__proxy = None
            self.__proxy_type = None

        self.__token = token

        self.info = self.__Info(self)
        self.account_info = self.__AccountInfo(self)

    def send_request(self, method: str, path: str, params: dict = None, data=None, files=None):
        url = self.base_url + path
        method = method.upper()
        # AntipublicApi.__auto_delay(self)
        if params is None:
            params = {}
        if self.__token is not None:
            params["key"] = f"{self.__token}"
        proxies = {}
        if self.__proxy_type is not None:
            if self.__proxy_type == "HTTP":
                proxies = {
                    "http": f"http://{self.__proxy}",
                    "https": f"http://{self.__proxy}"
                }
            elif self.__proxy_type == "HTTPS":
                proxies = {
                    "http": f"http://{self.__proxy}",
                    "https": f"https://{self.__proxy}"
                }
            if self.__proxy_type == "SOCKS4":
                proxies = {
                    "http": f"socks4://{self.__proxy}",
                    "https": f"socks4://{self.__proxy}"
                }
            if self.__proxy_type == "SOCKS5":
                proxies = {
                    "http": f"socks5://{self.__proxy}",
                    "https": f"socks5://{self.__proxy}"
                }
            else:
                raise Exception(
                    f"Proxy type has invalid value. It can be only https,http,socks4 or socks5")  # How tf you get that error?
        response = requests.request(method=method, url=url, params=params, data=data, files=files, proxies=proxies)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return response.text

    async def send_async_request(self, method: str, path: dict, params: dict = None, data=None):
        url = self.base_url + path
        method = method.upper()
        if params is None:
            params = {}
        params["key"] = f"{self.__token}"
        ptd = []
        for key, value in params.items():
            if params[key] is None:
                ptd.append(key)
        for key in ptd:
            del params[key]
        proxy_schemes = {
            "HTTP": "http",
            "HTTPS": "https",
            "SOCKS4": "socks4",
            "SOCKS5": "socks5"
        }
        request_methods = [
            "GET",
            "POST",
            "PUT",
            "DELETE",
        ]
        proxy = None
        if self.__proxy_type is not None:
            if self.__proxy_type in proxy_schemes:
                proxy_scheme = proxy_schemes[self.__proxy_type]
                proxy = f"{proxy_scheme}://{self.__proxy}"
            else:
                raise Exception("Proxy type has invalid value. It can be only https, http, socks4 or socks5")

        if method in request_methods:
            async with aiohttp.ClientSession() as session:
                async with session.request(method=method, url=url, params=params, data=data, proxy=proxy) as response:
                    # Иначе если делать не async with request as response и если запрос будет большим, то он не вернется. (бесконечно ждать будет)
                    # Я хуй знает почему, проблема aiohttp
                    try:
                        return await response.json()
                    except Exception:
                        return response
        else:
            raise Exception("Invalid requests method. Contact @AS7RID")

    async def send_as_async(self, func, **kwargs):
        """
        Send request as async

        :param func: Target function
        :param kwargs: Target function parameters

        :return: json server response
        """
        im_async = True
        arguments = func.__code__.co_varnames
        loc = locals()
        for arg in arguments:
            if arg != "self":
                exec(f"{arg} = None", loc)
        if True:  # Костыль для Tweak 1
            user_id = None
        for arg, value in kwargs.items():
            if arg not in arguments:
                raise Exception(f"""Function "{func.__name__}" don't have "{arg}" parameter""")
            else:
                loc[arg] = value
        func_code = str(inspect.getsource(func))
        func_code = func_code.split("):\n", 1)[1]
        lines = func_code.split("\n")
        spaces = lines[0].split('"""')[0]
        for line in lines:
            if " def " in line:
                lines.remove(line)
        return_code = "\n".join(lines).replace(spaces, "").split('"""')[2].split("return ")[1]
        func_code = "\n".join(lines).replace(spaces, "").split('"""')[2].split("return ")[0]

        exec(func_code, loc)
        path = loc.get("path")
        params = loc.get("params", {})
        data = loc.get("data", {})
        method = [eval(i.replace('method=', '')) for i in return_code.split(",") if "method=" in i][0]
        return await AntipublicApi.send_async_request(self=self, method=method, path=path, params=params,
                                                      data=data)

    class __Info:
        def __init__(self, api_self):
            self.__api = api_self

        def lines_count(self):
            """
            GET https://antipublic.one/api/v2/countLines

            Get count of rows in the AntiPublic db

            :return: json server response {'count': int}
            """

            path = f"/api/v2/countLines"
            return AntipublicApi.send_request(self=self.__api, method="GET", path=path)

        def lines_count_plain(self) -> str:
            """
            GET https://antipublic.one/api/v2/countLinesPlain

            Get count of rows in the AntiPublic db (raw format)

            :return: str
            """

            path = f"/api/v2/countLinesPlain"
            return AntipublicApi.send_request(self=self.__api, method="GET", path=path)

        def version(self):
            """
            GET https://antipublic.one/api/v2/version

            Get current antipublic version, change log and download url

            :return: json {'filename': str, 'version': str, 'changeLog': str, 'url': str}
            """

            path = f"/api/v2/version"
            return AntipublicApi.send_request(self=self.__api, method="GET", path=path)

    class __AccountInfo:
        def __init__(self, api_self):
            self.__api = api_self

        def access(self):
            """
            GET https://antipublic.one/api/v2/checkAccess

            Checks your license

            Token required

            :return: json server response {'count': int}
            """

            path = f"/api/v2/checkAccess"
            return AntipublicApi.send_request(self=self.__api, method="GET", path=path)

        def queries(self):
            """
            GET https://antipublic.one/api/v2/availableQueries

            Get your available queries

            Token required

            :return: json server response {'count': int}
            """

            path = f"/api/v2/availableQueries"
            return AntipublicApi.send_request(self=self.__api, method="GET", path=path)

    def check_lines(self, lines: list[str], insert: bool = None):
        """
        GET https://antipublic.one/api/v2/checkLines

        Check your lines.

        Token required
        :param lines: Lines for check, email:password or login:password
        :param insert: Upload private rows to AntiPublic db

        :return: json server response
        """
        params = {
            "lines": lines,
            "insert": insert
        }
        path = f"/api/v2/checkLines"
        return AntipublicApi.send_request(self=self, method="GET", path=path, params=params)

    def get_passwords(self, login: str):
        """
        GET https://antipublic.one/api/v2/emailSearch

        Get passwords for login/email

        Token required
        :param login: Email or login for search.

        :return: json server response
        """
        params = {
            "email": login
        }
        path = f"/api/v2/emailSearch"
        return AntipublicApi.send_request(self=self, method="GET", path=path, params=params)

    def get_passwords_plus(self, logins: list[str], limit: int = None):
        """
        GET https://antipublic.one/api/v2/emailPasswords

        Get passwords for emails. AntiPublic Plus subscription required.

        Token required
        :param logins: Email or login for search.
        :param limit: Result limit (per email)

        :return: json server response
        """
        params = {
            "emails": logins,
            "limit": limit
        }
        path = f"/api/v2/emailPasswords"
        return AntipublicApi.send_request(self=self, method="GET", path=path, params=params)

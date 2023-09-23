import requests


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
        if method == "GET":
            response = requests.get(url=url, params=params, data=data, files=files, proxies=proxies)
        elif method == "POST":
            response = requests.post(url=url, params=params, data=data, files=files, proxies=proxies)
        elif method == "PUT":
            response = requests.put(url=url, params=params, data=data, files=files, proxies=proxies)
        elif method == "DELETE":
            response = requests.delete(url=url, params=params, data=data, files=files, proxies=proxies)
        else:
            raise Exception(f"Invalid requests method. Contact @AS7RID")
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return response.text

    class __Info:
        def __init__(self, api_self):
            self.__api = api_self

        def lines_count(self) -> dict:
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

        def version(self) -> dict:
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

        def access(self) -> dict:
            """
            GET https://antipublic.one/api/v2/checkAccess

            Checks your license

            Token required

            :return: json server response {'count': int}
            """

            path = f"/api/v2/checkAccess"
            return AntipublicApi.send_request(self=self.__api, method="GET", path=path)

        def queries(self) -> dict:
            """
            GET https://antipublic.one/api/v2/availableQueries

            Get your available queries

            Token required

            :return: json server response {'count': int}
            """

            path = f"/api/v2/availableQueries"
            return AntipublicApi.send_request(self=self.__api, method="GET", path=path)

    def check_lines(self, lines: list[str], insert: bool = None) -> dict:
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

    def get_passwords(self, login: str) -> dict:
        """
        GET https://antipublic.one/api/v2/emailSearch

        Get passwords for login/email

        Token required
        :param login: Email or login for search.

        :return: json server response
        """
        params = {
            "email": login,
        }
        path = f"/api/v2/emailSearch"
        return AntipublicApi.send_request(self=self, method="GET", path=path, params=params)

    def get_passwords_plus(self, logins: list[str], limit: int = None) -> dict:
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

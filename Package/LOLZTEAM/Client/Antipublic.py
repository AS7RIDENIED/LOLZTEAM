from .Base import Constants
from .Base.Core import APIClient, NONE
from .Base.Wrappers import UNIVERSAL

from typing import Literal


class Antipublic(APIClient):
    """
    ### Antipublic API Client.

    You can view full class documentation here [click](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Antipublic.md)

    And also official documentation for Antipublic API is here [click](https://antipublic.readme.io)

    ## 💛Made with love💛
    """

    def __init__(self, token: str, delay_min: float = 0, timeout: float = 90, proxy: str = None):
        """
        Antipublic API Client

        **Parameters:**

        - token (str): Your token.
          > You can get it [there](https://zelenka.guru/account/antipublic) or in antipublic app
        - delay_min (float): Minimal delay between requests.
          > This parameter sets a strict minimal delay between your requests
        - timeout (float): Request timeout.
        - proxy (str): Proxy string.
          > protocol://ip:port or protocol://login:password@ip:port (socks5://login:password@192.168.1.1:8080)

        **Example:**

        ```python
        from LOLZTEAM.Client import Antipublic
        import asyncio

        token = "your_antipublic_key"

        antipublic = Antipublic(token=token)

        antipublic.settings.logger.enable()                                    # -> Start logging
        antipublic.settings.delay.enable()                                     # Enable delay. Idk why you would ever need to enable delay for antipublic, but there it is
        response = antipublic.info.lines()                                     # Sync request
        response = antipublic.request("GET", "/countLines")                    # Custom sync request

        async def async_example():
            async_response = await antipublic.info.lines()                     # Async request
            async_response = await antipublic.request("GET", "/countLines")    # Custom async request

        asyncio.run(async_example())

        antipublic.settings.token = "token"                                    # Change token
        antipublic.settings.proxy = "http://login:password@192.168.1.1:8080"   # Change proxy
        antipublic.settings.delay.min = 2410024                                # Change minimal delay
        antipublic.settings.delay.disable()                                    # Disable delay
        antipublic.settings.logger.disable()                                   # <- Stop logging
        ```
        """
        super().__init__(
            base_url="https://antipublic.one/api/v2",
            token=token,
            language=None,
            delay_min=delay_min,
            logger_name=Antipublic.__qualname__,
            proxy=proxy,
            timeout=timeout
        )
        self.settings.delay.set(0)
        self.settings.delay.disable()  # No delay for antipublic hmm
        self.core = self
        self.info = self.__Info(core=self)
        self.account = self.__Account(core=self)

    class __Info:
        def __init__(self, core: APIClient):
            self.core = core

        @UNIVERSAL()
        async def lines(self, plain: bool = False):
            """
            GET https://antipublic.one/api/v2/countLines

            GET https://antipublic.one/api/v2/countLinesPlain

            *Get count of rows in the AntiPublic db*

            **Example:**

            ```python
            response = antipublic.info.lines()
            print(response.text)
            ```
            """
            if plain:
                return await self.core.request("GET", "/countLinesPlain")
            return await self.core.request("GET", "/countLines")

        @UNIVERSAL()
        async def version(self):
            """
            GET https://antipublic.one/api/v2/version

            *Get version of the AntiPublic*

            **Example:**

            ```python
            response = antipublic.info.version()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/version")

    class __Account:
        def __init__(self, core: APIClient):
            self.core = core

        @UNIVERSAL()
        async def access(self):
            """
            GET https://antipublic.one/api/v2/checkAccess

            *Check access to the AntiPublic*

            **Example:**

            ```python
            response = antipublic.account.access()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/checkAccess")

        @UNIVERSAL()
        async def queries(self):
            """
            GET https://antipublic.one/api/v2/availableQueries

            *Get available queries*

            **Example:**

            ```python
            response = antipublic.account.queries()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/availableQueries")

    @UNIVERSAL()
    async def check(self, lines: list[str], insert: bool = False):
        """
        POST https://antipublic.one/api/v2/checkLines

        *Check lines in the AntiPublic db*

        **Parameters:**

        - lines (list[str]): Lines for check (email:password or login:password).
          > Maximum 1000 lines per request.
        - insert (bool): Upload private rows to AntiPublic db.

        **Example:**

        ```python
        response = antipublic.check(lines=["email:password", "login:password"], insert=True)
        print(response.json())
        ```
        """
        json = {"lines": lines, "insert": insert}
        return await self.core.request("POST", "/checkLines", json=json)

    @UNIVERSAL()
    async def search(self, searchBy: Constants.Antipublic.SearchBy._Literal,
                     query: dict[Constants.Antipublic.SearchBy._Literal, str],
                     direction: dict[Constants.Antipublic.SearchBy._Literal, Constants.Antipublic.SearchDirection._Literal] = NONE,
                     order: Literal["asc", "desc"] = NONE,
                     from_last_value_of_key: bool = NONE,
                     group_by: Literal["login@domain", "domain", "password"] = NONE,
                     format: Literal["login@domain:password", "login@domain", "login", "domain", "password"] = NONE,
                     token: str = NONE):
        """
        POST https://antipublic.one/api/v2/search

        *Search lines by email/password/domain*

        **Parameters:**

        - searchBy (str): Search by email/password/domain.
        - query (dict[str, str]): Query for search.
        - direction (dict[str, str]): Direction for search.
        - order (Literal["asc", "desc"]): [Premium subscription required] If you specify `desc` order, then most likely you will have a couple of results. Everything is fine and it should be. To get more results - you need to disable fuses by specifying all in direction for your query field. Or if the request field is strict, then specify fromLastValueOfKey equal to true.
        - from_last_value_of_key (bool): [Premium subscription required] When using this option and "strict direction" the starting position starts from the last value of the key. For example, we have email:pass1, email:pass2, email:pass3. Then when setting query = email, direction = strict, fromLastValueOfKey = true the first result obtained will be email:pass3.
        - group_by (Literal["login@domain", "domain", "password"]): [Premium subscription required] This option allows you to remove "duplicates". Only the first found line corresponding to the grouping will be returned and will move on to the next value.
        - format (Literal["login@domain:password", "login@domain", "login", "domain", "password"]): The format of the returned results. Allows you to quickly leave the most necessary without post-processing. When used correctly together with groupBy, the execution time of a database search query can be accelerated by eliminating JOIN operations on the server.
        - token (str): Page token.

        **Example:**

        ```python
        response = antipublic.search(searchBy="email", query={"email": "test@mail.ru"}, direction={"email": "start"})
        print(response.json())
        ```
        """
        json = {
            "searchBy": searchBy,
            "query": query,
            "direction": direction,
            "order": order,
            "fromLastValueOfKey": from_last_value_of_key,
            "groupBy": group_by,
            "format": format,
            "pageToken": token
        }
        return await self.core.request("POST", "/search", json=json)

    @UNIVERSAL()
    async def passwords(self, emails: list[str], limit: int = NONE, only_passwords: bool = NONE):
        """
        POST https://antipublic.one/api/v2/emailPasswords

        *Get passwords for login's/email's*

        **Parameters:**

        - emails (list[str]): List of emails or logins for search.
        - limit (int): Result limit (per email).
        - only_passwords (bool): Return only passwords.

        **Example:**

        ```python
        response = antipublic.passwords(emails=["test@mail.ru", "test2@mail.ru"], limit=1)
        print(response.json())
        ```
        """
        json = {"emails": emails, "limit": limit, "onlyPasswords": only_passwords}
        return await self.core.request("POST", "/emailPasswords", json=json)

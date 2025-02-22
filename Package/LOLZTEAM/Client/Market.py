from .Base import Constants
from .Base.Core import APIClient, AutoDelay, Response, _NONE, NONE
from .Base.Wrappers import UNIVERSAL
from typing import Literal, Union
from httpx import URL


class Market(APIClient):
    """
    ### LOLZTEAM Market API Client.

    You can view full class documentation here [click](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Market.md)

    And also official documentation for Market API is here [click](https://lzt-market.readme.io)

    ## 💛Made with love💛
    """

    def __init__(self, token: str, language: Literal["ru", "en"] = None, delay_min: float = 0, proxy: str = None, timeout: float = 90, verify: bool = True):
        """
        LOLZTEAM Market API Client

        **Parameters:**

        - **token** (str): Your token.
          > You can get it [there](https://zelenka.guru/account/api)
        - **language** (Literal["ru", "en"]): Language of the API responses.
        - **delay_min** (float): Minimal delay between requests.
          > This parameter sets a strict minimal delay between your requests.
        - **proxy** (str): Proxy string.
          > protocol://ip:port or protocol://login:password@ip:port (socks5://login:password@192.168.1.1:8080 or http://login:password@192.168.1.1:8080)
        - **timeout** (float): Request timeout.

        ```python
        from LOLZTEAM.Client import Market
        import asyncio

        token = "your_token"

        market = Market(token=token)

        market.settings.logger.enable()                                        # -> Start logging
        market.settings.delay.enable()                                         # Enable delay (btw delay is enabled by default)

        response = market.profile.get()                                        # Sync request
        job = market.profile.get.job()                                         # Job creation (Always SYNC)
        response = market.request("GET", "/me")                                # Custom request
        job = market.request.job("GET", "/me")                                 # Job creation for custom request

        async def async_example():
            response = await market.profile.get()                              # Async request
            job = market.profile.get.job()                                     # Job creation (Always SYNC)
            response = await market.request("GET", "/me")                      # Custom async request
            job = market.request.job("GET", "/me")                             # Job creation for custom request

        asyncio.run(async_example())

        # You should just add ".job" between function name and parentheses to create a job.
        # P.s Your IDE probably may not show that ".job" function exists but it does.

        market.settings.token = "token"                                        # Change token
        market.settings.language = "en"                                        # Change language
        market.settings.proxy = "http://login:password@192.168.1.1:8080"       # Change proxy
        market.settings.delay.min = 1                                          # Change minimal delay
        market.settings.delay.disable()                                        # Disable delay
        market.settings.logger.disable()                                       # <- Stop logging
        ```
        """
        super().__init__(
            base_url="https://api.lzt.market",
            token=token,
            language=language,
            delay_min=delay_min,
            logger_name=Market.__qualname__,
            proxy=proxy,
            timeout=timeout,
            verify=verify
        )
        self.categories = self.__Categories(self)
        self.list = self.__List(self)
        self.managing = self.__Managing(self)
        self.purchasing = self.__Purchasing(self)
        self.publishing = self.__Publishing(self)
        self.profile = self.__Profile(self)
        self.payments = self.__Payments(self)
        self.proxy = self.__Proxy(self)

    class __Categories:
        class __BaseCategory:
            def __init__(self, core: "Market", endpoint: str):
                self.core = core
                self.endpoint = endpoint

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(3)
            async def get(self, **kwargs) -> Response:
                """
                GET https://api.lzt.market/CATEGORY_NAME

                *Displays a list of accounts in a specific category according to your parameters.*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **title** (str): The word or words contained in the account title.
                - **pmin** (float): Minimal price of account (Inclusive).
                - **pmax** (float): Maximum price of account (Inclusive).
                - **origin** (list): List of account origins.
                - **not_origin** (list): List of account origins that won't be included.
                - **order_by** (str): Item order.
                - **sold_before** (bool): Sold before.
                - **sold_before_by_me** (bool): Sold before by me.
                - **not_sold_before** (bool): Not sold before.
                - **not_sold_before_by_me** (bool): Not sold before by me.
                - ****kwargs** (any): Any additional search parameters.

                **Example:**

                ```python
                response = market.categories.CATEGORY_NAME.get(pmin=100, pmax=500)
                print(response.json())
                ```
                """
                params = kwargs
                return await self.core.request("GET", self.endpoint, params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(3)
            async def params(self) -> Response:
                """
                GET https://api.lzt.market/CATEGORY_NAME/params

                *Displays a list of parameters for a specific category.*

                **Example:**

                ```python
                response = market.categories.CATEGORY_NAME.params()
                print(response.json())
                ```
                """
                self.core.__categoryEndpoint = self.endpoint
                return await self.core.request("GET", self.core.__categoryEndpoint + "/params")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(3)
            async def games(self) -> Response:
                """
                GET https://api.lzt.market/CATEGORY_NAME/games

                *Displays a list of games for a specific category.*

                **Example:**

                ```python
                response = market.categories.CATEGORY_NAME.games()
                print(response.json())
                ```
                """
                self.core.__categoryEndpoint = self.endpoint
                return await self.core.request("GET", self.core.__categoryEndpoint + "/games")

        class __Latest(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/")

        class __Steam(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/steam")

        class __Fortnite(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/fortnite")

        class __Mihoyo(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/mihoyo")

        class __Riot(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/riot")

        class __Telegram(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/telegram")

        class __Supercell(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/supercell")

        class __Origin(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/origin")

        class __Wot(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/world-of-tanks")

        class __Wot_Blitz(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/wot-blitz")

        class __Gifts(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/gifts")

        class __Epicgames(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/epicgames")

        class __Eft(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/escape-from-tarkov")

        class __SocialClub(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/socialclub")

        class __Uplay(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/uplay")

        class __War_Thunder(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/war-thunder")

        class __Discord(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/discord")

        class __Tiktok(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/tiktok")

        class __Instagram(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/instagram")

        class __BattleNet(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/battlenet")

        class __ChatGPT(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/chatgpt")

        class __VPN(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/vpn")

        class __Cinema(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/cinema")

        class __Roblox(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/roblox")

        class __Spotify(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/spotify")

        class __Warface(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/warface")

        class __Minecraft(__BaseCategory):
            def __init__(self, core: "Market"):
                super().__init__(core, "/minecraft")

        def __init__(self, core: "Market"):
            self.core = core
            self.latest = self.__Latest(self.core)
            self.steam = self.__Steam(self.core)
            self.fortnite = self.__Fortnite(self.core)
            self.mihoyo = self.__Mihoyo(self.core)
            self.riot = self.__Riot(self.core)
            self.telegram = self.__Telegram(self.core)
            self.supercell = self.__Supercell(self.core)
            self.origin = self.__Origin(self.core)
            self.wot = self.__Wot(self.core)
            self.wot_blitz = self.__Wot_Blitz(self.core)
            self.gifts = self.__Gifts(self.core)
            self.epicgames = self.__Epicgames(self.core)
            self.eft = self.__Eft(self.core)
            self.socialclub = self.__SocialClub(self.core)
            self.uplay = self.__Uplay(self.core)
            self.war_thunder = self.__War_Thunder(self.core)
            self.discord = self.__Discord(self.core)
            self.tiktok = self.__Tiktok(self.core)
            self.instagram = self.__Instagram(self.core)
            self.battlenet = self.__BattleNet(self.core)
            self.chatgpt = self.__ChatGPT(self.core)
            self.vpn = self.__VPN(self.core)
            self.cinema = self.__Cinema(self.core)
            self.roblox = self.__Roblox(self.core)
            self.spotify = self.__Spotify(self.core)
            self.warface = self.__Warface(self.core)
            self.minecraft = self.__Minecraft(self.core)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def list(self, top_queries: bool = False) -> Response:
            """
            GET https://api.lzt.market/category

            *Displays a list of categories.*

            **Parameters:**

            - **top_queries** (bool): Display top queries.

            **Example:**

            ```python
            response = market.categories.list()
            print(response.json())
            ```
            """
            params = {"topQueries": top_queries}
            return await self.core.request("GET", "/category", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(3)
        async def get(
            self,
            category_name: Constants.Market.Category._Literal,
            **kwargs,
        ) -> Response:
            """
            GET https://api.lzt.market/{category_name}

            *Displays a list of accounts in a specific category according to your parameters.*

            **Parameters:**

            - **category_name** (str): Category name.
            - **kwargs** (any): Additional search parameters for your request.

            **Example:**

            ```python
            response = market.category.get(category_name="telegram")
            print(response.json())
            ```
            """
            params = kwargs
            return await self.core.request("GET", f"/{category_name}", params=params)

    class __List:
        def __init__(self, core: "Market"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def owned(self, category_id: Constants.Market.CategoryID._Literal,
                        status: Constants.Market.ItemStatus._Literal = NONE,
                        **kwargs) -> Response:
            """
            GET https://api.lzt.market/user/items

            *Displays a list of accounts owned by you.*

            **Parameters:**

            - **category_id** (int): Category ID.
            - **show** (str): Show status.
            - **kwargs** (any): Any additional search parameters.

            **Example:**

            ```python
            response = market.list.owned(category_id=1, show="paid", pmin=250)
            print(response.json())
            ```
            """
            params = {
                "category_id": category_id,
                "show": status
            }
            params.update(kwargs)
            return await self.core.request("GET", "/user/items", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def purchased(self, category_id: Constants.Market.CategoryID._Literal, **kwargs) -> Response:
            """
            GET https://api.lzt.market/user/orders

            *Displays a list of accounts purchased by you.*

            **Parameters:**

            - **category_id** (int): Category ID.
            - **kwargs** (any): Any additional search parameters.

            **Example:**

            ```python
            response = market.list.purchased(category_id=1, pmin=250)
            print(response.json())
            ```
            """
            params = {
                "category_id": category_id,
            }
            params.update(kwargs)
            return await self.core.request("GET", "/user/orders", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def favorite(self, category_id: Constants.Market.CategoryID._Literal, **kwargs) -> Response:
            """
            GET https://api.lzt.market/fave

            *Displays a list of favorite accounts.*

            **Parameters:**

            - **category_id** (int): Category ID.
            - **kwargs** (any): Any additional search parameters.

            **Example:**

            ```python
            response = market.list.favorite(category_id=1, pmin=250)
            print(response.json())
            ```
            """
            params = {
                "category_id": category_id,
            }
            params.update(kwargs)
            return await self.core.request("GET", "/fave", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def viewed(self, category_id: Constants.Market.CategoryID._Literal, **kwargs) -> Response:
            """
            GET https://api.lzt.market/viewed

            *Displays a list of viewed accounts.*

            **Parameters:**

            - **category_id** (int): Category ID.
            - **kwargs** (any): Any additional search parameters.

            **Example:**

            ```python
            response = market.list.viewed(category_id=1, pmin=250)
            print(response.json())
            ```
            """
            params = {
                "category_id": category_id,
            }
            params.update(kwargs)
            return await self.core.request("GET", "/viewed", params=params)

    class __Managing:
        class __SteamMan:
            def __init__(self, core: "Market"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def item_value(self, item_id: str, app_id: Constants.Market.AppID._Literal, currency: Constants.Market.Currency._Literal = NONE, ignore_cache: bool = NONE) -> Response:
                """
                GET https://api.lzt.market/{item_id}/inventory-value

                *Displays the value of the account's inventory.*

                **Parameters:**

                - **item_id** (str): Item ID.
                - **app_id** (int): App ID.

                **Example:**

                ```python
                response = market.managing.steam.item_value(item_id="1234567890", app_id=730)
                print(response.json())
                ```
                """
                params = {
                    "app_id": app_id,
                    "currency": currency,
                    "ignore_cache": ignore_cache
                }
                return await self.core.request("GET", f"/{item_id}/inventory-value", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(3)
            async def inventory_value(self, url: str, app_id: Constants.Market.AppID._Literal = NONE, currency: Constants.Market.Currency._Literal = NONE, ignore_cache: bool = NONE) -> Response:
                """
                GET https://api.lzt.market/steam-value

                *Displays the value of the account's inventory.*

                **Parameters:**

                - **url** (str): Link or id of account.
                  > Can be [https://lzt.market/{item-id}/, https://steamcommunity.com/id/{steam-name}, https://steamcommunity.com/profiles/{steam-id}, {steam-id}].
                - **app_id** (int): App ID.
                - **currency** (str): Currency.
                - **ignore_cache** (bool): Ignore cache.

                **Example:**
                """
                params = {
                    "link": url,
                    "app_id": app_id,
                    "currency": currency,
                    "ignore_cache": ignore_cache
                }
                return await self.core.request("GET", "/steam-value", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def html_preview(self, item_id: int, type: Literal["profiles", "games"] = NONE) -> Response:
                """
                GET https://api.lzt.market/{item_id}/steam-preview

                *Returns a preview of the steam account.*

                **Parameters:**

                - **item_id** (int): Item ID.
                - **type** (str): Type of preview.
                  > Can be ["profiles", "games"].

                **Example:**

                ```python
                response = market.managing.steam.html_preview(item_id=1234567890, type="profiles")
                print(response.json())
                ```
                """
                params = {
                    "type": type
                }
                return await self.core.request("GET", f"/{item_id}/steam-preview", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def inventory_update(self, item_id: int, app_id: Constants.Market.AppID._Literal = NONE, all: bool = NONE) -> Response:
                """
                POST https://api.lzt.market/{item_id}/update-inventory

                *Updates the inventory of the steam account.*

                **Parameters:**

                - **item_id** (int): Item ID.
                - **app_id** (int): App ID.
                - **all** (bool): Update entire inventory.

                **Example:**

                ```python
                response = market.managing.steam.inventory_update(item_id=1234567890, all=True)
                print(response.json())
                ```
                """
                params = {
                    "app_id": app_id,
                    "all": all
                }
                return await self.core.request("POST", f"/{item_id}/update-inventory", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def mafile(self, item_id: int) -> Response:
                """
                GET https://api.lzt.market/{item_id}/mafile

                *Returns a mafile of the steam account.*
                  > This request will cancel active account guarantee.

                **Parameters:**

                - **item_id** (int): Item ID.

                **Example:**

                ```python
                response = market.managing.steam.mafile(item_id=1234567890)
                print(response.json())
                ```
                """
                return await self.core.request("GET", f"/{item_id}/mafile")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def mafile_remove(self, item_id: int) -> Response:
                """
                DELETE https://api.lzt.market/{item_id}/mafile

                *Removes the mafile of the steam account.*
                  > This will unlink the authenticator from the account and remove mafile from the item

                **Parameters:**

                - **item_id** (int): Item ID.

                **Example:**

                ```python
                response = market.managing.steam.mafile_remove(item_id=1234567890)
                print(response.json())
                ```
                """
                return await self.core.request("DELETE", f"/{item_id}/mafile")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def sda(self, item_id: int, id: int = NONE, nonce: int = NONE) -> Response:
                """
                POST https://api.lzt.market/{item_id}/confirm-sda

                *Confirm the steam account.*
                  > This request will cancel active account guarantee.

                **Parameters:**

                - **item_id** (int): Item ID.
                - **id** (int): ID.
                - **nonce** (int): Nonce.

                **Example:**

                ```python
                response = market.managing.steam.sda(item_id=1234567890, id=1234567890, nonce=1234567890)
                print(response.json())
                ```
                """
                params = {
                    "id": id,
                    "nonce": nonce
                }
                return await self.core.request("POST", f"/{item_id}/confirm-sda", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def guard(self, item_id: int) -> Response:
                """
                get https://api.lzt.market/{item_id}/guard-code

                *Gets confirmation code from MaFile.*

                **Example:**

                ```python
                response = market.managing.steam.guard(item_id=1234567890)
                print(response.json())
                ```
                """
                return await self.core.request("GET", f"/{item_id}/guard-code")

        class __TelegramMan:
            def __init__(self, core: "Market"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def code(self, item_id: str) -> Response:
                """
                GET https://api.lzt.market/{item_id}/telegram-login-code

                *Returns a telegram confirmation code.*

                **Parameters:**

                - **item_id** (str): Item ID.

                **Example:**

                ```python
                response = market.managing.telegram.code(item_id=1234567890)
                print(response.json())
                ```
                """
                return await self.core.request("GET", f"/{item_id}/telegram-login-code")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def reset_auth(self, item_id: str) -> Response:
                """
                POST https://api.lzt.market/{item_id}/telegram-reset-authorizations

                *Resets the telegram authorizations.*

                **Parameters:**

                - **item_id** (str): Item ID.

                **Example:**

                ```python
                response = market.managing.telegram.reset_auth(item_id=1234567890)
                print(response.json())
                ```
                """
                return await self.core.request("POST", f"/{item_id}/telegram-reset-authorizations")

        class __Guarantee:
            def __init__(self, core: "Market"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def cancel(self, item_id: int) -> Response:
                """
                POST https://api.lzt.market/{item_id}/refuse-guarantee

                *Cancels the account guarantee.*

                **Parameters:**

                - **item_id** (int): Item ID.

                **Example:**

                ```python
                response = market.managing.guarantee.cancel(item_id=1234567890)
                print(response.json())
                ```
                """
                return await self.core.request("POST", f"/{item_id}/refuse-guarantee")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.5)
            async def check(self, item_id: int) -> Response:
                """
                POST https://api.lzt.market/{item_id}/check-guarantee

                *Checks the account guarantee and cancels it if there is a reason to do so.*

                **Parameters:**

                - **item_id** (int): Item ID.

                **Example:**

                ```python
                response = market.managing.guarantee.check(item_id=1234567890)
                print(response.json())
                ```
                """
                return await self.core.request("POST", f"/{item_id}/check-guarantee")

        def __init__(self, core: "Market"):
            self.core = core
            self.steam = self.__SteamMan(self.core)
            self.telegram = self.__TelegramMan(self.core)
            self.guarantee = self.__Guarantee(self.core)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def get(self, item_id: int) -> Response:
            """
            GET https://api.lzt.market/{item_id}

            *Returns the item.*

            **Parameters:**

            - **item_id** (int): Item ID.

            **Example:**

            ```python
            response = market.managing.get(item_id=1234567890)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/{item_id}")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def bulk(self, item_ids: list[int]) -> Response:
            """
            POST https://api.lzt.market/bulk/items

            *Returns several amount of items.*
              >  You can get only your accounts or those you have purchased.

            **Parameters:**

            - **item_ids** (list[int]): Item IDs.
              > Max 250 items.

            **Example:**

            ```python
            response = market.managing.bulk(item_ids=[12345678900, 12345678901])
            print(response.json())
            ```
            """
            json = {"item_id": item_ids}
            return await self.core.request("POST", "/bulk/items", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def edit(
            self,
            item_id: int,
            title: str = NONE,
            title_en: str = NONE,
            price: float = NONE,
            currency: Constants.Market.Currency._Literal = NONE,
            origin: Constants.Market.ItemOrigin._Literal = NONE,
            description: str = NONE,
            information: str = NONE,
            email: str = NONE,
            email_type: Literal["native", "autoreg"] = NONE,
            allow_ask_discount: bool = NONE,
            proxy_id: int = NONE
        ) -> Response:
            """
            PUT https://api.lzt.market/{item_id}

            *Edits the item.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **title** (str): Title.
            - **title_en** (str): Title in English.
            - **price** (float): Price.
            - **currency** (str): Currency.
            - **origin** (str): Item origin.
            - **description** (str): Description.
            - **information** (str): Information.
            - **email** (str): Email.
            - **email_type** (str): Email type.
            - **allow_ask_discount** (bool): Allow ask discount.
            - **proxy_id** (int): Proxy ID.

            **Example:**

            ```python
            response = market.managing.edit(
                item_id=1234567890,
                title="New Title",
                price=100.0,
                currency="rub",
                origin="steam",
                description="New Description",
                information="New Information",
                email="email@example.com:email_password",
                email_type="native",
                allow_ask_discount=True,
                proxy_id=1234567890
            )
            print(response.json())
            ```
            """
            json = {
                "title": title,
                "title_en": title_en,
                "price": price,
                "currency": currency,
                "item_origin": origin,
                "description": description,
                "information": information,
                "email_login_data": email,
                "email_type": email_type,
                "allow_ask_discount": allow_ask_discount,
                "proxy_id": proxy_id
            }
            return await self.core.request("PUT", f"/{item_id}/edit", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def delete(self, item_id: int, reason: str) -> Response:
            """
            DELETE https://api.lzt.market/{item_id}

            *Deletes the item.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **reason** (str): Reason.
            """
            json = {
                "reason": reason
            }
            return await self.core.request("DELETE", f"/{item_id}", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def bump(self, item_id: int) -> Response:
            """
            POST https://api.lzt.market/{item_id}/bump

            *Bumps the item.*

            **Parameters:**

            - **item_id** (int): Item ID.

            **Example:**

            ```python
            response = market.managing.bump(item_id=1234567890)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/{item_id}/bump")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def note(self, item_id: int, text: str = NONE) -> Response:
            """
            POST https://api.lzt.market/{item_id}/note-save

            *Edits the note.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **text** (str): Text.

            **Example:**

            ```python
            response = market.managing.note(item_id=1234567890, text="New Note")
            print(response.json())
            ```
            """
            json = {
                "text": text
            }
            return await self.core.request("POST", f"/{item_id}/note-save", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def image(self, item_id: int, image_type: Literal["skins", "pickaxes", "dances", "gliders", "WeaponSkins", "Agent", "Buddy"]) -> Response:
            """
            GET https://api.lzt.market/{item_id}/image

            *Get item image.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **image_type** (str): Image type.

            **Example:**

            ```python
            response = market.managing.image(item_id=1234567890, image_type="skins")
            # Response is a bytes
            with open("image.png", "wb") as f:
                f.write(response.content)
            ```
            """
            return await self.core.request("GET", f"/{item_id}/image", params={"type": image_type})

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def arbitrage(self, item_id: int, post_body: str) -> Response:
            """
            POST https://api.lzt.market/{item_id}/claims

            *Create arbitrage for the item.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **post_body** (str): Post body.

            **Example:**

            ```python
            response = market.managing.arbitrage(item_id=1234567890, post_body="New Post Body")
            print(response.json())
            ```
            """
            json = {
                "post_body": post_body
            }
            return await self.core.request("POST", f"/{item_id}/claims", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def email_code(self, item_id: int = NONE, email: str = NONE, login: str = NONE) -> Response:
            """
            GET https://api.lzt.market/email-code

            *Gets an email code from the item.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **email** (str): Email.
            - **login** (str): Login.

            **Example:**

            ```python
            response = market.managing.email_code(item_id=1234567890)
            print(response.json())
            ```
            """
            json = {
                "item_id": item_id,
                "email": email,
                "login": login
            }
            return await self.core.request("GET", "/email-code", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def email_password(self, item_id: int) -> Response:
            """
            GET https://api.lzt.market/{item_id}/temp-email-password

            *Gets an temporary email password from the item.*

            **Parameters:**

            - **item_id** (int): Item ID.

            **Example:**

            ```python
            response = market.managing.email_password(item_id=1234567890)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/{item_id}/temp-email-password")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def change_password(self, item_id: int, cancel: bool = NONE) -> Response:
            """
            POST https://api.lzt.market/{item_id}/change-password

            *Changes the password of the item.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **cancel** (bool): Cancel change password recommendation. It will be helpful, if you don't want to change password and get login data.

            **Example:**

            ```python
            response = market.managing.change_password(item_id=1234567890)
            print(response.json())
            ```
            """
            json = {
                "_cancel": cancel
            }
            return await self.core.request("POST", f"/{item_id}/change-password", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def tag(self, item_id: int, tag_id: Union[int, list[int]]) -> Response:
            """
            POST https://api.lzt.market/{item_id}/tag

            *Tags the item.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **tag_id** (int): Tag ID.

            **Example:**

            ```python
            response = market.managing.tag(item_id=1234567890, tag_id=12345)
            print(response.json())
            ```
            """
            json = {
                "tag_id[]": tag_id
            }
            return await self.core.request("POST", f"/{item_id}/tag", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def untag(self, item_id: int, tag_id: Union[int, list[int]]) -> Response:
            """
            DELETE https://api.lzt.market/{item_id}/tag

            *Untags the item.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **tag_id** (int): Tag ID.

            **Example:**

            ```python
            response = market.managing.untag(item_id=1234567890, tag_id=12345)
            print(response.json())
            ```
            """
            json = {
                "tag_id[]": tag_id
            }
            return await self.core.request("DELETE", f"/{item_id}/tag", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def favorite(self, item_id: int) -> Response:
            """
            POST https://api.lzt.market/{item_id}/star

            *Adds the item to favorites.*

            **Parameters:**

            - **item_id** (int): Item ID.

            **Example:**

            ```python
            response = market.managing.favorite(item_id=1234567890)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/{item_id}/star")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def unfavorite(self, item_id: int) -> Response:
            """
            DELETE https://api.lzt.market/{item_id}/star

            *Removes the item from favorites.*

            **Parameters:**

            - **item_id** (int): Item ID.

            **Example:**

            ```python
            response = market.managing.unfavorite(item_id=1234567890)
            print(response.json())
            ```
            """
            return await self.core.request("DELETE", f"/{item_id}/star")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def stick(self, item_id: int) -> Response:
            """
            POST https://api.lzt.market/{item_id}/stick

            *Sticks the item to the top of search results.*

            **Parameters:**

            - **item_id** (int): Item ID.

            **Example:**

            ```python
            response = market.managing.sticky(item_id=1234567890)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/{item_id}/stick")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def unstick(self, item_id: int) -> Response:
            """
            DELETE https://api.lzt.market/{item_id}/stick

            *Unsticks the item from the top of search results.*

            **Parameters:**

            - **item_id** (int): Item ID.

            **Example:**

            ```python
            response = market.managing.unstick(item_id=1234567890)
            print(response.json())
            ```
            """
            return await self.core.request("DELETE", f"/{item_id}/stick")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def transfer(self, item_id: int, username: str, secret_answer: str) -> Response:
            """
            POST https://api.lzt.market/{item_id}/change-owner

            *Transfers the item to another user.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **username** (str): Username.
            - **secret_answer** (str): Secret answer.

            **Example:**

            ```python
            response = market.managing.transfer(item_id=1234567890, username="AS7RID", secret_answer="secret_answer")
            print(response.json())
            ```
            """
            json = {
                "username": username,
                "secret_answer": secret_answer
            }
            return await self.core.request("POST", f"/{item_id}/change-owner", json=json)

    class __Purchasing:
        def __init__(self, core: "Market"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def fast(self, item_id: int, price: float = NONE) -> Response:
            """
            POST https://api.lzt.market/{item_id}/fast-buy

            *Fast buy the item.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **price** (float): Price.

            **Example:**

            ```python
            response = market.purchasing.fast(item_id=1234567890)
            print(response.json())
            ```
            """
            json = {
                "price": price
            }
            return await self.core.request("POST", f"/{item_id}/fast-buy", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def check(self, item_id: int) -> Response:
            """
            POST https://api.lzt.market/{item_id}/check-account

            *Checks the account for validity.*

            **Parameters:**

            - **item_id** (int): Item ID.

            **Example:**

            ```python
            response = market.purchasing.check(item_id=1234567890)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/{item_id}/check-account")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def buy(self, item_id: int, price: float = NONE) -> Response:
            """
            POST https://api.lzt.market/{item_id}/confirm-buy

            *Buys the item.*
              > This method doesn't check account for validity.

            **Parameters:**

            - **item_id** (int): Item ID.
            - **price** (float): Price.

            **Example:**

            ```python
            response = market.purchasing.buy(item_id=1234567890, price=100)
            print(response.json())
            ```
            """
            json = {
                "price": price
            }
            return await self.core.request("POST", f"/{item_id}/confirm-buy", json=json)

    class __Publishing:
        def __init__(self, core: "Market"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def fast(
            self,
            price: float,
            category_id: Constants.Market.CategoryID._Literal,
            origin: Constants.Market.ItemOrigin._Literal,
            currency: Constants.Market.Currency._Literal = "rub",
            guarantee: Constants.Market.Guarantee._Literal = NONE,
            title: str = NONE,
            title_en: str = NONE,
            description: str = NONE,
            information: str = NONE,
            login: str = NONE,
            password: str = NONE,
            email: str = NONE,
            email_type: Literal["native", "autoreg"] = NONE,
            extra: dict[Constants.Market.Extra._Literal, str] = NONE,
            allow_ask_discount: bool = NONE,
            proxy_id: int = NONE,
            proxy_random: bool = NONE
        ) -> Response:
            """
            POST https://api.lzt.market/item/fast-sell

            *Adds and check account on validity. If account is valid, account will be published on the market.*
              > If you receive a "captcha" error, you should send the same request again.

            **Parameters:**

            - **price** (float): Price.
            - **category_id** (int): Category ID.
            - **origin** (str): Item origin.
            - **currency** (str): Currency.
            - **guarantee** (str): Guarantee.
            - **title** (str): Title.
            - **title_en** (str): Title in English.
            - **description** (str): Description.
            - **information** (str): Information.
            - **login** (str): Login.
            - **password** (str): Password.
            - **email** (str): Email.
            - **email_type** (str): Email type.
            - **extra** (dict[str, str]): Extra.
            - **allow_ask_discount** (bool): Allow ask discount.
            - **proxy_id** (int): Proxy ID.
            - **proxy_random** (bool): Proxy random.

            **Example:**

            ```python
            response = market.publishing.fast(
                item_id=1234567890,
                price=100,
                category_id=24,
                origin="autoreg",
                currency="rub",
                title="Telegram account",
                description="Public description",
                information="Private information",
                login="dc_id",
                password="auth_key",
                extra={"checkSpam": True},
                allow_ask_discount=True,
                proxy_id=12345
            )
            print(response.json())
            ```
            """
            json = {
                "price": price,
                "category_id": category_id,
                "item_origin": origin,
                "currency": currency,
                "guarantee": guarantee,
                # Item
                "title": title,
                "title_en": title_en,
                "description": description,
                "information": information,
                "login": login,
                "password": password,
                "has_email_login_data": bool(email) if email and not isinstance(email, _NONE) else email,
                "email_login_data": email,
                "email_type": email_type,
                "extra": extra,
                # Other
                "allow_ask_discount": allow_ask_discount,
                "proxy_id": proxy_id,
                "random_proxy": proxy_random
            }
            return await self.core.request("POST", "/item/fast-sell", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def add(
            self,
            price: float,
            category_id: Constants.Market.CategoryID._Literal,
            origin: Constants.Market.ItemOrigin._Literal,
            currency: Constants.Market.Currency._Literal = "rub",
            guarantee: Constants.Market.Guarantee._Literal = NONE,
            title: str = NONE,
            title_en: str = NONE,
            description: str = NONE,
            information: str = NONE,
            email: str = NONE,
            email_type: Literal["native", "autoreg"] = NONE,
            allow_ask_discount: bool = NONE,
            proxy_id: int = NONE,
            proxy_random: bool = NONE
        ) -> Response:
            """
            POST https://api.lzt.market/item/add

            *Adds the item to the market.*

            **Parameters:**

            - **price** (float): Price.
            - **category_id** (int): Category ID.
            - **origin** (str): Item origin.
            - **currency** (str): Currency.
            - **guarantee** (str): Guarantee.
            - **title** (str): Title.
            - **title_en** (str): Title in English.
            - **description** (str): Description.
            - **information** (str): Information.
            - **email** (str): Email.
            - **email_type** (str): Email type.
            - **allow_ask_discount** (bool): Allow ask discount.
            - **proxy_id** (int): Proxy ID.
            - **proxy_random** (bool): Proxy random.

            **Example:**

            ```python
            response = market.publishing.add(
                price=100,
                category_id=24,
                origin="autoreg",
                currency="rub",
                title="Telegram account",
                description="Public description",
                information="Private information"
            )
            print(response.json())
            ```
            """
            json = {
                "price": price,
                "category_id": category_id,
                "item_origin": origin,
                "currency": currency,
                "guarantee": guarantee,
                # Item
                "title": title,
                "title_en": title_en,
                "description": description,
                "information": information,
                "has_email_login_data": bool(email) if email and not isinstance(email, _NONE) else email,
                "email_login_data": email,
                "email_type": email_type,
                # Other
                "allow_ask_discount": allow_ask_discount,
                "proxy_id": proxy_id,
                "random_proxy": proxy_random
            }
            return await self.core.request("POST", "/item/add", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def check(
            self,
            item_id: int,
            login: str,
            password: str,
            resell_item_id: int = NONE,
            email: str = NONE,
            email_type: Literal["native", "autoreg"] = NONE,
            extra: dict[Constants.Market.Extra._Literal, str] = NONE
        ) -> Response:
            """
            POST https://api.lzt.market/{item_id}/goods/check

            *Checks the account for validity and finally making item available for purchase.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **login** (str): Login.
            - **password** (str): Password.
            - **resell_item_id** (int): Resell item ID.
            - **email** (str): Email.
            - **email_type** (str): Email type.
            - **extra** (dict[str, str]): Extra.

            **Example:**

            ```python
            response = market.publishing.check(
                item_id=1234567890,
                login="dc_id",
                password="auth_key"
            )
            print(response.json())
            ```
            """
            json = {
                "login": login,
                "password": password,
                "resell_item_id": resell_item_id,
                "has_email_login_data": bool(email) if email and not isinstance(email, _NONE) else email,
                "email_login_data": email,
                "email_type": email_type,
                "extra": extra
            }
            return await self.core.request("POST", f"/{item_id}/goods/check", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def mail(self, item_id: int, force_mail: bool = NONE, resell_item_id: int = NONE) -> Response:
            """
            GET https://api.lzt.market/{item_id}/goods/add

            *Get info about unpublished item. For categories that require temporary email, you will also get temporary email in response.*

            **Parameters:**

            - **item_id** (int): Item ID.
            - **force_mail** (bool): Force mail.
            - **resell_item_id** (int): Resell item ID.

            **Example:**

            ```python
            response = market.publishing.mail(item_id=1234567890)
            print(response.json())
            ```
            """
            params = {
                "forceTempEmail": force_mail,
                "resell_item_id": resell_item_id
            }
            return await self.core.request("GET", f"/{item_id}/goods/add", params=params)

    class __Profile:
        def __init__(self, core: "Market"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def get(self) -> Response:
            """
            GET https://api.lzt.market/me

            *Get info about your profile.*

            **Example:**

            ```python
            response = market.profile.get()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/me")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def edit(
            self,
            title: str = NONE,
            allow_ask_discount: bool = NONE,
            max_discount_percent: float = NONE,
            disable_steam_guard: bool = NONE,
            deauthorize_steam: bool = NONE,
            change_password_on_purchase: bool = NONE,
            hide_favorites: bool = NONE,
            show_too_low_price_change_warning: bool = NONE,
            allow_accept_accounts: list[str] = NONE,
            telegram_client: dict[str, str] = NONE
        ) -> Response:
            """
            POST https://api.lzt.market/me

            *Edit your profile.*

            **Parameters:**

            - **title** (str): Your market title.
            - **allow_ask_discount** (bool): Allow ask discount.
            - **max_discount_percent** (float): Max discount percent.
            - **disable_steam_guard** (bool): Disable steam guard.
            - **deauthorize_steam** (bool): Deauthorize steam.
            - **change_password_on_purchase** (bool): Change password on purchase.
            - **hide_favorites** (bool): Hide favorites.
            - **show_too_low_price_change_warning** (bool): Show too low price change warning.
            - **allow_transfer_accounts_from** (list[str]): Allow transfer accounts from.
            - **telegram_client** (dict[str, str]): Telegram client.

            **Example:**

            ```python
            response = market.profile.edit(
                title="I'am the best seller in da world",
                allow_ask_discount=True,
                max_discount_percent=25,
                change_password_on_purchase=True
            )
            print(response.json())
            ```
            """
            json = {
                "title": title,
                "user_allow_ask_discount": allow_ask_discount,
                "max_discount_percent": max_discount_percent,
                "disable_steam_guard": disable_steam_guard,
                "deauthorize_steam": deauthorize_steam,
                "change_password_on_purchase": change_password_on_purchase,
                "hide_favourites": hide_favorites,
                "show_too_low_price_change_warning": show_too_low_price_change_warning,
                "allow_accept_accounts": ",".join(allow_accept_accounts) if allow_accept_accounts else None
            }
            if not isinstance(telegram_client, _NONE):
                json["telegram_api_id"] = telegram_client.get("telegram_api_id", NONE)
                json["telegram_api_hash"] = telegram_client.get("telegram_api_hash", NONE)
                json["telegram_device_model"] = telegram_client.get("telegram_device_model", NONE)
                json["telegram_system_version"] = telegram_client.get("telegram_system_version", NONE)
                json["telegram_app_version"] = telegram_client.get("telegram_app_version", NONE)
                json["telegram_lang_pack"] = telegram_client.get("telegram_lang_pack", NONE)
                json["telegram_lang_code"] = telegram_client.get("telegram_lang_code", NONE)
                json["telegram_system_lang_code"] = telegram_client.get("telegram_system_lang_code", NONE)

            return await self.core.request("POST", "/me", json=json)

    class __Payments:
        def __init__(self, core: "Market"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def transfer(
            self,
            amount: float,
            secret_answer: str,
            currency: Constants.Market.Currency._Literal = "rub",
            user_id: int = NONE,
            username: str = NONE,
            comment: str = NONE,
            hold: int = NONE,
            hold_option: Constants.Market.HoldPeriod._Literal = NONE
        ) -> Response:
            """
            POST https://api.lzt.market/balance/transfer

            *Transfer money to another user.*

            **Parameters:**

            - **amount** (float): Amount to send in your currency.
            - **secret_answer** (str): Secret answer.
            - **currency** (str): Using currency for amount.
            - **user_id** (int): ID of user to transfer money.
            - **username** (str): Username to transfer money.
            - **comment** (str): Payment comment.
            - **hold** (int): Hold length.
            - **hold_option** (str): Hold option.

            **Example:**

            ```python
            response = market.payments.transfer(
                amount=100,
                currency="rub",
                secret_answer="secret_answer",
                user_id=2410024,
                comment="Payment comment",
                hold=10,
                hold_option="day"
            )
            print(response.json())
            ```
            """
            json = {
                "user_id": user_id,
                "username": username,
                "amount": amount,
                "currency": currency,
                "secret_answer": secret_answer,
                "comment": comment,
                "transfer_hold": bool(hold) if not isinstance(hold, _NONE) else hold,
                "hold_length_value": hold,
                "hold_length_option": hold_option
            }
            return await self.core.request("POST", "/balance/transfer", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def fee(self, amount: float) -> Response:
            """
            GET https://api.lzt.market/balance/transfer/fee

            *Calculate transfer fee.*

            **Parameters:**

            - **amount** (float): Amount you want to send in your currency.

            **Example:**

            ```python
            response = market.payments.fee(amount=5000)
            print(response.json())
            ```
            """
            params = {
                "amount": amount
            }
            return await self.core.request("GET", "/balance/transfer/fee", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def cancel(self, payment_id: int) -> Response:
            """
            POST https://api.lzt.market/balance/transfer/cancel

            *Cancel transfer.*
              > You can only cancel payments sended to you with hold.

            **Parameters:**

            - **payment_id** (int): Payment ID.

            **Example:**

            ```python
            response = market.payments.cancel(payment_id=1234567890)
            print(response.json())
            ```
            """
            json = {
                "payment_id": payment_id
            }
            return await self.core.request("POST", "/balance/transfer/cancel", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def history(self,
                          operation_type: Constants.Market.OperationTypes._Literal = NONE,
                          page: int = NONE,
                          min_amount: float = NONE,
                          max_amount: float = NONE,
                          operation_id_lt: int = NONE,
                          receiver: str = NONE,
                          sender: str = NONE,
                          comment: str = NONE,
                          hold: bool = NONE,
                          start_date: str = NONE,
                          end_date: str = NONE,
                          show_payment_stats: bool = NONE,
                          ) -> Response:
            """
            GET https://api.lzt.market/user/payments

            *Get your payments history.*

            **Parameters:**

            - **operation_type** (str): Operation type.
            - **page** (int): Page number.
            - **min_amount** (float): Minimum amount.
            - **max_amount** (float): Maximum amount.
            - **operation_id_lt** (int): Operation ID less than.
            - **receiver** (str): Receiver.
            - **sender** (str): Sender.
            - **comment** (str): Payment comment.
            - **hold** (bool): Hold transfer or not.
            - **start_date** (str): Start date.
            - **end_date** (str): End date.
            - **show_payment_stats** (bool): Show payment stats.

            **Example:**

            ```python
            response = market.payments.history(
                operation_type="income",
                min_amount=500,
                max_amount=500,
                comment="Payment comment",
                show_payment_stats=True
            )
            print(response.json())
            ```
            """
            params = {
                "type": operation_type,
                "page": page,
                "pmin": min_amount,
                "pmax": max_amount,
                "operation_id_lt": operation_id_lt,
                "receiver": receiver,
                "sender": sender,
                "comment": comment,
                "hold": hold,
                "start_date": start_date,
                "end_date": end_date,
                "show_payment_stats": show_payment_stats
            }
            return await self.core.request("GET", "/user/payments", params=params)

        @staticmethod
        def create_link(
            amount: float,
            user_id: int = NONE,
            username: str = NONE,
            comment: str = NONE,
            redirect_url: str = NONE,
            currency: Constants.Market.Currency._Literal = NONE,
            hold: int = NONE,
            hold_option: Constants.Market.HoldPeriod._Literal = NONE,
        ) -> str:
            """
            *Generate payment link.*

            **Parameters:**

            - **amount** (float): Amount to send in your currency.
            - **user_id** (int): ID of user to transfer money.
            - **username** (str): Username to transfer money.
            - **comment** (str): Payment comment.
            - **redirect_url** (str): Redirect url. User who paid on this link will be redirected to this url.
            - **currency** (str): Using currency for amount.
            - **hold** (int): Hold length in days.
              > Max length - 1 month.
            - **hold_option** (str): Hold period option.

            **Example:**

            ```python
            payment_link = market.payments.create_link(user_id=2410024, amount=250, comment="Comment", redirect_url="https://example.com")
            print(payment_link)
            #  https://lzt.market/balance/transfer?user_id=2410024&amount=250&comment=Comment&redirect=https%3A%2F%2Fexample.com
            ```
            """
            params = {
                "user_id": user_id,
                "username": username,
                "amount": amount,
                "comment": comment,
                "redirect": redirect_url,
                "currency": currency,
                "hold": bool(hold) if not isinstance(hold, _NONE) else hold,
                "hold_length_value": hold,
                "hold_length_option": hold_option,
            }
            url = URL("https://lzt.market/balance/transfer")
            params = _NONE.TrimNONE(params)
            url = url.copy_with(params=params)
            return str(url)

    class __Proxy:
        def __init__(self, core: "Market"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def get(self) -> Response:
            """
            GET https://api.lzt.market/proxy

            *Get your proxies.*

            **Example:**

            ```python
            response = market.proxies.get()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/proxy")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def add(self, proxy: Union[list, str]) -> Response:
            """
            POST https://api.lzt.market/proxy

            *Add proxies.*

            **Parameters:**

            - **proxy** (Union[list, str]): Single proxy or list of proxies.

            **Example:**

            ```python
            response = market.proxies.add(proxy=["login:password@192.168.1.0:8080", "login:password@192.168.1.1:8080"])
            print(response.json())
            ```
            """
            if isinstance(proxy, list):
                proxy = "\n".join(proxy)
            json = {
                "proxy_row": proxy
            }
            return await self.core.request("POST", "/proxy", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.5)
        async def delete(self, proxy_id: int = NONE, all: bool = NONE) -> Response:
            """
            DELETE https://api.lzt.market/proxy

            *Delete proxies.*

            **Parameters:**

            - **proxy_id** (int): Proxy ID.
            - **all** (bool): Delete all proxies.

            **Example:**

            ```python
            response = market.proxies.delete(all=True)
            print(response.json())
            ```
            """
            json = {
                "proxy_id": proxy_id,
                "delete_all": all
            }
            return await self.core.request("DELETE", "/proxy", json=json)

    @UNIVERSAL(batchable=False)
    @AutoDelay.WrapperSet(0.5)
    async def batch(self, jobs: list[dict[str, str]]) -> Response:
        """
        POST https://api.lzt.market/batch

        *Batch requests.*

        **Parameters:**

        - **jobs** (list[dict[str, str]]): Batch jobs.

        **Example:**

        ```python
        response = market.batch(jobs=[{"method": "GET", "url": "/1234567890", params: {}}])
        #  Also you can create jobs for almost all functions like this:
        #  job = market.managing.get.job(item_id=1234567890)
        print(response.json())

        #  You also can use executor to ease work with batch requests while you have a lot of jobs:
        jobs = [market.managing.get.job(item_id=1234567890) for _ in range(42)]
        while jobs:  # It will be running until all jobs will be executed
            jobs, response = market.batch.executor(jobs=jobs)
            print(response.json())
        ```
        """
        return await self.core.request("POST", "/batch", json=jobs)

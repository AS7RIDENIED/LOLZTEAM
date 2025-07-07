from .Base.Core import APIClient, AutoDelay, Response, _NONE, NONE
from .Base.Wrappers import UNIVERSAL
from .Base import Constants

from typing import Literal, Union
import builtins


class Forum(APIClient):
    """
    ### LOLZTEAM Forum API Client.

    You can view full class documentation here [click](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Forum.md)

    And also official documentation for LOLZTEAM Forum API is here [click](https://lolzteam.readme.io)

    ## 💛Made with love💛
    """

    def __init__(self, token: str, language: Literal["ru", "en"] = None, delay_min: float = 0, proxy: str = None, timeout: float = 90, verify: bool = True):
        """
        LOLZTEAM Forum API Client

        **Parameters:**

        - token (str): Your token.
          > You can get it [there](https://zelenka.guru/account/api)
        - language (Literal["ru", "en"]): Language of the API responses.
        - delay_min (float): Minimal delay between requests.
          > This parameter sets a strict minimal delay between your requests.
        - proxy (str): Proxy string.
          > protocol://ip:port or protocol://login:password@ip:port (socks5://login:password@192.168.1.1:8080 or http://login:password@192.168.1.1:8080)
        - timeout (float): Request timeout.

        ```python
        from LOLZTEAM.Client import Forum
        import asyncio

        token = "your_token"

        forum = Forum(token=token)

        forum.settings.logger.enable()                                        # -> Start logging
        forum.settings.delay.enable()                                         # Enable delay (btw delay is enabled by default)

        response = forum.users.get(user_id=2410024)                           # Sync request
        job = forum.users.get.job(user_id=2410024)                            # Job creation (Always SYNC)
        response = forum.request("GET", "/users/2410024")                     # Custom request
        job = forum.request.job("GET", "/users/2410024")                      # Job creation for custom request

        async def async_example():
            response = await forum.users.get(user_id=2410024)                 # Async request
            job = forum.users.get.job(user_id=2410024)                        # Job creation (Always SYNC)
            response = await forum.request("GET", "/users/2410024")           # Custom async request
            job = forum.request.job("GET", "/users/2410024")                  # Job creation for custom request

        asyncio.run(async_example())

        # You should just add ".job" between function name and parentheses to create a job.
        # You can't create a job for methods that are uploading files (like avatar/background) and ofc not for forum.batch(...) method.
        # P.s Your IDE probably may not show that ".job" function exists but it does.

        forum.settings.token = "token"                                        # Change token
        forum.settings.language = "en"                                        # Change language
        forum.settings.proxy = "http://login:password@192.168.1.1:8080"       # Change proxy
        forum.settings.delay.min = 1                                          # Change minimal delay
        forum.settings.delay.disable()                                        # Disable delay
        forum.settings.logger.disable()                                       # <- Stop logging
        ```
        """
        super().__init__(
            base_url="https://prod-api.lolz.live",
            token=token,
            language=language,
            delay_min=delay_min,
            logger_name=Forum.__qualname__,
            proxy=proxy,
            timeout=timeout,
            verify=verify
        )
        self.categories = self.__Categories(self)
        self.forums = self.__Forums(self)
        self.pages = self.__Pages(self)
        self.threads = self.__Threads(self)
        self.posts = self.__Posts(self)
        self.users = self.__Users(self)
        self.conversations = self.__Conversations(self)
        self.notifications = self.__Notifications(self)
        self.tags = self.__Tags(self)
        self.search = self.__Search(self)
        self.chat = self.__Chat(self)
        self.forms = self.__Forms(self)

    class __Categories:
        def __init__(self, core: "Forum"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self, parent_category_id: int = NONE, parent_forum_id: int = NONE, order: Literal["natural", "list"] = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/categories

            *Get categories.*

            **Parameters:**

            - parent_category_id (int): Parent category ID.
            - parent_forum_id (int): Parent forum ID.
            - order (str): Order of the categories.

            **Example:**

            ```python
            response = forum.categories.list(parent_category_id=1, parent_forum_id=1, order="natural")
            print(response.json())
            ```
            """
            params = {"parent_category_id": parent_category_id, "parent_forum_id": parent_forum_id, "order": order}
            return await self.core.request("GET", "/categories", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, category_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/categories/{category_id}

            *Get category.*

            **Parameters:**

            - category_id (int): Category ID.

            **Example:**

            ```python
            response = forum.categories.get(category_id=1)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/categories/{category_id}")

    class __Forums:
        def __init__(self, core: "Forum"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self, parent_category_id: int = NONE, parent_forum_id: int = NONE, order: Literal["natural", "list"] = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/forums

            *Get forums.*

            **Parameters:**

            - parent_category_id (int): Parent category ID.
            - parent_forum_id (int): Parent forum ID.
            - order (str): Order of the forums.

            **Example:**

            ```python
            response = forum.forums.list()
            print(response.json())
            ```
            """
            params = {"parent_category_id": parent_category_id, "parent_forum_id": parent_forum_id, "order": order}
            return await self.core.request("GET", "/forums", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, forum_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/forums/{forum_id}

            *Get forum.*

            **Parameters:**

            - forum_id (int): Forum ID.

            **Example:**

            ```python
            response = forum.forums.get(forum_id=876)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/forums/{forum_id}")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def followers(self, forum_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/forums/{forum_id}/followers

            *Get forum followers.*

            **Parameters:**

            - forum_id (int): Forum ID.

            **Example:**

            ```python
            response = forum.forums.followers(forum_id=876)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/forums/{forum_id}/followers")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def followed(self, total: bool = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/forums/followed

            *Get followed forums.*

            **Parameters:**

            - total (bool): Get total count of followed forums.

            **Example:**

            ```python
            response = forum.forums.followed(total=True)
            print(response.json())
            ```
            """
            params = {"total": total}
            return await self.core.request("GET", "/forums/followed", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def follow(self, forum_id: int,
                         post: bool = NONE,
                         alert: bool = NONE,
                         email: bool = NONE,
                         prefix_ids: builtins.list[int] = NONE,
                         minimal_contest_amount: float = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/forums/{forum_id}/followers

            *Follow forum.*

            **Parameters:**

            - post (bool): Get post notifications.
            - alert (bool): Get alert notifications.
            - email (bool): Get email notifications.
            - prefix_ids (list[int]): Prefix IDs.
            - minimal_contest_amount (float): Minimal contest amount.

            **Example:**

            ```python
            response = forum.forums.follow(forum_id=876, post=True, alert=True, email=False)
            print(response.json())
            ```
            """
            json = {"post": post, "alert": alert, "email": email, "prefix_ids": prefix_ids, "minimal_contest_amount": minimal_contest_amount}
            return await self.core.request("POST", f"/forums/{forum_id}/followers", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def unfollow(self, forum_id: int) -> Response:
            """
            DELETE https://prod-api.lolz.live/forums/{forum_id}/followers

            *Unfollow forum.*

            **Parameters:**

            - forum_id (int): Forum ID.

            **Example:**

            ```python
            response = forum.forums.unfollow(forum_id=876)
            print(response.json())
            ```
            """
            return await self.core.request("DELETE", f"/forums/{forum_id}/followers")

    class __Pages:
        def __init__(self, core: "Forum"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self) -> Response:
            """
            GET https://prod-api.lolz.live/pages

            *Get pages.*

            **Example:**

            ```python
            response = forum.pages.list()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/pages")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, page_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/pages/{page_id}

            *Get page.*

            **Parameters:**

            - page_id (int): Page ID.

            **Example:**

            ```python
            response = forum.pages.get(page_id=1)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/pages/{page_id}")

    class __Threads:

        class __Contests:
            def __init__(self, core: "Forum"):
                self.core = core
                self.money = self.__Money(self.core)
                self.upgrade = self.__Upgrade(self.core)

            class __Money:
                def __init__(self, core: "Forum"):
                    self.core = core

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def create_by_time(
                    self,
                    post_body: str,
                    prize_amount: float,
                    winners_count: int,
                    length: int,
                    length_option: Constants.Forum.Contests.Length._Literal,
                    require_week_sympathy: int,
                    require_total_sympathy: int,
                    secret_answer: str,
                    reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                    title: str = NONE,
                    title_en: str = NONE,
                    tags: list[str] = NONE,
                    hide_contacts: bool = NONE,
                    allow_ask_hidden_content: bool = NONE,
                    comment_ignore_group: bool = NONE,
                    dont_alert_followers: bool = NONE,
                    forum_notifications: bool = True,
                    email_notifications: bool = False,
                ) -> Response:
                    """
                    POST https://prod-api.lolz.live/threads

                    *Create a money contest.*

                    **Parameters:**

                    - post_body (str): Content of the new contest.
                    - prize_amount (float): How much money will each winner receive.
                    - winners_count (int): Winner count (prize count).
                        > The maximum value is 100.
                    - length (int): Contest duration value.
                        > The maximum duration is 3 days.
                    - length_option (str): Contest duration type.
                        > Can be [minutes, hours, days]. The maximum duration is 3 days.
                    - require_week_sympathy (int): Sympathies for this week.
                    - require_total_sympathy (int): Symapthies for all time.
                    - secret_answer (str): Secret answer of your account.
                    - reply_group (int): Allow to reply only users with chosen or higher group.
                    - title (str): Thread title.
                        > Can be skipped if title_en set.
                    - title_en (str): Thread title in english.
                        > Can be skipped if title set.
                    - tags (list[str]): Thread tags.
                    - hide_contacts (bool): Hide contacts.
                    - allow_ask_hidden_content (bool): Allow ask hidden content.
                    - comment_ignore_group (bool): Allow commenting if user can't post in thread.
                    - dont_alert_followers (bool): Don't alert followers.
                    - forum_notifications (bool): Get forum notifications.
                    - email_notifications (bool): Get email notifications.

                    **Example:**

                    ```python
                    response = forum.threads.contests.money.create_by_time(
                        post_body="Contest",
                        prize_amount=500,
                        winners_count=1,
                        length=3,
                        length_option="days",
                        require_week_sympathy=1,
                        require_total_sympathy=50,
                        secret_answer="My secret answer",
                        title="Contest"
                    )
                    print(response.json())
                    ```
                    """
                    json = {
                        "prize_data_money": prize_amount,
                        "count_winners": winners_count,
                        "length_value": length,
                        "length_option": length_option,
                        "require_like_count": require_week_sympathy,
                        "require_total_like_count": require_total_sympathy,
                        "secret_answer": secret_answer,
                        "contest_type": "by_finish_date",
                        "prize_type": "money",
                        "forum_id": 766,
                        "post_body": post_body,
                        "title": title,
                        "title_en": title_en,
                        "tags": ",".join(tags) if not isinstance(tags, _NONE) else tags,
                        "reply_group": reply_group,
                        "hide_contacts": hide_contacts,
                        "allow_ask_hidden_content": allow_ask_hidden_content,
                        "comment_ignore_group": comment_ignore_group,
                        "dont_alert_followers": dont_alert_followers,
                        "watch_thread_state": True if any([forum_notifications if not isinstance(forum_notifications, _NONE) else None, email_notifications if not isinstance(email_notifications, _NONE) else None]) else False,
                        "watch_thread": forum_notifications,
                        "watch_thread_email": email_notifications
                    }
                    return await self.core.request("POST", "/threads", json=json)

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def create_by_count(
                    self,
                    post_body: str,
                    prize_amount: float,
                    winners_count: int,
                    needed_members: int,
                    require_week_sympathy: int,
                    require_total_sympathy: int,
                    secret_answer: str,
                    reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                    title: str = NONE,
                    title_en: str = NONE,
                    tags: list[str] = NONE,
                    hide_contacts: bool = NONE,
                    allow_ask_hidden_content: bool = NONE,
                    comment_ignore_group: bool = NONE,
                    dont_alert_followers: bool = NONE,
                    forum_notifications: bool = True,
                    email_notifications: bool = False,
                ) -> Response:
                    """
                    POST https://prod-api.lolz.live/threads

                    *Create a money contest.*

                    **Parameters:**

                    - post_body (str): Content of the new contest.
                    - prize_amount (float): How much money will each winner receive.
                    - winners_count (int): Winner count (prize count).
                    - needed_members (int): Max member count.
                    - require_week_sympathy (int): Sympathies for this week.
                    - require_total_sympathy (int): Symapthies for all time.
                    - secret_answer (str): Secret answer of your account.
                    - reply_group (int): Allow to reply only users with chosen or higher group.
                    - title (str): Thread title.
                        > Can be skipped if title_en set.
                    - title_en (str): Thread title in english.
                        > Can be skipped if title set.
                    - tags (list[str]): Thread tags.
                    - hide_contacts (bool): Hide contacts.
                    - allow_ask_hidden_content (bool): Allow ask hidden content.
                    - comment_ignore_group (bool): Allow commenting if user can't post in thread.
                    - dont_alert_followers (bool): Don't alert followers.
                    - forum_notifications (bool): Get forum notifications.
                    - email_notifications (bool): Get email notifications.

                    **Example:**

                    ```python
                    response = forum.threads.contests.money.create_by_count(post_body="Contest", prize_amount=500, winners_count=1,
                                                                           needed_members=300, require_week_sympathy=1, require_total_sympathy=50,
                                                                           secret_answer="My secret answer", title="Contest")
                    print(response.json())
                    ```
                    """
                    json = {
                        "prize_data_money": prize_amount,
                        "count_winners": winners_count,
                        "needed_members": needed_members,
                        "require_like_count": require_week_sympathy,
                        "require_total_like_count": require_total_sympathy,
                        "secret_answer": secret_answer,
                        "contest_type": "by_needed_members",
                        "prize_type": "money",
                        "forum_id": 766,
                        "post_body": post_body,
                        "title": title,
                        "title_en": title_en,
                        "tags": ",".join(tags) if not isinstance(tags, _NONE) else tags,
                        "reply_group": reply_group,
                        "hide_contacts": hide_contacts,
                        "allow_ask_hidden_content": allow_ask_hidden_content,
                        "comment_ignore_group": comment_ignore_group,
                        "dont_alert_followers": dont_alert_followers,
                        "watch_thread_state": True if any([forum_notifications if not isinstance(forum_notifications, _NONE) else None, email_notifications if not isinstance(email_notifications, _NONE) else None]) else False,
                        "watch_thread": forum_notifications,
                        "watch_thread_email": email_notifications
                    }
                    return await self.core.request("POST", "/threads", json=json)

            class __Upgrade:
                def __init__(self, core: "Forum"):
                    self.core = core

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def create_by_time(
                    self,
                    post_body: str,
                    prize_group: Constants.Forum.Contests.UpgradePrize._Literal,
                    winners_count: int,
                    length: int,
                    length_option: Constants.Forum.Contests.Length._Literal,
                    require_week_sympathy: int,
                    require_total_sympathy: int,
                    secret_answer: str,
                    reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                    title: str = NONE,
                    title_en: str = NONE,
                    tags: list[str] = NONE,
                    hide_contacts: bool = NONE,
                    allow_ask_hidden_content: bool = NONE,
                    comment_ignore_group: bool = NONE,
                    dont_alert_followers: bool = NONE,
                    forum_notifications: bool = True,
                    email_notifications: bool = False,
                ) -> Response:
                    """
                    POST https://prod-api.lolz.live/threads

                    *Create a new contest.*

                    **Parameters:**

                    - post_body (str): Content of the new contest.
                    - prize_group (Constants.Forum.Contests.UpgradePrize._Literal): Which upgrade will each winner receive.
                    - winners_count (int): Winner count (prize count).
                        > The maximum value is 100.
                    - length (int): Contest duration value.
                        > The maximum duration is 3 days.
                    - length_option (Constants.Forum.Contests.Length._Literal): Contest duration type.
                        > Can be [minutes, hours, days]. The maximum duration is 3 days.
                    - require_week_sympathy (int): Sympathies for this week.
                    - require_total_sympathy (int): Sympathies for all time.
                    - secret_answer (str): Secret answer of your account.
                    - reply_group (Constants.Forum.ReplyGroups._Literal): Allow to reply only users with chosen or higher group.
                    - title (str): Thread title.
                        > Can be skipped if title_en set.
                    - title_en (str): Thread title in english.
                        > Can be skipped if title set.
                    - tags (list[str]): Thread tags.
                    - hide_contacts (bool): Hide contacts.
                    - allow_ask_hidden_content (bool): Allow ask hidden content.
                    - comment_ignore_group (bool): Allow commenting if user can't post in thread.
                    - dont_alert_followers (bool): Don't alert followers.
                    - forum_notifications (bool): Get forum notifications.
                    - email_notifications (bool): Get email notifications.

                    **Example:**

                    ```python
                    response = forum.threads.contests.upgrade.create_by_time(post_body="Contest", prize_group=1, winners_count=1,
                                                                           length=3, length_option="days", require_week_sympathy=1,
                                                                           require_total_sympathy=50, secret_answer="My secret answer", title="Contest")
                    print(response.json())
                    ```
                    """

                    json = {
                        "prize_data_upgrade": prize_group,
                        "count_winners": winners_count,
                        "length_value": length,
                        "length_option": length_option,
                        "require_like_count": require_week_sympathy,
                        "require_total_like_count": require_total_sympathy,
                        "secret_answer": secret_answer,
                        "contest_type": "by_finish_date",
                        "prize_type": "upgrades",
                        "forum_id": 766,
                        "post_body": post_body,
                        "title": title,
                        "title_en": title_en,
                        "tags": ",".join(tags) if not isinstance(tags, _NONE) else tags,
                        "reply_group": reply_group,
                        "hide_contacts": hide_contacts,
                        "allow_ask_hidden_content": allow_ask_hidden_content,
                        "comment_ignore_group": comment_ignore_group,
                        "dont_alert_followers": dont_alert_followers,
                        "watch_thread_state": True if any([forum_notifications if not isinstance(forum_notifications, _NONE) else None, email_notifications if not isinstance(email_notifications, _NONE) else None]) else False,
                        "watch_thread": forum_notifications,
                        "watch_thread_email": email_notifications
                    }
                    return await self.core.request("POST", "/threads", json=json)

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def create_by_count(
                    self,
                    post_body: str,
                    prize_group: Constants.Forum.Contests.UpgradePrize._Literal,
                    winners_count: int,
                    needed_members: int,
                    require_week_sympathy: int,
                    require_total_sympathy: int,
                    secret_answer: str,
                    reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                    title: str = NONE,
                    title_en: str = NONE,
                    tags: list[str] = NONE,
                    hide_contacts: bool = NONE,
                    allow_ask_hidden_content: bool = NONE,
                    comment_ignore_group: bool = NONE,
                    dont_alert_followers: bool = NONE,
                    forum_notifications: bool = True,
                    email_notifications: bool = False,
                ) -> Response:
                    """
                    POST https://prod-api.lolz.live/threads

                    *Create a new contest.*

                    **Parameters:**

                    - post_body (str): Content of the new contest.
                    - prize_group (Constants.Forum.Contests.UpgradePrize._Literal): Which upgrade will each winner receive.
                    - winners_count (int): Winner count (prize count).
                        > The maximum value is 100.
                    - needed_members (int): Max member count.
                    - require_week_sympathy (int): Sympathies for this week.
                    - require_total_sympathy (int): Sympathies for all time.
                    - secret_answer (str): Secret answer of your account.
                    - reply_group (Constants.Forum.ReplyGroups._Literal): Allow to reply only users with chosen or higher group.
                    - title (str): Thread title.
                        > Can be skipped if title_en set.
                    - title_en (str): Thread title in english.
                        > Can be skipped if title set.
                    - tags (list[str]): Thread tags.
                    - hide_contacts (bool): Hide contacts.
                    - allow_ask_hidden_content (bool): Allow ask hidden content.
                    - comment_ignore_group (bool): Allow commenting if user can't post in thread.
                    - dont_alert_followers (bool): Don't alert followers.
                    - forum_notifications (bool): Get forum notifications.
                    - email_notifications (bool): Get email notifications.

                    **Example:**

                    ```python
                    response = forum.threads.contests.upgrade.create_by_count(post_body="Contest", prize_group=1, winners_count=1,
                                                                           needed_members=300, require_week_sympathy=1,
                                                                           require_total_sympathy=50, secret_answer="My secret answer", title="Contest")
                    print(response.json())
                    ```
                    """
                    json = {
                        "prize_data_upgrade": prize_group,
                        "count_winners": winners_count,
                        "needed_members": needed_members,
                        "require_like_count": require_week_sympathy,
                        "require_total_like_count": require_total_sympathy,
                        "secret_answer": secret_answer,
                        "contest_type": "by_needed_members",
                        "prize_type": "upgrades",
                        "forum_id": 766,
                        "post_body": post_body,
                        "title": title,
                        "title_en": title_en,
                        "tags": ",".join(tags) if not isinstance(tags, _NONE) else tags,
                        "reply_group": reply_group,
                        "hide_contacts": hide_contacts,
                        "allow_ask_hidden_content": allow_ask_hidden_content,
                        "comment_ignore_group": comment_ignore_group,
                        "dont_alert_followers": dont_alert_followers,
                        "watch_thread_state": True if any([forum_notifications if not isinstance(forum_notifications, _NONE) else None, email_notifications if not isinstance(email_notifications, _NONE) else None]) else False,
                        "watch_thread": forum_notifications,
                        "watch_thread_email": email_notifications
                    }
                    return await self.core.request("POST", "/threads", json=json)

        class __Arbitrage:
            def __init__(self, core: "Forum"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def market(
                self,
                responder: str,
                item_id: Union[str, int],
                amount: float,
                post_body: str,
                currency: Constants.Market.Currency._Literal = NONE,
                conversation_screenshot: str = "no",
                tags: list[str] = NONE,
                hide_contacts: bool = NONE,
                allow_ask_hidden_content: bool = NONE,
                dont_alert_followers: bool = NONE,
                forum_notifications: bool = True,
                email_notifications: bool = NONE,
            ) -> Response:
                """
                POST https://prod-api.lolz.live/claims

                *Create a Arbitrage.*

                **Parameters:**

                - responder (str): To whom the complaint is filed. Specify a nickname or a link to the profile.
                - item_id (str|int): Write account link or item_id.
                - amount (float): Amount by which the responder deceived you.
                - post_body (str): You should describe what's happened.
                - currency (str): Currency of Arbitrage.
                - conversation_screenshot (str): Screenshot showing the respondent's Telegram login. If the correspondence was conducted in Telegram, upload screenshot that will display the respondent's Telegram login against the background of your dialogue. The screenshot must be uploaded to Imgur. If the correspondence was conducted elsewhere, write "no".
                - tags (list[str]): Thread tags.
                - hide_contacts (bool): Hide contacts.
                - allow_ask_hidden_content (bool): Allow ask hidden content.
                - dont_alert_followers (bool): Don't alert followers.
                - forum_notifications (bool): Get forum notifications.
                - email_notifications (bool): Get email notifications.

                **Example:**

                ```python
                response = forum.threads.arbitrage.market(responder="AS7RID", item_id=1000000, amount=1000,
                                                          post_body="Arbitrage test", currency="rub")
                print(response.json())
                ```
                """
                json = {
                    "post_body": post_body,
                    "as_responder": responder,
                    "as_is_market_deal": 1,
                    "as_market_item_id": item_id,
                    "as_amount": amount,
                    "currency": currency,
                    "as_funds_receipt": "no",
                    "as_tg_login_screenshot": conversation_screenshot,
                    "tags": ",".join(tags) if not isinstance(tags, _NONE) else tags,
                    "hide_contacts": hide_contacts,
                    "allow_ask_hidden_content": allow_ask_hidden_content,
                    "dont_alert_followers": dont_alert_followers,
                    "watch_thread_state": True if any([forum_notifications if not isinstance(forum_notifications, _NONE) else None, email_notifications if not isinstance(email_notifications, _NONE) else None]) else False,
                    "watch_thread": forum_notifications,
                    "watch_thread_email": email_notifications
                }
                return await self.core.request("POST", "/claims", json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def non_market(
                self,
                responder: str,
                amount: float,
                receipt: str,
                post_body: str,
                pay_claim: Literal["now", "later"] = "later",
                conversation_screenshot: str = "no",
                responder_data: str = NONE,
                currency: Constants.Market.Currency._Literal = NONE,
                transfer_type: Constants.Forum.Arbitrage.TransferType._Literal = "notsafe",
                tags: list[str] = NONE,
                hide_contacts: bool = NONE,
                allow_ask_hidden_content: bool = NONE,
                dont_alert_followers: bool = NONE,
                forum_notifications: bool = True,
                email_notifications: bool = NONE,
            ) -> Response:
                """
                POST https://prod-api.lolz.live/claims

                *Create a Arbitrage.*


                **Parameters:**

                - responder (str): To whom the complaint is filed. Specify a nickname or a link to the profile.
                - amount (float): Amount by which the responder deceived you.
                - receipt (str): Funds transfer recipient. Upload a receipt for the transfer of funds, use the "View receipt" button in your wallet. Must be uploaded to Imgur. Write "no" if you have not paid.
                - post_body (str): You should describe what's happened.
                - pay_claim (str): If you set this parameter to "now" forum will automatically calculate the amount and debit it from your account.
                    > For filing claims, it is necessary to make a contribution in the amount of 5% of the amount of damage (but not less than 50 rubles and not more than 5000 rubles). For example, for an amount of damage of 300 rubles, you will need to pay 50 rubles, for 2,000 and 10,000 rubles - 100 and 500 rubles, respectively).
                - conversation_screenshot (str): Screenshot showing the respondent's Telegram login. If the correspondence was conducted in Telegram, upload screenshot that will display the respondent's Telegram login against the background of your dialogue. The screenshot must be uploaded to Imgur. If the correspondence was conducted elsewhere, write "no".
                - responder_data (str): Contacts and wallets of the responder. Specify the known data about the responder (Skype, Vkontakte, Qiwi, WebMoney, etc.), if any.
                - currency (str): Currency of Arbitrage.
                - transfer_type (str): The transaction took place through a guarantor or there was a transfer to the market with a hold?
                - tags (list[str]): Thread tags.
                - hide_contacts (bool): Hide contacts.
                - allow_ask_hidden_content (bool): Allow ask hidden content.
                - comment_ignore_group (bool): Allow commenting if user can't post in thread.
                - dont_alert_followers (bool): Don't alert followers.
                - reply_group (int): Allow to reply only users with chosen or higher group.
                - forum_notifications (bool): Get forum notifications.
                - email_notifications (bool): Get email notifications.

                **Example:**

                ```python
                response = forum.threads.arbitrage.non_market(responder="AS7RID", amount=100, currency="rub", receipt="no",
                                                              post_body="Non market arbitrage", pay_claim="now", transfer_type="notsafe")
                print(response.json())
                ```
                """
                json = {
                    "post_body": post_body,
                    "as_responder": responder,
                    "as_is_market_deal": 0,
                    "as_amount": amount,
                    "currency": currency,
                    "as_data": responder_data,
                    "pay_claim": pay_claim,
                    "transfer_type": transfer_type,
                    "as_funds_receipt": receipt,
                    "as_tg_login_screenshot": conversation_screenshot,
                    "tags": ",".join(tags) if not isinstance(tags, _NONE) else tags,
                    "hide_contacts": hide_contacts,
                    "allow_ask_hidden_content": allow_ask_hidden_content,
                    "dont_alert_followers": dont_alert_followers,
                    "watch_thread_state": True if any([forum_notifications if not isinstance(forum_notifications, _NONE) else None, email_notifications if not isinstance(email_notifications, _NONE) else None]) else False,
                    "watch_thread": forum_notifications,
                    "watch_thread_email": email_notifications
                }
                return await self.core.request("POST", "/claims", json=json)

        class __Poll:
            def __init__(self, core: "Forum"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def get(self, thread_id: int) -> Response:
                """
                GET https://prod-api.lolz.live/threads/{thread_id}/poll

                *Get poll.*

                **Parameters:**

                - thread_id (int): Thread ID.

                **Example:**

                ```python
                response = forum.threads.poll.get(thread_id=5523020)
                print(response.json())
                ```
                """
                return await self.core.request("GET", f"/threads/{thread_id}/poll")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def vote(self, thread_id: int, option_ids: Union[builtins.list[int], int]) -> Response:
                """
                POST https://prod-api.lolz.live/threads/{thread_id}/poll/votes

                *Vote in poll.*

                **Parameters:**

                - thread_id (int): Thread ID.
                - option_ids (list[int] | int): Option IDs.

                **Example:**

                ```python
                response = forum.threads.poll.vote(thread_id=5523020, option_ids=[1, 2, 3])
                print(response.json())
                ```
                """
                json = {"response_ids": option_ids}
                return await self.core.request("POST", f"/threads/{thread_id}/poll/votes", json=json)

        def __init__(self, core: "Forum"):
            self.core = core
            self.poll = self.__Poll(self.core)
            self.contests = self.__Contests(self.core)
            self.arbitrage = self.__Arbitrage(self.core)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list_unread(self, forum_id: int = NONE,
                              limit: int = NONE,
                              data_limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/threads/new

            *Get unread threads.*

            **Parameters:**

            - forum_id (int): Forum ID.
            - limit (int): Limit of threads.
            - data_limit (int): Limit of data.

            **Example:**

            ```python
            response = forum.threads.list_unread(forum_id=876, limit=10, data_limit=10)
            print(response.json())
            ```
            """
            params = {"forum_id": forum_id, "limit": limit, "data_limit": data_limit}
            return await self.core.request("GET", "/threads/new", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list_recent(self, days: int = NONE,
                              forum_id: int = NONE,
                              limit: int = NONE,
                              data_limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/threads/recent

            *Get recent threads.*

            **Parameters:**

            - days (int): Maximum number of days to search for threads.
            - forum_id (int): Forum ID.
            - limit (int): Limit of threads.
            - data_limit (int): Limit of data.

            **Example:**

            ```python
            response = forum.threads.list_recent(days=1, forum_id=876, limit=10, data_limit=10)
            print(response.json())
            ```
            """
            params = {"days": days, "forum_id": forum_id, "limit": limit, "data_limit": data_limit}
            return await self.core.request("GET", "/threads/recent", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self, forum_id: int,
                       user_id: int = NONE,
                       prefix_id: int = NONE,
                       tag_id: int = NONE,
                       page: int = NONE,
                       limit: int = NONE,
                       sticky: bool = NONE,
                       order: Constants.Forum.ThreadOrder._Literal = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/threads

            *Get threads.*

            **Parameters:**

            - forum_id (int): Forum ID.
            - user_id (int): Filter to get only threads created by the specified user.
            - prefix_id (int): Filter to get only threads with the specified prefix.
            - tag_id (int): Filter to get only threads with the specified tag.
            - page (int): Page.
            - limit (int): Limit of threads.
            - order (str): Order of threads.
            - sticky (bool): Filter to get only sticky or non-sticky threads. By default, all threads will be included and sticky ones will be at the top of the result on the first page.

            **Example:**
            """
            params = {
                "forum_id": forum_id,
                "creator_user_id": user_id,
                "thread_prefix_id": prefix_id,
                "thread_tag_id": tag_id,
                "page": page,
                "limit": limit,
                "sticky": sticky,
                "order": order
            }
            return await self.core.request("GET", "/threads", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, thread_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/threads/{thread_id}

            *Get thread.*

            **Parameters:**

            - thread_id (int): Thread ID.

            **Example:**

            ```python
            response = forum.threads.get(thread_id=5523020)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/threads/{thread_id}")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def create(self, forum_id: int,
                         post_body: str,
                         title: str = NONE,
                         title_en: str = NONE,
                         prefix_ids: builtins.list[int] = NONE,
                         tags: builtins.list[int] = NONE,
                         hide_contacts: bool = NONE,
                         allow_ask_hidden_content: bool = NONE,
                         reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                         comment_ignore_group: bool = NONE,
                         dont_alert_followers: bool = NONE,
                         forum_notifications: bool = NONE,
                         email_notifications: bool = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/threads

            *Create a thread.*

            **Parameters:**

            - forum_id (int): Forum ID.
            - post_body (str): Content of the new thread.
            - title (str): Title.
            - title_en (str): Title in English.
            - prefix_ids (list[int]): Prefix IDs.
            - tags (list[int]): Tags.
            - reply_group (int): Reply group.
            - hide_contacts (bool): Hide contacts.
            - allow_ask_hidden_content (bool): Allow ask hidden content.
            - comment_ignore_group (bool): Comment ignore group.
            - dont_alert_followers (bool): Don't alert followers.
            - forum_notifications (bool): Get forum notifications.
            - email_notifications (bool): Get email notifications.

            **Example:**

            ```python
            response = forum.threads.create(
                forum_id=876,
                post_body="Test thread",
                title="Test thread",
                title_en="Test thread",
                prefix_ids=[1, 2, 3],
                tags=["tag1", "tag2", "tag3"],
                reply_group=2,
                hide_contacts=False,
                allow_ask_hidden_content=False,
                comment_ignore_group=False,
                dont_alert_followers=False,
                forum_notifications=True,
                email_notifications=False
            )
            print(response.json())
            ```
            """
            json = {"forum_id": forum_id,
                    "post_body": post_body,
                    "title": title,
                    "title_en": title_en,
                    "prefix_id": prefix_ids,
                    "tags": ",".join(tags) if not isinstance(tags, _NONE) else tags,
                    "reply_group": reply_group,
                    "hide_contacts": hide_contacts,
                    "allow_ask_hidden_content": allow_ask_hidden_content,
                    "comment_ignore_group": comment_ignore_group,
                    "dont_alert_followers": dont_alert_followers,
                    "watch_thread_state": True if any([forum_notifications if not isinstance(forum_notifications, _NONE) else None, email_notifications if not isinstance(email_notifications, _NONE) else None]) else False,
                    "watch_thread": forum_notifications,
                    "watch_thread_email": email_notifications
                    }
            return await self.core.request("POST", "/threads", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def edit(self, thread_id: int,
                       title: str = NONE,
                       title_en: str = NONE,
                       post_body: str = NONE,
                       prefix_ids: builtins.list[int] = NONE,
                       tags: builtins.list[int] = NONE,
                       discussion_state: bool = NONE, hide_contacts: bool = NONE,
                       allow_ask_hidden_content: bool = NONE,
                       reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                       comment_ignore_group: bool = NONE) -> Response:
            """
            PUT https://prod-api.lolz.live/threads/{thread_id}

            *Edit a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.
            - title (str): Title.
            - title_en (str): Title in English.
            - post_body (str): Post body.
            - prefix_ids (list[int]): Prefix IDs.
            - tags (list[int]): Tags.
            - discussion_state (bool): Discussion state.
            - hide_contacts (bool): Hide contacts.
            - allow_ask_hidden_content (bool): Allow ask hidden content.
            - reply_group (int): Reply group.
            - comment_ignore_group (bool): Comment ignore group.

            **Example:**

            ```python
            response = forum.threads.edit(
                thread_id=5523020,
                title="Test thread",
                title_en="Test thread",
                post_body="Test thread",
                prefix_ids=[1, 2, 3],
                tags=["tag1", "tag2", "tag3"],
                discussion_state=True,
                hide_contacts=False,
                allow_ask_hidden_content=False,
                reply_group=2,
                comment_ignore_group=False
            )
            print(response.json())
            ```
            """
            json = {"title": title,
                    "title_en": title_en,
                    "post_body": post_body,
                    "prefix_id": prefix_ids,
                    "tags": ",".join(tags) if not isinstance(tags, _NONE) else tags,
                    "discussion_state": discussion_state,
                    "hide_contacts": hide_contacts,
                    "allow_ask_hidden_content": allow_ask_hidden_content,
                    "reply_group": reply_group,
                    "comment_ignore_group": comment_ignore_group}
            return await self.core.request("PUT", f"/threads/{thread_id}", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def delete(self, thread_id: int, reason: str = NONE) -> Response:
            """
            DELETE https://prod-api.lolz.live/threads/{thread_id}

            *Delete a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.
            - reason (str): Reason.

            **Example:**

            ```python
            response = forum.threads.delete(thread_id=5523020, reason="Test reason")
            print(response.json())
            ```
            """
            json = {"reason": reason}
            return await self.core.request("DELETE", f"/threads/{thread_id}", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def bump(self, thread_id: int) -> Response:
            """
            POST https://prod-api.lolz.live/threads/{thread_id}/bump

            *Bump a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.

            **Example:**

            ```python
            response = forum.threads.bump(thread_id=5523020)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/threads/{thread_id}/bump")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def move(self, thread_id: int, forum_id: int, title: str = NONE, title_en: str = NONE, prefix_ids: builtins.list[int] = NONE, send_alert: bool = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/threads/{thread_id}/move

            *Move a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.
            - forum_id (int): Target forum ID.
            - title (str): Title.
            - title_en (str): Title in English.
            - prefix_ids (list[int]): Prefix IDs.
            - send_alert (bool): Send alert.

            **Example:**

            ```python
            response = forum.threads.move(thread_id=5523020, forum_id=876, title="Test thread", title_en="Test thread", prefix_ids=[1, 2, 3], send_alert=True)
            print(response.json())
            ```
            """
            json = {
                "forum_id": forum_id,
                "title": title,
                "title_en": title_en,
                "prefix_id": prefix_ids,
                "apply_thread_prefix": True if prefix_ids and not isinstance(prefix_ids, _NONE) else NONE,
                "send_alert": send_alert
            }
            return await self.core.request("POST", f"/threads/{thread_id}/move", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def followers(self, thread_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/threads/{thread_id}/followers

            *Get followers of a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.

            **Example:**

            ```python
            response = forum.threads.followers(thread_id=5523020)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/threads/{thread_id}/followers")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def followed(self, thread_id: int, total: bool = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/threads/{thread_id}/followed

            *Get followed users of a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.
            - total (bool): Total.

            **Example:**

            ```python
            response = forum.threads.followed(thread_id=5523020, total=True)
            print(response.json())
            ```
            """
            params = {"total": total}
            return await self.core.request("GET", f"/threads/{thread_id}/followed", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def follow(self, thread_id: int, email: bool = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/threads/{thread_id}/followers

            *Follow a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.
            - email (bool): Email.

            **Example:**

            ```python
            response = forum.threads.follow(thread_id=5523020, email=True)
            print(response.json())
            ```
            """
            json = {"email": email}
            return await self.core.request("POST", f"/threads/{thread_id}/followers", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def unfollow(self, thread_id: int) -> Response:
            """
            DELETE https://prod-api.lolz.live/threads/{thread_id}/followers

            *Unfollow a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.

            **Example:**

            ```python
            response = forum.threads.unfollow(thread_id=5523020)
            print(response.json())
            ```
            """
            return await self.core.request("DELETE", f"/threads/{thread_id}/followers")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def navigation(self, thread_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/threads/{thread_id}/navigation

            *Get navigation of a thread.*

            **Parameters:**

            - thread_id (int): Thread ID.

            **Example:**

            ```python
            response = forum.threads.navigation(thread_id=5523020)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/threads/{thread_id}/navigation")

    class __Posts:
        class __Comments:
            def __init__(self, core: "Forum"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def list(self, post_id: int, before_comment: int = NONE, before: int = NONE) -> Response:
                """
                GET https://prod-api.lolz.live/posts/{post_id}/comments

                *Get comments of a post.*

                **Parameters:**

                - post_id (int): Post ID.
                - before_comment (int): Parse comments before this comment.
                - before (int): Parse comments before this timestamp.

                **Example:**

                ```python
                response = forum.posts.comments.list(post_id=5523020, before_comment=100)
                print(response.json())
                ```
                """
                params = {"before_comment": before_comment, "before": before}
                return await self.core.request("GET", f"/posts/{post_id}/comments", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def create(self, post_id: int, comment_body: str) -> Response:
                """
                POST https://prod-api.lolz.live/posts/{post_id}/comments

                *Create a comment.*

                **Parameters:**

                - post_id (int): Post ID.
                - comment_body (str): Post body.

                **Example:**

                ```python
                response = forum.posts.comments.create(post_id=5523020, post_body="Test comment")
                print(response.json())
                ```
                """
                json = {"comment_body": comment_body}
                return await self.core.request("POST", f"/posts/{post_id}/comments", json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def edit(self, comment_id: int, comment_body: str) -> Response:
                """
                PUT https://prod-api.lolz.live/posts/comments

                *Edit a comment.*

                **Parameters:**

                - comment_id (int): Comment ID.
                - comment_body (str): Comment body.

                **Example:**

                ```python
                response = forum.posts.comments.edit(comment_id=5523020, comment_body="Test comment")
                print(response.json())
                ```
                """
                json = {"comment_body": comment_body, "post_comment_id": comment_id}
                return await self.core.request("PUT", "/posts/comments", json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def delete(self, post_comment_id: int) -> Response:
                """
                DELETE https://prod-api.lolz.live/posts/comments

                *Delete a post comment.*

                **Parameters:**

                - post_comment_id (int): Id of post comment to delete.

                **Example:**

                ```python
                response = forum.posts.comments.delete(post_comment_id=123456)
                print(response.json())
                ```
                """
                params = {"post_comment_id": post_comment_id}
                return await self.core.request("DELETE", "/posts/comments", params=params)

        def __init__(self, core: "Forum"):
            self.core = core
            self.comments = self.__Comments(self.core)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self, thread_id: int = NONE, post_id: int = NONE, page: int = NONE, limit: int = NONE, order: Constants.Forum.PostOrder._Literal = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/posts

            *Get posts.*

            **Parameters:**

            - thread_id (int): Thread ID.
            - post_id (int): Parse posts from page of this post.
            - page (int): Page.
            - limit (int): Posts limit per page.
            - order (str): Posts order.

            **Example:**

            ```python
            response = forum.posts.list(thread_id=5523020, page=1, limit=10, order="natural")
            print(response.json())
            ```
            """
            params = {"thread_id": thread_id, "page_of_post_id": post_id, "page": page, "limit": limit, "order": order}
            return await self.core.request("GET", "/posts", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, post_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/posts/{post_id}

            *Get a post.*

            **Parameters:**

            - post_id (int): Post ID.

            **Example:**

            ```python
            response = forum.posts.get(post_id=5523020)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/posts/{post_id}")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def create(self, post_body: str, thread_id: int = NONE, quote_post_id: int = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/posts

            *Create a post.*

            **Parameters:**

            - post_body (str): Post body.
            - thread_id (int): Thread ID.
            - quote_post_id (int): Quote post ID.

            **Example:**

            ```python
            response = forum.posts.create(post_body="Test post", thread_id=5523020, quote_post_id=1234567)
            print(response.json())
            ```
            """
            json = {"post_body": post_body, "thread_id": thread_id, "quote_post_id": quote_post_id}
            return await self.core.request("POST", "/posts", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def edit(self, post_id: int, post_body: str = NONE) -> Response:
            """
            PUT https://prod-api.lolz.live/posts/{post_id}

            *Edit a post.*

            **Parameters:**

            - post_id (int): Post ID.
            - post_body (str): Post body.

            **Example:**

            ```python
            response = forum.posts.edit(post_id=5523020, post_body="Test post")
            print(response.json())
            ```
            """
            json = {"post_body": post_body}
            return await self.core.request("PUT", f"/posts/{post_id}", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def delete(self, post_id: int, reason: str = NONE) -> Response:
            """
            DELETE https://prod-api.lolz.live/posts/{post_id}

            *Delete a post.*

            **Parameters:**

            - post_id (int): Post ID.
            - reason (str): Reason.

            **Example:**

            ```python
            response = forum.posts.delete(post_id=5523020, reason="Test reason")
            print(response.json())
            ```
            """
            json = {"reason": reason}
            return await self.core.request("DELETE", f"/posts/{post_id}", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def likes(self, post_id: int, page: int = NONE, limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/posts/{post_id}/likes

            *Get likes of a post.*

            **Parameters:**

            - post_id (int): Post ID.
            - page (int): Page.
            - limit (int): Likes limit per page.

            **Example:**

            ```python
            response = forum.posts.likes(post_id=5523020, page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"page": page, "limit": limit}
            return await self.core.request("GET", f"/posts/{post_id}/likes", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def like(self, post_id: int) -> Response:
            """
            POST https://prod-api.lolz.live/posts/{post_id}/likes

            *Like a post.*

            **Parameters:**

            - post_id (int): Post ID.

            **Example:**

            ```python
            response = forum.posts.like(post_id=5523020)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/posts/{post_id}/likes")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def unlike(self, post_id: int) -> Response:
            """
            DELETE https://prod-api.lolz.live/posts/{post_id}/likes

            *Unlike a post.*

            **Parameters:**

            - post_id (int): Post ID.

            **Example:**

            ```python
            response = forum.posts.unlike(post_id=5523020)
            print(response.json())
            ```
            """
            return await self.core.request("DELETE", f"/posts/{post_id}/likes")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def report(self, post_id: int, reason: str = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/posts/{post_id}/report

            *Report a post.*

            **Parameters:**

            - post_id (int): Post ID.
            - reason (str): Reason.

            **Example:**

            ```python
            response = forum.posts.report(post_id=5523020, reason="Test reason")
            print(response.json())
            ```
            """
            json = {"message": reason}
            return await self.core.request("POST", f"/posts/{post_id}/report", json=json)

    class __Users:
        class __Avatar:
            def __init__(self, core: "Forum"):
                self.core = core

            @UNIVERSAL(batchable=False)
            @AutoDelay.WrapperSet(0.2)
            async def upload(self, file: bytes, x: int = NONE, y: int = NONE, size: int = NONE) -> Response:
                """
                POST https://prod-api.lolz.live/users/me/avatar

                *Upload an avatar.*
                > You can't create batch job for this method

                **Parameters:**

                - file (bytes): Avatar bytes.
                - x (int): X.
                - y (int): Y.
                - size (int): Selection size.
                  > Minimum value - 16.

                **Example:**

                ```python
                with open("avatar.png", "rb") as file:
                    response = forum.users.avatar.upload(file=file.read(), x=100, y=100, size=100)
                print(response.json())
                ```
                """
                files = {"avatar": file}
                json = {"x": x, "y": y, "size": size}
                return await self.core.request("POST", "/users/me/avatar", files=files, json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def delete(self) -> Response:
                """
                DELETE https://prod-api.lolz.live/users/me/avatar

                **Delete an avatar.**

                **Example:**

                ```python
                response = forum.users.avatar.delete()
                print(response.json())
                ```
                """
                return await self.core.request("DELETE", "/users/me/avatar")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def crop(self, x: int, y: int, size: int) -> Response:
                """
                POST https://prod-api.lolz.live/users/me/avatar/crop

                *Crop an avatar.*

                **Parameters:**

                - x (int): X.
                - y (int): Y.
                - size (int): Selection size.
                  > Minimum value - 16.

                **Example:**

                ```python
                response = forum.users.avatar.crop(x=100, y=100, size=100)
                print(response.json())
                ```
                """
                json = {"x": x, "y": y, "crop": size}
                return await self.core.request("POST", "/users/me/avatar/crop", json=json)

        class __Background:
            def __init__(self, core: "Forum"):
                self.core = core

            @UNIVERSAL(batchable=False)
            @AutoDelay.WrapperSet(0.2)
            async def upload(self, file: bytes, x: int = NONE, y: int = NONE, size: int = NONE) -> Response:
                """
                POST https://prod-api.lolz.live/users/me/background

                *Upload a background.*
                > You can't create batch job for this method

                **Parameters:**

                - file (bytes): Background bytes.
                - x (int): X.
                - y (int): Y.
                - size (int): Selection size.
                  > Minimum value - 100.

                **Example:**

                ```python
                with open("background.png", "rb") as file:
                    response = forum.users.background.upload(file=file.read(), x=100, y=100, size=100)
                print(response.json())
                ```
                """
                files = {"background": file}
                json = {"x": x, "y": y, "size": size}
                return await self.core.request("POST", "/users/me/background", files=files, json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def delete(self) -> Response:
                """
                DELETE https://prod-api.lolz.live/users/me/background

                **Delete a background.**

                **Example:**

                ```python
                response = forum.users.background.delete()
                print(response.json())
                ```
                """
                return await self.core.request("DELETE", "/users/me/background")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def crop(self, x: int, y: int, size: int) -> Response:
                """
                POST https://prod-api.lolz.live/users/me/background/crop

                *Crop a background.*

                **Parameters:**

                - x (int): X.
                - y (int): Y.
                - size (int): Selection size.
                  > Minimum value - 100.

                **Example:**

                ```python
                response = forum.users.background.crop(x=100, y=100, size=100)
                print(response.json())
                ```
                """
                json = {"x": x, "y": y, "crop": size}
                return await self.core.request("POST", "/users/me/background/crop", json=json)

        class __Profile_Posts:
            class __Comments:
                def __init__(self, core: "Forum"):
                    self.core = core

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def list(self, post_id: int, before: int = NONE, limit: int = NONE) -> Response:
                    """
                    GET https://prod-api.lolz.live/profile-posts/{post_id}/comments

                    *Get comments of a profile post.*

                    **Parameters:**

                    - post_id (int): Profile post ID.
                    - before (int): Parse comments before this timestamp.
                    - limit (int): Comments limit per page.

                    **Example:**

                    ```python
                    response = forum.users.profile_posts.comments.list(post_id=5523020, before=100, limit=10)
                    print(response.json())
                    ```
                    """
                    params = {"before": before, "limit": limit}
                    return await self.core.request("GET", f"/profile-posts/{post_id}/comments", params=params)

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def get(self, post_id: int, comment_id: int) -> Response:
                    """
                    GET https://prod-api.lolz.live/profile-posts/{post_id}/comments/{comment_id}

                    *Get a comment of a profile post.*

                    **Parameters:**

                    - post_id (int): Profile post ID.
                    - comment_id (int): Comment ID.

                    **Example:**

                    ```python
                    response = forum.users.profile_posts.comments.get(post_id=5523020, comment_id=1)
                    print(response.json())
                    ```
                    """
                    return await self.core.request("GET", f"/profile-posts/{post_id}/comments/{comment_id}")

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def create(self, post_id: int, post_body: str) -> Response:
                    """
                    POST https://prod-api.lolz.live/profile-posts/{post_id}/comments

                    *Create a comment of a profile post.*

                    **Parameters:**

                    - post_id (int): Profile post ID.
                    - post_body (str): Comment body.

                    **Example:**

                    ```python
                    response = forum.users.profile_posts.comments.create(post_id=5523020, post_body="Test comment")
                    print(response.json())
                    ```
                    """
                    json = {"comment_body": post_body}
                    return await self.core.request("POST", f"/profile-posts/{post_id}/comments", json=json)

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def edit(self, comment_id: int, comment_body: str) -> Response:
                    """
                    PUT https://prod-api.lolz.live/profile-posts/comments

                    *Edit a profile post comment.*

                    **Parameters:**

                    - comment_id (int): Id of profile post comment.
                    - comment_body (str): New content for the profile post comment.

                    **Example:**

                    ```python
                    response = forum.users.profile_posts.comments.edit(comment_id=123456, comment_body="Updated comment")
                    print(response.json())
                    ```
                    """
                    json = {"comment_body": comment_body}
                    params = {"comment_id": comment_id}
                    return await self.core.request("PUT", "/profile-posts/comments", json=json, params=params)

                @UNIVERSAL(batchable=True)
                @AutoDelay.WrapperSet(0.2)
                async def delete(self, comment_id: int) -> Response:
                    """
                    DELETE https://prod-api.lolz.live/profile-posts/comments

                    *Delete a profile post comment.*

                    **Parameters:**

                    - comment_id (int): Id of profile post comment.

                    **Example:**

                    ```python
                    response = forum.users.profile_posts.comments.delete(comment_id=123456)
                    print(response.json())
                    ```
                    """
                    params = {"comment_id": comment_id}
                    return await self.core.request("DELETE", "/profile-posts/comments", params=params)

            def __init__(self, core: "Forum"):
                self.core = core
                self.comments = self.__Comments(self.core)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def list(self, user_id: Union[int, str], page: int = NONE, limit: int = NONE) -> Response:
                """
                GET https://prod-api.lolz.live/users/{user_id}/profile-posts

                *Get profile posts of a user.*

                **Parameters:**

                - user_id (int): User ID.
                - page (int): Page.
                - limit (int): Posts limit per page.

                **Example:**

                ```python
                response = forum.users.profile_posts.list(user_id=2410024, page=1, limit=10)
                print(response.json())
                ```
                """
                params = {"page": page, "limit": limit}
                return await self.core.request("GET", f"/users/{user_id}/profile-posts", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def get(self, post_id: int) -> Response:
                """
                GET https://prod-api.lolz.live/profile-posts/{post_id}

                *Get a profile post.*

                **Parameters:**

                - post_id (int): Profile post ID.

                **Example:**

                ```python
                response = forum.users.profile_posts.get(post_id=5523020)
                print(response.json())
                ```
                """
                return await self.core.request("GET", f"/profile-posts/{post_id}")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def create(self, user_id: Union[int, str], post_body: str) -> Response:
                """
                POST https://prod-api.lolz.live/users/{user_id}/profile-posts

                *Create a profile post.*

                **Parameters:**

                - user_id (int): User ID.
                - post_body (str): Post body.

                **Example:**

                ```python
                response = forum.users.profile_posts.create(user_id=2410024, post_body="Test post")
                print(response.json())
                ```
                """
                json = {"post_body": post_body}
                return await self.core.request("POST", f"/users/{user_id}/profile-posts", json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def edit(self, post_id: int, post_body: str = NONE) -> Response:
                """
                PUT https://prod-api.lolz.live/profile-posts/{post_id}

                *Edit a profile post.*

                **Parameters:**

                - post_id (int): Profile post ID.
                - post_body (str): Post body.

                **Example:**

                ```python
                response = forum.users.profile_posts.edit(post_id=5523020, post_body="Test post")
                print(response.json())
                ```
                """
                json = {"post_body": post_body}
                return await self.core.request("PUT", f"/profile-posts/{post_id}", json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def delete(self, post_id: int, reason: str = NONE) -> Response:
                """
                DELETE https://prod-api.lolz.live/profile-posts/{post_id}

                **Delete a profile post.**

                **Parameters:**

                - post_id (int): Profile post ID.
                - reason (str): Delete reason.

                **Example:**

                ```python
                response = forum.users.profile_posts.delete(post_id=5523020, reason="Test reason")
                print(response.json())
                ```
                """
                json = {"reason": reason}
                return await self.core.request("DELETE", f"/profile-posts/{post_id}", json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def likes(self, post_id: int) -> Response:
                """
                GET https://prod-api.lolz.live/profile-posts/{post_id}/likes

                *Get likes of a profile post.*

                **Parameters:**

                - post_id (int): Profile post ID.

                **Example:**

                ```python
                response = forum.users.profile_posts.likes.list(post_id=5523020)
                print(response.json())
                ```
                """
                return await self.core.request("GET", f"/profile-posts/{post_id}/likes")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def like(self, post_id: int) -> Response:
                """
                POST https://prod-api.lolz.live/profile-posts/{post_id}/likes

                **Like a profile post.**

                **Example:**

                ```python
                response = forum.users.profile_posts.likes.like(post_id=5523020)
                print(response.json())
                ```
                """
                return await self.core.request("POST", f"/profile-posts/{post_id}/likes")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def unlike(self, post_id: int) -> Response:
                """
                DELETE https://prod-api.lolz.live/profile-posts/{post_id}/likes

                **Unlike a profile post.**

                **Example:**

                ```python
                response = forum.users.profile_posts.likes.unlike(post_id=5523020)
                print(response.json())
                ```
                """
                return await self.core.request("DELETE", f"/profile-posts/{post_id}/likes")

        def __init__(self, core: "Forum"):
            self.core = core
            self.avatar = self.__Avatar(self.core)
            self.background = self.__Background(self.core)
            self.profile_posts = self.__Profile_Posts(self.core)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self, page: int = NONE, limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/users

            *Get users.*

            **Parameters:**

            - page (int): Page.
            - limit (int): Users limit per page.

            **Example:**

            ```python
            response = forum.users.list(page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"page": page, "limit": limit}
            return await self.core.request("GET", "/users", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def search(self, username: str = NONE, fields: dict[str, str] = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/users/find

            *Search users.*

            **Parameters:**

            - username (str): Username of the user.
            - fields (dict[str, str]): Custom fields.

            **Example:**

            ```python
            response = forum.users.search(username="test", fields={"field1": "value1", "field2": "value2"})
            print(response.json())
            ```
            """
            params = {"username": username}
            if not isinstance(fields, _NONE):
                for k, v in fields.items():
                    params[f"custom_fields[{str(k)}]"] = v
            return await self.core.request("GET", "/users/find", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, user_id: Union[int, str] = "me") -> Response:
            """
            GET https://prod-api.lolz.live/users/{user_id}

            *Get a user.*

            **Parameters:**

            - user_id (int): User ID.

            **Example:**

            ```python
            response = forum.users.get(user_id=2410024)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/users/{user_id}")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def edit(
            self,
            title: str = NONE,
            display_group_id: Constants.Forum.User.GroupID._Literal = NONE,
            dob: tuple[int, int, int] = NONE,
            fields: dict[str, str] = NONE,
            display_icon_group_id: int = NONE,
            display_banner_id: int = NONE,
            conv_welcome_message: str = NONE,
            username: str = NONE,
            secret_answer: str = NONE,
            secret_answer_type: int = NONE,
            short_link: str = NONE,
        ) -> Response:
            """
            PUT https://prod-api.lolz.live/users/me

            *Edit a user.*

            **Parameters:**

            - title (str): Title.
            - display_group_id (int): Display group ID.
            - dob (tuple[int, int, int]): Date of birth.
            - fields (dict[str, str]): Custom fields.
            - display_icon_group_id (int): ID of the icon group you want to display.
            - display_banner_id (int): ID of the banner you want to display.
            - conv_welcome_message (str): This message is shown when someone wants to write to you.
            - username (str): New username.
            - secret_answer (str): Secret answer.
            - secret_answer_type (int): Secret answer type.
            - short_link (str): Profile short link.

            **Example:**

            ```python
            response = forum.users.edit(
                title="Test title",
                display_group_id=1,
                dob=(1, 1, 2000),
                fields={"_4": "My new interests", "occupation": "My new occupation"},
                username="RiceMorgan",
                secret_answer="***********",
                secret_answer_type=1,
                short_link="ricemorgan"
            )
            print(response.json())
            ```
            """
            json = {
                "title": title,
                "display_group_id": display_group_id,
                "fields": fields,
                "display_icon_group_id": display_icon_group_id,
                "display_banner_id": display_banner_id,
                "conv_welcome_message": conv_welcome_message,
                "username": username,
                "secret_answer": secret_answer,
                "secret_answer_type": secret_answer_type,
                "short_link": short_link,
            }
            if not isinstance(dob, _NONE) and len(dob) == 3:
                json["user_dob_day"] = dob[0]
                json["user_dob_month"] = dob[1]
                json["user_dob_year"] = dob[2]
            return await self.core.request("PUT", "/users/me", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def fields(self) -> Response:
            """
            GET https://prod-api.lolz.live/users/fields

            *Get your fields.*

            **Example:**

            ```python
            response = forum.users.fields()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/users/fields")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def trophies(self, user_id: Union[int, str] = "me") -> Response:
            """
            GET https://prod-api.lolz.live/users/{user_id}/trophies

            *Get user trophies.*

            **Example:**

            ```python
            response = forum.users.trophies(user_id=2410024)
            print(response.json())
            ```/
            """
            return await self.core.request("GET", f"/users/{user_id}/trophies")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def followers(self, user_id: Union[int, str] = "me", order: Constants.Forum.User.FollowOrder._Literal = NONE, page: int = NONE, limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/users/{user_id}/followers

            *Get followers of a user.*

            **Parameters:**

            - user_id (int): User ID.
            - order (str): Order.
            - page (int): Page.
            - limit (int): Followers limit per page.

            **Example:**

            ```python
            response = forum.users.followers(user_id=2410024, order="follow_date", page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"order": order, "page": page, "limit": limit}
            return await self.core.request("GET", f"/users/{user_id}/followers", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def followed(self, user_id: Union[int, str] = "me", order: Constants.Forum.User.FollowOrder._Literal = NONE, page: int = NONE, limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/users/{user_id}/followings

            *Get followed users of a user.*

            **Parameters:**

            - user_id (int): User ID.
            - order (str): Order.
            - page (int): Page.
            - limit (int): Followed users limit per page.

            **Example:**

            ```python
            response = forum.users.followed(user_id=2410024, order="follow_date", page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"order": order, "page": page, "limit": limit}
            return await self.core.request("GET", f"/users/{user_id}/followings", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def follow(self, user_id: Union[int, str]) -> Response:
            """
            POST https://prod-api.lolz.live/users/{user_id}/followers

            **Follow a user.**

            **Example:**

            ```python
            response = forum.users.follow(user_id=2410024)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/users/{user_id}/followers")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def unfollow(self, user_id: Union[int, str]) -> Response:
            """
            DELETE https://prod-api.lolz.live/users/{user_id}/followers

            **Unfollow a user.**

            **Example:**

            ```python
            response = forum.users.unfollow(user_id=2410024)
            print(response.json())
            ```
            """
            return await self.core.request("DELETE", f"/users/{user_id}/followers")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def ignored(self) -> Response:
            """
            GET https://prod-api.lolz.live/users/ignored

            *Get ignored users.*

            **Example:**

            ```python
            response = forum.users.ignored()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/users/ignored")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def ignore(self, user_id: Union[int, str]) -> Response:
            """
            POST https://prod-api.lolz.live/users/{user_id}/ignore

            **Ignore a user.**

            **Example:**

            ```python
            response = forum.users.ignore(user_id=2410024)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/users/{user_id}/ignore")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def unignore(self, user_id: Union[int, str]) -> Response:
            """
            DELETE https://prod-api.lolz.live/users/{user_id}/ignore

            **Unignore a user.**

            **Example:**

            ```python
            response = forum.users.unignore(user_id=2410024)
            print(response.json())
            ```
            """
            return await self.core.request("DELETE", f"/users/{user_id}/ignore")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def content(self, user_id: Union[int, str] = "me", page: int = NONE, limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/users/{user_id}/timeline

            *Get timeline of a user.*

            **Example:**

            ```python
            response = forum.users.content(user_id=2410024, page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"page": page, "limit": limit}
            return await self.core.request("GET", f"/users/{user_id}/timeline", params=params)

    class __Conversations:
        class __Messages:
            def __init__(self, core: "Forum"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def list(self,
                           conversation_id: int,
                           page: int = NONE,
                           limit: int = NONE,
                           order: Literal["natural", "natural_reverse"] = NONE,
                           before: int = NONE,
                           after: int = NONE) -> Response:
                """
                GET https://prod-api.lolz.live/conversations/messages

                *Get messages of a conversation.*
                """
                params = {
                    "conversation_id": conversation_id,
                    "page": page,
                    "limit": limit,
                    "order": order,
                    "before": before,
                    "after": after
                }
                return await self.core.request("GET", "/conversations/messages", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def get(self, message_id: int) -> Response:
                """
                GET https://prod-api.lolz.live/conversations/messages/{message_id}

                *Get a message.*

                **Parameters:**

                - message_id (int): Message ID.

                **Example:**

                ```python
                response = forum.conversations.messages.get(message_id=123456)
                print(response.json())
                ```
                """
                return await self.core.request("GET", f"/conversations/messages/{message_id}")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def create(self, conversation_id: int, message: str) -> Response:
                """
                POST https://prod-api.lolz.live/conversations/messages

                **Create a message.**

                **Parameters:**

                - conversation_id (int): Conversation ID.
                - message (str): Message.

                **Example:**

                ```python
                response = forum.conversations.messages.create(conversation_id=123456, message="Hello, world!")
                print(response.json())
                ```
                """
                json = {"message_body": message, "conversation_id": conversation_id}
                return await self.core.request("POST", "/conversations/messages", json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def edit(self, conversation_id: int, message_id: int, message: str) -> Response:
                """
                PUT https://prod-api.lolz.live/conversations/messages/{message_id}

                **Edit a message.**

                **Parameters:**

                - conversation_id (int): Conversation ID.
                - message_id (int): Message ID.
                - message (str): Message.

                **Example:**

                ```python
                response = forum.conversations.messages.edit(conversation_id=123456, message_id=1234567890, message="Hello, world!")
                print(response.json())
                ```
                """
                json = {"conversation_id": conversation_id, "message_body": message}
                return await self.core.request("PUT", f"/conversations/messages/{message_id}", json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def stick(self, conversation_id: int, message_id: int) -> Response:
                """
                POST https://prod-api.lolz.live/conversations/{conversation_id}/messages/{message_id}/stick

                **Stick a message in a conversation.**

                **Parameters:**

                - conversation_id (int): Conversation ID.
                - message_id (int): Message ID.

                **Example:**

                ```python
                response = forum.conversations.messages.stick(conversation_id=123456, message_id=789012)
                print(response.json())
                ```
                """
                return await self.core.request("POST", f"/conversations/{conversation_id}/messages/{message_id}/stick")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def unstick(self, conversation_id: int, message_id: int) -> Response:
                """
                DELETE https://prod-api.lolz.live/conversations/{conversation_id}/messages/{message_id}/stick

                **Unstick a message in a conversation.**

                **Parameters:**

                - conversation_id (int): Conversation ID.
                - message_id (int): Message ID.

                **Example:**

                ```python
                response = forum.conversations.messages.unstick(conversation_id=123456, message_id=789012)
                print(response.json())
                ```
                """
                return await self.core.request("DELETE", f"/conversations/{conversation_id}/messages/{message_id}/stick")

        class __Alerts:
            def __init__(self, core: "Forum"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def enable(self, conversation_id: int) -> Response:
                """
                POST https://prod-api.lolz.live/conversations/{conversation_id}/alerts

                **Enable alerts for a conversation.**

                **Parameters:**

                - conversation_id (int): Conversation ID.

                **Example:**

                ```python
                response = forum.conversations.alerts.enable(conversation_id=123456)
                print(response.json())
                ```
                """
                return await self.core.request("POST", f"/conversations/{conversation_id}/alerts")

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def disable(self, conversation_id: int) -> Response:
                """
                DELETE https://prod-api.lolz.live/conversations/{conversation_id}/alerts

                **Disable alerts for a conversation.**

                **Parameters:**

                - conversation_id (int): Conversation ID.

                **Example:**

                ```python
                response = forum.conversations.alerts.disable(conversation_id=123456)
                print(response.json())
                ```
                """
                return await self.core.request("DELETE", f"/conversations/{conversation_id}/alerts")

        def __init__(self, core: "Forum"):
            self.core = core
            self.messages = self.__Messages(self.core)
            self.alerts = self.__Alerts(self.core)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self, page: int = NONE, limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/conversations

            *Get conversations.*

            **Parameters:**

            - page (int): Page.
            - limit (int): Limit.

            **Example:**

            ```python
            response = forum.conversations.list(page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"page": page, "limit": limit}
            return await self.core.request("GET", "/conversations", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, conversation_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/conversations/{conversation_id}

            *Get a conversation.*

            **Parameters:**

            - conversation_id (int): Conversation ID.

            **Example:**

            ```python
            response = forum.conversations.get(conversation_id=123456)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/conversations/{conversation_id}")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def create(self, user_id: int, message: str) -> Response:
            """
            POST https://prod-api.lolz.live/conversations

            **Create a conversation.**

            **Parameters:**

            - user_id (int): User ID.
            - message (str): Message.

            **Example:**

            ```python
            response = forum.conversations.create(user_id=2410024, message="Hello, world!")
            print(response.json())
            ```
            """
            json = {"message_body": message, "recipient_id": user_id, "is_group": False}
            return await self.core.request("POST", "/conversations", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def create_group(self,
                               usernames: builtins.list[str],
                               message: str,
                               title: str,
                               open_invite: bool = NONE,
                               conversation_locked: bool = NONE,
                               allow_edit_messages: bool = NONE,
                               ) -> Response:
            """
            POST https://prod-api.lolz.live/conversations

            **Create a group conversation.**

            **Parameters:**

            - usernames (list[str]): Usernames.
            - message (str): Message.
            - title (str): Title.
            - open_invite (bool): Open invite.
            - conversation_locked (bool): Conversation locked.
            - allow_edit_messages (bool): Allow edit messages.

            **Example:**

            ```python
            response = forum.conversations.create_group(
                usernames=["user1", "user2"],
                message="Hello, world!",
                title="Group Conversation",
                open_invite=True,
                conversation_locked=False,
                allow_edit_messages=True
            )
            print(response.json())
            ```
            """
            json = {
                "message_body": message,
                "recipients": ",".join(usernames),
                "title": title,
                "open_invite": open_invite,
                "conversation_locked": conversation_locked,
                "allow_edit_messages": allow_edit_messages,
                "is_group": True
            }
            return await self.core.request("POST", "/conversations", json=json)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def leave(self, conversation_id: int, leave_type: Literal["delete", "delete_ignore"] = "delete") -> Response:
            """
            DELETE https://prod-api.lolz.live/conversations/{conversation_id}

            **Leave from a conversation.**

            **Parameters:**

            - conversation_id (int): Conversation ID.
            - leave_type (str): Leave type.

            **Example:**

            ```python
            response = forum.conversations.leave(conversation_id=123456, leave_type="delete")
            print(response.json())
            ```
            """
            params = {"leave_type": leave_type}
            return await self.core.request("DELETE", f"/conversations/{conversation_id}", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def star(self, conversation_id: int) -> Response:
            """
            POST https://prod-api.lolz.live/conversations/{conversation_id}/star

            **Star a conversation.**

            **Parameters:**

            - conversation_id (int): Conversation ID.

            **Example:**

            ```python
            response = forum.conversations.star(conversation_id=123456)
            print(response.json())
            ```
            """
            return await self.core.request("POST", f"/conversations/{conversation_id}/star")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def unstar(self, conversation_id: int) -> Response:
            """
            DELETE https://prod-api.lolz.live/conversations/{conversation_id}/star

            **Unstar a conversation.**

            **Parameters:**

            - conversation_id (int): Conversation ID.

            **Example:**

            ```python
            response = forum.conversations.unstar(conversation_id=123456)
            print(response.json())
            ```
            """
            return await self.core.request("DELETE", f"/conversations/{conversation_id}/star")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def read_all(self) -> Response:
            """
            POST https://prod-api.lolz.live/conversations/read-all

            **Mark all conversations as read.**

            **Example:**

            ```python
            response = forum.conversations.read_all()
            print(response.json())
            ```
            """
            return await self.core.request("POST", "/conversations/read-all")

    class __Notifications:
        def __init__(self, core: "Forum"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self) -> Response:
            """
            GET https://prod-api.lolz.live/notifications

            *Get notifications.*

            **Example:**

            ```python
            response = forum.notifications.list()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/notifications")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, notification_id: int) -> Response:
            """
            GET https://prod-api.lolz.live/notifications/{notification_id}

            *Get a notification.*

            **Parameters:**

            - notification_id (int): Notification ID.

            **Example:**

            ```python
            response = forum.notifications.get(notification_id=123456)
            print(response.json())
            ```
            """
            return await self.core.request("GET", f"/notifications/{notification_id}")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def read(self, notification_id: int = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/notifications/read

            **Read a notification.**

            **Parameters:**

            - notification_id (int): Notification ID.

            **Example:**

            ```python
            response = forum.notifications.read()
            print(response.json())
            ```
            """
            params = {"notification_id": notification_id}
            return await self.core.request("POST", "/notifications/read", params=params)

    class __Tags:
        def __init__(self, core: "Forum"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self, page: int = NONE, limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/tags/list

            *Get tags.*

            **Parameters:**

            - page (int): Page.
            - limit (int): Limit.

            **Example:**

            ```python
            response = forum.tags.list(page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"page": page, "limit": limit}
            return await self.core.request("GET", "/tags/list", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, tag_id: int, page: int = NONE, limit: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/tags/{tag_id}

            *Get a tag.*

            **Parameters:**

            - tag_id (int): Tag ID.
            - page (int): Page.
            - limit (int): Limit.

            **Example:**

            ```python
            response = forum.tags.get(tag_id=123456, page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"page": page, "limit": limit}
            return await self.core.request("GET", f"/tags/{tag_id}", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def popular(self) -> Response:
            """
            GET https://prod-api.lolz.live/tags/popular

            *Get popular tags.*

            **Example:**

            ```python
            response = forum.tags.popular()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/tags/popular")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def search(self, tag: str) -> Response:
            """
            GET https://prod-api.lolz.live/tags/find

            **Search for a tag.**

            **Parameters:**

            - tag (str): Tag.

            **Example:**

            ```python
            response = forum.tags.search(tag="example")
            print(response.json())
            ```
            """
            params = {"tag": tag}
            return await self.core.request("GET", "/tags/find", params=params)

    class __Search:
        def __init__(self, core: "Forum"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def all(self, query: str = NONE, user_id: int = NONE, tag: str = NONE, forum_id: int = NONE, page: int = NONE, limit: int = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/search

            **Search for all types of content.**

            **Parameters:**

            - query (str): Query.
            - user_id (int): User ID.
            - tag (str): Tag.
            - forum_id (int): Forum ID.
            - page (int): Page.
            - limit (int): Limit.

            **Example:**

            ```python
            response = forum.search.all(user_id=2410024, forum_id=876, page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"q": query, "user_id": user_id, "tag": tag, "forum_id": forum_id, "page": page, "limit": limit}
            return await self.core.request("POST", "/search", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def threads(self, query: str = NONE, user_id: int = NONE, page: int = NONE, limit: int = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/search/threads

            **Search for threads.**

            **Parameters:**

            - query (str): Query.
            - user_id (int): User ID.
            - page (int): Page.
            - limit (int): Limit.

            **Example:**

            ```python
            response = forum.search.threads(user_id=2410024, page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"q": query, "user_id": user_id, "page": page, "limit": limit}
            return await self.core.request("POST", "/search/threads", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def posts(self, query: str = NONE, user_id: int = NONE, page: int = NONE, limit: int = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/search/posts

            **Search for posts.**

            **Parameters:**

            - query (str): Query.
            - user_id (int): User ID.
            - page (int): Page.
            - limit (int): Limit.

            **Example:**

            ```python
            response = forum.search.posts(user_id=2410024, page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"q": query, "user_id": user_id, "page": page, "limit": limit}
            return await self.core.request("POST", "/search/posts", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def profile_posts(self, query: str = NONE, user_id: int = NONE, page: int = NONE, limit: int = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/search/profile-posts

            **Search for profile posts.**

            **Parameters:**

            - query (str): Query.
            - user_id (int): User ID.
            - page (int): Page.
            - limit (int): Limit.

            **Example:**

            ```python
            response = forum.search.profile_posts(user_id=2410024, page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"q": query, "user_id": user_id, "page": page, "limit": limit}
            return await self.core.request("POST", "/search/profile-posts", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def tagged(self, tag: str = NONE, tags: list[str] = NONE, page: int = NONE, limit: int = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/search/tagged

            **Search for tagged content.**

            **Parameters:**

            - tag (str): Tag.
            - tags (list[str]): Tags.
            - page (int): Page.
            - limit (int): Limit.

            **Example:**

            ```python
            response = forum.search.tagged(tag="example", tags=["example", "example2"], page=1, limit=10)
            print(response.json())
            ```
            """
            params = {"tag": tag, "tags": tags, "page": page, "limit": limit}
            return await self.core.request("POST", "/search/tagged", params=params)

    class __Chat:
        class __Messages:
            def __init__(self, core: "Forum"):
                self.core = core

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def list(self, room_id: Constants.Forum.ChatRoomIDs._Literal, before_message_id: int = NONE) -> Response:
                """
                GET https://prod-api.lolz.live/chatbox/messages

                *Get chat messages.*

                **Parameters:**

                - room_id (int): Room ID.
                - before_message_id (intsas): Message id to get older chat messages.

                **Example:**

                ```python
                response = forum.chat.messages.list(room_id=1)
                print(response.json())

                # With before_message_id
                response = forum.chat.messages.list(room_id=1)
                print(response.json())
                ```
                """
                params = {"room_id": room_id,
                          "before_message_id": before_message_id}
                return await self.core.request("GET", "/chatbox/messages", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def create(
                self,
                room_id: Constants.Forum.ChatRoomIDs._Literal,
                message: str,
                reply_message_id: int = NONE
            ) -> Response:
                """
                POST https://prod-api.lolz.live/chatbox/messages

                *Create a chat message.*

                **Parameters:**

                - room_id (int): Room ID.
                - message (str): Message.
                - reply_message_id (int, optional): ID of the message being replied to.

                **Example:**

                ```python
                response = forum.chat.messages.create(room_id=1, message="/sex AS7RID")
                print(response.json())
                ```
                """
                params = {"room_id": room_id,
                          "reply_message_id": reply_message_id}
                json = {"message": message}
                return await self.core.request("POST", "/chatbox/messages", params=params, json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def edit(self, message_id: int, message: str) -> Response:
                """
                PUT https://prod-api.lolz.live/chatbox/messages

                *Edit a chat message.*

                **Parameters:**

                - message_id (int): Message ID.
                - message (str): Message.

                **Example:**

                ```python
                response = forum.chat.messages.edit(message_id=1234567890, message="Hello, world!")
                print(response.json())
                ```
                """
                params = {"message_id": message_id}
                json = {"message": message}
                return await self.core.request("PUT", "/chatbox/messages", params=params, json=json)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def delete(self, message_id: int) -> Response:
                """
                DELETE https://prod-api.lolz.live/chatbox/messages

                *Delete a chat message.*

                **Parameters:**

                - message_id (int): Message ID.

                **Example:**

                ```python
                response = forum.chat.messages.delete(message_id=1234567890)
                print(response.json())
                ```
                """
                params = {"message_id": message_id}
                return await self.core.request("DELETE", "/chatbox/messages", params=params)

            @UNIVERSAL(batchable=True)
            @AutoDelay.WrapperSet(0.2)
            async def report(self, message_id: int, reason: str) -> Response:
                """
                POST https://prod-api.lolz.live/chatbox/messages/report

                *Report a chat message.*

                **Parameters:**

                - message_id (int): Message ID.
                - reason (str): Reason.

                **Example:**

                ```python
                response = forum.chat.messages.report(message_id=1234567890, reason="Report reason.")
                print(response.json())
                ```
                """
                params = {"message_id": message_id}
                json = {"reason": reason}
                return await self.core.request("POST", "/chatbox/messages/report", params=params, json=json)

        def __init__(self, core: "Forum"):
            self.core = core
            self.messages = self.__Messages(core)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def get(self, room_id: Constants.Forum.ChatRoomIDs._Literal = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/chatbox

            *Get Chats.*

            **Parameters:**

            - room_id (int): Room ID.

            **Example:**

            ```python
            response = forum.chat.get(room_id=1)
            print(response.json())
            ```
            """
            params = {"room_id": room_id}
            return await self.core.request("GET", "/chatbox", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def ignored(self) -> Response:
            """
            GET https://prod-api.lolz.live/chatbox/ignore

            *Get ignored users.*

            **Example:**

            ```python
            response = forum.chat.ignored()
            print(response.json())
            ```
            """
            return await self.core.request("GET", "/chatbox/ignore")

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def ignore(self, user_id: int = NONE) -> Response:
            """
            POST https://prod-api.lolz.live/chatbox/ignore

            *Ignore chat user.*

            **Parameters:**

            - user_id (int): User ID.

            **Example:**

            ```python
            response = forum.chat.ignore(user_id=2410024)
            print(response.json())
            ```
            """
            params = {"user_id": user_id}
            return await self.core.request("POST", "/chatbox/ignore", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def unignore(self, user_id: int = NONE) -> Response:
            """
            DELETE https://prod-api.lolz.live/chatbox/ignore

            *Unignore chat user.*

            **Parameters:**

            - user_id (int): User ID.

            **Example:**

            ```python
            response = forum.chat.unignore(user_id=2410024)
            print(response.json())
            ```
            """
            params = {"user_id": user_id}
            return await self.core.request("DELETE", "/chatbox/ignore", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def leaderboard(self, duration: Literal["day", "week", "month"] = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/chatbox/messages/leaderboard

            *Get chat leaderboard.*

            **Parameters:**

            - duration (str, optional): Duration.

            **Example:**

            ```python
            response = forum.chat.leaderboard(duration="month")
            print(response.json())
            ```
            """
            params = {"duration": duration}
            return await self.core.request("GET", "/chatbox/messages/leaderboard", params=params)

    class __Forms:
        def __init__(self, core: "Forum"):
            self.core = core

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def list(self, page: int = NONE) -> Response:
            """
            GET https://prod-api.lolz.live/forms

            *Get Forms list.*

            **Parameters:**

            - page (int): Page.

            **Example:**

            ```python
            response = forum.forms.list()
            print(response.json())
            ```
            """
            params = {"page": page}
            return await self.core.request("GET", "/forms", params=params)

        @UNIVERSAL(batchable=True)
        @AutoDelay.WrapperSet(0.2)
        async def create(self, form_id: int, fields: dict[str, str]) -> Response:
            """
            GET https://prod-api.lolz.live/forms/save

            *Create thread by form.*

            **Parameters:**

            - form_id (int): Form ID.
            - fields (dict[str, str]): Form fields.

            **Example:**

            ```python
            response = forum.forms.create(form_id=1, fields={
                "7": "sell",
                "8": 100,
                "11": 99,
                "15": "market",
                "16": "rub",
                "17": "SBP",
                "18": "rub",
                "14": "Note to the exchange"
            })
            print(response.json())
            ```
            """
            params = {"form_id": form_id}
            json = {"fields": fields}
            return await self.core.request("GET", "/forms/save", params=params, json=json)

    @UNIVERSAL(batchable=True)
    @AutoDelay.WrapperSet(0.2)
    async def navigation(self, parent: int = NONE) -> Response:
        """
        GET https://prod-api.lolz.live/navigation

        *Get navigation.*

        **Parameters:**

        - parent (int): Parent ID.

        **Example:**

        ```python
        response = forum.navigation()
        print(response.json())
        ```
        """
        params = {"parent": parent}
        return await self.core.request("GET", "/navigation", params=params)

    @UNIVERSAL(batchable=True)
    @AutoDelay.WrapperSet(0.2)
    async def css(self, query: Union[str, list], **kwargs) -> Response:
        """
        GET https://prod-api.lolz.live/css

        *Get navigation.*

        **Parameters:**

        - css (Union[str, list]): The names or identifiers of the CSS selectors to retrieve.
        - **kwargs (dict[str, any]): Additional query parameters.

        **Example:**

        ```python
        response = forum.css(query="public")
        print(response.json())
        ```
        """
        params = {"css": query if isinstance(query, str) else ",".join(query)}
        if kwargs:
            params.update(kwargs)
        return await self.core.request("GET", "/navigation", params=params)

    @UNIVERSAL(batchable=False)
    @AutoDelay.WrapperSet(0.2)
    async def batch(self, jobs: list[dict[str, str]]) -> Response:
        """
        POST https://prod-api.lolz.live/batch

        *Batch requests.*

        **Parameters:**

        - jobs (list[dict[str, str]]): Batch jobs.

        **Example:**

        ```python
        response = forum.batch(jobs=[{"method": "GET", "url": "/users/2410024", "params": {}}])
        #  Also you can create jobs for almost all functions like this:
        #  job = forum.users.get.job(user_id=2410024)
        print(response.json())

        #  You also can use executor to ease work with batch requests while you have a lot of jobs:
        jobs = [forum.users.get.job(user_id=i*1000) for i in range(42)]
        while jobs:  # It will be running until all jobs will be executed
            jobs, response = forum.batch.executor(jobs=jobs)
            print(response.json())
        ```
        """
        return await self.core.request("POST", "/batch", json=jobs)

import logging
import builtins
import httpx
import time
import json
import re

from importlib.metadata import version
from typing import Union, Literal, Optional

from . import Exceptions
from . import Constants
from .Tweaks import _MainTweaks

_WarningsHandler = logging.StreamHandler()
_WarningsHandler.setFormatter(logging.Formatter("\033[93mWARNING:%(message)s\033[0m"))
_WarningsLogger = logging.getLogger("LOLZTEAM.Warnings")
_WarningsLogger.setLevel(level=logging.WARNING)
_WarningsLogger.addHandler(_WarningsHandler)


_DebugLogger = logging.getLogger("LOLZTEAM.Debug")
_DebugLogger.setLevel(level=100)


def _send_request(self, method: str, path: dict, params: dict = None, data=None, dataJ=None, files=None) -> httpx.Response:
    return _MainTweaks._AsyncExecutor(_send_async_request(self=self, method=method, path=path, params=params, data=data, dataJ=dataJ, files=files))


@_MainTweaks._RetryWrapper
async def _send_async_request(self, method: str, path: dict, params: dict = None, data=None, dataJ=None, files=None) -> httpx.Response:
    url = self.base_url + path
    if type(self) is Antipublic:
        if params:
            params["key"] = self.token
        else:
            params = {"key": self.token}
    method = method.upper()

    if re.search(self.base_url + self._delay_pattern, url):
        await _MainTweaks._auto_delay_async(self=self)
    elif type(self) is Market:
        await _MainTweaks._auto_delay_async(self=self, delay=0.5)

    if params:
        if not params.get("locale"):  # Фикс для какого-то метода. Там коллизия параметра locale
            params["locale"] = self._locale
        params.update(self.custom.params)
        ptd = []
        for key, value in params.items():  # Убираем None
            if params[key] is None:
                ptd.append(key)
        for key in ptd:
            del params[key]
    if data:
        if type(data) is dict:
            data.update(self.custom.data)
            if dataJ:
                dataJ = None
    elif dataJ:
        if type(dataJ) is dict:
            dataJ.update(self.custom.json)

    headers = self._main_headers.copy()
    headers["User-Agent"] = f"LOLZTEAM v{version('LOLZTEAM')}"
    headers.update(self.custom.headers)

    proxy_schemes = {
        "HTTP": "http",
        "HTTPS": "https",
        "SOCKS4": "socks4",
        "SOCKS5": "socks5",
    }
    request_methods = [
        "GET",
        "POST",
        "PUT",
        "DELETE",
    ]
    proxy = None
    if self._proxy_type is not None:
        if self._proxy_type in proxy_schemes:
            proxy = f"{proxy_schemes[self._proxy_type]}://{self._proxy}"
        else:
            raise Exceptions.INVALID_PROXY_TYPE("Proxy type has invalid value. It can be only https, http, socks4 or socks5")

    if method in request_methods:
        censored_headers = headers.copy()
        censored_headers["Authorization"] = "bearer ***Token***"
        if data:
            body = json.dumps(data)
        elif dataJ:
            body = json.dumps(dataJ)
        else:
            body = None
        _DebugLogger.debug(f"{method} {url} | Params: {json.dumps(params)} | Data: {body} | Files: {files} | Headers: {json.dumps(censored_headers)} | Proxy: {json.dumps(proxy)} | Timeout: {self.timeout}")
        tbr = time.time()
        async with httpx.AsyncClient(proxies=proxy) as client:
            response = await client.request(method=method, url=url, params=params, data=data, json=dataJ, files=files, headers=headers, timeout=self.timeout)
            _DebugLogger.debug(f"Response: {response} | Plain response: {response.content}")
            if self.reset_custom_variables:
                self.custom.reset()
            if self._delay_synchronizer:
                self._delay_synchronizer._synchronize(tbr)
            else:
                self._auto_delay_time = tbr
            return response
    else:
        raise Exceptions.AS7RID_FUCK_UP("Invalid request method. Contact @AS7RID")


class Forum:
    def __init__(
        self,
        token: str,
        bypass_429: bool = True,
        language: str = None,
        proxy_type: str = None,
        proxy: str = None,
        reset_custom_variables: bool = True,
        timeout: int = 90,
    ):
        """
        - **token** (str): Your token.
            > You can get it [there](https://zelenka.guru/account/api)
        - **bypass_429** (bool): Bypass status code 429 by sleep
        - **language** (str): Language for your api responses.
        - **proxy_type** (str): Your proxy type.
        - **proxy** (str): Proxy string.
        - **reset_custom_variables** (bool): Reset custom variables.
        - **timeout** (int): Request timeout.
        """
        self.base_url = "https://api.zelenka.guru"
        if proxy_type is not None:
            proxy_type = proxy_type.upper()
            if proxy_type in ["HTTPS", "HTTP", "SOCKS4", "SOCKS5"]:
                self._proxy_type = proxy_type
                self._proxy = proxy
            else:
                raise Exceptions.INVALID_PROXY_TYPE(
                    "Proxy type has invalid value. It can be only https,http,socks4 or socks5"
                )
        else:
            self._proxy = None
            self._proxy_type = None

        self._token = token
        self._scopes = None
        _MainTweaks.setup_jwt(self=self, token=token)
        self._main_headers = {"Authorization": f"bearer {self._token}"}

        self.bypass_429 = bypass_429
        self.timeout = timeout
        self._auto_delay_time = 0
        self.additional_delay = 0.1
        self._locale = language
        self._delay_synchronizer = None
        self._lock = None
        self._delay_pattern = ".*"

        self.reset_custom_variables = reset_custom_variables
        self.custom = _MainTweaks._Custom()

        self.categories = self.__Categories(self)
        self.forums = self.__Forums(self)
        self.pages = self.__Pages(self)
        self.threads = self.__Threads(self)
        self.posts = self.__Posts(self)
        self.tags = self.__Tags(self)
        self.users = self.__Users(self)
        self.profile_posts = self.__Profile_posts(self)
        self.conversations = self.__Conversations(self)
        self.notifications = self.__Notifications(self)
        self.search = self.__Search(self)

    @property
    def scopes(self):
        return self._scopes

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value
        _MainTweaks.setup_jwt(self=self, token=value)

    def change_proxy(self, proxy_type: str = None, proxy: str = None):
        """
        Delete or change your proxy

        Skip proxy_type and proxy if you want to delete it

        :param proxy_type: Your proxy type. You can use types ( Constants.Proxy.socks5 or socks4,https,http )
        :param proxy: Proxy string. Example -> ip:port or login:password@ip:port
        """
        if proxy_type is not None:
            if proxy_type in ["HTTPS", "HTTP", "SOCKS4", "SOCKS5"]:
                self._proxy_type = proxy_type
            else:
                raise Exceptions.INVALID_PROXY_TYPE(
                    "Proxy type has invalid value. It can be only https,http,socks4 or socks5"
                )
        else:
            self._proxy_type = None
        self._proxy = proxy

    def _add_delay_synchronizer(self, synchronizer):
        self._delay_synchronizer = synchronizer

    def _remove_delay_synchronizer(self):
        self._delay_synchronizer = None
        self._auto_delay_time = self._auto_delay_time.value
        self._lock = None

    class __Categories:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: Literal["natural", "list"] = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/categories

            *List of all categories in the system.*

            Required scopes: *read*

            **Parameters:**

            - **parent_category_id** (int): ID of parent category.
            - **parent_forum_id** (int): ID of parent forum.
            - **order** (str): Ordering of categories.

            **Example:**

            ```python
            forum.categories.list()
            ```
            """
            path = "/categories"
            params = {
                "parent_category_id": parent_category_id,
                "parent_forum_id": parent_forum_id,
                "order": order,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, category_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/categories/{category_id}

            *Detail information of a category.*

            Required scopes: *read*

            **Parameters:**

            - **category_id** (int): Category ID.

            **Example:**

            ```python
            response = forum.categories.get(category_id=1)
            print(response.json())
            ```
            """
            path = f"/categories/{category_id}"
            return _send_request(self=self._api, method="GET", path=path)

    class __Forums:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: Literal["natural", "list"] = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/forums

            *List of all forums in the system.*

            Required scopes: *read*

            **Parameters:**

            - **parent_category_id** (int): ID of parent category.
            - **parent_forum_id** (int): ID of parent forum.
            - **order** (str): Ordering of categories.

            **Example:**

            ```python
            response = forum.forums.list()
            print(response.json())
            ```
            """
            path = "/forums"
            params = {
                "parent_category_id": parent_category_id,
                "parent_forum_id": parent_forum_id,
                "order": order,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, forum_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/forums/{forum_id}

            *Detail information of a forum.*

            Required scopes: *read*

            **Parameters:**

            - **transfer_type** (str): ID of forum.

            **Example:**

            ```python
            response = forum.forums.get(forum_id=766)
            print(response.json())
            ```
            """
            path = f"/forums/{forum_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def follow(
            self,
            forum_id: int,
            prefix_ids: list = None,
            minimal_contest_amount: int = None,
            post: bool = None,
            alert: bool = None,
            email: bool = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/forums/{forum_id}/followers

            *Follow a forum.*

            Required scopes: *post*

            **Parameters:**

            - **transfer_type** (str): Forum id.
            - **prefix_ids** (list): List with prefix id's.
            - **minimal_contest_amount** (int): Minimal contest amount.
                > For forum id 766
            - **post** (bool): Whether to receive notification for post.
            - **alert** (bool): Whether to receive notification as alert.
            - **email** (bool): Whether to receive notification as email.

            **Example:**

            ```python
            response = forum.forums.follow(forum_id=766)
            print(response.json())
            ```
            """
            path = f"/forums/{forum_id}/followers"
            params = {
                "post": int(post) if post else post,
                "alert": int(alert) if alert else alert,
                "email": int(email) if email else email,
                "minimal_contest_amount": minimal_contest_amount,
                "prefix_ids[]": prefix_ids,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unfollow(self, forum_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/forums/{forum_id}/followers

            *Unfollow a forum.*

            Required scopes: *post*

            **Parameters:**

            - **transfer_type** (str): Forum ID.

            **Example:**

            ```python
            response = forum.forums.unfollow(forum_id=766)
            print(response.json())
            ```
            """
            path = f"/forums/{forum_id}/followers"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followers(self, forum_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/forums/{forum_id}/followers

            *List of a forum's followers. For privacy reason, only the current user will be included in the list (if the user follows the specified forum).*

            Required scopes: *read*

            **Parameters:**

            - **transfer_type** (str): Forum ID.

            **Example:**

            ```python
            response = forum.forums.followers(forum_id=766)
            print(response.json())
            ```
            """
            path = f"/forums/{forum_id}/followers"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followed(self, total: bool = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/forums/followed

            *List of followed forums by current user.*

            Required scopes: *read*

            **Parameters:**

            - **total** (bool): If included in the request, only the forum count is returned as forums_total.

            **Example:**

            ```python
            response = forum.forums.followed()
            print(response.json())
            ```
            """
            path = "/forums/followed"
            params = {"total": int(total) if total else total}
            return _send_request(self=self._api, method="GET", path=path, params=params)

    class __Pages:
        def __init__(self, _api_self) -> httpx.Response:
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(
            self, parent_page_id: int = None, order: Literal["natural", "list"] = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/pages

            *List of all pages in the system.*

            Required scopes: *read*

            **Parameters:**

            - **parent_page_id** (int): ID of parent page.
                > If exists, filter pages that are direct children of that page.
            - **order** (str): Ordering of pages.

            **Example:**

            ```python
            response = forum.pages.list()
            print(response.json())
            ```
            """
            path = "/pages"
            params = {"parent_page_id": parent_page_id, "order": order}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, page_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/pages/page_id

            *Detail information of a page.*

            Required scopes: *read*

            **Parameters:**

            - **page_id** (int): ID of parent page. If exists, filter pages that are direct children of that page.

            **Example:**

            ```python
            response = forum.pages.get(page_id=1)
            print(response.json())
            ```
            """
            path = f"/pages/{page_id}"
            return _send_request(self=self._api, method="GET", path=path)

    class __Posts:
        class __Posts_comments:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["read"])
            def get(self, post_id: int, before: int = None) -> httpx.Response:
                """
                GET https://api.zelenka.guru/posts/{post_id}/comments

                *List of post comments in a thread (with pagination).*

                Required scopes: *read*

                **Parameters:**

                - **post_id** (int): Post ID.
                - **before** (int): The time in milliseconds (e.g. 1652177794083) before last comment date

                **Example:**

                ```python
                response = forum.posts.comments.get(post_id=1000000)
                print(response.json())
                ```
                """
                path = f"/posts/{post_id}/comments"
                params = {"before": before}
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["post"])
            def create(self, post_id: int, comment_body: str = None) -> httpx.Response:
                """
                POST https://api.zelenka.guru/posts/{post_id}/comments

                *Create a new post comment.*

                Required scopes: *post*

                **Parameters:**

                - **post_id** (int): Post ID.
                - **comment_body** (str): Content of the new post.

                **Example:**

                ```python
                response = forum.posts.comments.create(post_id=1000000, comment_body="Comment text")
                print(response.json())
                ```
                """
                path = f"/posts/{post_id}/comments"
                dataJ = {"comment_body": comment_body}
                return _send_request(
                    self=self._api, method="POST", path=path, dataJ=dataJ
                )

        def __init__(self, _api_self):
            self._api = _api_self
            self.comments = self.__Posts_comments(self._api)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(
            self,
            thread_id: int = None,
            page_of_post_id: int = None,
            post_ids: list = None,
            page: int = None,
            limit: int = None,
            order: Constants.Forum.PostOrder._Literal = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/posts

            *List of posts in a thread (with pagination).*

            Required scopes: *read*

            **Parameters:**

            - **thread_id** (int): ID of the containing thread.
            - **page_of_post_id** (int): ID of a post, posts that are in the same page with the specified post will be returned.
                > If this parameter is set, thread_id may be skipped.
            - **post_ids** (list): ID's of needed posts.
                > If this parameter is set, all other filtering parameters will be ignored.
            - **page** (int): Page number of posts.
            - **limit** (int): Number of posts in a page.
            - **order** (str): Ordering of posts.

            **Example:**

            ```python
            response = forum.posts.list(thread_id=1000000)
            print(response.json())
            ```
            """
            path = "/posts"
            if type(post_ids) is list:
                post_ids = ",".join(str(i) for i in post_ids)
            params = {
                "thread_id": thread_id,
                "page_of_post_id": page_of_post_id,
                "post_ids": post_ids,
                "page": page,
                "limit": limit,
                "order": order,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, post_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/posts/{post_id}

            *Detail information of a post.*

            Required scopes: *read*

            **Parameters:**

            - **post_id** (int): Post ID.

            **Example:**

            ```python
            response = forum.posts.get(post_id=1000000)
            print(response.json())
            ```
            """
            path = f"/posts/{post_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def create(
            self, post_body: str, thread_id: int = None, quote_post_id: int = None
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/posts

            *Create a new post.*

            Required scopes: *post*

            **Parameters:**

            - **post_body** (str): Content of the new post.
            - **thread_id** (int): ID of the target thread.
            - **quote_post_id** (int): ID of the quote post.
                > It's possible to skip thread_id if this parameter is provided. An extra check is performed if both parameters exist and does not match.

            **Example:**

            ```python
            response = forum.posts.create(post_body="Post text", thread_id=1000000)
            print(response.json())
            ```
            """
            path = "/posts"
            params = {
                "thread_id": thread_id,
                "quote_post_id": quote_post_id,
            }
            data = {"post_body": post_body}
            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                params=params,
                data=data,
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def edit(
            self, post_id: int, post_body: str = None, message_state: str = Literal["visible", "deleted", "moderated"]
        ) -> httpx.Response:
            """
            PUT https://api.zelenka.guru/posts/{post_id}

            *Edit a post.*

            Required scopes: *post*

            **Parameters:**

            - **post_id** (int): Post ID.
            - **message_state** (str): Message state.
                > Can be [visible, deleted, moderated]
            - **post_body** (str): New content of the post.

            **Example:**

            ```python
            response = forum.posts.edit(post_id=1000000, post_body="New text")
            print(response.json())
            ```
            """
            path = f"/posts/{post_id}"
            params = {"message_state": message_state}
            data = {"post_body": post_body}
            return _send_request(
                self=self._api,
                method="PUT",
                path=path,
                params=params,
                data=data,
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def delete(self, post_id: int, reason: str = None) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/posts/{post_id}

            *Delete a post.*

            Required scopes: *post*

            **Parameters:**

            - **post_id** (int): Post ID.
            - **reason** (str): Reason of the post removal.

            **Example:**

            ```python
            response = forum.posts.delete(post_id=1000000, reason="test")
            print(response.json())
            ```
            """
            path = f"/posts/{post_id}"
            data = {"reason": reason}
            return _send_request(self=self._api, method="DELETE", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def likes(
            self, post_id: int, page: int = None, limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/posts/{post_id}/likes

            *List of users who liked a post.*

            Required scopes: *read*

            **Parameters:**

            - **post_id** (int): Post ID.
            - **page** (int): Page number of users.
            - **limit** (int): Number of users in a page.

            **Example:**

            ```python
            response = forum.posts.likes(post_id=1000000)
            print(response.json())
            ```
            """
            path = f"/posts/{post_id}/likes"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def like(self, post_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/posts/{post_id}/likes

            *Like a post.*

            Required scopes: *post*

            **Parameters:**

            - **post_id** (int): Post ID.

            **Example:**

            ```python
            response = forum.posts.like(post_id=1000000)
            print(response.json())
            ```
            """
            path = f"/posts/{post_id}/likes"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unlike(self, post_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/posts/{post_id}/likes

            *Unlike a post.*

            Required scopes: *post*

            **Parameters:**

            - **post_id** (int): Post ID.

            **Example:**

            ```python
            response = forum.posts.unlike(post_id=1000000)
            print(response.json())
            ```
            """
            path = f"/posts/{post_id}/likes"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def report(self, post_id: int, reason: str) -> httpx.Response:
            """
            POST https://api.zelenka.guru/posts/{post_id}/report

            *Report a post.*

            Required scopes: *post*

            **Parameters:**

            - **post_id** (int): Post ID.
            - **reason** (str): Reason of the report.

            **Example:**

            ```python
            response = forum.posts.report(post_id=1000000, reason="test")
            print(response.json())
            ```
            """
            path = f"/posts/{post_id}/report"
            data = {"message": reason}
            return _send_request(self=self._api, method="POST", path=path, data=data)

    class __Threads:
        def __init__(self, _api_self):
            self._api = _api_self
            self.contests = self.__Contests(self._api)
            self.arbitrage = self.__Arbitrage(self._api)

        class __Contests:
            def __init__(self, _api_self):
                self._api = _api_self
                self.money = self.__Money(self._api)
                self.upgrade = self.__Upgrade(self._api)

            class __Money:
                def __init__(self, _api_self):
                    self._api = _api_self

                @_MainTweaks._CheckScopes(scopes=["post"])
                def create_by_time(
                    self,
                    post_body: str,
                    prize_data_money: float,
                    count_winners: int,
                    length_value: int,
                    length_option: Constants.Forum.Contests.Length._Literal,
                    require_like_count: int,
                    require_total_like_count: int,
                    secret_answer: str,
                    reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                    title: str = None,
                    title_en: str = None,
                    prefix_ids: list = None,
                    tags: list = None,
                    allow_ask_hidden_content: bool = None,
                    comment_ignore_group: bool = None,
                    dont_alert_followers: bool = None,
                ) -> httpx.Response:
                    """
                    POST https://api.zelenka.guru/threads

                    *Create a new thread.*

                    Required scopes: *post*

                    **Parameters:**

                    - **post_body** (str): Content of the new thread.
                    - **prize_data_money** (float): How much money will each winner receive.
                    - **count_winners** (int): Winner count (prize count).
                        > The maximum value is 100.
                    - **length_value** (int): Giveaway duration value.
                        > The maximum duration is 3 days.
                    - **length_option** (str): Giveaway duration type.
                        > Can be [minutes, hours, days]. The maximum duration is 3 days.
                    - **require_like_count** (int): Sympathies for this week.
                    - **require_total_like_count** (int): Symapthies for all time.
                    - **secret_answer** (str): Secret answer of your account.
                    - **reply_group** (int): Allow to reply only users with chosen or higher group.
                    - **title** (str): Thread title.
                        > Can be skipped if title_en set.
                    - **title_en** (str): Thread title in english.
                        > Can be skipped if title set.
                    - **prefix_ids** (list): Thread prefixes.
                    - **tags** (list): Thread tags.
                    - **allow_ask_hidden_content** (bool): Allow ask hidden content.
                    - **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
                    - **dont_alert_followers** (bool): Don't alert followers.

                    **Example:**

                    ```python
                    response = forum.threads.contests.money.create_by_time(post_body="Contest",prize_data_money=500, count_winners=1,
                                                                           length_value=3, length_option="days", require_like_count=1,
                                                                           require_total_like_count=50, secret_answer="My secret answer", title="Contest")
                    print(response.json())
                    ```
                    """
                    contest_type = "by_finish_date"
                    prize_type = "money"
                    forum_id = 766
                    if tags:
                        tags = ",".join(tags)
                    params = {
                        "prefix_id[]": prefix_ids,
                        "tags": tags,
                        "hide_contacts": 0,
                        "allow_ask_hidden_content": int(allow_ask_hidden_content) if allow_ask_hidden_content is not None else allow_ask_hidden_content,
                        "dont_alert_followers": int(dont_alert_followers) if dont_alert_followers is not None else dont_alert_followers,
                        "reply_group": reply_group,
                        "comment_ignore_group": int(comment_ignore_group) if comment_ignore_group is not None else comment_ignore_group,
                        "count_winners": count_winners,
                        "length_value": length_value,
                        "length_option": length_option,
                        "require_like_count": require_like_count,
                        "require_total_like_count": require_total_like_count,
                        "prize_type": prize_type,
                        "contest_type": contest_type,
                        "prize_data_money": prize_data_money,
                    }
                    data = {
                        "title": title,
                        "title_en": title_en,
                        "secret_answer": secret_answer,
                    }
                    required = {
                        "forum_id": forum_id,
                        "post_body": post_body,
                    }
                    if "CREATE_JOB" in locals() or "SEND_AS_ASYNC" in locals():
                        base_api = self
                    else:
                        base_api = self._api
                    return base_api.threads.create(
                        **required,
                        **params,
                        **data,
                    )

                @_MainTweaks._CheckScopes(scopes=["post"])
                def create_by_count(
                    self,
                    post_body: str,
                    prize_data_money: float,
                    count_winners: int,
                    needed_members: int,
                    require_like_count: int,
                    require_total_like_count: int,
                    secret_answer: str,
                    reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                    title: str = None,
                    title_en: str = None,
                    prefix_ids: list = None,
                    tags: list = None,
                    allow_ask_hidden_content: bool = None,
                    comment_ignore_group: bool = None,
                    dont_alert_followers: bool = None,
                ) -> httpx.Response:
                    """
                    POST https://api.zelenka.guru/threads

                    *Create a new thread.*

                    Required scopes: *post*

                    **Parameters:**

                    - **post_body** (str): Content of the new thread.
                    - **prize_data_money** (float): How much money will each winner receive.
                    - **count_winners** (int): Winner count (prize count).
                    - **needed_members** (int): Max member count.
                    - **require_like_count** (int): Sympathies for this week.
                    - **require_total_like_count** (int): Symapthies for all time.
                    - **secret_answer** (str): Secret answer of your account.
                    - **reply_group** (int): Allow to reply only users with chosen or higher group.
                    - **title** (str): Thread title.
                        > Can be skipped if title_en set.
                    - **title_en** (str): Thread title in english.
                        > Can be skipped if title set.
                    - **prefix_ids** (list): Thread prefixes.
                    - **tags** (list): Thread tags.
                    - **allow_ask_hidden_content** (bool): Allow ask hidden content.
                    - **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
                        > The maximum value is 100.
                    - **dont_alert_followers** (bool): Don't alert followers.

                    **Example:**

                    ```python
                    response = forum.threads.contests.money.create_by_count(post_body="Contest",prize_data_money=500, count_winners=1,
                                                                           needed_members=300, require_like_count=1, require_total_like_count=50,
                                                                           secret_answer="My secret answer", title="Contest")
                    print(response.json())
                    ```
                    """
                    contest_type = "by_needed_members"
                    prize_type = "money"
                    forum_id = 766
                    params = {
                        "prefix_id[]": prefix_ids,
                        "tags": ",".join(tags) if tags else tags,
                        "hide_contacts": 0,
                        "allow_ask_hidden_content": int(allow_ask_hidden_content) if allow_ask_hidden_content is not None else allow_ask_hidden_content,
                        "reply_group": reply_group,
                        "comment_ignore_group": int(comment_ignore_group) if comment_ignore_group is not None else comment_ignore_group,
                        "count_winners": count_winners,
                        "require_like_count": require_like_count,
                        "require_total_like_count": require_total_like_count,
                        "prize_type": prize_type,
                        "contest_type": contest_type,
                        "needed_members": needed_members,
                        "prize_data_money": prize_data_money,
                        "dont_alert_followers": int(dont_alert_followers) if dont_alert_followers is not None else dont_alert_followers,
                    }
                    data = {
                        "title": title,
                        "title_en": title_en,
                        "secret_answer": secret_answer,
                    }
                    required = {
                        "forum_id": forum_id,
                        "post_body": post_body,
                    }
                    if "CREATE_JOB" in locals() or "SEND_AS_ASYNC" in locals():
                        base_api = self
                    else:
                        base_api = self._api
                    return base_api.threads.create(
                        **required,
                        **params,
                        **data,
                    )

            class __Upgrade:
                def __init__(self, _api_self):
                    self._api = _api_self

                @_MainTweaks._CheckScopes(scopes=["post"])
                def create_by_time(
                    self,
                    post_body: str,
                    prize_data_upgrade: Constants.Forum.Contests.UpgradePrize._Literal,
                    count_winners: int,
                    length_value: int,
                    length_option: Constants.Forum.Contests.Length._Literal,
                    require_like_count: int,
                    require_total_like_count: int,
                    secret_answer: str,
                    reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                    title: str = None,
                    title_en: str = None,
                    prefix_ids: list = None,
                    tags: list = None,
                    allow_ask_hidden_content: bool = None,
                    comment_ignore_group: bool = None,
                    dont_alert_followers: bool = None,
                ) -> httpx.Response:
                    """
                    POST https://api.zelenka.guru/threads

                    *Create a new thread.*

                    Required scopes: *post*

                    **Parameters:**

                    - **post_body** (str): Content of the new thread.
                    - **prize_data_upgrade** (int): Which upgrade will each winner receive.
                    - **count_winners** (int): Winner count (prize count).
                        > The maximum value is 100.
                    - **length_value** (int): Giveaway duration value.
                        > The maximum duration is 3 days.
                    - **length_option** (str): Giveaway duration type.
                        > Can be [minutes, hours, days]. The maximum duration is 3 days.
                    - **require_like_count** (int): Sympathies for this week.
                    - **require_total_like_count** (int): Symapthies for all time.
                    - **secret_answer** (str): Secret answer of your account.
                    - **reply_group** (int): Allow to reply only users with chosen or higher group.
                    - **title** (str): Thread title.
                        > Can be skipped if title_en set.
                    - **title_en** (str): Thread title in english.
                        > Can be skipped if title set.
                    - **prefix_ids** (list): Thread prefixes.
                    - **tags** (list): Thread tags.
                    - **allow_ask_hidden_content** (bool): Allow ask hidden content.
                    - **dont_alert_followers** (bool): Don't alert followers.
                    - **comment_ignore_group** (bool): Allow commenting if user can't post in thread.

                    **Example:**

                    ```python
                    response = forum.threads.contests.upgrade.create_by_time(post_body="Contest",prize_data_upgrade=1, count_winners=1,
                                                                           length_value=3, length_option="days", require_like_count=1,
                                                                           require_total_like_count=50, secret_answer="My secret answer", title="Contest")
                    print(response.json())
                    ```
                    """
                    contest_type = "by_finish_date"
                    prize_type = "upgrades"
                    forum_id = 766
                    params = {
                        "prefix_id[]": prefix_ids,
                        "tags": ",".join(tags) if tags else tags,
                        "hide_contacts": 0,
                        "allow_ask_hidden_content": int(allow_ask_hidden_content) if allow_ask_hidden_content is not None else allow_ask_hidden_content,
                        "reply_group": reply_group,
                        "comment_ignore_group": int(comment_ignore_group) if comment_ignore_group is not None else comment_ignore_group,
                        "count_winners": count_winners,
                        "require_like_count": require_like_count,
                        "require_total_like_count": require_total_like_count,
                        "prize_type": prize_type,
                        "contest_type": contest_type,
                        "dont_alert_followers": int(dont_alert_followers) if dont_alert_followers is not None else dont_alert_followers,
                        "prize_data_upgrade": prize_data_upgrade,
                        "length_value": length_value,
                        "length_option": length_option,
                    }
                    data = {
                        "title": title,
                        "title_en": title_en,
                        "secret_answer": secret_answer,
                    }
                    required = {
                        "forum_id": forum_id,
                        "post_body": post_body,
                    }
                    if "CREATE_JOB" in locals() or "SEND_AS_ASYNC" in locals():
                        base_api = self
                    else:
                        base_api = self._api
                    return base_api.threads.create(
                        **required,
                        **params,
                        **data,
                    )

                @_MainTweaks._CheckScopes(scopes=["post"])
                def create_by_count(
                    self,
                    post_body: str,
                    prize_data_upgrade: Constants.Forum.Contests.UpgradePrize._Literal,
                    count_winners: int,
                    needed_members: int,
                    require_like_count: int,
                    require_total_like_count: int,
                    secret_answer: str,
                    reply_group: Constants.Forum.ReplyGroups._Literal = 2,
                    title: str = None,
                    title_en: str = None,
                    prefix_ids: list = None,
                    tags: list = None,
                    allow_ask_hidden_content: bool = None,
                    comment_ignore_group: bool = None,
                    dont_alert_followers: bool = None,
                ) -> httpx.Response:
                    """
                    POST https://api.zelenka.guru/threads

                    *Create a new thread.*

                    Required scopes: *post*

                    **Parameters:**

                    - **post_body** (str): Content of the new thread.
                    - **prize_data_upgrade** (int): Which upgrade will each winner receive.
                    - **count_winners** (int): Winner count (prize count).
                        > The maximum value is 100.
                    - **needed_members** (int): Max member count.
                    - **require_like_count** (int): Sympathies for this week.
                    - **require_total_like_count** (int): Symapthies for all time.
                    - **secret_answer** (str): Secret answer of your account.
                    - **reply_group** (int): Allow to reply only users with chosen or higher group.
                    - **title** (str): Thread title.
                        > Can be skipped if title_en set.
                    - **title_en** (str): Thread title in english.
                        > Can be skipped if title set.
                    - **prefix_ids** (list): Thread prefixes.
                    - **tags** (list): Thread tags.
                    - **allow_ask_hidden_content** (bool): Allow ask hidden content.
                    - **dont_alert_followers** (bool): Don't alert followers.
                    - **comment_ignore_group** (bool): Allow commenting if user can't post in thread.

                    **Example:**

                    ```python
                    response = forum.threads.contests.money.create_by_count(post_body="Contest",prize_data_upgrade=1, count_winners=1,
                                                                           needed_members=300, require_like_count=1, require_total_like_count=50,
                                                                           secret_answer="My secret answer", title="Contest")
                    print(response.json())
                    ```
                    """
                    params = {
                        "prefix_id[]": prefix_ids,
                        "tags": ",".join(tags) if tags else tags,
                        "hide_contacts": 0,
                        "allow_ask_hidden_content": int(allow_ask_hidden_content) if allow_ask_hidden_content is not None else allow_ask_hidden_content,
                        "reply_group": reply_group,
                        "comment_ignore_group": int(comment_ignore_group) if comment_ignore_group is not None else comment_ignore_group,
                        "count_winners": count_winners,
                        "require_like_count": require_like_count,
                        "require_total_like_count": require_total_like_count,
                        "prize_type": "upgrades",
                        "contest_type": "by_needed_members",
                        "needed_members": needed_members,
                        "dont_alert_followers": int(dont_alert_followers) if dont_alert_followers is not None else dont_alert_followers,
                        "prize_data_upgrade": prize_data_upgrade,
                    }

                    data = {
                        "title": title,
                        "title_en": title_en,
                        "secret_answer": secret_answer,
                    }
                    required = {
                        "forum_id": 766,
                        "post_body": post_body,
                    }
                    if "CREATE_JOB" in locals() or "SEND_AS_ASYNC" in locals():
                        base_api = self
                    else:
                        base_api = self._api
                    return base_api.threads.create(
                        **required,
                        **params,
                        **data,
                    )

        class __Arbitrage:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["post"])
            def market(
                self,
                responder: str,
                item_id: Union[str, int],
                amount: float,
                post_body: str,
                currency: Constants.Market.Currency._Literal = None,
                conversation_screenshot: str = "no",
                tags: list = None,
                hide_contacts: bool = None,
                allow_ask_hidden_content: bool = None,
                comment_ignore_group: bool = None,
                dont_alert_followers: bool = None,
                reply_group: Constants.Forum.ReplyGroups._Literal = 2,
            ) -> httpx.Response:
                """
                POST https://api.zelenka.guru/claims

                *Create a Arbitrage.*

                Required scopes: *post*

                **Parameters:**

                - **responder** (str): To whom the complaint is filed. Specify a nickname or a link to the profile.
                - **item_id** (str|int): Write account link or item_id.
                - **amount** (float): Amount by which the responder deceived you.
                - **post_body** (str): You should describe what's happened.
                - **currency** (str): Currency of Arbitrage.
                - **conversation_screenshot** (str): Screenshot showing the respondent's Telegram login. If the correspondence was conducted in Telegram, upload screenshot that will display the respondent's Telegram login against the background of your dialogue. The screenshot must be uploaded to Imgur. If the correspondence was conducted elsewhere, write "no".
                - **tags** (list): Thread tags.
                - **hide_contacts** (bool): Hide contacts.
                - **allow_ask_hidden_content** (bool): Allow ask hidden content.
                - **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
                - **dont_alert_followers** (bool): Don't alert followers.
                - **reply_group** (int): Allow to reply only users with chosen or higher group.

                **Example:**

                ```python
                response = forum.threads.arbitrage.market(responder="AS7RID", item_id=1000000, amount=1000,
                                                          post_body="Arbitrage test", currency="rub")
                print(response.json())
                ```
                """
                path = "/claims"
                data = {
                    "post_body": post_body,
                    "as_responder": responder,
                    "as_is_market_deal": 1,
                    "as_market_item_id": item_id,
                    "as_amount": amount,
                    "currency": currency,
                    "as_funds_receipt": "no",
                    "as_tg_login_screenshot": conversation_screenshot,
                    "tags": ",".join(tags) if tags else tags,
                    "hide_contacts": int(hide_contacts) if hide_contacts is not None else hide_contacts,
                    "allow_ask_hidden_content": int(allow_ask_hidden_content) if allow_ask_hidden_content is not None else allow_ask_hidden_content,
                    "comment_ignore_group": int(comment_ignore_group) if comment_ignore_group is not None else comment_ignore_group,
                    "dont_alert_followers": int(dont_alert_followers) if dont_alert_followers is not None else dont_alert_followers,
                    "reply_group": reply_group,
                }
                return _send_request(
                    self=self._api, method="POST", path=path, data=data
                )

            @_MainTweaks._CheckScopes(scopes=["post"])
            def non_market(
                self,
                responder: str,
                amount: float,
                receipt: str,
                post_body: str,
                pay_claim: bool,
                conversation_screenshot: str = "no",
                responder_data: str = None,
                currency: Constants.Market.Currency._Literal = None,
                transfer_type: Constants.Forum.Arbitrage.TransferType._Literal = "notsafe",
                tags: list = None,
                hide_contacts: bool = None,
                allow_ask_hidden_content: bool = None,
                comment_ignore_group: bool = None,
                dont_alert_followers: bool = None,
                reply_group: Constants.Forum.ReplyGroups._Literal = 2,
            ) -> httpx.Response:
                """
                POST https://api.zelenka.guru/claims

                *Create a Arbitrage.*

                Required scopes: *post*

                **Parameters:**

                - **responder** (str): To whom the complaint is filed. Specify a nickname or a link to the profile.
                - **amount** (float): Amount by which the responder deceived you.
                - **currency** (str): Currency of Arbitrage.
                - **receipt** (str): Funds transfer recipient. Upload a receipt for the transfer of funds, use the "View receipt" button in your wallet. Must be uploaded to Imgur. Write "no" if you have not paid.
                - **post_body** (str): You should describe what's happened.
                - **pay_claim** (bool): If you set this parameter to **True** forum will automatically calculate the amount and debit it from your account.
                    > For filing claims, it is necessary to make a contribution in the amount of 5% of the amount of damage (but not less than 50 rubles and not more than 5000 rubles). For example, for an amount of damage of 300 rubles, you will need to pay 50 rubles, for 2,000 and 10,000 rubles - 100 and 500 rubles, respectively).
                - **pay_claim** (str): Contacts and wallets of the responder. Specify the known data about the responder (Skype, Vkontakte, Qiwi, WebMoney, etc.), if any.
                - **transfer_type** (str): The transaction took place through a guarantor or there was a transfer to the market with a hold? Can be ["safe", "notsafe"]
                - **conversation_screenshot** (str): Screenshot showing the respondent's Telegram login. If the correspondence was conducted in Telegram, upload screenshot that will display the respondent's Telegram login against the background of your dialogue. The screenshot must be uploaded to Imgur. If the correspondence was conducted elsewhere, write "no".
                - **tags** (list): Thread tags.
                - **hide_contacts** (bool): Hide contacts.
                - **allow_ask_hidden_content** (bool): Allow ask hidden content.
                - **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
                - **dont_alert_followers** (bool): Don't alert followers.
                - **reply_group** (int): Allow to reply only users with chosen or higher group.

                **Example:**

                ```python
                response = forum.threads.arbitrage.non_market(responder="AS7RID", amount=100, currency="rub", receipt="no",
                                                              post_body="Non market arbitrage", pay_claim=True, transfer_type="safe")
                print(response.json())
                ```
                """
                path = "/claims"
                data = {
                    "post_body": post_body,
                    "as_responder": responder,
                    "as_is_market_deal": 0,
                    "as_amount": amount,
                    "currency": currency,
                    "conversation_screenshot": conversation_screenshot,
                    "as_data": responder_data,
                    "pay_claim": pay_claim,
                    "transfer_type": transfer_type,
                    "as_funds_receipt": receipt,
                    "as_tg_login_screenshot": conversation_screenshot,
                    "tags": ",".join(tags) if tags else tags,
                    "hide_contacts": int(hide_contacts) if hide_contacts is not None else hide_contacts,
                    "allow_ask_hidden_content": int(allow_ask_hidden_content) if allow_ask_hidden_content is not None else allow_ask_hidden_content,
                    "comment_ignore_group": int(comment_ignore_group) if comment_ignore_group is not None else comment_ignore_group,
                    "dont_alert_followers": dont_alert_followers,
                    "reply_group": reply_group,
                }
                return _send_request(
                    self=self._api, method="POST", path=path, data=data
                )

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(
            self,
            forum_id: int = None,
            thread_ids: str = None,
            creator_user_id: int = None,
            sticky: bool = None,
            thread_prefix_id: int = None,
            thread_tag_id: int = None,
            page: int = None,
            limit: int = None,
            order: Constants.Forum.ThreadOrder._Literal = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads

            *List of threads in a forum (with pagination).*

            Required scopes: *read*

            **Parameters:**

            - **forum_id** (int): ID of the containing forum.
                > Can be skipped if thread_ids set.
            - **thread_ids** (list): ID's of needed threads (separated by comma).
                > If this parameter is set, all other filtering parameters will be ignored.
            - **creator_user_id** (int): Filter to get only threads created by the specified user.
            - **sticky** (bool): Filter to get only sticky or non-sticky threads.
                > By default, all threads will be included and sticky ones will be at the top of the result on the first page. In mixed mode, sticky threads are not counted towards threads_total and does not affect pagination.
            - **thread_prefix_id** (int): Filter to get only threads with the specified prefix.
            - **thread_tag_id** (int): Filter to get only threads with the specified tag.
            - **page** (int): Page number of threads.
            - **limit** (int): Number of threads in a page.
            - **order** (str): Threads order.
                > Can be [natural, thread_create_date, thread_create_date_reverse, thread_update_date, thread_update_date_reverse, thread_view_count, thread_view_count_reverse, thread_post_count, thread_post_count_reverse]

            **Example:**

            ```python
            response = forum.threads.list(forum_id=766)
            print(response.json())
            ```
            """
            path = "/threads"
            params = {
                "forum_id": forum_id,
                "thread_ids": thread_ids,
                "creator_user_id": creator_user_id,
                "sticky": int(sticky) if sticky else sticky,
                "thread_prefix_id": thread_prefix_id,
                "thread_tag_id": thread_tag_id,
                "page": page,
                "limit": limit,
                "order": order,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, thread_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/{thread_id}

            *Detail information of a thread.*

            Required scopes: *read*

            **Parameters:**

            - **thread_id** (int): ID of thread.

            **Example:**

            ```python
            response = forum.threads.get(thread_id=1000000)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def create(
            self,
            forum_id: int,
            post_body: str,
            reply_group: Constants.Forum.ReplyGroups._Literal = 2,
            title: str = None,
            title_en: str = None,
            prefix_ids: list = None,
            tags: list = None,
            hide_contacts: bool = None,
            allow_ask_hidden_content: bool = None,
            comment_ignore_group: bool = None,
            dont_alert_followers: bool = None,
            **kwargs,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/threads

            *Create a new thread.*

            Required scopes: *post*

            **Parameters:**

            - **forum_id** (int): ID of the target forum.
            - **post_body** (str): Content of the new thread.
            - **title** (str): Thread title.
                        > Can be skipped if title_en set.
            - **title_en** (str): Thread title in english.
                        > Can be skipped if title set.
            - **prefix_ids** (list): Thread prefixes.
            - **tags** (list): Thread tags.
            - **hide_contacts** (bool): Hide contacts.
            - **allow_ask_hidden_content** (bool): Allow ask hidden content.
            - **reply_group** (int): Allow to reply only users with chosen or higher group.
            - **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
            - **dont_alert_followers** (bool): Don't alert followers.

            **Example:**

            ```python
            response = forum.threads.create(forum_id=876, post_body="Test thread in test forum", title="Test thread")
            print(response.json())
            ```
            """
            path = "/threads"
            params = {
                "prefix_id[]": prefix_ids,
                "tags": ",".join(tags) if tags else tags,
                "hide_contacts": int(hide_contacts) if hide_contacts is not None else hide_contacts,
                "allow_ask_hidden_content": int(allow_ask_hidden_content) if allow_ask_hidden_content is not None else allow_ask_hidden_content,
                "reply_group": reply_group,
                "comment_ignore_group": int(comment_ignore_group) if comment_ignore_group is not None else comment_ignore_group,
                "dont_alert_followers": dont_alert_followers,
            }
            data = {
                "forum_id": forum_id,
                "title": title,
                "title_en": title_en,
                "post_body": post_body,
            }
            if kwargs:
                for key, value in kwargs.items():
                    if (key not in params) and (key not in data):
                        data[key] = value
            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                data=data,
                params=params,
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def edit(
            self,
            thread_id: int,
            title: str = None,
            title_en: str = None,
            prefix_ids: list = None,
            tags: list = None,
            discussion_open: bool = None,
            hide_contacts: bool = None,
            allow_ask_hidden_content: bool = None,
            reply_group: Constants.Forum.ReplyGroups._Literal = None,
            comment_ignore_group: bool = None,
        ) -> httpx.Response:
            """
            PUT https://api.zelenka.guru/threads/{thread_id}

            *Edit a thread.*

            Required scopes: *post*

            Reply groups:

            **Parameters:**

            - **thread_id** (int): Id of thread.
            - **title** (str): Thread title.
            - **title_en** (str): Thread title in english.
            - **prefix_ids** (list): Thread prefixes.
            - **tags** (list): Thread tags.
            - **discussion_open** (bool): Discussion state.
            - **hide_contacts** (bool): Hide contacts.
            - **allow_ask_hidden_content** (bool): Allow ask hidden content.
            - **reply_group** (int): Allow to reply only users with chosen or higher group.
            - **comment_ignore_group** (bool): Allow commenting if user can't post in thread.

            **Example:**

            ```python
            response = forum.threads.edit(thread_id=1000000, title="New thread title")
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}"
            data = {
                "title": title,
                "title_en": title_en,
                "prefix_id[]": prefix_ids,
                "tags": ",".join(tags) if tags else tags,
                "discussion_open": int(discussion_open) if discussion_open is not None else discussion_open,
                "hide_contacts": int(hide_contacts) if hide_contacts is not None else hide_contacts,
                "allow_ask_hidden_content": int(allow_ask_hidden_content) if allow_ask_hidden_content is not None else allow_ask_hidden_content,
                "reply_group": reply_group,
                "comment_ignore_group": int(comment_ignore_group) if comment_ignore_group is not None else comment_ignore_group,
            }
            return _send_request(self=self._api, method="PUT", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def move(
            self,
            thread_id: int,
            forum_id: int,
            title: str = None,
            title_en: str = None,
            prefix_ids: list = None,
            send_alert: bool = None
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/threads/{thread_id}/move

            *Move a thread.*

            Required scopes: *post*

            **Parameters:**

            - **thread_id** (int): Id of thread.
            - **forum_id** (int): Target forum id.
            - **title** (str): Thread title.
            - **title_en** (str): Thread title in english.
            - **prefix_ids** (list): Thread prefixes.
            - **send_alert** (bool): Send a notification to users who are followed to target node.

            **Example:**

            ```python
            response = forum.threads.move(thread_id=1000000, forum_id=876)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}/move"
            data = {
                "node_id": forum_id,
                "title": title,
                "title_en": title_en,
                "prefix_id[]": prefix_ids,
                "apply_thread_prefix": 1 if prefix_ids else None,
                "send_alert": int(send_alert) if send_alert else send_alert
            }
            return _send_request(self=self._api, method="POST", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def delete(self, thread_id: int, reason: str = None) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/threads/{thread_id}

            *Delete a thread.*

            Required scopes: *post*

            **Parameters:**

            - **thread_id** (int): ID of thread.
            - **reason** (str): Reason of the thread removal.

            **Example:**

            ```python
            response = forum.threads.delete(thread_id=1000000, reason="delete reason)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}"
            params = {"reason": reason}
            return _send_request(
                self=self._api, method="DELETE", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followers(self, thread_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/{thread_id}/followers

            *List of a thread's followers. For privacy reason, only the current user will be included in the list.*

            Required scopes: *read*

            **Parameters:**

            - **thread_id** (int): ID of thread.

            **Example:**

            ```python
            response = forum.threads.followers(thread_id=1000000)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}/followers"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followed(self, total: bool = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/followed

            *List of followed threads by current user.*

            Required scopes: *read*

            **Parameters:**

            - **total** (bool): If included in the request, only the thread count is returned as threads_total.

            **Example:**

            ```python
            response = forum.threads.followed()
            print(response.json())
            ```
            """
            path = "/threads/followed"
            params = {"total": int(total) if total else total}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def follow(self, thread_id: int, email: bool = None) -> httpx.Response:
            """
            POST https://api.zelenka.guru/threads/{thread_id}/followers

            *Follow a thread.*

            Required scopes: *post*

            **Parameters:**

            - **thread_id** (int): ID of thread.
            - **email** (bool): Whether to receive notification as email.

            **Example:**

            ```python
            response = forum.threads.follow(threads_id=1000000, email=False)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}/followers"
            params = {"email": int(email) if email else email}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unfollow(self, thread_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/threads/{thread_id}/followers

            *Unfollow a thread.*

            Required scopes: *post*

            **Parameters:**

            - **thread_id** (int): ID of thread.

            **Example:**

            ```python
            response = forum.threads.unfollow(thread_id=1000000)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}/followers"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def navigation(self, thread_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/{thread_id}/navigation

            *List of navigation elements to reach the specified thread.*

            Required scopes: *read*

            **Parameters:**

            - **thread_id** (int): ID of thread.

            **Example:**

            ```python
            response = forum.threads.navigation(thread_id=1000000)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}/navigation"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def votes(self, thread_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/{thread_id}/poll

            *Detail information of a poll.*

            Required scopes: *read*

            **Parameters:**

            - **thread_id** (int): ID of thread.

            **Example:**

            ```python
            response = forum.threads.votes(thread_id=1000000)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}/poll"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def vote(
            self,
            thread_id: int,
            response_ids: Union[builtins.list[int], int],
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/threads/{thread_id}/pool/votes

            *Vote on a thread poll.*

            Required scopes: *post*

            **Parameters:**

            - **thread_id** (int): ID of thread.
            - **response_ids** (list): Pool response ids. (if the poll allows multiple choices).

            **Example:**

            ```python
            response = forum.threads.vote(thread_id=1000000, response_ids=264758)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}/pool/votes"

            if type(response_ids) is list:
                for element in response_ids:
                    if not isinstance(element, int):
                        _WarningsLogger.warn(f"{FutureWarning.__name__} All response_ids elements should be integer")
            elif type(response_ids) is int:
                response_ids = [response_ids]
            params = {"response_id": response_ids[0]} if len(response_ids) == 1 else {
                "response_ids[]": response_ids}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["read"])
        def new(
            self, forum_id: int = None, limit: int = None, data_limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/new

            *List of unread threads (must be logged in).*

            Required scopes: *read*

            **Parameters:**

            - **forum_id** (int): ID of the container forum to search for threads.
                > Child forums of the specified forum will be included in the search.
            - **limit** (int): Maximum number of result threads.
            - **data_limit** (int): Number of thread data to be returned.
                > Default value is 20.

            **Example:**

            ```python
            response = forum.threads.new(thread_id=876)
            print(response.json())
            ```
            """
            path = "/threads/new"
            params = {
                "forum_id": forum_id,
                "limit": limit,
                "data_limit": data_limit,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def recent(
            self,
            days: int = None,
            forum_id: int = None,
            limit: int = None,
            data_limit: int = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/recent

            *List of recent threads.*

            Required scopes: *read*

            **Parameters:**

            - **days** (int): Maximum number of days to search for threads.
            - **forum_id** (int): ID of the container forum to search for threads.
                > Child forums of the specified forum will be included in the search.
            - **limit** (int): Maximum number of result threads.
            - **data_limit** (int): Number of thread data to be returned.
                > Default value is 20.

            **Example:**

            ```python
            response = forum.threads.recent(days=3, forum_id=876)
            print(response.json())
            ```
            """
            path = "/threads/recent"
            params = {
                "days": days,
                "forum_id": forum_id,
                "limit": limit,
                "data_limit": data_limit,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def bump(self, thread_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/threads/{thread_id}/bump

            *Bump a thread.*

            Required scopes: *post*

            **Parameters:**

            - **thread_id** (int): ID of thread.

            **Example:**

            ```python
            response = forum.threads.bump(thread_id=1000000)
            print(response.json())
            ```
            """
            path = f"/threads/{thread_id}/bump"
            return _send_request(self=self._api, method="POST", path=path)

    class __Tags:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["read"])
        def popular(self) -> httpx.Response:
            """
            GET https://api.zelenka.guru/tags

            *List of popular tags (no pagination).*

            Required scopes: *read*

            **Example:**

            ```python
            response = forum.tags.popular()
            print(response.json())
            ```
            """
            path = "/tags"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(self, page: int = None, limit: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/tags/list

            *List of tags.*

            Required scopes: *read*

            **Parameters:**

            - **page** (int): Page number of tags list.
            - **limit** (int): Limit of tags on a page.

            **Example:**

            ```python
            response = forum.tags.list(page=123)
            print(response.json())
            ```
            """
            path = "/tags/list"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def tagged(
            self, tag_id: int, page: int = None, limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/tags/{tag_id}

            *List of tagged contents.*

            Required scopes: *read*

            **Parameters:**

            - **tag_id** (int): ID of tag.
            - **page** (int): Page number of tags list.
            - **limit** (int): Number of tagged contents in a page.

            **Example:**

            ```python
            response = forum.tags.tagged(tag_id=1000)
            print(response.json())
            ```
            """
            path = f"/tags/{tag_id}"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def find(self, tag: str) -> httpx.Response:
            """
            GET https://api.zelenka.guru/tags/find

            *Filtered list of tags.*

            Required scopes: *read*

            **Parameters:**

            - **tag** (str): Tag to filter. Tags start with the query will be returned.

            **Example:**

            ```python
            response = forum.tags.find(tag="LOLZTEAM")
            print(response.json())
            ```
            """
            path = "/tags/find"
            params = {"tag": tag}
            return _send_request(self=self._api, method="GET", path=path, params=params)

    class __Users:
        class __Avatar:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["post?admincp"])
            def upload(self, avatar: bytes, user_id: int = None) -> httpx.Response:
                """
                POST https://api.zelenka.guru/users/{user_id}/avatar

                *Upload avatar for a user.*

                Required scopes: *post*

                **Parameters:**

                - **user_id** (int): ID of user.
                    > If you do not specify the user_id, then you will change the avatar of the current user
                - **avatar** (binary): Binary data of the avatar.

                **Example:**

                ```python
                with open("avatar.png", "rb") as file:
                    avatar = file.read()
                response = forum.users.avatar.upload(avatar=avatar)
                print(response.json())
                ```
                """
                if "CREATE_JOB" in locals():
                    _WarningsLogger.warn(
                        msg=f"{FutureWarning.__name__}: You can't upload avatar using batch")
                path = "/users/me/avatar" if not user_id else f"/users/{user_id}/avatar"
                files = {"avatar": avatar}
                params = {"user_id": user_id}
                return _send_request(
                    self=self._api, method="POST", path=path, files=files, params=params
                )

            @_MainTweaks._CheckScopes(scopes=["post?admincp"])
            def delete(self, user_id: int = None) -> httpx.Response:
                """
                DELETE https://api.zelenka.guru/users/{user_id}/avatar

                *Delete avatar for a user.*

                Required scopes: *post*

                **Parameters:**

                - **user_id** (int): ID of user.
                    > If you do not specify the user_id, then you will delete the avatar of the current user

                **Example:**

                ```python
                response = forum.users.avatar.delete()
                print(response.json())
                ```
                """
                if user_id is None:
                    path = "/users/me/avatar"
                else:
                    path = f"/users/{user_id}/avatar"
                return _send_request(self=self._api, method="DELETE", path=path)

            @_MainTweaks._CheckScopes(scopes=["post?admincp"])
            def crop(
                self, user_id: int = None, size: int = 16, x: int = None, y: int = None
            ) -> httpx.Response:
                """
                POST https://api.zelenka.guru/users/{user_id}/avatar-crop

                *Crop avatar for a user.*

                Required scopes: *post*

                **Parameters:**

                - **user_id** (int): ID of user.
                - **x** (int): The starting point of the selection by width.
                - **y** (int): The starting point of the selection by height
                - **size** (int): Selection size.
                    > Minimum value - 16.

                **Example:**

                ```python
                response = forum.users.avatar.crop(size=128, x=256, y=384)
                print(response.json())
                ```
                """
                params = {"x": x, "y": y, "crop": size}
                if user_id:
                    path = f"/users/{user_id}/avatar-crop"
                else:
                    path = "/users/me/avatar-crop"
                return _send_request(
                    self=self._api,
                    method="POST",
                    path=path,
                    params=params,
                )

        def __init__(self, _api_self):
            self._api = _api_self
            self.avatar = self.__Avatar(self._api)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(self, page: int = None, limit: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users

            *List of users (with pagination).*

            Required scopes: *read*

            **Parameters:**

            - **page** (int): Page number of users.
            - **limit** (int): Number of users in a page.

            **Example:**

            ```python
            response = forum.users.list(page=1)
            print(response.json())
            ```
            """
            path = "/users"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def fields(self) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/fields

            *List of user fields.*

            Required scopes: *read*

            **Example:**

            ```python
            response = forum.users.fields()
            print(response.json())
            ```
            """

            path = "/users/fields"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read?admincp"])
        def search(
            self,
            username: str = None,
            user_email: str = None,
            custom_fields: dict = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/find

            *Filtered list of users by username, email or custom fields.*

            Required scopes: *read*

            **Parameters:**

            - **username** (str): Username to filter. Usernames start with the query will be returned.
            - **user_email** (str): Email to filter.
                > Requires admincp scope.
            - **custom_fields** (str): Custom fields to filter.
                > Example {"telegram": "AS7RID"}

            **Example:**

            ```python
            response = forum.users.search(username="AS7RID)
            print(response.json())
            ```
            """
            path = "/users/find"
            params = {
                "username": username,
                "user_email": user_email,
            }
            if custom_fields is not None:
                if "CREATE_JOB" in locals():
                    # Костыль CreateJob
                    params["custom_fields"] = custom_fields
                else:
                    for key, value in custom_fields.items():
                        cf = f"custom_fields[{key}]"
                        params[cf] = value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read?basic"])
        def get(self, user_id: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/{user_id}

            *Detail information of a user.*

            Required scopes: *read*, *basic*

            **Parameters:**

            - **user_id** (int): ID of user.
                > If you do not specify the user_id, you will get info about current user

            **Example:**

            ```python
            response = forum.users.get(user_id=2410024)
            print(response.json())
            ```
            """
            if user_id is None:
                path = "/users/me"
            else:
                path = f"/users/{user_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def timeline(
            self, user_id: int = None, page: int = None, limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/{user_id}/timeline

            *List of contents created by user (with pagination).*

            Required scopes: *read*

            **Parameters:**

            - **user_id** (int): ID of user.
                > If you do not specify the user_id, you will get timeline of current user
            - **page** (int): Page number of contents.
            - **limit** (int): Number of contents in a page.

            **Example:**

            ```python
            response = forum.users.timeline(user_id=2410024)
            print(response.json())
            ```
            """
            if user_id is None:
                path = "/users/me/timeline"
            else:
                path = f"/users/{user_id}/timeline"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post?admincp"])
        def edit(
            self,
            user_id: int = None,
            password: str = None,
            password_old: str = None,
            password_algo: str = None,
            user_email: str = None,
            username: str = None,
            user_title: str = None,
            primary_group_id: int = None,
            secondary_group_ids: builtins.list[int] = None,
            user_dob_day: int = None,
            user_dob_month: int = None,
            user_dob_year: int = None,
            fields: dict = None,
            display_group_id: int = None,
        ) -> httpx.Response:
            """
            PUT https://api.zelenka.guru/users/{user_id}

            *Edit a user.*

            Required scopes: *post*

            **Parameters:**

            - **user_id** (int): ID of user.
                > If you do not specify the user_id, you will edit current user
            - **password** (str): New password.
            - **password_old** (str): Data of the existing password, it is not required if (1) the current authenticated user has user admin permission, (2) the admincp scope is granted and (3) the user being edited is not the current authenticated user.
            - **password_algo** (str): Algorithm used to encrypt the password and password_old parameters.
            - **user_email** (str): New email of the user.
            - **username** (str): New username of the user.
                > Changing username requires Administrator permission.
            - **user_title** (str): New custom title of the user.
            - **primary_group_id** (int): ID of new primary group.
            - **secondary_group_ids** (list): Array of ID's of new secondary groups.
            - **user_dob_day** (int): Date of birth (day) of the new user.
            - **user_dob_month** (int): Date of birth (month) of the new user.
            - **user_dob_year** (int): Date of birth (year) of the new user.
            - **fields** (dict): Dictionary for user fields.
            - **display_group_id** (int): Id of group you want to display.

            **Example:**

            ```python
            response = forum.users.edit(title="New title")
            print(response.json())
            ```
            """
            if user_id:
                path = f"/users/{user_id}"
            else:
                path = "/users/me"
            params = {
                "user_email": user_email,
                "username": username,
                "primary_group_id": primary_group_id,
                "secondary_group_ids[]": secondary_group_ids,
                "user_dob_day": user_dob_day,
                "user_dob_month": user_dob_month,
                "user_dob_year": user_dob_year,
                "display_group_id": display_group_id,
            }
            data = {
                "user_title": user_title,
                "password": password,
                "password_old": password_old,
                "password_algo": password_algo,
            }
            if fields is not None:
                if "CREATE_JOB" in locals():
                    data["fields"] = fields  # Костыль CreateJob
                else:
                    for key, value in fields.items():
                        field = f"fields[{key}]"
                        data[field] = value
            return _send_request(
                self=self._api,
                method="PUT",
                path=path,
                params=params,
                data=data,
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def follow(self, user_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/users/{user_id}/followers

            *Follow a user.*

            Required scopes: *post*

            **Parameters:**

            - **user_id** (int): ID of user

            **Example:**

            ```python
            response = forum.users.follow(user_id=2410024)
            print(response.json())
            ```
            """
            path = f"/users/{user_id}/followers"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unfollow(self, user_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/users/{user_id}/followers

            *Unfollow a user.*

            Required scopes: *post*

            **Parameters:**

            - **user_id** (int): ID of user

            **Example:**

            ```python
            response = forum.users.unfollow(user_id=2410024)
            print(response.json())
            ```
            """
            path = f"/users/{user_id}/followers"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followers(
            self,
            user_id: int = None,
            order: Literal["natural", "follow_date", "follow_date_reverse"] = None,
            page: int = None,
            limit: int = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/{user_id}/followers

            *List of a user's followers.*

            Required scopes: *read*

            **Parameters:**

            - **user_id** (int): ID of user.
                > If you do not specify the user_id, you will get followers of current user
            - **order** (str): Ordering of followers.
            - **page** (int): Page number of followers.
            - **limit** (int): Number of followers in a page.

            **Example:**

            ```python
            response = forum.users.followers(user_id=2410024)
            print(response.json())
            ```
            """
            if user_id is None:
                path = "/users/me/followers"
            else:
                path = f"/users/{user_id}/followers"
            params = {"order": order, "page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followings(
            self,
            user_id: int = None,
            order: Literal["natural", "follow_date", "follow_date_reverse"] = None,
            page: int = None,
            limit: int = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/{user_id}/followings

            *List of users whom are followed by a user.*

            Required scopes: *read*

            **Parameters:**

            - **user_id** (int): ID of user.
                > If you do not specify the user_id, you will get followings users by current user
            - **order** (str): Ordering of users.
            - **page** (int): Page number of users.
            - **limit** (int): Number of users in a page.

            **Example:**

            ```python
            response = forum.users.followings(user_id=2410024)
            print(response.json())
            ```
            """
            if user_id:
                path = f"/users/{user_id}/followings"
            else:
                path = "/users/me/followings"
            params = {"order": order, "page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def ignored(self, total: bool = None) -> httpx.Response:
            """
             GET https://api.zelenka.guru/users/ignored

            *List of ignored users of current user.*

            Required scopes: *read*

            **Parameters:**

            - **total** (bool): If included in the request, only the user count is returned as users_total.

            **Example:**

            ```python
            response = forum.users.ignored()
            print(response.json())
            ```
            """
            path = "/users/ignored"
            params = {"total": int(total) if total else total}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def ignore(self, user_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/users/{user_id}/ignore

            *Ignore a user.*

            Required scopes: *post*

            **Parameters:**

            - **user_id** (int): ID of user

            **Example:**

            ```python
            response = forum.users.ignore(user_id=2410024)
            print(response.json())
            ```
            """

            path = f"/users/{user_id}/ignore"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unignore(self, user_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/users/{user_id}/ignore

            *Unignore a user.*

            Required scopes: *post*

            **Parameters:**

            - **user_id** (int): ID of user

            **Example:**

            ```python
            response = forum.users.unignore(user_id=2410024)
            print(response.json())
            ```
            """

            path = f"/users/{user_id}/ignore"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def groups(self, user_id: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/{user_id}/groups

            *List of a user's groups.*

            Required scopes: *read*

            **Parameters:**

            - **user_id** (int): ID of user.
                > If user_id skipped, method will return current user groups

            **Example:**

            ```python
            response = forum.users.groups(user_id=2410024)
            print(response.json())
            ```
            """
            if user_id:
                path = f"/users/{user_id}/groups"
            else:
                path = "/users/me/groups"
            return _send_request(self=self._api, method="GET", path=path)

    class __Profile_posts:
        class __Profile_posts_comments:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["read"])
            def list(
                self, profile_post_id: int, before: int = None, limit: int = None
            ) -> httpx.Response:
                """
                GET https://api.zelenka.guru/profile-posts/{profile_post_id}/comments

                *List of comments of a profile post.*

                Required scopes: *read*

                **Parameters:**

                - **profile_post_id** (int): ID of profile post.
                - **before** (int): Date to get older comments.
                - **limit** (int): Number of profile posts in a page.

                **Example:**

                ```python
                response = forum.profile_posts.comments.list(profile_post_id=1000000)
                print(response.json())
                ```
                """
                path = f"/profile-posts/{profile_post_id}/comments"
                params = {"before": before, "limit": limit}
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["read"])
            def get(self, profile_post_id: int, comment_id: int) -> httpx.Response:
                """
                GET https://api.zelenka.guru/profile-posts/{profile_post_id}/comments/{comment_id}

                *Detail information of a profile post comment.*

                Required scopes: *read*

                **Parameters:**

                - **profile_post_id** (int): ID of profile post.
                - **comment_id** (int): ID of profile post comment

                **Example:**

                ```python
                response = forum.profile_posts.comments.get(profile_post_id=1000000, comment_id=1000000)
                print(response.json())
                ```
                """
                path = f"/profile-posts/{profile_post_id}/comments/{comment_id}"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["post"])
            def create(self, profile_post_id: int, comment_body: str) -> httpx.Response:
                """
                POST https://api.zelenka.guru/profile-posts/{profile_post_id}/comments

                *Create a new profile post comment.*

                Required scopes: *post*

                **Parameters:**

                - **profile_post_id** (int): ID of profile post.
                - **comment_body** (str): Content of the new profile post comment.

                **Example:**

                ```python
                response = forum.profile_posts.comments.create(profile_post_id=1000000, comment_body="Comment text")
                print(response.json())
                ```
                """
                path = f"/profile-posts/{profile_post_id}/comments"
                data = {
                    "comment_body": comment_body,
                }
                return _send_request(
                    self=self._api, method="POST", path=path, data=data
                )

        def __init__(self, _api_self):
            self._api = _api_self
            self.comments = self.__Profile_posts_comments(self._api)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(
            self, user_id: int, page: int = None, limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/{user_id}/profile-posts

            *List of profile posts (with pagination).*

            Required scopes: *read*

            **Parameters:**

            - **user_id** (int): ID of user.
            - **page** (int): Page number of contents.
            - **limit** (int): Number of contents in a page.

            **Example:**

            ```python
            response = forum.profile_posts.list(user_id=2410024)
            print(response.json())
            ```
            """
            params = {"page": page, "limit": limit}
            path = f"/users/{user_id}/profile-posts"
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, profile_post_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/profile-posts/{profile_post_id}

            *Detail information of a profile post.*

            Required scopes: *read*

            **Parameters:**

            - **profile_post_id** (int): ID of profile post.

            **Example:**

            ```python
            response = forum.profile_posts.get(profile_post_id=1000000)
            print(response.json())
            ```
            """
            path = f"/profile-posts/{profile_post_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def create(self, post_body: str, user_id: int = None) -> httpx.Response:
            """
           POST https://api.zelenka.guru/users/{user_id}/timeline

            *Create a new profile post on a user timeline.*

            Required scopes: *post*

            **Parameters:**

            - **user_id** (int): ID of user.
                > If you do not specify the user_id, you will create profile post in current user's timeline
            - **post_body** (str): Content of the new profile post.

            **Example:**

            ```python
            response = forum.profile_posts.create(user_id=2410024, post_body="Profile post text")
            print(response.json())
            ```
            """
            if user_id:
                path = f"/users/{user_id}/timeline"
            else:
                path = "/users/me/timeline"
            data = {"post_body": post_body}
            return _send_request(self=self._api, method="POST", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def edit(self, profile_post_id: int, post_body: str) -> httpx.Response:
            """
            PUT https://api.zelenka.guru/profile-posts/{profile_post_id}

            *Edit a profile post.*

            Required scopes: *post*

            **Parameters:**

            - **profile_post_id** (int): ID of profile post.
            - **post_body** (str): New content of the profile post.

            **Example:**

            ```python
            response = forum.profile_posts.edit(profile_post_id=1000000, post_body="New profile post text")
            print(response.json())
            ```
            """

            path = f"/profile-posts/{profile_post_id}"
            data = {"post_body": post_body}
            return _send_request(self=self._api, method="PUT", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def delete(self, profile_post_id: int, reason: str = None) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/profile-posts/{profile_post_id}

            *Delete a profile post.*

            Required scopes: *post*

            **Parameters:**

            - **profile_post_id** (int): ID of profile post.
            - **reason** (str): Reason of the profile post removal.

            **Example:**

            ```python
            response = forum.profile_posts.delete(profile_post_id=1000000, reason="Reason")
            print(response.json())
            ```
            """
            path = f"/profile-posts/{profile_post_id}"
            data = {"reason": reason}
            return _send_request(self=self._api, method="DELETE", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def likes(self, profile_post_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/profile-posts/{profile_post_id}/likes

            *List of users who liked a profile post.*

            Required scopes: *read*

            **Parameters:**

            - **profile_post_id** (int): ID of profile post.

            **Example:**

            ```python
            response = forum.profile_posts.likes(profile_post_id=1000000)
            print(response.json())
            ```
            """

            path = f"/profile-posts/{profile_post_id}/likes"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def like(self, profile_post_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/profile-posts/{profile_post_id}/likes

            *Like a profile post.*

            Required scopes: *post*

            **Parameters:**

            - **profile_post_id** (int): ID of profile post.

            **Example:**

            ```python
            response = forum.profile_posts.like(profile_post_id=1000000)
            print(response.json())
            ```
            """
            path = f"/profile-posts/{profile_post_id}/likes"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unlike(self, profile_post_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/profile-posts/{profile_post_id}/likes

            *Unlike a profile post.*

            Required scopes: *post*

            **Parameters:**

            - **profile_post_id** (int): ID of profile post.

            **Example:**

            ```python
            response = forum.profile_posts.unlike(profile_post_id=1000000)
            print(response.json())
            ```
            """
            path = f"/profile-posts/{profile_post_id}/likes"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def report(self, profile_post_id: int, reason: str) -> httpx.Response:
            """
            POST https://api.zelenka.guru/profile-posts/{profile_post_id}/report

            *Report a profile post.*

            Required scopes: *post*

            **Parameters:**

            - **profile_post_id** (int): ID of profile post.
            - **reason** (str): Reason of the report.

            **Example:**

            ```python
            response = forum.profile_posts.report(profile_post_id=1000000, reason="Reason")
            print(response.json())
            ```
            """
            path = f"/profile-posts/{profile_post_id}/report"
            data = {"message": reason}
            return _send_request(self=self._api, method="POST", path=path, data=data)

    class __Search:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["post"])
        def all(
            self,
            q: str = None,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/search

            *Search for threads.*

            Required scopes: *post*

            **Parameters:**

            - **q** (str): Search query. Can be skipped if user_id is set.
            - **tag** (str): Tag to search for tagged contents.
            - **forum_id** (int): ID of the container forum to search for contents. Child forums of the specified forum will be included in the search.
            - **user_id** (int): ID of the creator to search for contents.
            - **page** (int): Page number of results.
            - **limit** (int): Number of results in a page.

            **Example:**

            ```python
            response = forum.search.all(q="LOLZTEAM)
            print(response.json())
            ```
            """
            path = "/search"
            params = {
                "q": q,
                "tag": tag,
                "forum_id": forum_id,
                "user_id": user_id,
                "page": page,
                "limit": limit,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def thread(
            self,
            q: str = None,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
            data_limit: int = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/search/threads

            *Search for threads.*

            Required scopes: *post*

            **Parameters:**

            - **q** (str): Search query.
                > Can be skipped if user_id is set.
            - **tag** (str): Tag to search for tagged contents.
            - **forum_id** (int): ID of the container forum to search for contents.
                > Child forums of the specified forum will be included in the search.
            - **user_id** (int): ID of the creator to search for contents.
            - **page** (int): Page number of results.
            - **limit** (int): Number of results in a page.
            - **data_limit** (int): Number of thread data to be returned.

            **Example:**

            ```python
            response = forum.search.thread(q="LOLZTEAM")
            print(response.json())
            ```
            """
            path = "/search/threads"
            params = {
                "q": q,
                "tag": tag,
                "forum_id": forum_id,
                "user_id": user_id,
                "page": page,
                "limit": limit,
                "data_limit": data_limit,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def post(
            self,
            q: str = None,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
            data_limit: int = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/search/posts

            *Search for posts.*

            Required scopes: *post*

            **Parameters:**

            - **q** (str): Search query.
                > Can be skipped if user_id is set.
            - **tag** (str): Tag to search for tagged contents.
            - **forum_id** (int): ID of the container forum to search for contents.
                > Child forums of the specified forum will be included in the search.
            - **user_id** (int): ID of the creator to search for contents.
            - **page** (int): Page number of results.
            - **limit** (int): Number of results in a page.
            - **data_limit** (int): Number of thread data to be returned.

            **Example:**

            ```python
            response = forum.search.post(q="LOLZTEAM")
            print(response.json())
            ```
            """
            path = "/search/posts"
            params = {
                "q": q,
                "tag": tag,
                "forum_id": forum_id,
                "user_id": user_id,
                "page": page,
                "limit": limit,
                "data_limit": data_limit,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def tag(
            self,
            tags: Union[list[str], str] = None,
            page: int = None,
            limit: int = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/search/tagged

            *Search for tagged contents.*

            Required scopes: *post*

            **Parameters:**

            - **tags** (str|list): Array of tags to search for tagged contents.
            - **page** (int): Page number of results.
            - **limit** (int): Number of results in a page.

            **Example:**

            ```python
            response = forum.search.tag(tag="LOLZTEAM")
            print(response.json())
            ```
            """
            path = "/search/tagged"
            if type(tags) is str:
                tags = list(tags)
            params = {
                "tags[]": tags,
                "page": page,
                "limit": limit,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def profile_posts(
            self,
            q: str = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/search/profile-posts

            *Search for threads.*

            Required scopes: *post*

            **Parameters:**

            - **q** (str): Search query.
                > Can be skipped if user_id is set.
            - **user_id** (int): ID of the creator to search for contents.
            - **page** (int): Page number of results.
            - **limit** (int): Number of results in a page.

            **Example:**

            ```python
            response = forum.search.profile_posts(q="LOLZTEAM)
            print(response.json())
            ```
            """
            path = "/search/profile-posts"
            params = {"q": q, "user_id": user_id, "page": page, "limit": limit}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

    class __Notifications:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["read"])
        def list(self) -> httpx.Response:
            """
            GET https://api.zelenka.guru/notifications

            *List of notifications (both read and unread).*

            Required scopes: *read*

            **Example:**

            ```python
            response = forum.notifications.list()
            print(response.json())
            ```
            """
            path = "/notifications"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, notification_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/notifications/{notification_id}/content

            *Get associated content of notification. The response depends on the content type.*

            Required scopes: *read*

            **Parameters:**

            - **notification_id** (int): ID of notification.

            **Example:**

            ```python
            response = forum.notifications.get(notification_id=1000000)
            print(response.json())
            ```
            """
            path = f"/notifications/{notification_id}/content"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def read(self, notification_id: int = None) -> httpx.Response:
            """
            POST https://api.zelenka.guru/notifications/read

            *Mark single notification or all existing notifications read.*

            Required scopes: *post*

            **Parameters:**

            - **notification_id** (int): ID of notification.
                > If notification_id is omitted, it's mark all existing notifications as read.

            **Example:**

            ```python
            response = forum.notifications.read()
            print(response.json())
            ```
            """
            path = "/notifications/read"
            params = {"notification_id": notification_id}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

    class __Conversations:
        class __Conversations_messages:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["conversate", "read"])
            def list(
                self,
                conversation_id: int,
                page: int = None,
                limit: int = None,
                order: Literal["natural", "natural_reverse"] = None,
                before: int = None,
                after: int = None,
            ) -> httpx.Response:
                """
                GET https://api.zelenka.guru/conversation-messages

                *List of messages in a conversation (with pagination).*

                Required scopes: *conversate*, *read*

                **Parameters:**

                - **conversation_id** (int): ID of conversation.
                - **page** (int): Page number of messages.
                - **limit** (int): Number of messages in a page.
                - **order** (str): Ordering of messages.
                - **before** (int): Date to get older messages.
                - **after** (int): Date to get newer messages.

                **Example:**

                ```python
                response = forum.conversations.messages.list(conversation_id=1000000)
                print(response.json())
                ```
                """
                path = "/conversation-messages"
                params = {
                    "conversation_id": conversation_id,
                    "page": page,
                    "limit": limit,
                    "order": order,
                    "before": before,
                    "after": after,
                }
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["conversate", "read"])
            def get(self, message_id: int) -> httpx.Response:
                """
                GET https://api.zelenka.guru/conversation-messages/{message_id}

                *Detail information of a message.*

                Required scopes: *conversate*, *read*

                **Parameters:**

                - **message_id** (int): ID of conversation message.

                **Example:**

                ```python
                response = forum.conversations.messages.get(message_id=1000000)
                print(response.json())
                ```
                """
                path = f"/conversation-messages/{message_id}"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
            def create(self, conversation_id: int, message_body: str) -> httpx.Response:
                """
                POST https://api.zelenka.guru/conversation-messages

                *Create a new conversation message.*

                Required scopes: *conversate*, *post*

                **Parameters:**

                - **conversation_id** (int): ID of conversation.
                - **message_body** (str): Content of the new message.

                **Example:**

                ```python
                response = forum.conversations.messages.create(conversation_id=1000000, message_body="Message text")
                print(response.json())
                ```
                """
                path = "/conversation-messages"
                params = {
                    "conversation_id": conversation_id,
                }
                data = {"message_body": message_body}
                return _send_request(
                    self=self._api,
                    method="POST",
                    path=path,
                    params=params,
                    data=data,
                )

            @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
            def edit(self, message_id: int, message_body: str) -> httpx.Response:
                """
                PUT https://api.zelenka.guru/conversation-messages/{message_id}

                *Edit a message.*

                Required scopes: *conversate*, *post*

                **Parameters:**

                - **message_id** (int): ID of conversation message.
                - **message_body** (str): New content of the message.

                **Example:**

                ```python
                response = forum.conversation.messages.edit(message_id=1000000, message_body="New message text")
                print(response.json())
                ```
                """
                path = f"/conversation-messages/{message_id}"
                data = {"message_body": message_body}
                return _send_request(self=self._api, method="PUT", path=path, data=data)

            @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
            def delete(self, message_id: int) -> httpx.Response:
                """
                DELETE https://api.zelenka.guru/conversation-messages/{message_id}

                *Delete a message.*

                Required scopes: *conversate*, *post*

                **Parameters:**

                - **message_id** (int): ID of conversation message.

                **Example:**

                ```python
                response = forum.conversations.messages.delete(message_id=1000000)
                print(response.json())
                ```
                """
                path = f"/conversation-messages/{message_id}"
                return _send_request(self=self._api, method="DELETE", path=path)

        def __init__(self, _api_self):
            self._api = _api_self
            self.messages = self.__Conversations_messages(self._api)

        @_MainTweaks._CheckScopes(scopes=["conversate", "read"])
        def list(self, page: int = None, limit: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/conversations

            *List of conversations (with pagination).*

            Required scopes: *conversate*, *read*

            **Parameters:**

            - **page** (int): Page number of conversations.
            - **limit** (int): Number of conversations in a page.

            **Example:**

            ```python
            response = forum.conversations.list()
            print(response.json())
            ```
            """
            path = "/conversations"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["conversate", "read"])
        def get(self, conversation_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/conversations/{conversation_id}

            *Detail information of a conversation.*

            Required scopes: *conversate*, *read*

            **Parameters:**

            - **conversation_id** (int): ID of conversation.

            **Example:**

            ```python
            response = forum.conversations.get(conversation_id=1000000)
            print(response.json())
            ```
            """
            path = f"/conversations/{conversation_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
        def leave(
            self, conversation_id: int, leave_type: Literal["delete", "delete_ignore"] = "delete"
        ) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/conversations/{conversation_id}

            *Leave from conversation*

            Required scopes: *conversate*, *post*

            **Parameters:**

            - **conversation_id** (int): ID of conversation.
            - **leave_type** (str): Leave type.

            **Example:**

            ```python
            response = forum.conversations.leave(conversation_id=1000000)
            print(response.json())
            ```
            """
            params = {"delete_type": leave_type}
            path = f"/conversations/{conversation_id}"
            return _send_request(
                self=self._api, method="DELETE", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
        def create(
            self,
            recipient_id: int,
            message: str,
            open_invite: bool = False,
            conversation_locked: bool = False,
            allow_edit_messages: bool = True,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/conversations

            *Create a new conversation.*

            Required scopes: *conversate*, *post*

            **Parameters:**

            - **recipient_id** (int): ID of recipient.
            - **message** (str): First message in conversation.
            - **open_invite** (bool): Allow invites in conversation.
            - **conversation_locked** (bool): Is conversation locked.
            - **allow_edit_messages** (bool): Allow edit messages.

            **Example:**

            ```python
            response = forum.conversations.create(recipient_id=2410024, message="First message text")
            print(response.json())
            ```
            """
            path = "/conversations"
            params = {
                "recipient_id": recipient_id,
                "is_group": 0,
                "open_invite": int(open_invite) if open_invite else open_invite,
                "conversation_locked": int(conversation_locked) if conversation_locked else conversation_locked,
                "allow_edit_messages": int(allow_edit_messages) if allow_edit_messages else allow_edit_messages,
            }
            data = {"message_body": message}
            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                params=params,
                data=data,
            )

        @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
        def create_group(
            self,
            recipients: list,
            title: str,
            message: str = None,
            open_invite: bool = True,
            conversation_locked: bool = False,
            allow_edit_messages: bool = True,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/conversations

            *Create a new group conversation.*

            Required scopes: *conversate*, *post*

            **Parameters:**

            - **recipients** (list): List of usernames.
                > Max recipients count is 10
            - **title** (str): The title of new conversation.
            - **message** (str): First message in conversation.
            - **open_invite** (bool): Allow invites in conversation.
            - **conversation_locked** (bool): Is conversation locked.
            - **allow_edit_messages** (bool): Allow edit messages.

            **Example:**

            ```python
            response = forum.conversations.create_group(recipients=["AS7RID", "a911"], title="Group title", message="First message text")
            print(response.json())
            ```
            """
            path = "/conversations"
            params = {
                "recipients": ",".join(recipients),
                "title": title,
                "is_group": 1,
                "open_invite": int(open_invite) if open_invite else open_invite,
                "conversation_locked": int(conversation_locked) if conversation_locked else conversation_locked,
                "allow_edit_messages": int(allow_edit_messages) if allow_edit_messages else allow_edit_messages,
            }
            data = {"message_body": message}
            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                params=params,
                data=data,
            )

    @_MainTweaks._CheckScopes(scopes=["read"])
    def navigation(self, parent: int = None) -> httpx.Response:
        """
        GET https://api.zelenka.guru/navigation

        *List of navigation elements within the system.*

        Required scopes: *read*

        **Parameters:**

        - **parent** (int): ID of parent element. If exists, filter elements that are direct children of that element.

        **Example:**

        ```python
        response = forum.navigation()
        print(response.json())
        ```
        """
        path = "/navigation"
        params = {"parent": parent}
        return _send_request(self=self, method="GET", path=path, params=params)

    def batch(self, jobs: list[dict]) -> httpx.Response:
        """
        POST https://api.zelenka.guru/batch

        *Execute multiple API requests at once. Maximum batch jobs is 10.*

        **Example json jobs scheme:**

        [
            {
            "id": "job_1",
            "uri": "https://api.zelenka.guru/users/2410024",
            "method": "GET",
            "params": {}
            },
            {
            "id": "job_2",
            "uri": "https://api.zelenka.guru/users/1",
            "method": "GET",
            "params": {}
            }
        ]

        Required scopes: *Same as called API requests.*

        **Parameters:**

        - **jobs** (list): List of batch jobs.

        **Example:**

        ```python
        response = forum.batch(jobs=[
            {"id": "job_1","uri": "https://api.zelenka.guru/users/2410024","method": "GET","params": {}},
            {"id": "job_2","uri": "https://api.zelenka.guru/users/1","method": "GET","params": {}}
        ])
        print(response.json())
        ```
        """
        path = "/batch"
        dataJ = jobs
        return _send_request(self=self, method="POST", path=path, dataJ=dataJ)


class Market:
    def __init__(
        self,
        token: str,
        bypass_429: bool = True,
        language: str = None,
        proxy_type: str = None,
        proxy: str = None,
        reset_custom_variables: bool = True,
        timeout: int = 90,
    ):
        """
        - **token** (str): Your token.
            > You can get it [there](https://zelenka.guru/account/api)
        - **bypass_429** (bool): Bypass status code 429 by sleep
        - **language** (str): Language for your api responses.
        - **proxy_type** (str): Your proxy type.
        - **proxy** (str): Proxy string.
        - **reset_custom_variables** (bool): Reset custom variables.
        - **timeout** (int): Request timeout.
        """
        self.base_url = "https://api.lzt.market"
        if proxy_type is not None:
            proxy_type = proxy_type.upper()
            if proxy_type in ["HTTPS", "HTTP", "SOCKS4", "SOCKS5"]:
                self._proxy_type = proxy_type
                self._proxy = proxy
            else:
                raise Exceptions.INVALID_PROXY_TYPE(
                    "Proxy type has invalid value. It can be only https,http,socks4 or socks5"
                )
        else:
            self._proxy = None
            self._proxy_type = None

        self._token = token
        self._scopes = None
        _MainTweaks.setup_jwt(self=self, token=token)
        self._main_headers = {"Authorization": f"bearer {self._token}"}

        self.bypass_429 = bypass_429
        self.timeout = timeout
        self._auto_delay_time = 0
        self.additional_delay = 0.1
        self._locale = language
        self._delay_synchronizer = None
        self._lock = None

        from . import Constants

        _categories = "|".join(
            [
                category
                for category in Constants.Market.Category.__dict__.keys()
                if not category.startswith("__")
            ]
        )
        self._delay_pattern = rf"/(?:{_categories}|steam-value)(?:/|$)"
        self.profile = self.__Profile(self)
        self.payments = self.__Payments(self)
        self.category = self.__Category(self)
        self.list = self.__List(self)
        self.publishing = self.__Publishing(self)
        self.purchasing = self.__Purchasing(self)
        self.managing = self.__Managing(self)
        self.proxy = self.__Proxy(self)

        self.reset_custom_variables = reset_custom_variables
        self.custom = _MainTweaks._Custom()

    @property
    def scopes(self):
        return self._scopes

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value
        _MainTweaks.setup_jwt(self=self, token=value)

    def change_proxy(self, proxy_type: str = None, proxy: str = None):
        """
        Delete or change your proxy

        Skip proxy_type and proxy if you want to delete it

        :param proxy_type: Your proxy type. You can use types ( Constants.Proxy.socks5 or socks4,https,http )
        :param proxy: Proxy string. Example -> ip:port or login:password@ip:port
        """
        if proxy_type is not None:
            if proxy_type in ["HTTPS", "HTTP", "SOCKS4", "SOCKS5"]:
                self._proxy_type = proxy_type
            else:
                raise Exceptions.INVALID_PROXY_TYPE(
                    "Proxy type has invalid value. It can be only https,http,socks4 or socks5"
                )
        else:
            self._proxy_type = None
        self._proxy = proxy

    def _add_delay_synchronizer(self, synchronizer):
        self._delay_synchronizer = synchronizer

    def _remove_delay_synchronizer(self):
        self._delay_synchronizer = None
        self._auto_delay_time = self._auto_delay_time.value
        self._lock = None

    class __Profile:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["market"])
        def get(self) -> httpx.Response:
            """
            GET https://api.lzt.market/me

            *Displays info about your profile.*

            Required scopes: *market*

            **Example:**

            ```python
            response = market.profile.get()
            print(response.json())
            ```
            """
            path = "/me"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def edit(
            self,
            disable_steam_guard: bool = None,
            user_allow_ask_discount: bool = None,
            max_discount_percent: int = None,
            allow_accept_accounts: str = None,
            hide_favorites: bool = None,
            title: str = None,
            telegram_client: dict = None,
            deauthorize_steam: bool = None,
            hide_bids: bool = None,
        ) -> httpx.Response:
            """
            PUT https://api.lzt.market/me

            *Change settings about your profile on the market.*

            Required scopes: *market*

            **Parameters:**

            - **disable_steam_guard** (bool): Disable Steam Guard on account purchase moment
            - **user_allow_ask_discount** (bool): Allow users ask discount for your accounts
            - **max_discount_percent** (int): Maximum discount percents for your accounts
            - **allow_accept_accounts** (str): Usernames who can transfer market accounts to you. Separate values with a comma.
            - **hide_favorites** (bool): Hide your profile info when you add an account to favorites
            - **title** (str): Market title.
            - **telegram_client** (dict): Telegram client. It should be {"telegram_api_id"
            - **deauthorize_steam** (bool): Finish all Steam sessions after purchase.
            - **hide_bids** (bool): Hide your profile when bid on the auction.

            **Example:**

            ```python
            response = market.profile.edit(user_allow_ask_discount=True, max_discount_percent=25, title="Selling some stuff")
            print(response.json())
            ```
            """
            path = "/me"
            params = {
                "disable_steam_guard": int(disable_steam_guard) if disable_steam_guard else disable_steam_guard,
                "user_allow_ask_discount": int(user_allow_ask_discount) if user_allow_ask_discount else user_allow_ask_discount,
                "max_discount_percent": max_discount_percent,
                "allow_accept_accounts": allow_accept_accounts,
                "hide_favourites": int(hide_favorites) if hide_favorites else hide_favorites,
                "market_custom_title": title,
                "deauthorize_steam": int(deauthorize_steam) if deauthorize_steam else deauthorize_steam,
                "hide_bids": int(hide_bids) if hide_bids else hide_bids,
            }
            if telegram_client:
                for key, value in telegram_client.items():
                    if key not in ["telegram_api_id", "telegram_api_hash", "telegram_device_model", "telegram_system_version", "telegram_app_version"]:
                        _WarningsLogger.warn(
                            f'{FutureWarning.__name__} Unknown param in telegram_client - "{key}"')
                    else:
                        params[key] = value
            return _send_request(self=self._api, method="PUT", path=path, params=params)

    class __Category:
        class __Steam:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/steam

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.steam.get()
                print(response.json())
                ```
                """
                path = "/steam"
                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/steam/params

                *Displays search parameters for a category.*

                Required scopes: *market*

                **Example:**

                ```python
                response = market.category.steam.params()
                print(response.json())
                ```
                """
                path = "/steam/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/steam/games

                *Displays a list of games in the category.*

                Required scopes: *market*

                **Example:**

                ```python
                response = market.category.steam.games()
                print(response.json())
                ```
                """
                path = "/steam/games"
                return _send_request(self=self._api, method="GET", path=path)

        class __Fortnite:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/fortnite

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.fortnite.get()
                print(response.json())
                ```
                """
                path = "/fortnite"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/fortnite/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.fortnite.params()
                print(response.json())
                ```
                """
                path = "/fortnite/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __MiHoYo:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/mihoyo

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.mihoyo.get()
                print(response.json())
                ```
                """
                path = "/mihoyo"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/mihoyo/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.mihoyo.params()
                print(response.json())
                ```
                """
                path = "/mihoyo/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Riot:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/riot

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.riot.get()
                print(response.json())
                ```
                """
                path = "/riot"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/riot/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.riot.params()
                print(response.json())
                ```
                """
                path = "/riot/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def valorant_data(self, data_type: Literal["Agent", "Buddy", "WeaponSkins"], language: Literal["en-US", "ru-RU"] = None) -> httpx.Response:
                """
                GET https://api.lzt.market/data/valorant

                *Displays data for specified type in valorant category.*

                **Example:**

                ```python
                response = market.category.riot.valorant_data(data_type="Agent")
                print(response.json())
                ```
                """
                path = "/data/valorant"
                params = {
                    "type": data_type,
                    "locale": language
                }
                return _send_request(self=self._api, method="GET", path=path, params=params)

        class __Telegram:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/telegram

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.telegram.get()
                print(response.json())
                ```
                """
                path = "/telegram"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/telegram/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.telegram.params()
                print(response.json())
                ```
                """
                path = "/telegram/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Supercell:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/supercell

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.supercell.get()
                print(response.json())
                ```
                """
                path = "/supercell"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/supercell/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.supercell.params()
                print(response.json())
                ```
                """
                path = "/supercell/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Origin:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/origin

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.origin.get()
                print(response.json())
                ```
                """
                path = "/origin"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/origin/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.origin.params()
                print(response.json())
                ```
                """
                path = "/origin/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/origin/games

                *Displays a list of games in the category.*

                Required scopes: *market*

                **Example:**

                ```python
                response = market.category.origin.games()
                print(response.json())
                ```
                """
                path = "/origin/games"
                return _send_request(self=self._api, method="GET", path=path)

        class __WorldOfTanks:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/world-of-tanks

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.wot.get()
                print(response.json())
                ```
                """
                path = "/world-of-tanks"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/world-of-tanks/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.wot.params()
                print(response.json())
                ```
                """
                path = "/world-of-tanks/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __WorldOfTanksBlitz:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/wot-blitz

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.wot_blitz.get()
                print(response.json())
                ```
                """
                path = "/wot-blitz"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/wot-blitz/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.wot_blitz.params()
                print(response.json())
                ```
                """
                path = "/wot-blitz/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Gifts:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/gifts

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.gifts.get()
                print(response.json())
                ```
                """
                path = "/gifts"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/gifts/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.gitfs.params()
                print(response.json())
                ```
                """
                path = "/gifts/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __EpicGames:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/epicgames

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.epicgames.get()
                print(response.json())
                ```
                """
                path = "/epicgames"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/epicgames/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.epicgames.params()
                print(response.json())
                ```
                """
                path = "/epicgames/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/epicgames/games

                *Displays a list of games in the category.*

                Required scopes: *market*

                **Example:**

                ```python
                response = market.category.epicgames.games()
                print(response.json())
                ```
                """
                path = "/epicgames/games"
                return _send_request(self=self._api, method="GET", path=path)

        class __EscapeFromTarkov:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/espace-from-tarkov

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.eft.get()
                print(response.json())
                ```
                """
                path = "/escape-from-tarkov"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/escape-from-tarkov/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.eft.params()
                print(response.json())
                ```
                """
                path = "/escape-from-tarkov/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __SocialClub:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/socialclub

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.socialclub.get()
                print(response.json())
                ```
                """
                path = "/socialclub"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/socialclub/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.socialclub.params()
                print(response.json())
                ```
                """
                path = "/socialclub/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/socialclub/games

                *Displays a list of games in the category.*

                Required scopes: *market*

                **Example:**

                ```python
                response = market.category.socialclub.games()
                print(response.json())
                ```
                """
                path = "/socialclub/games"
                return _send_request(self=self._api, method="GET", path=path)

        class __Uplay:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/uplay

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.uplat.get()
                print(response.json())
                ```
                """
                path = "/uplay"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/uplay/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.uplay.params()
                print(response.json())
                ```
                """
                path = "/uplay/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/uplay/games

                *Displays a list of games in the category.*

                Required scopes: *market*

                **Example:**

                ```python
                response = market.category.uplay.games()
                print(response.json())
                ```
                """
                path = "/steam/games"
                return _send_request(self=self._api, method="GET", path=path)

        class __WarThunder:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/war-thunder

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.war_thunder.get()
                print(response.json())
                ```
                """
                path = "/war-thunder"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/war-thunder/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.war_thunder.params()
                print(response.json())
                ```
                """
                path = "/war-thunder/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Discord:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/discord

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.discord.get()
                print(response.json())
                ```
                """
                path = "/discord"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/discord/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.discord.params()
                print(response.json())
                ```
                """
                path = "/discord/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __TikTok:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/tiktok

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.tiktok.get()
                print(response.json())
                ```
                """
                path = "/tiktok"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/tiktok/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.tiktok.params()
                print(response.json())
                ```
                """
                path = "/tiktok/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Instagram:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/telegram

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.telegram.get()
                print(response.json())
                ```
                """
                path = "/instagram"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/telegram/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.telegram.params()
                print(response.json())
                ```
                """
                path = "/instagram/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __BattleNet:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/battlenet

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.battlenet.get()
                print(response.json())
                ```
                """
                path = "/battlenet"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/battlenet/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.battlenet.params()
                print(response.json())
                ```
                """
                path = "/battlenet/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/battlenet/games

                *Displays a list of games in the category.*

                Required scopes: *market*

                **Example:**

                ```python
                response = market.category.battlenet.games()
                print(response.json())
                ```
                """
                path = "/battlenet/games"
                return _send_request(self=self._api, method="GET", path=path)

        class __VPN:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/vpn

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.vpn.get()
                print(response.json())
                ```
                """
                path = "/vpn"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/vpn/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.vpn.params()
                print(response.json())
                ```
                """
                path = "/vpn/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Cinema:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/cinema

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.cinema.get()
                print(response.json())
                ```
                """
                path = "/cinema"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/cinema/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.cinema.params()
                print(response.json())
                ```
                """
                path = "/cinema/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Roblox:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/roblox

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.roblox.get()
                print(response.json())
                ```
                """
                path = "/roblox"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/roblox/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.roblox.params()
                print(response.json())
                ```
                """
                path = "/roblox/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Spotify:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/spotify

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.spotify.get()
                print(response.json())
                ```
                """
                path = "/spotify"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/spotify/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.spotify.params()
                print(response.json())
                ```
                """
                path = "/spotify/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Warface:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/warface

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.warface.get()
                print(response.json())
                ```
                """
                path = "/warface"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/warface/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.warface.params()
                print(response.json())
                ```
                """
                path = "/warface/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Minecraft:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def get(
                self,
                page: int = None,
                auction: str = None,
                title: str = None,
                pmin: int = None,
                pmax: int = None,
                origin: Union[str, list] = None,
                not_origin: Union[str, list] = None,
                order_by: Constants.Market.ItemOrder._Literal = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,

                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/minecraft

                *Displays a list of accounts in a specific category according to your parameters.*

                Required scopes: *market*

                **Parameters:**

                - **page** (int): The number of the page to display results from
                - **auction** (bool): Auction.
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
                - **kwargs** (any): Additional search parameters for your request.

                **Example:**

                ```python
                response = market.category.minecraft.get()
                print(response.json())
                ```
                """
                path = "/minecraft"

                params = {
                    "page": page,
                    "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                    "title": title,
                    "pmin": pmin,
                    "pmax": pmax,
                    "origin[]": origin,
                    "not_origin[]": not_origin,
                    "order_by": order_by,
                    "sb": sold_before,
                    "sb_by_me": sold_before_by_me,
                    "nsb": not_sold_before,
                    "nsb_by_me": not_sold_before_by_me,
                }

                if kwargs:
                    for kwarg_name, kwarg_value in kwargs.items():
                        params[str(kwarg_name)] = kwarg_value
                return _send_request(
                    self=self._api,
                    method="GET",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def params(self) -> httpx.Response:
                """
                GET https://api.lzt.market/minecraft/params

                *Displays search parameters for a category.*

                **Example:**

                ```python
                response = market.category.minecraft.params()
                print(response.json())
                ```
                """
                path = "/minecraft/params"
                return _send_request(self=self._api, method="GET", path=path)

        def __init__(self, _api_self):
            self._api = _api_self
            self.steam = self.__Steam(_api_self)
            self.fortnite = self.__Fortnite(_api_self)
            self.mihoyo = self.__MiHoYo(_api_self)
            self.riot = self.__Riot(_api_self)
            self.telegram = self.__Telegram(_api_self)
            self.supercell = self.__Supercell(_api_self)
            self.origin = self.__Origin(_api_self)
            self.wot = self.__WorldOfTanks(_api_self)
            self.wot_blitz = self.__WorldOfTanksBlitz(_api_self)
            self.gifts = self.__Gifts(_api_self)
            self.epicgames = self.__EpicGames(_api_self)
            self.eft = self.__EscapeFromTarkov(_api_self)
            self.socialclub = self.__SocialClub(_api_self)
            self.uplay = self.__Uplay(_api_self)
            self.war_thunder = self.__WarThunder(_api_self)
            self.discord = self.__Discord(_api_self)
            self.tiktok = self.__TikTok(_api_self)
            self.instagram = self.__Instagram(_api_self)
            self.battlenet = self.__BattleNet(_api_self)
            self.vpn = self.__VPN(_api_self)
            self.cinema = self.__Cinema(_api_self)
            self.spotify = self.__Spotify(_api_self)
            self.warface = self.__Warface(_api_self)
            self.minecraft = self.__Minecraft(_api_self)
            self.roblox = self.__Roblox(_api_self)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def get(
            self,
            category_name: Constants.Market.Category._Literal,
            page: int = None,
            auction: str = None,
            title: str = None,
            pmin: float = None,
            pmax: float = None,
            origin: Union[str, list] = None,
            not_origin: Union[str, list] = None,
            order_by: Constants.Market.ItemOrder._Literal = None,
            sold_before: bool = None,
            sold_before_by_me: bool = None,
            not_sold_before: bool = None,
            not_sold_before_by_me: bool = None,

            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/{category_name}

            *Displays a list of accounts in a specific category according to your parameters.*

            Required scopes: *market*

            **Parameters:**

            - **category_name** (str): Category name.
            - **page** (int): The number of the page to display results from
            - **auction** (bool): Auction.
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
            - **kwargs** (any): Additional search parameters for your request.

            **Example:**

            ```python
            response = market.category.get(category_name="telegram")
            print(response.json())
            ```
            """
            path = f"/{category_name}"
            if True:  # Tweak market
                auction = _MainTweaks.market_variable_fix(auction)
            params = {
                "page": page,
                "auction": _MainTweaks.market_variable_fix(auction),  # Tweak market
                "title": title,
                "pmin": pmin,
                "pmax": pmax,
                "origin[]": origin,
                "not_origin[]": not_origin,
                "order_by": order_by,
                "sb": sold_before,
                "sb_by_me": sold_before_by_me,
                "nsb": not_sold_before,
                "nsb_by_me": not_sold_before_by_me,
            }

            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(
                self=self._api,
                method="GET",
                path=path,
                params=params,
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def list(self, top_queries: bool = None) -> httpx.Response:
            """
            GET https://api.lzt.market/category

            *Display category list.*

            Required scopes: *market*

            **Parameters:**

            - **top_queries** (bool): Display top queries for per category.

            **Example:**

            ```python
            response = market.category.list()
            print(response.json())
            ```
            """
            path = "/category"
            params = {"top_queries": top_queries}
            return _send_request(
                self=self._api,
                method="GET",
                path=path,
                params=params,
            )

    class __List:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["market"])
        def from_url(self, url: str) -> httpx.Response:
            """
            Displays a list of the latest accounts from your market url with search params

            Required scopes: *market**

            **Parameters:**

            - **url** (str): Your market search url.
                > It can be *https://lzt.market/search_params* or *https://api.lzt.market/search_params*

            **Example:**

            ```python
            response = market.list.from_url(url="https://lzt.market/steam?origin[]=fishing&eg=1")
            print(response.json())
            ```
            """
            if "CREATE_JOB" in locals() or "SEND_AS_ASYNC" in locals():
                base_api = self
            else:
                base_api = self._api
            if base_api.base_url.replace("api.", "") in url:
                url = url.replace("https://lzt.market", "")
            elif base_api.base_url in url:
                url = url.replace("https://api.lzt.market", "")
            else:
                raise Exceptions.URL_IS_DIFFERENT_FROM_BASE_MARKET(
                    f"Unknown link. It should be \"{base_api.base_url}\" or \"{base_api.base_url.replace('api.','')}\""
                )
            path = f"{url}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def latest(
            self,
            page: int = None,
            title: str = None,

            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/

            *Displays a list of the latest accounts.*

            Required scopes: *market*

            **Parameters:**

            - **page** (int): The number of the page to display results from
            - **title** (str): The word or words contained in the account title.
            - **kwargs** (any): Additional search parameters for your request.

            **Example:**

            ```python
            response = market.list.latest()
            print(response.json())
            ```
            """
            path = "/"
            params = {"page": page, "title": title}

            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def owned(
            self,
            user_id: int = None,
            page: int = None,
            category_id: Constants.Market.CategoryId._Literal = None,
            pmin: float = None,
            pmax: float = None,
            title: str = None,
            status: Constants.Market.ItemStatus._Literal = None,

            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/user/{user_id}/items

            *Displays a list of owned accounts.*

            Required scopes: *market*

            **Parameters:**

            - **user_id** (int): ID of user.
            - **page** (int): Page
            - **category_id** (int): Accounts category
            - **pmin** (float): Minimal price of account (Inclusive).
            - **pmax** (float): Maximum price of account (Inclusive).
            - **title** (str): The word or words contained in the account title.
            - **status** (str): Account status.
            - **kwargs** (any): Additional search parameters for your request.

            **Example:**

            ```python
            response = market.list.owned()
            print(response.json())
            ```
            """
            params = {
                "user_id": user_id,
                "category_id": category_id,
                "pmin": pmin,
                "pmax": pmax,
                "title": title,
                "page": page,
                "show": status,
            }
            path = "/user/items"

            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def purchased(
            self,
            user_id: int = None,
            page: int = None,
            category_id: Constants.Market.CategoryId._Literal = None,
            pmin: float = None,
            pmax: float = None,
            title: str = None,
            status: Constants.Market.ItemStatus._Literal = None,

            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/user/{user_id}/orders

            *Displays a list of purchased accounts.*

            Required scopes: *market*

            **Parameters:**

            - **user_id** (int): ID of user.
            - **page** (int): Page
            - **category_id** (int): Accounts category
            - **pmin** (float): Minimal price of account (Inclusive).
            - **pmax** (float): Maximum price of account (Inclusive).
            - **title** (str): The word or words contained in the account title.
            - **status** (str): Account status.
            - **kwargs** (any): Additional search parameters for your request.

            **Example:**

            ```python
            response = market.list.orders()
            print(response.json())
            ```
            """
            params = {
                "category_id": category_id,
                "pmin": pmin,
                "pmax": pmax,
                "title": title,
                "page": page,
                "show": status,
                "user_id": user_id,
            }

            path = "/user/orders"
            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def favorite(
            self,
            page: int = None,
            status: Constants.Market.ItemStatus._Literal = None,
            title: str = None,

            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/fave

            *Displays a list of favourites accounts.*

            Required scopes: *market*

            **Parameters:**

            - **page** (int): The number of the page to display results from
            - **status** (str): Account status.
            - **title** (str): The word or words contained in the account title.
            - **kwargs** (any): Additional search parameters for your request.

            **Example:**

            ```python
            response = market.list.favorite()
            print(response.json())
            ```
            """
            path = "/fave"
            params = {"page": page, "show": status, "title": title}

            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def viewed(
            self,
            page: int = None,
            status: Constants.Market.ItemStatus._Literal = None,
            title: str = None,

            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/viewed

            *Displays a list of viewed accounts.*

            Required scopes: *market*

            **Parameters:**

            - **page** (int): The number of the page to display results from
            - **status** (str): Account status.
            - **title** (str): The word or words contained in the account title.
            - **kwargs** (any): Additional search parameters for your request.

            **Example:**

            ```python
            response = market.list.viewed()
            print(response.json())
            ```
            """
            path = "/viewed"
            params = {"page": page, "show": status, "title": title}

            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

    class __Payments:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["market"])
        def history(
            self,
            user_id: int = None,
            operation_type: Constants.Market.OperationTypes._Literal = None,
            pmin: float = None,
            pmax: float = None,
            page: int = None,
            operation_id_lt: int = None,
            receiver: str = None,
            sender: str = None,
            start_date: str = None,
            end_date: str = None,
            wallet: str = None,
            comment: str = None,
            is_hold: bool = None,
            show_payments_stats: bool = None,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/user/{user_id}/payments

            *Displays info about your profile.*

            Required scopes: *market*

            **Parameters:**

            - **user_id** (int): ID of user.
            - **operation_type** (str): Type of operation.
            - **pmin** (float): Minimal price of operation (Inclusive).
            - **pmax** (float): Maximum price of operation (Inclusive).
            - **page** (int): The number of the page to display results from.
            - **operation_id_lt** (int): ID of the operation from which the result begins.
            - **receiver** (str): Username of user, which receive money from you.
            - **sender** (str): Username of user, which sent money to you.
            - **start_date** (str): Start date of operation (RFC 3339 date format).
            - **end_date** (str): End date of operation (RFC 3339 date format).
            - **wallet** (str): Wallet, which used for money payots.
            - **comment** (str): Comment for money transfers.
            - **is_hold** (bool): Display hold operations.
            - **show_payments_stats** (bool): Display payment stats for selected period (outgoing value, incoming value).

            **Example:**

            ```python
            response = market.payments.history()
            print(response.json())
            ```
            """
            path = "/user/payments"
            params = {
                "user_id": user_id,
                "operation_type": operation_type,
                "pmin": pmin,
                "pmax": pmax,
                "page": page,
                "operation_id_lt": operation_id_lt,
                "receiver": receiver,
                "sender": sender,
                "start_date": start_date,
                "end_date": end_date,
                "wallet": wallet,
                "comment": comment,
                "is_hold": int(is_hold) if is_hold else is_hold,
                "show_payments_stats": int(show_payments_stats) if show_payments_stats else show_payments_stats,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def transfer(
            self,
            amount: float,
            secret_answer: str,
            currency: Constants.Market.Currency._Literal = "rub",
            user_id: int = None,
            username: str = None,
            comment: str = None,
            transfer_hold: bool = None,
            hold_length_option: Constants.Market.HoldPeriod._Literal = None,
            hold_length_value: int = None,
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/balance/transfer

            *Send money to any user.*

            Required scopes: *market*

            **Parameters:**

            - **amount** (float): Amount to send in your currency.
            - **secret_answer** (str): Secret answer of your account.
            - **currency** (str): Using currency for amount.
            - **user_id** (int): User id of receiver. If user_id specified, username is not required.
            - **username** (str): Username of receiver. If username specified, user_id is not required.
            - **comment** (str): Transfer comment.
            - **transfer_hold** (bool): Hold transfer or not.
            - **hold_length_option** (str): Hold length option.
            - **hold_length_value** (int): Hold length value.

            **Example:**

            ```python
            response = market.payments.transfer(user_id=2410024, amount=250, currency="rub", secret_answer="My secret answer")
            print(response.json())
            ```
            """
            path = "/balance/transfer"
            params = {
                "amount": amount,
                "secret_answer": secret_answer,
                "user_id": user_id,
                "username": username,
                "currency": currency,
                "comment": comment,
                "hold": transfer_hold,
                "hold_length_value": hold_length_value,
                "hold_length_option": hold_length_option,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def fee(
            self,
            amount: float = None
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/balance/transfer/fee

            *Get transfer limits and get fee amount for transfer.*

            Required scopes: *market*

            **Parameters:**

            - **amount** (float): Amount to send in your currency.

            **Example:**

            ```python
            response = market.payments.fee(amount=250)
            print(response.json())
            ```
            """
            path = "/balance/transfer/fee"
            params = {
                "amount": amount
            }
            return _send_request(
                self=self._api, method="GET", path=path, params=params
            )

        @staticmethod
        def generate_link(
            amount: float,
            user_id: int = None,
            username: str = None,
            comment: str = None,
            redirect_url: str = None,
            currency: Constants.Market.Currency._Literal = None,
            hold: bool = None,
            hold_length: int = None,
            hold_option: Literal["hours", "days", "weeks", "months"] = None,
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
            - **hold** (bool): Hold transfer or not.
            - **hold_length** (int): Hold length.
                > Max - 1 month.
            - **hold_period** (str): Hold option.

            **Example:**

            ```python
            payment_link = market.payments.generate_link(user_id=2410024, amount=250, comment="Comment", redirect_url="https://example.com")
            print(payment_link)
            ```
            """
            if hold:
                if hold_option in ["hour", "day", "week", "month"]:
                    hold_option += "s"
            params = {
                "user_id": user_id,
                "username": username,
                "amount": amount,
                "comment": comment,
                "redirect": redirect_url,
                "currency": currency,
                "hold": int(hold) if hold else hold,
                "hold_length_value": hold_length,
                "hold_length_option": hold_option,
            }
            url = httpx.URL("https://lzt.market/balance/transfer")
            url = url.copy_with(params=params)
            return url

    class __Managing:
        def __init__(self, _api_self):
            self._api = _api_self
            self.tag = self.__Tag(self._api)
            self.steam = self.__SteamMan(self._api)
            self.telegram = self.__TelegramMan(self._api)

        class __Tag:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def delete(self, item_id: int, tag_id: int) -> httpx.Response:
                """
                DELETE https://api.lzt.market/{item_id}/tag

                *Deletes tag for the account.*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.
                - **tag_id** (int): Tag id.
                    > Tag list is available via market.profile.get()

                **Example:**

                ```python
                response = market.managing.tag.delete(item_id=1000000, tag_id=1000)
                print(response.json())
                ```
                """
                path = f"/{item_id}/tag"
                params = {"tag_id": tag_id}
                return _send_request(
                    self=self._api,
                    method="DELETE",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def add(self, item_id: int, tag_id: int) -> httpx.Response:
                """
                POST https://api.lzt.market/{item_id}/tag

                *Adds tag for the account.*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.
                - **tag_id** (int): Tag id.
                    > Tag list is available via market.profile.get()

                **Example:**

                ```python
                response = market.managing.tag.add(item_id=1000000, tag_id=1000)
                print(response.json())
                ```
                """
                path = f"/{item_id}/tag"
                params = {"tag_id": tag_id}
                return _send_request(
                    self=self._api,
                    method="POST",
                    path=path,
                    params=params,
                )

        class __SteamMan:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def guard(self, item_id: int) -> httpx.Response:
                """
                GET https://api.lzt.market/{item_id}/guard-code

                *Gets confirmation code from MaFile (Only for Steam accounts).*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.

                **Example:**

                ```python
                response = market.managing.steam.guard(item_id=1000000)
                print(response.json())
                ```
                """
                path = f"/{item_id}/guard-code"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def mafile(self, item_id: int) -> httpx.Response:
                """
                GET https://api.lzt.market/{item_id}/mafile

                *Returns mafile in JSON.*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.

                **Example:**

                ```python
                response = market.managing.steam.mafile(item_id=1000000)
                print(response.json())
                ```
                """
                path = f"/{item_id}/mafile"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def update_inventory(self, item_id: int, app_id: Constants.Market.AppID._Literal) -> httpx.Response:
                """
                POST https://api.lzt.market/{item_id}/update-inventory

                *Update inventory value.*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.
                - **app_id** (int): App id.

                **Example:**

                ```python
                response = market.managing.steam.update_inventory(item_id=1000000, app_id=730)
                print(response.json())
                ```
                """
                params = {"app_id": app_id}
                path = f"/{item_id}/update-inventory"
                return _send_request(
                    self=self._api, method="POST", path=path, params=params
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def inventory_value(
                self, url: str = None, item_id: int = None, app_id: int = 730, currency: Constants.Market.Currency._Literal = None, ignore_cache: bool = None
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/steam-value

                *Gets steam value.*

                **Parameters:**

                - **url** (str): Link or id of account.
                    > Can be [https://lzt.market/{item-id}/, https://steamcommunity.com/id/{steam-name}, https://steamcommunity.com/profiles/{steam-id}, {steam-id}].
                - **item_id** (int): Item id.
                - **app_id** (int): Application id.
                - **currency** (str): Using currency for amount.
                - **ignore_cache** (bool): Ignore cache.

                **Example:**

                ```python
                response = market.managing.steam.inventory_value(item_id=1000000, app_id=730)
                print(response.json())
                ```
                """
                params = {
                    "app_id": app_id,
                    "currency": currency,
                    "ignore_cache": ignore_cache,
                }
                if url:
                    params["link"] = url
                    path = "/steam-value"
                elif item_id:
                    path = f"/{item_id}/inventory-value"
                return _send_request(self=self._api, method="GET", path=path, params=params)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def confirm_sda(
                self, item_id: int, id: int = None, nonce: int = None
            ) -> httpx.Response:
                """
                POST https://api.lzt.market/{item_id}/confirm-sda

                *Confirm steam action.*
                > Don't set id and nonce parameters to get list of available confirmation requests.

                **Parameters:**

                - **item_id** (int): Item id.
                - **id** (int): Confirmation id.
                    > Required along with **nonce** if you want to confirm action.
                - **nonce** (int): Confirmation nonce.
                    > Required along with **id** if you want to confirm action.

                **Example:**

                ```python
                response = market.managing.steam.confirm_sda(item_id=1000000)
                print(response.json())
                ```
                """
                params = {
                    "id": id,
                    "nonce": nonce,
                }
                path = f"/{item_id}/confirm-sda"
                return _send_request(
                    self=self._api, method="POST", path=path, params=params
                )

        class __TelegramMan:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def code(self, item_id: int) -> httpx.Response:
                """
                GET https://api.lzt.market/{item_id}/telegram-login-code

                *Gets confirmation code from Telegram.*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.

                **Example:**

                ```python
                response = market.managing.telegram.code(item_id=1000000)
                print(response.json())
                ```
                """
                path = f"/{item_id}/telegram-login-code"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def reset_auth(self, item_id: int) -> httpx.Response:
                """
                POST https://api.lzt.market/{item_id}/telegram-reset-authorizations

                *Resets Telegram authorizations.*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.

                **Example:**

                ```python
                response = market.managing.telegram.reset_auth(item_id=1000000)
                print(response.json())
                ```
                """
                path = f"/{item_id}/telegram-reset-authorizations"
                return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def password_temp_mail(self, item_id: int) -> httpx.Response:
            """
            GET https://api.lzt.market/{item_id}/temp-email-password

            *Gets password from temp email of account.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.managing.password_temp_mail(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/temp-email-password"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def get(
            self,
            item_id: int,
            auction: bool = False,
            steam_preview: bool = False,
            preview_type: Literal["profiles", "games"] = None,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/{item_id}
            GET https://api.lzt.market/{item_id}/steam-preview
            GET https://api.lzt.market/{item_id}/auction

            *Displays account information or returns Steam account html code.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.
            - **steam_preview** (bool): Set it True if you want to get steam html and False/None if you want to get account info
            - **preview_type** (str): Type of page - profiles or games

            **Example:**

            ```python
            response = market.managing.get(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}"
            if auction:
                path = f"/{item_id}/auction"
            elif steam_preview:
                path = f"/{item_id}/steam-preview"
            params = {"type": preview_type}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def bulk_get(
            self,
            item_ids: list
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/bulk/items

            *Bulk get up to 250 accounts.*

            Required scopes: *market*

            **Parameters:**

            - **item_ids** (list): Item ids.

            **Example:**

            ```python
            response = market.managing.bulk_get(item_ids=[1000000, 2000000, 3000000, 4000000, 500000])
            print(response.json())
            ```
            """
            path = "/bulk/items"
            dataJ = {"item_id": item_ids}
            return _send_request(self=self._api, method="POST", path=path, dataJ=dataJ)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def delete(self, item_id: int, reason: str = "Market.Managing.Delete") -> httpx.Response:
            """
            DELETE https://api.lzt.market/{item_id}

            *Deletes your account from public search. Deletetion type is soft. You can restore account after deletetion if you want.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.
            - **reason** (str): Delete reason.

            **Example:**

            ```python
            response = market.managing.delete(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}"
            params = {"reason": reason}
            return _send_request(
                self=self._api, method="DELETE", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def email(self, item_id: int = None, email: str = None, login: str = None) -> httpx.Response:
            """
            GET https://api.lzt.market/email-code

            *Gets confirmation code or link.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.
            - **email** (str): Account email.
            - **login** (str): Account login.

            **Example:**

            ```python
            response = market.managing.email(item_id=1000000)
            print(response.json())
            ```
            """
            path = "/email-code"
            params = {"email ": email, "login": login, "item_id": item_id}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def refuse_guarantee(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/refuse-guarantee

            *Cancel guarantee of account. It can be useful for account reselling.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.managing.refuse_guarantee(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/refuse-guarantee"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def check_guarantee(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/check-guarantee

            *Checks the guarantee and cancels it if there are reasons to cancel it.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.managing.check_guarantee(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/check-guarantee"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def change_password(self, item_id: int, _cancel: bool = None) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/change-password

            *Changes password of account.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.
            - **_cancel** (bool): Cancel change password recommendation. It will be helpful, if you don't want to change password and get login data

            **Example:**

            ```python
            response = market.managing.change_password(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/change-password"
            params = {"_cancel": int(_cancel) if _cancel else _cancel}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def stick(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/stick

            *Stick account in the top of search.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.managing.stick(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/stick"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def unstick(self, item_id: int) -> httpx.Response:
            """
            DELETE https://api.lzt.market/{item_id}/stick

            *Unstick account of the top of search.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.managing.unstick(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/stick"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def favorite(self, item_id: int) -> httpx.Response:
            """
             POST https://api.lzt.market/{item_id}/star

            *Adds account to favourites.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.managing.favorite(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/star"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def unfavorite(self, item_id: int) -> httpx.Response:
            """
            DELETE https://api.lzt.market/{item_id}/star

            *Deletes account from favourites.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.managing.unfavorite(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/star"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def bump(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/bump

            *Bumps account in the search.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.managing.bump(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/bump"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def change_owner(
            self, item_id: int, username: str, secret_answer: str
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/change-owner

            *Change of account owner.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.
            - **username** (str): The username of the new account owner.
            - **secret_answer** (str): Secret answer of your account.

            **Example:**

            ```python
            response = market.managing.change_owner(item_id=1000000, username="AS7RID", secret_answer="My secret answer")
            print(response.json())
            ```
            """
            path = f"/{item_id}/change-owner"
            params = {"username": username, "secret_answer": secret_answer}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def edit(
            self,
            item_id: int,
            price: float = None,
            currency: Constants.Market.Currency._Literal = None,
            item_origin: Constants.Market.ItemOrigin._Literal = None,
            title: str = None,
            title_en: str = None,
            description: str = None,
            information: str = None,
            email_login_data: str = None,
            email_type: str = None,
            allow_ask_discount: bool = None,
            proxy_id: int = None,
        ) -> httpx.Response:
            """
            PUT https://api.lzt.market/{item_id}/edit

            *Edits any details of account.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item
            - **price** (float): Account price in your currency.
            - **currency** (str): Using currency.
            - **item_origin** (str): Account origin.
            - **title** (str): Russian title of account.
                > If title specified and title_en is empty, title_en will be automatically translated to English language.
            - **title_en** (str): English title of account.
                > If title_en specified and title is empty, title will be automatically translated to Russian language.
            - **description** (str): Account public description.
            - **information** (str): Account private information (visible for buyer only if purchased).
            - **email_login_data** (str): Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
            - **email_type** (str): Email type.
            - **allow_ask_discount** (bool): Allow users to ask discount for this account.
            - **proxy_id** (int): Using proxy id for account checking.

            **Example:**

            ```python
            response = market.managing.edit(item_id=1000000, price=1000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/edit"
            params = {
                "price": price,
                "currency": currency,
                "item_origin": item_origin,
                "title": title,
                "title_en": title_en,
                "description": description,
                "information": information,
                "email_login_data": email_login_data,
                "email_type": email_type,
                "allow_ask_discount": allow_ask_discount,
                "proxy_id": proxy_id,
            }
            return _send_request(self=self._api, method="PUT", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def arbitrage(
            self,
            item_id: int,
            post_body: str
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/claims

            *Create a Arbitrage.*

            Required scopes: *post*

            **Parameters:**

            - **post_body** (str): You should describe what's happened.

            **Example:**

            ```python
            response = market.managing.arbitrage(item_id=1000000, post_body="There i'am discribe what's happened.")
            print(response.json())
            ```
            """
            path = f"/{item_id}/claims"
            data = {
                "post_body": post_body
            }
            return _send_request(
                self=self._api, method="POST", path=path, data=data
            )

    class __Purchasing:
        def __init__(self, _api_self):
            self._api = _api_self
            self.auction = self.__Auction(self._api)

        class __Auction:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def place_bid(
                self, item_id: int, amount: float, currency: Constants.Market.Currency._Literal = None
            ) -> httpx.Response:
                """
                POST https://api.lzt.market/{item_id}/auction/bid

                *Create a new auction bid.*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.
                - **amount** (float): Amount bid.
                - **currency** (str): Using currency.

                **Example:**

                ```python
                response = market.purchasing.auction.place_bid(item_id=1000000, amount=1000)
                print(response.json())
                ```
                """
                params = {"amount": amount, "currency": currency}
                path = f"/{item_id}/auction/bid"
                return _send_request(
                    self=self._api,
                    method="POST",
                    path=path,
                    params=params,
                )

            @_MainTweaks._CheckScopes(scopes=["market"])
            def delete_bid(self, item_id: int, bid_id: int) -> httpx.Response:
                """
                GET https://api.lzt.market/{item_id}/auction/bid

                *Delete your auction bid.*

                Required scopes: *market*

                **Parameters:**

                - **item_id** (int): ID of item.
                - **bid_id** (int): ID of bid.

                **Example:**

                ```python
                response = market.purchasing.auction.delete_bid(item_id=1000000, bid_id=1000)
                print(response.json())
                ```
                """
                params = {"bid_id": bid_id}
                path = f"/{item_id}/auction/bid"
                return _send_request(
                    self=self._api,
                    method="DELETE",
                    path=path,
                    params=params,
                )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def check(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/check-account

            *Checking account for validity. If the account is invalid, the purchase will be canceled automatically*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.

            **Example:**

            ```python
            response = market.purchasing.check(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/check-account"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def confirm(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/confirm-buy

            *Confirm buy.*

            Required scopes: *market*

            **Example:**

            ```python
            response = market.purchasing.confirm(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/confirm-buy"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def fast_buy(
            self, item_id: int, price: float, buy_without_validation: bool = None
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/fast-buy

            *Check and buy account.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.
            - **price** (float): Current price of account in your currency.
            - **buy_without_validation** (bool): Use TRUE if you want to buy account without account data validation (not safe).

            **Example:**

            ```python
            response = market.purchasing.fast_buy(item_id=1000000, price=1000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/fast-buy"
            params = {
                "price": price,
                "buy_without_validation": int(buy_without_validation) if buy_without_validation else buy_without_validation,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

    class __Publishing:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["market"])
        def info(self, item_id: int, resell_item_id: int = None) -> httpx.Response:
            """
            GET https://api.lzt.market/{item_id}/goods/add

            *Get info about not published item. For categories, which required temporary email (Steam, Social Club), you will get temporary email in response.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID of item.
            - **resell_item_id** (int): Put item id, if you are trying to resell item. This is useful to pass temporary email from reselling item to new item. You will get same temporary email from reselling account.

            **Example:**

            ```python
            response = market.publishing.info(item_id=1000000)
            print(response.json())
            ```
            """
            path = f"/{item_id}/goods/add"
            params = {"resell_item_id": resell_item_id}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def check(
            self,
            item_id: int,
            login: str = None,
            password: str = None,
            login_password: str = None,
            close_item: bool = None,
            extra: dict = None,
            resell_item_id: int = None,
            random_proxy: bool = None,
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/{item_id}/goods/check

            *Check account on validity. If account is valid, account will be published on the market.*

            Required scopes: *market*

            **Parameters:**

            - **item_id** (int): ID for item.
            - **login** (str): Account login (or email).
            - **password** (str): Account password.
            - **login_password** (str): Account login data format login:password.
            - **close_item** (bool): If True, the item will be closed item_state = closed.
            - **extra** (str): Extra params for account checking.
            - **resell_item_id** (int): Put item id, if you are trying to resell item.
            - **random_proxy** (bool): Pass True, if you get captcha in previous response.

            **Example:**

            ```python
            response = market.publishing.check(item_id=1000000, login="login", password="password")
            print(response.json())
            ```
            """
            path = f"/{item_id}/goods/check"
            params = {
                "login": login,
                "password": password,
                "login_password": login_password,
                "close_item": int(close_item) if close_item else close_item,
                "resell_item_id": resell_item_id,
                "random_proxy": int(random_proxy) if random_proxy else random_proxy,
            }
            data = {}
            if extra:
                data["extra"] = extra
            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                params=params,
                data=data,
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def add(
            self,
            category_id: Constants.Market.CategoryId._Literal,
            price: float,
            currency: Constants.Market.Currency._Literal,
            item_origin: Constants.Market.ItemOrigin._Literal,
            extended_guarantee: Constants.Market.Guarantee._Literal = None,
            title: str = None,
            title_en: str = None,
            description: str = None,
            information: str = None,
            has_email_login_data: bool = None,
            email_login_data: str = None,
            email_type: str = None,
            allow_ask_discount: bool = None,
            proxy_id: int = None,
            random_proxy: bool = None,
            auction: bool = False,
            auction_duration_value: int = None,
            auction_duration_option: Literal["minutes", "hours", "days"] = None,
            instabuy_price: float = None,
            not_bids_action: str = None,
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/item/add

            *Adds account on the market.*

            Required scopes: *market*

            **Parameters:**

            - **category_id** (int): Accounts category.
            - **price** (float): Account price in your currency.
            - **currency** (str): Using currency.
            - **item_origin** (str): Account origin. Where did you get it from.
            - **extended_guarantee** (int): Guarantee type.
            - **title** (str): Russian title of account.
                > If title specified and title_en is empty, title_en will be automatically translated to English language.
            - **title_en** (str): English title of account.
                > If title_en specified and title is empty, title will be automatically translated to Russian language.
            - **description** (str): Account public description.
            - **information** (str): Account private information (visible for buyer only if purchased).
            - **has_email_login_data** (bool): Required if a category is one of list of Required email login data categories.
            - **email_login_data** (str): Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
            - **email_type** (str): Email type.
            - **allow_ask_discount** (bool): Allow users to ask discount for this account.
            - **proxy_id** (int): Using proxy id for account checking.
            - **random_proxy** (bool): Pass True, if you get captcha in previous response
            - **auction** (bool): Pass True if you want to create auction
            - **auction_duration_value** (int): Duration auction value.
            - **auction_duration_option** (str): Duration auction option.
            - **instabuy_price** (float): The price for which you can instantly redeem your account.
            - **not_bids_action** (str): If you set cancel, at the end of the auction with 0 bids, the account can be purchased at the price you specified as the minimum bid. Can be [close, cancel]

            **Example:**

            ```python
            response = market.publishing.add(category_id=24, price=100, currency="rub", item_origin="stealer", title="Telegram")
            print(response.json())
            ```
            """
            path = "/item/add"
            params = {
                "category_id": category_id,
                "type_sell": "auction" if auction else "price",
                "duration_auction_value": auction_duration_value if auction else None,
                "duration_auction_option": auction_duration_option if auction else None,
                "instant_price": instabuy_price if auction else None,
                "not_bids_action": not_bids_action if auction else None,
                "price": price,
                "currency": currency,
                "item_origin": item_origin,
                "extended_guarantee": extended_guarantee,
                "title": title,
                "title_en": title_en,
                "description": description,
                "information": information,
                "has_email_login_data": has_email_login_data,
                "email_login_data": email_login_data,
                "email_type": email_type,
                "allow_ask_discount": allow_ask_discount,
                "proxy_id": proxy_id,
                "random_proxy": int(random_proxy) if random_proxy else random_proxy,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def fast_sell(
            self,
            category_id: Constants.Market.CategoryId._Literal,
            price: float,
            currency: Constants.Market.Currency._Literal,
            item_origin: Constants.Market.ItemOrigin._Literal,
            extended_guarantee: Constants.Market.Guarantee._Literal = None,
            title: str = None,
            title_en: str = None,
            description: str = None,
            information: str = None,
            has_email_login_data: bool = None,
            email_login_data: str = None,
            email_type: str = None,
            allow_ask_discount: bool = None,
            proxy_id: int = None,
            random_proxy: bool = None,
            login: str = None,
            password: str = None,
            login_password: str = None,
            extra: dict = None,
            auction: bool = False,
            auction_duration_value: int = None,
            auction_duration_option: Literal["minutes", "hours", "days"] = None,
            instabuy_price: float = None,
            not_bids_action: str = None,
            close_item: bool = None,
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/item/fast-sell

            *Adds and check account on validity. If account is valid, account will be published on the market.*

            Required scopes: *market*

            **Parameters:**

            - **category_id** (int): Accounts category.
            - **price** (float): Account price in your currency.
            - **currency** (str): Using currency.
            - **item_origin** (str): Account origin. Where did you get it from.
            - **extended_guarantee** (int): Guarantee type.
            - **title** (str): Russian title of account.
                > If title specified and title_en is empty, title_en will be automatically translated to English language.
            - **title_en** (str): English title of account.
                > If title_en specified and title is empty, title will be automatically translated to Russian language.
            - **description** (str): Account public description.
            - **information** (str): Account private information (visible for buyer only if purchased).
            - **has_email_login_data** (bool): Required if a category is one of list of Required email login data categories.
            - **email_login_data** (str): Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
            - **email_type** (str): Email type.
            - **allow_ask_discount** (bool): Allow users to ask discount for this account.
            - **proxy_id** (int): Using proxy id for account checking.
            - **random_proxy** (bool): Pass True, if you get captcha in previous response.
            - **login** (str): Account login (or email).
            - **password** (str): Account password.
            - **login_password** (str): Account login data format login:password.
            - **extra** (str): Extra params for account checking.
            - **auction** (bool): Pass True if you want to create auction.
            - **auction_duration_value** (int): Duration auction value.
            - **auction_duration_option** (str): Duration auction option.
            - **instabuy_price** (float): The price for which you can instantly redeem your account.
            - **not_bids_action** (str): If you set cancel, at the end of the auction with 0 bids, the account can be purchased at the price you specified as the minimum bid. Can be [close, cancel]
            - **close_item** (bool): If True, the item will be closed item_state = closed.

            **Example:**

            ```python
            response = market.publishing.add(category_id=24, price=100, currency="rub", item_origin="stealer", login="auth_key", password="dc_id", title="Telegram")
            print(response.json())
            ```
            """
            path = "/item/fast-sell"
            params = {
                "category_id": category_id,
                "price": price,
                "type_sell": "auction" if auction else "price",
                "duration_auction_value": auction_duration_value if auction else None,
                "duration_auction_option": auction_duration_option if auction else None,
                "instant_price": instabuy_price if auction else None,
                "not_bids_action": not_bids_action if auction else None,
                "currency": currency,
                "item_origin": item_origin,
                "extended_guarantee": extended_guarantee,
                "title": title,
                "title_en": title_en,
                "description": description,
                "information": information,
                "has_email_login_data": has_email_login_data,
                "email_login_data": email_login_data,
                "email_type": email_type,
                "allow_ask_discount": allow_ask_discount,
                "proxy_id": proxy_id,
                "random_proxy": int(random_proxy) if random_proxy else random_proxy,
                "login": login,
                "password": password,
                "login_password": login_password,
                "close_item": int(close_item) if close_item else close_item,
            }
            data = {}
            if extra:
                data["extra"] = extra
            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                params=params,
                data=data,
            )

    class __Proxy:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["market"])
        def get(self) -> httpx.Response:
            """
            GET https://api.lzt.market/proxy

            *Gets your proxy list.*

            Required scopes: *market*

            **Example:**

            ```python
            response = market.proxy.get()
            print(response.json())
            ```
            """
            path = "/proxy"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def delete(
            self, proxy_id: int = None, delete_all: bool = None
        ) -> httpx.Response:
            """
            DELETE https://api.lzt.market/proxy

            *Delete single or all proxies.*

            Required scopes: *market*

            **Parameters:**

            - **proxy_id** (int): ID of an existing proxy.
            - **delete_all** (bool): Use True if you want to delete all proxy.

            **Example:**

            ```python
            response = market.proxy.delete(delete_all=True)
            print(response.json())
            ```
            """
            path = "/proxy"
            params = {"proxy_id": proxy_id, "delete_all": delete_all}
            return _send_request(
                self=self._api, method="DELETE", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def add(
            self,
            proxy_ip: str = None,
            proxy_port: int = None,
            proxy_user: str = None,
            proxy_pass: str = None,
            proxy_row: str = None,
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/proxy

            *Add single proxy or proxy list.*

            Required scopes: *market*

            **Parameters:**

            - **proxy_ip** (str): Proxy ip or host.
            - **proxy_port** (str): Proxy port
            - **proxy_user** (str): Proxy username
            - **proxy_pass** (str): Proxy password
            - **proxy_row** (str): Proxy list in String format ip:port:user:pass.
                > Each proxy must be start with new line (use *\\n* separator)

            **Example:**

            ```python
            response = market.proxy.add(proxy_row="192.168.1.1:8080:login:password\n192.168.2.2:8080:login:password")
            print(response.json())
            ```
            """
            path = "/proxy"
            params = {
                "proxy_ip": proxy_ip,
                "proxy_port": proxy_port,
                "proxy_user": proxy_user,
                "proxy_pass": proxy_pass,
                "proxy_row": proxy_row,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

    @_MainTweaks._CheckScopes(scopes=["market"])
    def batch(self, jobs: list[dict]) -> httpx.Response:
        """
        POST https://api.lzt.market/batch

        Execute multiple API requests at once.(10 max)

        Example scheme:

        [
            {
            "id": "1",
            "uri": "https://api.lzt.market/me",
            "method": "GET",
            "params": {}
            }
        ]

        :param jobs: List of batch jobs. (Check example above)
        :return: httpx Response object
        """
        import json

        path = "/batch"
        data = jobs
        return _send_request(self=self, method="POST", path=path, data=data)


class Antipublic:
    def __init__(
        self,
        token: str = None,
        proxy_type: str = None,
        proxy: str = None,
        reset_custom_variables: bool = True,
        timeout: int = 90,
    ):
        """
        - **token** (str): Your token.
            > You can get it [there](https://zelenka.guru/account/antipublic) or in antipublic app
        - **proxy_type** (str): Your proxy type.
        - **proxy** (str): Proxy string.
            > ip:port or login:password@ip:port
        - **reset_custom_variables** (bool): Reset custom variables.
        - **timeout** (int): Request timeout.
        """
        self.base_url = "https://antipublic.one"
        if proxy_type is not None:
            proxy_type = proxy_type.upper()
            if proxy_type in ["HTTPS", "HTTP", "SOCKS4", "SOCKS5"]:
                self._proxy_type = proxy_type
                self._proxy = proxy
            else:
                raise Exceptions.INVALID_PROXY_TYPE(
                    "Proxy type has invalid value. It can be only https,http,socks4 or socks5"
                )
        else:
            self._proxy = None
            self._proxy_type = None

        self.token = token
        self.timeout = timeout
        self._locale = None
        self._delay_synchronizer = None
        self._lock = None
        self._delay_pattern = "^$"

        self.reset_custom_variables = reset_custom_variables
        self.custom = _MainTweaks._Custom()
        self._main_headers = {}

        self.info = self.__Info(self)
        self.account = self.__Account(self)

    class __Info:
        def __init__(self, _api_self):
            self._api = _api_self

        def lines_count(self) -> httpx.Response:
            """
            GET https://antipublic.one/api/v2/countLines

            *Get count of rows in the AntiPublic db*

            **Example:**

            ```python
            response = antipublic.info.lines_count()
            print(response.json())
            ```
            """

            path = "/api/v2/countLines"
            return _send_request(self=self._api, method="GET", path=path)

        def lines_count_plain(self) -> str:
            """
            GET https://antipublic.one/api/v2/countLinesPlain

            *Get count of rows in the AntiPublic db (raw format)*

            **Example:**

            ```python
            response = antipublic.info.lines_count_plain()
            print(response.text)
            ```
            """

            path = "/api/v2/countLinesPlain"
            return _send_request(self=self._api, method="GET", path=path)

        def version(self) -> httpx.Response:
            """
            GET https://antipublic.one/api/v2/version

            *Get current antipublic version, change log and download url*

            **Example:**

            ```python
            response = antipublic.info.version()
            print(response.json())
            ```
            """

            path = "/api/v2/version"
            return _send_request(self=self._api, method="GET", path=path)

    class __Account:
        def __init__(self, _api_self):
            self._api = _api_self

        def license(self) -> httpx.Response:
            """
            GET https://antipublic.one/api/v2/checkAccess

            *Checks your license*

            Token required

            **Example:**

            ```python
            response = antipublic.account.license()
            print(response.json())
            ```
            """
            path = "/api/v2/checkAccess"
            return _send_request(self=self._api, method="GET", path=path)

        def queries(self) -> httpx.Response:
            """
            GET https://antipublic.one/api/v2/availableQueries

            *Get your available queries*

            **Example:**

            ```python
            response = antipublic.account.queries()
            print(response.json())
            ```
            """
            path = "/api/v2/availableQueries"
            return _send_request(self=self._api, method="GET", path=path)

    def check(self, lines: list[str], insert: bool = None) -> httpx.Response:
        """
        POST https://antipublic.one/api/v2/checkLines

        *Check your lines.*

        **Parameters:**

        - **lines** (list): Lines for check, email:password or login:password
        - **insert** (bool): Upload private rows to AntiPublic db

        **Example:**

        ```python
        response = antipublic.check(lines=["email:password", "login:password"])
        print(response.json())
        ```
        """
        dataJ = {"lines": lines, "insert": insert}
        path = "/api/v2/checkLines"
        return _send_request(self=self, method="POST", path=path, dataJ=dataJ)

    def search(self, search_by: Constants.Antipublic.SearchBy._Literal, query: str, direction: Constants.Antipublic.SearchDirection._Literal = None, page_token: Optional[str] = None) -> httpx.Response:
        """
        POST https://antipublic.one/api/v2/search

        *Search lines by email/password/domain.*

        **Parameters:**

        - **search_by** (str): Search type.
            > For password and domain search you need Antipublic Plus subscription
        - **query** (str): Search query.
        - **direction** (str): Search direction.

        **Example:**

        ```python
        response = antipublic.search(search_by="email", query="email7357@example.com")
        print(response.json())
        ```
        """
        path = "/api/v2/search"
        if search_by not in ["email", "password", "domain"]:
            _WarningsLogger.warn("Search type has invalid value. It can be only \"email\", \"password\" or \"domain\"")
        dataJ = {
            "searchBy": search_by,
            "query": {str(search_by): query},
        }
        if direction:
            dataJ["direction"] = {str(search_by): direction}
        if page_token:
            dataJ["pageToken"] = page_token
        return _send_request(self=self, method="POST", path=path, dataJ=dataJ)

    def email_passwords(
        self, emails: list[str] = None, limit: int = None
    ) -> httpx.Response:
        """
        POST https://antipublic.one/api/v2/emailPasswords

        *Get passwords for login's/email's*

        **Parameters:**

        - **emails** (list): List of emails or logins for search.
        - **limit** (int): Result limit (per email).

        **Example:**

        ```python
        response = antipublic.email_passwords(emails=["email7357@example.com", "email7358@example.com"], limit=1)
        print(response.json())
        ```
        """
        dataJ = {"emails": emails, "limit": limit}
        path = "/api/v2/emailPasswords"
        return _send_request(self=self, method="POST", path=path, dataJ=dataJ)

import logging
import asyncio
import base64
import httpx
import time
import json
import re

from typing import Union

from . import Exceptions
from .Tweaks import _MainTweaks

logging.basicConfig(format="\033[93mWARNING:%(message)s\033[0m", level=logging.WARNING)


@_MainTweaks._RetryWrapper
def _send_request(
    self, method: str, path: dict, params: dict = None, data=None, files=None
) -> httpx.Response:
    if self._delay_synchronizer:
        self._lock.acquire()
    url = self.base_url + path
    if type(self) is Antipublic:
        url += f"?key={self.token}"
    method = method.upper()
    if re.search(self._delay_pattern, path):
        _MainTweaks._auto_delay(self=self)
    if params is None:
        params = {}
    params["locale"] = self._locale
    params.update(self.custom_params)
    if type(data) is dict:
        data.update(self.custom_body)
    headers = self._main_headers.copy()
    headers.update(self.custom_headers)

    ptd = []
    for key in params.keys():
        if params[key] is None:
            ptd.append(key)
    for key in ptd:
        del params[key]

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
            proxy_scheme = proxy_schemes[self._proxy_type]
            proxy = {
                "http": f"{proxy_scheme}://{self._proxy}",
                "https": f"{proxy_scheme}://{self._proxy}",
            }
        else:
            raise Exceptions.INVALID_PROXY_TYPE(
                "Proxy type has invalid value. It can be only https, http, socks4 or socks5"
            )
    if method in request_methods:
        response = httpx.request(
            method=method,
            url=url,
            params=params,
            data=data,
            files=files,
            headers=headers,
            proxies=proxy,
            timeout=self.timeout,
        )
        if self.reset_custom_variables:
            self.custom_params = {}
            self.custom_body = {}
            self.custom_headers = {}
        if self.debug:
            print(response.request.method)
            print(response.json())
            print(response.request.headers)
            print(response.request.url)
            print(response.request.body)
            print(response.text)
        if self._delay_synchronizer:
            self._delay_synchronizer._synchronize(time.time())
            self._lock.release()
        else:
            self._auto_delay_time = time.time()
        return response
    else:
        raise Exceptions.AS7RID_FUCK_UP("Invalid request method. Contact @AS7RID")


@_MainTweaks._RetryWrapper
async def _send_async_request(
    self, method: str, path: dict, params: dict = None, data=None, files=None
) -> httpx.Response:
    if self._delay_synchronizer:
        self._lock.acquire()
    url = self.base_url + path
    if type(self) is Antipublic:
        url += f"?key={self.token}"
    method = method.upper()
    if re.search(self._delay_pattern, path):
        await _MainTweaks._auto_delay_async(self=self)
    if params is None:
        params = {}
    params["locale"] = self._locale
    ptd = []

    params.update(self.custom_params)
    if type(data) is dict:
        data.update(self.custom_body)
    headers = self._main_headers.copy()
    headers.update(self.custom_headers)

    for key, value in params.items():
        if type(params[key]) is bool:
            params[key] = str(value)
        if params[key] is None:
            ptd.append(key)
    for key in ptd:
        del params[key]
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
            proxy_scheme = proxy_schemes[self._proxy_type]
            proxy = f"{proxy_scheme}://{self._proxy}"
        else:
            raise Exceptions.INVALID_PROXY_TYPE(
                "Proxy type has invalid value. It can be only https, http, socks4 or socks5"
            )

    if method in request_methods:
        async with httpx.AsyncClient(proxies=proxy) as client:
            response = await client.request(
                method=method,
                url=url,
                params=params,
                data=data,
                files=files,
                headers=self._main_headers,
                timeout=self.timeout,
            )
            if self.debug:
                print(response.request_info.method)
                print(response.json())
                print(response.request_info.headers)
                print(response.request_info.url)
                print(response._body)
                print(response.text)
            if self._delay_synchronizer:
                self._delay_synchronizer._synchronize(time.time())
                self._lock.release()
            else:
                self._auto_delay_time = time.time()
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
        :param token: Your token. You can get in there -> https://zelenka.guru/account/api
        :param bypass_429: Bypass status code 429 by sleep
        :param language: Language for your api responses. Pass "en" if you want to get responses in english or pass "ru" if you want to get responses in russian.
        :param proxy_type: Your proxy type. You can use types ( Constants.Proxy.socks5 or socks4,https,http )
        :param proxy: Proxy string. Example -> ip:port or login:password@ip:port
        """
        self.base_url = "https://api.zelenka.guru"
        self.debug = False
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
        _MainTweaks.setup_jwt(
            self=self, token=token, user_id=locals().get("user_id", None)
        )
        self._main_headers = {"Authorization": f"bearer {self._token}"}

        self.bypass_429 = bypass_429
        self.timeout = timeout
        self._auto_delay_time = time.time() - 3
        self._locale = language
        self._delay_synchronizer = None
        self._lock = None
        self._delay_pattern = ".*"

        self.reset_custom_variables = reset_custom_variables
        self.custom_params = {}
        self.custom_body = {}
        self.custom_headers = {}

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
        self.oauth = self.__Oauth(self)

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
        def get_categories(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: str = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/categories

            List of all categories in the system.

            Required scopes: read

            :param parent_category_id: ID of parent category.
            :param parent_forum_id: ID of parent forum.
            :param order: Ordering of categories. Can be [natural, list]
            :return: httpx Response object
            """
            path = "/categories"
            params = {
                "parent_category_id": parent_category_id,
                "parent_forum_id": parent_forum_id,
                "order": order,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_category(self, category_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/categories/{category_id}

            Detail information of a category.

            Required scopes: read

            :param category_id: ID of category we want to get
            :return: httpx Response object
            """
            path = f"/categories/{category_id}"
            return _send_request(self=self._api, method="GET", path=path)

    class __Forums:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_forums(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: str = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/forums

            List of all forums in the system.

            Required scopes: read

            :param parent_category_id: ID of parent category.
            :param parent_forum_id: ID of parent forum.
            :param order: Ordering of categories. Can be [natural, list]
            :return: httpx Response object
            """
            path = "/forums"
            params = {
                "parent_category_id": parent_category_id,
                "parent_forum_id": parent_forum_id,
                "order": order,
            }
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_forum(self, forum_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/forums/{forum_id}

            Detail information of a forum.

            Required scopes: read

            :param forum_id: ID of forum we want to get
            :return: httpx Response object
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
            POST https://api.zelenka.guru/forums/forum_id/followers
            Follow a forum.

            Required scopes: post

            :param forum_id: ID of forum we want to get
            :param prefix_ids: List with prefix id's.
            :param minimal_contest_amount: Minimal contest amount.( for forumid 766 )
            :param post: Whether to receive notification for post.
            :param alert: Whether to receive notification as alert.
            :param email: Whether to receive notification as email.

            :return: httpx Response object
            """
            path = f"/forums/{forum_id}/followers"
            if True:  # Tweak 0
                if post:
                    post = 1
                if alert:
                    alert = 1
                if email:
                    email = 1
            params = {
                "post": post,
                "alert": alert,
                "email": email,
                "minimal_contest_amount": minimal_contest_amount,
                "prefix_ids[]": prefix_ids,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unfollow(self, forum_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/forums/forum_id/followers
            Unfollow a forum.

            Required scopes: post

            :param forum_id: ID of forum we want to get

            :return: httpx Response object
            """
            path = f"/forums/{forum_id}/followers"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followers(self, forum_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/forums/forum_id/followers

            List of a forum's followers. For privacy reason, only the current user will be included in the list (if the user follows the specified forum).

            Required scopes: read

            :param forum_id: ID of forum we want to get
            :return: httpx Response object
            """
            path = f"/forums/{forum_id}/followers"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followed(self, total: bool = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/forums/followed

            List of followed forums by current user.

            Required scopes: read

            :param total: If included in the request, only the forum count is returned as forums_total.

            :return: httpx Response object
            """
            path = "/forums/followed"
            if True:  # Tweak 0
                if total is True:
                    total = 1
                elif total is False:
                    total = 0
            params = {"total": total}
            return _send_request(self=self._api, method="GET", path=path, params=params)

    class __Pages:
        def __init__(self, _api_self) -> httpx.Response:
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_pages(
            self, parent_page_id: int = None, order: str = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/pages

            List of all pages in the system.

            Required scopes: read

            :param parent_page_id: ID of parent page. If exists, filter pages that are direct children of that page.
            :param order: Ordering of pages. Can be [natural, list]

            :return: httpx Response object
            """
            path = "/pages"
            params = {"parent_page_id": parent_page_id, "order": order}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_page(self, page_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/pages/page_id

            Detail information of a page.

            Required scopes: read

            :param page_id: ID of parent page. If exists, filter pages that are direct children of that page.

            :return: httpx Response object
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
                GET https://api.zelenka.guru/posts/post_id/comments

                List of post comments in a thread (with pagination).

                Required scopes: read

                :param post_id: ID of post.
                :param before: The time in milliseconds (e.g. 1652177794083) before last comment date

                :return: httpx Response object
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
                POST https://api.zelenka.guru/posts/post_id/comments

                Create a new post comment.

                Required scopes: post

                :param post_id: ID of post.
                :param comment_body: Content of the new post

                :return: httpx Response object
                """
                path = f"/posts/{post_id}/comments"
                data = {"comment_body": comment_body}
                return _send_request(
                    self=self._api, method="POST", path=path, data=data
                )

        def __init__(self, _api_self):
            self._api = _api_self
            self.comments = self.__Posts_comments(self._api)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_posts(
            self,
            thread_id: int = None,
            page_of_post_id: int = None,
            post_ids: list = None,
            page: int = None,
            limit: int = None,
            order: int = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/posts

            List of posts in a thread (with pagination).

            Required scopes: read

            :param thread_id: ID of the containing thread.
            :param page_of_post_id: ID of a post, posts that are in the same page with the specified post will be returned. thread_id may be skipped.
            :param post_ids: ID's of needed posts. If this parameter is set, all other filtering parameters will be ignored.
            :param page: Page number of posts.
            :param limit: Number of posts in a page. Default value depends on the system configuration.
            :param order: Ordering of posts. Can be [natural, natural_reverse, post_create_date, post_create_date_reverse].
            :return: httpx Response object
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
            GET https://api.zelenka.guru/posts/post_id

            Detail information of a post.

            Required scopes: read

            :param post_id: ID of post.

            :return: httpx Response object
            """
            path = f"/posts/{post_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def create(
            self, post_body: str, thread_id: int = None, quote_post_id: int = None
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/posts

            Create a new post.

            Required scopes: post

            :param post_body: Content of the new post.
            :param thread_id: ID of the target thread.
            :param quote_post_id: ID of the quote post. It's possible to skip thread_id if this parameter is provided. An extra check is performed if both parameters exist and does not match.

            :return: httpx Response object
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
            self, post_id: int, post_body: str = None, message_state: str = None
        ) -> httpx.Response:
            """
            PUT https://api.zelenka.guru/posts/post_id

            Edit a post.

            Required scopes: post

            :param post_id: ID of post.
            :param message_state: Message state. Can be [visible,deleted,moderated]
            :param post_body: New content of the post.

            :return: httpx Response object
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
            DELETE https://api.zelenka.guru/posts/post_id

            Delete a post.

            Required scopes: post

            :param post_id: ID of post.
            :param reason: Reason of the post removal.

            :return: httpx Response object
            """
            path = f"/posts/{post_id}"
            data = {"reason": reason}
            return _send_request(self=self._api, method="DELETE", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def likes(
            self, post_id: int, page: int = None, limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/posts/post_id/likes

            List of users who liked a post.

            Required scopes: read

            :param post_id: ID of post.
            :param page: Page number of users.
            :param limit: Number of users in a page. Default value depends on the system configuration.

            :return: httpx Response object
            """
            path = f"/posts/{post_id}/likes"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def like(self, post_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/posts/post_id/likes

            Like a post.

            Required scopes: post

            :param post_id: ID of post.

            :return: httpx Response object
            """
            path = f"/posts/{post_id}/likes"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unlike(self, post_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/posts/post_id/likes

            Unlike a post.

            Required scopes: post

            :param post_id: ID of post.

            :return: httpx Response object
            """
            path = f"/posts/{post_id}/likes"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def report(self, post_id: int, message: str) -> httpx.Response:
            """
            POST https://api.zelenka.guru/posts/post_id/report

            Report a post.

            Required scopes: post

            :param post_id: ID of post.
            :param message: Reason of the report.

            :return: httpx Response object
            """
            path = f"/posts/{post_id}/report"
            data = {"message": message}
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
                    prize_data_money: int,
                    count_winners: int,
                    length_value: int,
                    length_option: str,
                    require_like_count: int,
                    require_total_like_count: int,
                    secret_answer: str,
                    reply_group: int = 2,
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

                    Create a new thread.

                    Required scopes: post

                    :param post_body: Content of the new thread.
                    :param title: Thread title. Can be skipped if title_en set.
                    :param title_en: Thread title in english. Can be skipped if title set.
                    :param prefix_ids: Thread prefixes.
                    :param tags: Thread tags.
                    :param allow_ask_hidden_content: Allow ask hidden content.
                    :param dont_alert_followers: Don't alert followers
                    :param reply_group: Allow to reply only users with chosen or higher group.
                    :param comment_ignore_group: Allow commenting if user can't post in thread.
                    :param prize_data_money: How much money will each winner receive.
                    :param count_winners: Winner count (prize count). The maximum value is 100.
                    :param length_value: Giveaway duration value. The maximum duration is 3 days.
                    :param length_option: Giveaway duration type. Can be [minutes, hours, days]. The maximum duration is 3 days.
                    :param require_like_count: Sympathies for this week.
                    :param require_total_like_count: Symapthies for all time.
                    :param secret_answer:Secret answer of your account.

                    :return: httpx Response object
                    """
                    contest_type = "by_finish_date"
                    prize_type = "money"
                    forum_id = 766
                    if True:  # Tweak 0
                        if allow_ask_hidden_content is True:
                            allow_ask_hidden_content = 1
                        elif allow_ask_hidden_content is False:
                            allow_ask_hidden_content = 0
                        if comment_ignore_group is True:
                            comment_ignore_group = 1
                        elif comment_ignore_group is False:
                            comment_ignore_group = 0
                        if dont_alert_followers is True:
                            dont_alert_followers = 1
                        elif dont_alert_followers is False:
                            dont_alert_followers = 0
                    if tags:
                        tags = ",".join(tags)
                    params = {
                        "prefix_id[]": prefix_ids,
                        "tags": tags,
                        "hide_contacts": 0,
                        "allow_ask_hidden_content": allow_ask_hidden_content,
                        "dont_alert_followers": dont_alert_followers,
                        "reply_group": reply_group,
                        "comment_ignore_group": comment_ignore_group,
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
                    prize_data_money: int,
                    count_winners: int,
                    needed_members: int,
                    require_like_count: int,
                    require_total_like_count: int,
                    secret_answer: str,
                    reply_group: int = 2,
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

                    Create a new thread.

                    Required scopes: post

                    :param post_body: Content of the new thread.
                    :param title: Thread title. Can be skipped if title_en set.
                    :param title_en: Thread title in english. Can be skipped if title set.
                    :param prefix_ids: Thread prefixes.
                    :param tags: Thread tags.
                    :param allow_ask_hidden_content: Allow ask hidden content.
                    :param dont_alert_followers: Don't alert followers
                    :param reply_group: Allow to reply only users with chosen or higher group.
                    :param comment_ignore_group: Allow commenting if user can't post in thread.
                    :param prize_data_money: How much money will each winner receive.
                    :param count_winners: Winner count (prize count). The maximum value is 100.
                    :param needed_members: Max member count.
                    :param require_like_count: Sympathies for this week.
                    :param require_total_like_count: Symapthies for all time.
                    :param secret_answer:Secret answer of your account.

                    :return: httpx Response object
                    """
                    contest_type = "by_needed_members"
                    prize_type = "money"
                    forum_id = 766
                    if True:  # Tweak 0
                        if allow_ask_hidden_content is True:
                            allow_ask_hidden_content = 1
                        elif allow_ask_hidden_content is False:
                            allow_ask_hidden_content = 0
                        if comment_ignore_group is True:
                            comment_ignore_group = 1
                        elif comment_ignore_group is False:
                            comment_ignore_group = 0
                        if dont_alert_followers is True:
                            dont_alert_followers = 1
                        elif dont_alert_followers is False:
                            dont_alert_followers = 0
                    if tags:
                        tags = ",".join(tags)
                    params = {
                        "prefix_id[]": prefix_ids,
                        "tags": tags,
                        "hide_contacts": 0,
                        "allow_ask_hidden_content": allow_ask_hidden_content,
                        "reply_group": reply_group,
                        "comment_ignore_group": comment_ignore_group,
                        "count_winners": count_winners,
                        "require_like_count": require_like_count,
                        "require_total_like_count": require_total_like_count,
                        "prize_type": prize_type,
                        "contest_type": contest_type,
                        "needed_members": needed_members,
                        "prize_data_money": prize_data_money,
                        "dont_alert_followers": dont_alert_followers,
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
                    prize_data_upgrade: int,
                    count_winners: int,
                    length_value: int,
                    length_option: str,
                    require_like_count: int,
                    require_total_like_count: int,
                    secret_answer: str,
                    reply_group: int = 2,
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

                    Create a new thread.

                    Contest prize upgrade type:

                    1 - Supreme - 3 months.

                    6 - Legend - 12 months.

                    12 - AntiPublic.One Plus subscription - 1 month.

                    14 - Uniq - lifetime.

                    17 - 18+ Photo leaks - 6 months.

                    19 - Auto giveaway participation - 1 month.

                    Required scopes: post

                    :param post_body: Content of the new thread.
                    :param title: Thread title. Can be skipped if title_en set.
                    :param title_en: Thread title in english. Can be skipped if title set.
                    :param prefix_ids: Thread prefixes.
                    :param tags: Thread tags.
                    :param allow_ask_hidden_content: Allow ask hidden content.
                    :param reply_group: Allow to reply only users with chosen or higher group.
                    :param comment_ignore_group: Allow commenting if user can't post in thread.
                    :param dont_alert_followers: Don't alert followers
                    :param prize_data_upgrade: Which upgrade will each winner receive. Check description above
                    :param count_winners: Winner count (prize count). The maximum value is 100.
                    :param length_value: Giveaway duration value. The maximum duration is 3 days.
                    :param length_option: Giveaway duration type. Can be [minutes, hours, days]. The maximum duration is 3 days.
                    :param require_like_count: Sympathies for this week.
                    :param require_total_like_count: Symapthies for all time.
                    :param secret_answer:Secret answer of your account.

                    :return: httpx Response object
                    """
                    contest_type = "by_finish_date"
                    prize_type = "upgrades"
                    forum_id = 766

                    if True:  # Tweak 0
                        if allow_ask_hidden_content is True:
                            allow_ask_hidden_content = 1
                        elif allow_ask_hidden_content is False:
                            allow_ask_hidden_content = 0
                        if comment_ignore_group is True:
                            comment_ignore_group = 1
                        elif comment_ignore_group is False:
                            comment_ignore_group = 0
                        if dont_alert_followers is True:
                            dont_alert_followers = 1
                        elif dont_alert_followers is False:
                            dont_alert_followers = 0
                    if tags:
                        tags = ",".join(tags)
                    params = {
                        "prefix_id[]": prefix_ids,
                        "tags": tags,
                        "hide_contacts": 0,
                        "allow_ask_hidden_content": allow_ask_hidden_content,
                        "reply_group": reply_group,
                        "comment_ignore_group": comment_ignore_group,
                        "count_winners": count_winners,
                        "require_like_count": require_like_count,
                        "require_total_like_count": require_total_like_count,
                        "prize_type": prize_type,
                        "contest_type": contest_type,
                        "dont_alert_followers": dont_alert_followers,
                        "prize_data_upgrade": prize_data_upgrade,
                        "count_winners": count_winners,
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
                    prize_data_upgrade: int,
                    count_winners: int,
                    needed_members: int,
                    require_like_count: int,
                    require_total_like_count: int,
                    secret_answer: str,
                    reply_group: int = 2,
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

                    Create a new thread.

                    Contest prize upgrade type:

                    1 - Supreme - 3 months.

                    6 - Legend - 12 months.

                    12 - AntiPublic.One Plus subscription - 1 month.

                    14 - Uniq - lifetime.

                    17 - 18+ Photo leaks - 6 months.

                    19 - Auto giveaway participation - 1 month.

                    Required scopes: post

                    :param post_body: Content of the new thread.
                    :param title: Thread title. Can be skipped if title_en set.
                    :param title_en: Thread title in english. Can be skipped if title set.
                    :param prefix_ids: Thread prefixes.
                    :param tags: Thread tags.
                    :param allow_ask_hidden_content: Allow ask hidden content.
                    :param reply_group: Allow to reply only users with chosen or higher group.
                    :param comment_ignore_group: Allow commenting if user can't post in thread.
                    :param dont_alert_followers: Don't alert followers
                    :param prize_data_upgrade: Which upgrade will each winner receive. Check description above
                    :param count_winners: Winner count (prize count). The maximum value is 100.
                    :param needed_members: Max member count.
                    :param require_like_count: Sympathies for this week.
                    :param require_total_like_count: Symapthies for all time.
                    :param secret_answer:Secret answer of your account.

                    :return: httpx Response object
                    """
                    path = "/threads"
                    contest_type = "by_needed_members"
                    prize_type = "upgrades"

                    forum_id = 766
                    if True:  # Tweak 0
                        if allow_ask_hidden_content is True:
                            allow_ask_hidden_content = 1
                        elif allow_ask_hidden_content is False:
                            allow_ask_hidden_content = 0
                        if comment_ignore_group is True:
                            comment_ignore_group = 1
                        elif comment_ignore_group is False:
                            comment_ignore_group = 0
                        if dont_alert_followers is True:
                            dont_alert_followers = 1
                        elif dont_alert_followers is False:
                            dont_alert_followers = 0
                    if tags:
                        tags = ",".join(tags)
                    params = {
                        "prefix_id[]": prefix_ids,
                        "tags": tags,
                        "hide_contacts": 0,
                        "allow_ask_hidden_content": allow_ask_hidden_content,
                        "reply_group": reply_group,
                        "comment_ignore_group": comment_ignore_group,
                        "count_winners": count_winners,
                        "require_like_count": require_like_count,
                        "require_total_like_count": require_total_like_count,
                        "prize_type": prize_type,
                        "contest_type": contest_type,
                        "needed_members": needed_members,
                        "prize_type": prize_type,
                        "contest_type": contest_type,
                        "needed_members": needed_members,
                        "dont_alert_followers": dont_alert_followers,
                        "prize_data_upgrade": prize_data_upgrade,
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

        class __Arbitrage:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["post"])
            def market(
                self,
                responder: str,
                item_id: int,
                amount: float,
                post_body: str,
                currency: str = None,
                conversation_screenshot: str = "no",
                tags: list = None,
                hide_contacts: bool = None,
                allow_ask_hidden_content: bool = None,
                comment_ignore_group: bool = None,
                dont_alert_followers: bool = None,
                reply_group: int = 2,
            ) -> httpx.Response:
                """
                POST https://api.zelenka.guru/claims

                Create a Arbitrage.

                Required scopes: post

                :param responder: To whom the complaint is filed. Specify a nickname or a link to the profile.
                :param item_id: Write account link or item_id.
                :param amount: Amount by which the responder deceived you.
                :param post_body: You should describe what's happened.
                :param currency: Currency of Arbitrage.
                :param conversation_screenshot: Screenshot showing the respondent's Telegram login. If the correspondence was conducted in Telegram, upload screenshot that will display the respondent's Telegram login against the background of your dialogue. The screenshot must be uploaded to Imgur. If the correspondence was conducted elsewhere, write "no".
                :param tags: Thread tags.
                :param hide_contacts: Hide contacts.
                :param allow_ask_hidden_content: Allow ask hidden content.
                :param comment_ignore_group: Allow commenting if user can't post in thread.
                :param dont_alert_followers: Don't alert followers
                :param reply_group: Allow to reply only users with chosen or higher group.

                :return: httpx Response object
                """
                path = "/claims"
                if type(item_id) is int:
                    if "CREATE_JOB" in locals() or "SEND_AS_ASYNC" in locals():
                        base_api = self
                    else:
                        base_api = self._api
                    item_id = f"{base_api.base_url}/market/{item_id}"
                if True:  # Tweak 0
                    if hide_contacts is True:
                        hide_contacts = 1
                    elif hide_contacts is False:
                        hide_contacts = 0
                    if allow_ask_hidden_content is True:
                        allow_ask_hidden_content = 1
                    elif allow_ask_hidden_content is False:
                        allow_ask_hidden_content = 0
                    if comment_ignore_group is True:
                        comment_ignore_group = 1
                    elif comment_ignore_group is False:
                        comment_ignore_group = 0
                    if dont_alert_followers is True:
                        dont_alert_followers = 1
                    elif dont_alert_followers is False:
                        dont_alert_followers = 0
                if tags:
                    tags = ",".join(tags)
                data = {
                    "post_body": post_body,
                    "as_responder": responder,
                    "as_is_market_deal": 1,
                    "as_market_item_link": item_id,
                    "as_amount": amount,
                    "currency": currency,
                    "as_funds_receipt": "no",
                    "as_tg_login_screenshot": conversation_screenshot,
                    "tags": tags,
                    "hide_contacts": hide_contacts,
                    "allow_ask_hidden_content": allow_ask_hidden_content,
                    "comment_ignore_group": comment_ignore_group,
                    "dont_alert_followers": dont_alert_followers,
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
                currency: str = None,
                transfer_type: str = "notsafe",
                tags: list = None,
                hide_contacts: bool = None,
                allow_ask_hidden_content: bool = None,
                comment_ignore_group: bool = None,
                dont_alert_followers: bool = None,
                reply_group: int = 2,
            ) -> httpx.Response:
                """
                POST https://api.zelenka.guru/claims

                Create a Arbitrage.

                Required scopes: post

                :param responder: To whom the complaint is filed. Specify a nickname or a link to the profile.
                :param amount: Amount by which the responder deceived you.
                :param currency: Currency of Arbitrage.
                :param receipt: Funds transfer recipient. Upload a receipt for the transfer of funds, use the "View receipt" button in your wallet. Must be uploaded to Imgur. Write "no" if you have not paid.
                :param post_body: You should describe what's happened.
                :param pay_claim: !!!  If you set this parameter to **True** forum will automatically calculate the amount and debit it from your account.  !!!\nFor filing claims, it is necessary to make a contribution in the amount of 5% of the amount of damage (but not less than 50 rubles and not more than 5000 rubles). For example, for an amount of damage of 300 rubles, you will need to pay 50 rubles, for 2,000 and 10,000 rubles - 100 and 500 rubles, respectively).
                :param responder_data: Contacts and wallets of the responder. Specify the known data about the responder (Skype, Vkontakte, Qiwi, WebMoney, etc.), if any.
                :param transfer_type: The transaction took place through a guarantor or there was a transfer to the market with a hold? Can be ["safe", "notsafe"]
                :param conversation_screenshot: Screenshot showing the respondent's Telegram login. If the correspondence was conducted in Telegram, upload screenshot that will display the respondent's Telegram login against the background of your dialogue. The screenshot must be uploaded to Imgur. If the correspondence was conducted elsewhere, write "no".
                :param tags: Thread tags.
                :param hide_contacts: Hide contacts.
                :param allow_ask_hidden_content: Allow ask hidden content.
                :param comment_ignore_group: Allow commenting if user can't post in thread.
                :param dont_alert_followers: Don't alert followers
                :param reply_group: Allow to reply only users with chosen or higher group.

                :return: httpx Response object
                """
                path = "/claims"
                if True:  # Tweak 0
                    if hide_contacts is True:
                        hide_contacts = 1
                    elif hide_contacts is False:
                        hide_contacts = 0
                    if allow_ask_hidden_content is True:
                        allow_ask_hidden_content = 1
                    elif allow_ask_hidden_content is False:
                        allow_ask_hidden_content = 0
                    if comment_ignore_group is True:
                        comment_ignore_group = 1
                    elif comment_ignore_group is False:
                        comment_ignore_group = 0
                    if dont_alert_followers is True:
                        dont_alert_followers = 1
                    elif dont_alert_followers is False:
                        dont_alert_followers = 0
                if tags:
                    tags = ",".join(tags)
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
                    "tags": tags,
                    "hide_contacts": hide_contacts,
                    "allow_ask_hidden_content": allow_ask_hidden_content,
                    "comment_ignore_group": comment_ignore_group,
                    "dont_alert_followers": dont_alert_followers,
                    "reply_group": reply_group,
                }
                return _send_request(
                    self=self._api, method="POST", path=path, data=data
                )

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_threads(
            self,
            forum_id: int = None,
            thread_ids: str = None,
            creator_user_id: int = None,
            sticky: bool = None,
            thread_prefix_id: int = None,
            thread_tag_id: int = None,
            page: int = None,
            limit: int = None,
            order: str = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads

            List of threads in a forum (with pagination).

            Required scopes: read

            :param forum_id: ID of the containing forum. Can be skipped if thread_ids set.
            :param thread_ids: ID's of needed threads (separated by comma). If this parameter is set, all other filtering parameters will be ignored.
            :param creator_user_id: Filter to get only threads created by the specified user.
            :param sticky: Filter to get only sticky <sticky=1> or non-sticky <sticky=0> threads. By default, all threads will be included and sticky ones will be at the top of the result on the first page. In mixed mode, sticky threads are not counted towards threads_total and does not affect pagination.
            :param thread_prefix_id: Filter to get only threads with the specified prefix.
            :param thread_tag_id: Filter to get only threads with the specified tag.
            :param page: Page number of threads.
            :param limit: Number of threads in a page.
            :param order: Can be [natural, thread_create_date, thread_create_date_reverse, thread_update_date, thread_update_date_reverse, thread_view_count, thread_view_count_reverse, thread_post_count, thread_post_count_reverse]
            :return: httpx Response object
            """
            path = "/threads"
            if sticky is True:  # Tweak 0
                sticky = 1
            elif sticky is False:
                sticky = 0
            params = {
                "forum_id": forum_id,
                "thread_ids": thread_ids,
                "creator_user_id": creator_user_id,
                "sticky": sticky,
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
            GET https://api.zelenka.guru/threads/thread_id

            Detail information of a thread.

            Required scopes: read

            :param thread_id: ID of thread.

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def create(
            self,
            forum_id: int,
            post_body: str,
            reply_group: int = 2,
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

            Create a new thread.

            Required scopes: post

            Reply groups:

            0 - Only staff members and curators can reply in thread.

            2 - Everyone can reply in thread.

            21 - Local and higher can reply in thread.

            22 - Resident or higher can reply in thread.

            23 - Expert or higher can reply in thread.

            60 - Guru and higher can reply in thread.

            351 - Artificial Intelligence and higher can reply in thread.

            :param forum_id: ID of the target forum.
            :param post_body: Content of the new thread.
            :param title: Thread title. Can be skipped if title_en set.
            :param title_en: Thread title in english. Can be skipped if title set.
            :param prefix_ids: Thread prefixes.
            :param tags: Thread tags.
            :param hide_contacts: Hide contacts.
            :param allow_ask_hidden_content: Allow ask hidden content.
            :param reply_group: Allow to reply only users with chosen or higher group.
            :param comment_ignore_group: Allow commenting if user can't post in thread.
            :param dont_alert_followers: Don't alert followers

            :return: httpx Response object
            """
            path = "/threads"
            if True:  # Tweak 0
                if hide_contacts is True:
                    hide_contacts = 1
                elif hide_contacts is False:
                    hide_contacts = 0
                if allow_ask_hidden_content is True:
                    allow_ask_hidden_content = 1
                elif allow_ask_hidden_content is False:
                    allow_ask_hidden_content = 0
                if comment_ignore_group is True:
                    comment_ignore_group = 1
                elif comment_ignore_group is False:
                    comment_ignore_group = 0
                if dont_alert_followers is True:
                    dont_alert_followers = 1
                elif dont_alert_followers is False:
                    dont_alert_followers = 0
            if tags:
                tags = ",".join(tags)
            params = {
                "prefix_id[]": prefix_ids,
                "tags": tags,
                "hide_contacts": hide_contacts,
                "allow_ask_hidden_content": allow_ask_hidden_content,
                "reply_group": reply_group,
                "comment_ignore_group": comment_ignore_group,
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
            reply_group: int = None,
            comment_ignore_group: bool = None,
        ) -> httpx.Response:
            """
            PUT https://api.zelenka.guru/threads/thread_id

            Edit a thread.

            Required scopes: post

            Reply groups:

            0 - Only staff members and curators can reply in thread.

            2 - Everyone can reply in thread.

            21 - Local and higher can reply in thread.

            22 - Resident or higher can reply in thread.

            23 - Expert or higher can reply in thread.

            60 - Guru and higher can reply in thread.

            351 - Artificial Intelligence and higher can reply in thread.

            :param thread_id: Id of thread.
            :param title: Thread title.
            :param title_en: Thread title in english.
            :param prefix_ids: Thread prefixes.
            :param tags: Thread tags.
            :param discussion_open: Discussion state.
            :param hide_contacts: Hide contacts.
            :param allow_ask_hidden_content: Allow ask hidden content.
            :param reply_group: Allow to reply only users with chosen or higher group.
            :param comment_ignore_group: Allow commenting if user can't post in thread.

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}"
            if True:  # Tweak 0
                if discussion_open is True:
                    discussion_open = 1
                elif discussion_open is False:
                    discussion_open = 0
                if hide_contacts is True:
                    hide_contacts = 1
                elif hide_contacts is False:
                    hide_contacts = 0
                if allow_ask_hidden_content is True:
                    allow_ask_hidden_content = 1
                elif allow_ask_hidden_content is False:
                    allow_ask_hidden_content = 0
                if comment_ignore_group is True:
                    comment_ignore_group = 1
                elif comment_ignore_group is False:
                    comment_ignore_group = 0
            if tags:
                tags = ",".join(tags)
            data = {
                "title": title,
                "title_en": title_en,
                "prefix_id[]": prefix_ids,
                "tags": tags,
                "discussion_open": discussion_open,
                "hide_contacts": hide_contacts,
                "allow_ask_hidden_content": allow_ask_hidden_content,
                "reply_group": reply_group,
                "comment_ignore_group": comment_ignore_group,
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
            send_alert: bool = None,
            send_starter_alert: bool = None,
            starter_alert_reason: str = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/threads/thread_id/move

            Move a thread.

            Required scopes: post

            :param thread_id: Id of thread.
            :param forum_id: Target forum id.
            :param title: Thread title.
            :param title_en: Thread title in english.
            :param prefix_ids: Thread prefixes.
            :param send_alert: Send a notification to users who are followed to target node.
            :param send_starter_alert: Send alert to thread starter.
            :param starter_alert_reason: Reason of moving thread which will sent to thread starter. (Required if **send_starter_alert** is set)

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}/move"
            if True:  # Tweak 0
                if prefix_ids:
                    apply_thread_prefix = 1
                else:
                    apply_thread_prefix = None
                if send_alert is True:
                    send_alert = 1
                elif send_alert is False:
                    send_alert = 0
                if send_starter_alert is True:
                    send_starter_alert = 1
                elif send_starter_alert is False:
                    send_starter_alert = 0
            data = {
                "node_id": forum_id,
                "title": title,
                "title_en": title_en,
                "prefix_id[]": prefix_ids,
                "apply_thread_prefix": apply_thread_prefix,
                "send_alert": send_alert,
                "send_starter_alert": send_starter_alert,
                "starter_alert_reason": starter_alert_reason,
            }
            return _send_request(self=self._api, method="POST", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def delete(self, thread_id: int, reason: str = None) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/threads/thread_id

            Delete a thread.

            Required scopes: post

            :param thread_id: ID of thread.
            :param reason: Reason of the thread removal.

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}"
            params = {"reason": reason}
            return _send_request(
                self=self._api, method="DELETE", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followers(self, thread_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/thread_id/followers

            List of a thread's followers. For privacy reason, only the current user will be included in the list.

            Required scopes: read

            :param thread_id: ID of thread.

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}/followers"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followed(self, total: bool = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/followed

            List of followed threads by current user.

            Required scopes: read

            :param total: If included in the request, only the thread count is returned as threads_total.

            :return: httpx Response object
            """
            path = "/threads/followed"
            if True:  # Tweak 0
                if total is True:
                    total = 1
                elif total is False:
                    total = 0
            params = {"total": total}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def follow(self, thread_id: int, email: bool = None) -> httpx.Response:
            """
            POST https://api.zelenka.guru/threads/thread_id/followers

            Follow a thread.

            Required scopes: post

            :param thread_id: ID of thread.
            :param email: Whether to receive notification as email.

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}/followers"
            if True:  # Tweak 0
                if email:
                    email = 1
            params = {"email": email}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unfollow(self, thread_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/threads/thread_id/followers

            Unfollow a thread.

            Required scopes: post

            :param thread_id: ID of thread.

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}/followers"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def navigation(self, thread_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/thread_id/navigation

            List of navigation elements to reach the specified thread.

            Required scopes: read

            :param thread_id: ID of thread.

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}/navigation"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def votes(self, thread_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/thread_id/poll

            Detail information of a poll.

            Required scopes: read

            :param thread_id: ID of thread.

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}/poll"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def vote(
            self,
            thread_id: int,
            response_id: int = None,
            response_ids: list[int] = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/threads/thread_id/pool/votes

            Vote on a thread poll.

            Required scopes: post

            :param thread_id: ID of thread.
            :param response_id: The id of the response to vote for. Can be skipped if response_ids set.
            :param response_ids: An array of ids of responses (if the poll allows multiple choices).

            :return: httpx Response object
            """
            path = f"/threads/{thread_id}/pool/votes"
            if type(response_ids) is list:
                for element in response_ids:
                    if not isinstance(element, int):
                        raise TypeError("All response_ids need to be integer")

            params = (
                {"response_id": response_id}
                if response_id
                else {"response_ids[]": response_ids}
            )

            if response_ids:
                for element in response_ids:
                    if not isinstance(element, int):
                        raise TypeError("All response_ids need to be integers")

            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["read"])
        def new(
            self, forum_id: int = None, limit: int = None, data_limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/threads/new

            List of unread threads (must be logged in).

            Required scopes: read

            :param forum_id: ID of the container forum to search for threads. Child forums of the specified forum will be included in the search.
            :param limit: Maximum number of result threads. The limit may get decreased if the value is too large (depending on the system configuration).
            :param data_limit: Number of thread data to be returned. Default value is 20.
            :return: httpx Response object
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

            List of recent threads.

            Required scopes: read

            :param days: Maximum number of days to search for threads.
            :param forum_id: ID of the container forum to search for threads. Child forums of the specified forum will be included in the search.
            :param limit: Maximum number of result threads. The limit may get decreased if the value is too large (depending on the system configuration).
            :param data_limit: Number of thread data to be returned. Default value is 20.
            :return: httpx Response object
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
            POST https://api.zelenka.guru/threads/thread_id/bump

            Bump a thread.

            Required scopes: post

            :param thread_id: ID of thread.

            :return: httpx Response object
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

            List of popular tags (no pagination).

            Required scopes: read

            :return: httpx Response object
            """
            path = "/tags"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def tags(self, page: int = None, limit: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/tags/list

            List of tags.

            Required scopes: read


            :param page: Page number of tags list.
            :param limit: Limit of tags on a page.

            :return: httpx Response object
            """
            path = "/tags/list"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def tagged(
            self, tag_id: int, page: int = None, limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/tags/tag_id

            List of tagged contents.

            Required scopes: read

            :param tag_id: ID of tag.
            :param page: Page number of tags list.
            :param limit: Number of tagged contents in a page.

            :return: httpx Response object
            """
            path = f"/tags/{tag_id}"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def find(self, tag: str) -> httpx.Response:
            """
            GET https://api.zelenka.guru/tags/find

            Filtered list of tags.

            Required scopes: read

            :param tag: tag to filter. Tags start with the query will be returned.

            :return: httpx Response object
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
                POST https://api.zelenka.guru/users/user_id/avatar

                Upload avatar for a user.

                Required scopes: post / admincp

                :param user_id: ID of user. If you do not specify the user_id, then you will change the avatar of the current user
                :param avatar: Binary data of the avatar.

                :return: httpx Response object
                """
                if "CREATE_JOB" in locals():
                    logging.warn(
                        message=f"{FutureWarning.__name__}:You can't upload avatar using batch"
                    )
                if user_id is None:
                    path = "/users/me/avatar"
                else:
                    path = f"/users/{user_id}/avatar"
                files = {"avatar": avatar}
                return _send_request(
                    self=self._api, method="POST", path=path, files=files
                )

            @_MainTweaks._CheckScopes(scopes=["post?admincp"])
            def delete(self, user_id: int = None) -> httpx.Response:
                """
                DELETE https://api.zelenka.guru/users/user_id/avatar

                Delete avatar for a user.

                Required scopes: post / admincp

                :param user_id: ID of user. If you do not specify the user_id, then you will delete the avatar of the current user

                :return: httpx Response object
                """
                if user_id is None:
                    path = "/users/me/avatar"
                else:
                    path = f"/users/{user_id}/avatar"
                return _send_request(self=self._api, method="DELETE", path=path)

            @_MainTweaks._CheckScopes(scopes=["post?admincp"])
            def crop(
                self, user_id: int, size: int, x: int = None, y: int = None
            ) -> httpx.Response:
                """
                POST https://api.zelenka.guru/users/user_id/avatar-crop

                Crop avatar for a user.

                Required scopes: post / admincp

                :param user_id: ID of user.
                :param x: The starting point of the selection by width.
                :param y: The starting point of the selection by height
                :param size: Selection size. Minimum value - 16.

                :return: httpx Response object
                """
                params = {"x": x, "y": y, "crop": size}
                if (
                    user_id is None
                ):  # Пока такое не работает, но надеюсь пофиксят. Пусть лежит
                    path = "/users/me/avatar-crop"
                else:
                    path = f"/users/{user_id}/avatar-crop"
                return _send_request(
                    self=self._api,
                    method="POST",
                    path=path,
                    params=params,
                )

        def __init__(self, _api_self):
            self._api = _api_self
            self.avatar = self.__Avatar(self._api)

        def lost_password(
            self, oauth_token: str, username: str = None, email: str = None
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/lost-password

            Request a password reset via email. Either username or email parameter must be provided. If both are provided, username will be used.

            Required scopes: None

            :param oauth_token: A valid one time token.
            :param username: Username
            :param email: Email

            :return: httpx Response object
            """
            path = "/lost-password"
            params = {
                "oauth_token": oauth_token,
                "username": username,
                "email": email,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["read"])
        def users(self, page: int = None, limit: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users

            List of users (with pagination).

            Required scopes: read

            :param page: Page number of users.
            :param limit: Number of users in a page.
            :return: httpx Response object
            """
            path = "/users"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def fields(self) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/fields

            List of user fields.

            Required scopes: read

            :return: httpx Response object
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

            Filtered list of users by username, email or custom fields.

            Required scopes: read / admincp

            :param username: Username to filter. Usernames start with the query will be returned.
            :param user_email: Email to filter. Requires admincp scope.
            :param custom_fields: Custom fields to filter. Example: {"telegram": "Telegram_Login"}

            :return: httpx Response object
            """
            path = "/users/find"
            params = {
                "username": username,
                "user_email": user_email,
            }
            if custom_fields is not None:
                if "CREATE_JOB" in locals():
                    params["custom_fields"] = custom_fields  # Костыль CreateJob
                else:
                    for key, value in custom_fields.items():
                        cf = f"custom_fields[{key}]"
                        params[cf] = value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read?basic"])
        def get(self, user_id: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/user_id

            Detail information of a user.

            Required scopes: read, basic

            :param user_id: ID of user. If you do not specify the user_id, you will get info about current user
            :return: httpx Response object
            """
            if user_id is None:
                path = "/users/me"
            else:
                path = f"/users/{user_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_timeline(
            self, user_id: int = None, page: int = None, limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/user_id/timeline

            List of contents created by user (with pagination).

            Required scopes: read

            :param user_id: ID of user. If you do not specify the user_id, you will get timeline of current user
            :param page: Page number of contents.
            :param limit: Number of contents in a page.

            :return: httpx Response object
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
            secondary_group_ids: list[int] = None,
            user_dob_day: int = None,
            user_dob_month: int = None,
            user_dob_year: int = None,
            fields: dict = None,
            display_group_id: int = None,
        ) -> httpx.Response:
            """
            PUT https://api.zelenka.guru/users/user_id

            Edit a user.

            Encryption:
            For sensitive information like password, encryption can be used to increase data security. For all encryption with key support, the client_secret will be used as the key. List of supported encryptions:
            aes128: AES 128-bit encryption (mode: ECB, padding: PKCS#7). Because of algorithm limitation, the binary md5 hash of key will be used instead of the key itself.

            Required scopes: post / admincp

            :param user_id: ID of user. If you do not specify the user_id, you will edit current user
            :param password: New password.
            :param password_old: Data of the existing password, it is not required if (1) the current authenticated user has user admin permission, (2) the admincp scope is granted and (3) the user being edited is not the current authenticated user.
            :param password_algo: Algorithm used to encrypt the password and password_old parameters. See Encryption section for more information.
            :param user_email:New email of the user.
            :param username: New username of the user. Changing username requires Administrator permission.
            :param user_title: New custom title of the user.
            :param primary_group_id: ID of new primary group.
            :param secondary_group_ids: Array of ID's of new secondary groups.
            :param user_dob_day: Date of birth (day) of the new user.
            :param user_dob_month: Date of birth (month) of the new user.
            :param user_dob_year: Date of birth (year) of the new user.
            :param fields: Array of values for user fields.
            :param display_group_id: Id of group you want to display.

            :return: httpx Response object
            """
            if user_id is None:
                path = "/users/me"
            else:
                path = f"/users/{user_id}"
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
            POST https://api.zelenka.guru/users/user_id/followers

            Follow a user.

            Required scopes: post

            :param user_id: ID of user

            :return: httpx Response object
            """
            path = f"/users/{user_id}/followers"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unfollow(self, user_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/users/user_id/followers

            Unfollow a user.

            Required scopes: post

            :param user_id: ID of user

            :return: httpx Response object
            """
            path = f"/users/{user_id}/followers"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def followers(
            self,
            user_id: int = None,
            order: str = None,
            page: int = None,
            limit: int = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/user_id/followers

            List of a user's followers.


            Required scopes: read

            :param user_id: ID of user. If you do not specify the user_id, you will get followers of current user
            :param order: Ordering of followers. Support: natural, follow_date, follow_date_reverse
            :param page: Page number of followers.
            :param limit: Number of followers in a page.

            :return: httpx Response object
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
            order: str = None,
            page: int = None,
            limit: int = None,
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/user_id/followings

            List of users whom are followed by a user.

            Required scopes: read

            :param user_id: ID of user. If you do not specify the user_id, you will get followings users by current user
            :param order: Ordering of users. Support: natural, follow_date, follow_date_reverse
            :param page: Page number of users.
            :param limit: Number of users in a page.

            :return: httpx Response object
            """
            if user_id is None:
                path = "/users/me/followings"
            else:
                path = f"/users/{user_id}/followings"
            params = {"order": order, "page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def ignored(self, total: bool = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/ignored

            List of ignored users of current user.

            Required scopes: read

            :param total: If included in the request, only the user count is returned as users_total.

            :return: httpx Response object
            """
            path = "/users/ignored"
            if True:  # Tweak 0
                if total is True:
                    total = 1
                elif total is False:
                    total = 0
            params = {"total": total}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def ignore(self, user_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/users/user_id/ignore

            Ignore a user.

            Required scopes: post

            :param user_id: ID of user

            :return: httpx Response object
            """

            path = f"/users/{user_id}/ignore"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unignore(self, user_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/users/user_id/ignore

            Unignore a user.

            Required scopes: post

            :param user_id: ID of user

            :return: httpx Response object
            """

            path = f"/users/{user_id}/ignore"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def groups(self, user_id: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/user_id/groups

            List of a user's groups.

            Required scopes: read / admincp

            :param user_id: ID of user. If user_id skipped, method will return current user groups

            :return: httpx Response object
            """
            if user_id is None:
                path = "/users/me/groups"
            else:
                path = f"/users/{user_id}/groups"
            return _send_request(self=self._api, method="GET", path=path)

    class __Profile_posts:
        class __Profile_posts_comments:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["read"])
            def comments(
                self, profile_post_id: int, before: int = None, limit: int = None
            ) -> httpx.Response:
                """
                GET https://api.zelenka.guru/profile-posts/profile_post_id/comments

                List of comments of a profile post.

                Required scopes: read

                :param profile_post_id: ID of profile post.
                :param before: Date to get older comments. Please note that this entry point does not support the page parameter, but it still does support limit.
                :param limit: Number of profile posts in a page.

                :return: httpx Response object
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
                GET https://api.zelenka.guru/profile-posts/profile_post_id/comments/comment_id

                Detail information of a profile post comment.

                Required scopes: read

                :param profile_post_id: ID of profile post.
                :param comment_id: ID of profile post comment

                :return: httpx Response object
                """
                path = f"/profile-posts/{profile_post_id}/comments/{comment_id}"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["post"])
            def create(self, profile_post_id: int, comment_body: str) -> httpx.Response:
                """
                POST https://api.zelenka.guru/profile-posts/profile_post_id/comments

                Create a new profile post comment.

                Required scopes: post

                :param profile_post_id: ID of profile post.
                :param comment_body: Content of the new profile post comment.

                :return: httpx Response object
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
        def get_posts(
            self, user_id: int, page: int = None, limit: int = None
        ) -> httpx.Response:
            """
            GET https://api.zelenka.guru/users/user_id/profile-posts

            List of profile posts (with pagination).

            Required scopes: read

            :param user_id: ID of user.
            :param page: Page number of contents.
            :param limit: Number of contents in a page.

            :return: httpx Response object
            """
            params = {"page": page, "limit": limit}
            path = f"/users/{user_id}/profile-posts"
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, profile_post_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/profile-posts/profile_post_id

            Detail information of a profile post.

            Required scopes: read

            :param profile_post_id: ID of profile post.

            :return: httpx Response object
            """
            path = f"/profile-posts/{profile_post_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def create(self, post_body: str, user_id: int = None) -> httpx.Response:
            """
            POST https://api.zelenka.guru/users/user_id/timeline

            Create a new profile post on a user timeline.

            Required scopes: post

            :param user_id: ID of user. If you do not specify the user_id, you will create profile post in current user's timeline
            :param post_body: Content of the new profile post.

            :return: httpx Response object
            """
            if user_id is None:
                path = "/users/me/timeline"
            else:
                path = f"/users/{user_id}/timeline"
            data = {"post_body": post_body}
            return _send_request(self=self._api, method="POST", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def edit(self, profile_post_id: int, post_body: str) -> httpx.Response:
            """
            PUT https://api.zelenka.guru/profile-posts/profile_post_id

            Edit a profile post.

            Required scopes: post

            :param profile_post_id: ID of profile post.
            :param post_body: New content of the profile post.

            :return: httpx Response object
            """

            path = f"/profile-posts/{profile_post_id}"
            data = {"post_body": post_body}
            return _send_request(self=self._api, method="PUT", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def delete(self, profile_post_id: int, reason: str = None) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/profile-posts/profile_post_id

            Delete a profile post.

            Required scopes: post

            :param profile_post_id: ID of profile post.
            :param reason: Reason of the profile post removal.


            :return: httpx Response object
            """
            path = f"/profile-posts/{profile_post_id}"
            data = {"reason": reason}
            return _send_request(self=self._api, method="DELETE", path=path, data=data)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def likes(self, profile_post_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/profile-posts/profile_post_id/likes

            List of users who liked a profile post.

            Required scopes: read

            :param profile_post_id: ID of profile post.

            :return: httpx Response object
            """

            path = f"/profile-posts/{profile_post_id}/likes"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def like(self, profile_post_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/profile-posts/profile_post_id/likes

            Like a profile post.

            Required scopes: post

            :param profile_post_id: ID of profile post.

            :return: httpx Response object
            """

            path = f"/profile-posts/{profile_post_id}/likes"

            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def unlike(self, profile_post_id: int) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/profile-posts/profile_post_id/likes

            Unlike a profile post.

            Required scopes: post

            :param profile_post_id: ID of profile post.

            :return: httpx Response object
            """
            path = f"/profile-posts/{profile_post_id}/likes"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def report(self, profile_post_id: int, message: str) -> httpx.Response:
            """
            POST https://api.zelenka.guru/profile-posts/profile_post_id/report

            Report a profile post.

            Required scopes: post

            :param profile_post_id: ID of profile post.
            :param message: Reason of the report.

            :return: httpx Response object
            """
            path = f"/profile-posts/{profile_post_id}/report"
            data = {"message": message}
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

            Search for threads.

            Required scopes: post

            :param q: Search query. Can be skipped if user_id is set.
            :param tag: Tag to search for tagged contents.
            :param forum_id: ID of the container forum to search for contents. Child forums of the specified forum will be included in the search.
            :param user_id: ID of the creator to search for contents.
            :param page: Page number of results.
            :param limit: Number of results in a page.

            :return: httpx Response object
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

            Search for threads.

            Required scopes: post
            :param q: Search query. Can be skipped if user_id is set.
            :param tag: Tag to search for tagged contents.
            :param forum_id: ID of the container forum to search for contents. Child forums of the specified forum will be included in the search.
            :param user_id: ID of the creator to search for contents.
            :param page: Page number of results.
            :param limit: Number of results in a page.
            :param data_limit: Number of thread data to be returned.

            :return: httpx Response object
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

            Search for posts.

            Required scopes: post
            :param q: Search query. Can be skipped if user_id is set.
            :param tag: Tag to search for tagged contents.
            :param forum_id: ID of the container forum to search for contents. Child forums of the specified forum will be included in the search.
            :param user_id: ID of the creator to search for contents.
            :param page: Page number of results.
            :param limit: Number of results in a page.
            :param data_limit: Number of thread data to be returned.

            :return: httpx Response object
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
            tag: str = None,
            tags: list[str] = None,
            page: int = None,
            limit: int = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/search/tagged

            Search for tagged contents.

            Required scopes: post
            :param tag: Tag to search for tagged contents.
            :param tags: Array of tags to search for tagged contents.
            :param page: Page number of results.
            :param limit: Number of results in a page.
            :return: httpx Response object
            """
            path = "/search/tagged"
            params = {
                "tag": tag,
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

            Search for threads.

            Required scopes: post
            :param q: Search query. Can be skipped if user_id is set.
            :param user_id: ID of the creator to search for contents.
            :param page: Page number of results.
            :param limit: Number of results in a page.

            :return: httpx Response object
            """
            path = "/search/profile-posts"
            params = {"q": q, "user_id": user_id, "page": page, "limit": limit}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def indexing(
            self,
            content_type: str,
            content_id: str,
            title: str,
            body: str,
            link: str,
            date: int = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/search/indexing

            Index external content data into search system to be searched later.

            Required scopes: post

            :param content_type: The type of content being indexed.
            :param content_id:  The unique id for the content.
            :param title:  Content title.
            :param body:  Content body.
            :param link:  Link related to content.
            :param date: Unix timestamp in second of the content. If missing, current time will be used.

            :return: httpx Response object
            """
            path = "/search/indexing"
            data = {
                "content_type": content_type,
                "content_id": content_id,
                "title": title,
                "body": body,
                "link": link,
                "date": date,
            }

            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                data=json.dumps(data),
            )

    class __Notifications:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get_all(self) -> httpx.Response:
            """
            GET https://api.zelenka.guru/notifications

            List of notifications (both read and unread).

            Required scopes: read

            :return: httpx Response object
            """
            path = "/notifications"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["read"])
        def get(self, notification_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/notifications/{notification_id}/content

            Get associated content of notification. The response depends on the content type.

            Required scopes: read
            :param notification_id: ID of notification.

            :return: httpx Response object
            """
            path = f"/notifications/{notification_id}/content"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["post"])
        def read(self, notification_id: int = None) -> httpx.Response:
            """
            POST https://api.zelenka.guru/notifications/read

            Mark single notification or all existing notifications read.

            Required scopes: post
            :param notification_id: ID of notification. If notification_id is omitted, it's mark all existing notifications as read.

            :return: httpx Response object
            """
            path = "/notifications/read"
            params = {"notification_id": notification_id}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["post"])
        def custom(
            self,
            user_id: int = None,
            username: str = None,
            message: str = None,
            message_html: str = None,
            notification_type: str = None,
            extra_data: str = None,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/notifications/custom

            Send a custom alert.

            Required scopes: post, Send custom alert permission
            :param user_id: The alert receiver.
            :param username: The alert receiver.
            :param message: The alert message.
            :param message_html: The alert message.
            :param notification_type: The notification type.
            :param extra_data: Extra data when sending alert. Предположительно это словарик, но я не уверен

            :return: httpx Response object
            """

            path = "/notifications/custom"
            params = {
                "user_id": user_id,
                "username": username,
                "notification_type": notification_type,
            }
            data = {
                "message": message,
                "message_html": message_html,
                "extra_data": extra_data,
            }
            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                params=params,
                data=data,
            )

    class __Conversations:
        class __Conversations_messages:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["conversate", "read"])
            def get_all(
                self,
                conversation_id: int,
                page: int = None,
                limit: int = None,
                order: str = None,
                before: int = None,
                after: int = None,
            ) -> httpx.Response:
                """
                GET https://api.zelenka.guru/conversation-messages

                List of messages in a conversation (with pagination).

                Required scopes: conversate, read

                :param conversation_id: ID of conversation.
                :param page: Page number of messages.
                :param limit: Number of messages in a page.
                :param order: Ordering of messages. Can be [natural, natural_reverse].
                :param before: Date to get older messages.
                :param after: Date to get newer messages.

                :return: httpx Response object
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
                GET https://api.zelenka.guru/conversation-messages/message_id

                Detail information of a message.

                Required scopes: conversate, read

                :param message_id: ID of conversation message.

                :return: httpx Response object
                """
                path = f"/conversation-messages/{message_id}"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
            def create(self, conversation_id: int, message_body: str) -> httpx.Response:
                """
                POST https://api.zelenka.guru/conversation-messages

                Create a new conversation message.

                Required scopes: conversate, post

                :param conversation_id: ID of conversation.
                :param message_body: Content of the new message.

                :return: httpx Response object
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
                PUT https://api.zelenka.guru/conversation-messages/message_id

                Edit a message.

                Required scopes: conversate, post

                :param message_id: ID of conversation message.
                :param message_body: New content of the message.

                :return: httpx Response object
                """
                path = f"/conversation-messages/{message_id}"
                data = {"message_body": message_body}
                return _send_request(self=self._api, method="PUT", path=path, data=data)

            @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
            def delete(self, message_id: int) -> httpx.Response:
                """
                DELETE https://api.zelenka.guru/conversation-messages/message_id

                Delete a message.

                Required scopes: conversate, post

                :param message_id: ID of conversation message.

                :return: httpx Response object
                """
                path = f"/conversation-messages/{message_id}"
                return _send_request(self=self._api, method="DELETE", path=path)

            @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
            def report(self, message_id: int, message: str = None) -> httpx.Response:
                """
                POST https://api.zelenka.guru/conversation-messages/message_id/report

                Create a new conversation message.

                Required scopes: conversate, post

                :param message_id: ID of conversation message.
                :param message : Reason of the report.

                :return: httpx Response object
                """

                path = f"/conversation-messages/{message_id}/report"
                data = {"message": message}
                return _send_request(
                    self=self._api, method="POST", path=path, data=data
                )

        def __init__(self, _api_self):
            self._api = _api_self
            self.messages = self.__Conversations_messages(self._api)

        @_MainTweaks._CheckScopes(scopes=["conversate", "read"])
        def get_all(self, page: int = None, limit: int = None) -> httpx.Response:
            """
            GET https://api.zelenka.guru/conversations

            List of conversations (with pagination).

            Required scopes: conversate, read

            :param page: Page number of conversations.
            :param limit: Number of conversations in a page.

            :return: httpx Response object
            """
            path = "/conversations"
            params = {"page": page, "limit": limit}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["conversate", "read"])
        def get(self, conversation_id: int) -> httpx.Response:
            """
            GET https://api.zelenka.guru/conversations/conversation_id

            Detail information of a conversation.

            Required scopes: conversate, read

            :param conversation_id: ID of conversation.

            :return: httpx Response object
            """
            path = f"/conversations/{conversation_id}"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["conversate", "post"])
        def leave(
            self, conversation_id: int, leave_type: str = "delete"
        ) -> httpx.Response:
            """
            DELETE https://api.zelenka.guru/conversations/conversation_id

            Leave from conversation

            Required scopes: conversate, post

            :param conversation_id: ID of conversation.
            :param leave_type: Leave type. Can be [delete,delete_ignore].

            :return: httpx Response object
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

            Create a new conversation.

            Required scopes: conversate, post

            :param recipient_id: ID of recipient.
            :param message: First message in conversation.
            :param open_invite: Allow invites in conversation.
            :param conversation_locked: Is conversation locked.
            :param allow_edit_messages: Allow edit messages.

            :return: httpx Response object
            """
            if True:  # Tweak 0
                if open_invite is True:
                    open_invite = 1
                elif open_invite is False:
                    open_invite = 0

                if conversation_locked is True:
                    conversation_locked = 1
                elif conversation_locked is False:
                    conversation_locked = 0

                if allow_edit_messages is True:
                    allow_edit_messages = 1
                elif allow_edit_messages is False:
                    allow_edit_messages = 0
            params = {
                "recipient_id": recipient_id,
                "is_group": 0,
                "open_invite": open_invite,
                "conversation_locked": conversation_locked,
                "allow_edit_messages": allow_edit_messages,
            }
            data = {"message_body": message}
            path = "/conversations"
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

            Create a new group conversation.

            Required scopes: conversate, post

            :param recipients: List of usernames. Max recipients count is 10
            :param title: The title of new conversation.
            :param message: First message in conversation.
            :param open_invite: Allow invites in conversation.
            :param conversation_locked: Is conversation locked.
            :param allow_edit_messages: Allow edit messages.

            :return: httpx Response object
            """
            if True:  # Tweak 0
                if open_invite is True:
                    open_invite = 1
                elif open_invite is False:
                    open_invite = 0

                if conversation_locked is True:
                    conversation_locked = 1
                elif conversation_locked is False:
                    conversation_locked = 0

                if allow_edit_messages is True:
                    allow_edit_messages = 1
                elif allow_edit_messages is False:
                    allow_edit_messages = 0
            params = {
                "recipients": ",".join(recipients),
                "title": title,
                "is_group": 1,
                "open_invite": open_invite,
                "conversation_locked": conversation_locked,
                "allow_edit_messages": allow_edit_messages,
            }
            data = {"message_body": message}
            path = "/conversations"
            return _send_request(
                self=self._api,
                method="POST",
                path=path,
                params=params,
                data=data,
            )

    class __Oauth:
        def __init__(self, _api_self):
            self._api = _api_self

        def facebook(
            self, client_id: int, client_secret: str, facebook_token: str
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/oauth/token/facebook

            Request API access token using Facebook access token. Please note that because Facebook uses app-scoped user_id, it is not possible to recognize user across different Facebook Applications.

            Required scopes: None

            :param client_id: ID of facebook client.
            :param client_secret: Secret phrase of facebook client.
            :param facebook_token: Facebook token.

            :return: httpx Response object or token string
            """
            path = "/oauth/token/facebook"
            params = {
                "client_id": client_id,
                "client_secret": client_secret,
                "facebook_token": facebook_token,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        def twitter(
            self,
            client_id: int,
            client_secret: str,
            twitter_url: str,
            twitter_auth: str,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/oauth/token/twitter

            Request API access token using Twitter access token. The twitter_uri and twitter_auth parameters are similar to X-Auth-Service-Provider and X-Verify-Credentials-Authorization as specified in Twitter's OAuth Echo specification.

            Required scopes: None

            :param client_id: ID of twitter client.
            :param client_secret: Secret phrase of twitter client.
            :param twitter_url: "the full /account/verify_credentials.json uri that has been used to calculate OAuth signature. For security reason, the uri must use HTTPS protocol and the hostname must be either "twitter.com" or "api.twitter.com"."
            :param twitter_auth: the complete authentication header that starts with "OAuth". Consult Twitter document for more information.

            :return: httpx Response object or token string
            """
            path = "/oauth/token/twitter"
            params = {
                "client_id": client_id,
                "client_secret": client_secret,
                "twitter_uri": twitter_url,
                "twitter_auth": twitter_auth,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        def google(
            self, client_id: int, client_secret: str, google_token: str
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/oauth/token/google

            Request API access token using Google access token.

            Required scopes: None

            :param client_id: ID of facebook client.
            :param client_secret: Secret phrase of facebook client.
            :param google_token : Google token.

            :return: httpx Response object or token string
            """
            path = "/oauth/token/google"
            params = {
                "client_id": client_id,
                "client_secret": client_secret,
                "facebook_token": google_token,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["admincp"])
        def admin(self, user_id: int) -> httpx.Response:
            """
            POST https://api.zelenka.guru/oauth/token/admin

            Request API access token for another user. This requires admincp scope and the current user must have sufficient system permissions.

            Required scopes: admincp

            :param user_id: ID of the user that needs access token.

            :return: httpx Response object or token string
            """
            path = "/oauth/token/admin"
            params = {"user_id": user_id}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        def associate(
            self,
            client_id: int,
            user_id: str,
            password: str,
            extra_data: str,
            extra_timestamp: int,
        ) -> httpx.Response:
            """
            POST https://api.zelenka.guru/oauth/token/associate

            Request API access token and associate social account with an existing user account.

            Required scopes: None

            :param client_id: ID of associate client.
            :param user_id: ID of user.
            :param password: Can be used with password_algo for better security. See Encryption section for more information.
            :param extra_data: Extra data
            :param extra_timestamp: Extra timestamp

            :return: httpx Response object or token string
            """
            path = "/oauth/token/associate"
            params = {
                "client_id": client_id,
                "user_id": user_id,
                "password": password,
                "extra_data": extra_data,
                "extra_timestamp": extra_timestamp,
            }
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

    @_MainTweaks._CheckScopes(scopes=["read"])
    def navigation(self, parent: int = None) -> httpx.Response:
        """
        GET https://api.zelenka.guru/navigation

        List of navigation elements within the system.

        Required scopes: read

        :param parent: ID of parent element. If exists, filter elements that are direct children of that element.

        :return: httpx Response object
        """
        path = "/navigation"
        params = {"parent": parent}
        return _send_request(self=self, method="GET", path=path, params=params)

    def batch(self, jobs: list[dict]) -> httpx.Response:
        """
        POST https://api.zelenka.guru/batch

        Execute multiple API requests at once. Maximum batch jobs is 10.

        Example scheme:

        [
            {
            "id": "job_1",
            "uri": "https://api.zelenka.guru/users/2410024",
            "method": "GET",
            "params": {}
            }
        ]

        Required scopes: Same as called API requests.

        :param jobs: List of batch jobs. (Check example above)
        :return: httpx Response object
        """
        import json

        path = "/batch"
        data = json.dumps(jobs)
        return _send_request(self=self, method="POST", path=path, data=data)


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
        :param token: Your token. You can get in there -> https://zelenka.guru/account/api
        :param bypass_429: Bypass status code 429 by sleep
        :param language: Language for your api responses. Pass "en" if you want to get responses in english or pass "ru" if you want to get responses in russian.
        :param proxy_type: Your proxy type. You can use types ( Constants.Proxy.socks5 or socks4,https,http )
        :param proxy: Proxy string. Example -> ip:port or login:password@ip:port
        """
        self.base_url = "https://api.lzt.market"
        self.debug = False
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
        _MainTweaks.setup_jwt(
            self=self, token=token, user_id=locals().get("user_id", None)
        )
        self._main_headers = {"Authorization": f"bearer {self._token}"}

        self.bypass_429 = bypass_429
        self.timeout = timeout
        self._auto_delay_time = time.time() - 3
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
        self._delay_pattern = f"/(?:{_categories})(?:/|$)" + "|" + r"/(\d+)(?:/.*|$)"

        self.profile = self.__Profile(self)
        self.payments = self.__Payments(self)
        self.category = self.__Category(self)
        self.list = self.__List(self)
        self.publishing = self.__Publishing(self)
        self.purchasing = self.__Purchasing(self)
        self.managing = self.__Managing(self)
        self.proxy = self.__Proxy(self)

        self.reset_custom_variables = reset_custom_variables
        self.custom_params = {}
        self.custom_body = {}
        self.custom_headers = {}

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
        data = json.dumps(jobs)
        return _send_request(self=self, method="POST", path=path, data=data)

    class __Profile:
        def __init__(self, _api_self):
            self._api = _api_self

        @_MainTweaks._CheckScopes(scopes=["market"])
        def get(self) -> httpx.Response:
            """
            GET https://api.lzt.market/me

            Displays info about your profile.

            Required scopes: market

            :return: httpx Response object

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
            vk_ua: str = None,
            vk_show_links: bool = None,
            title: str = None,
            telegram_client: dict = None,
            deauthorize_steam: bool = None,
            hide_bids: bool = None,
        ) -> httpx.Response:
            """
            PUT https://api.lzt.market/me

            Change settings about your profile on the market.

            Required scopes: market

            :param disable_steam_guard: Disable Steam Guard on account purchase moment
            :param user_allow_ask_discount: Allow users ask discount for your accounts
            :param max_discount_percent: Maximum discount percents for your accounts
            :param allow_accept_accounts: Usernames who can transfer market accounts to you. Separate values with a comma.
            :param hide_favourites: Hide your profile info when you add an account to favorites
            :param vk_ua: Your vk useragent to accounts
            :param title: Market title.
            :param telegram_client: Telegram client. It should be {"telegram_api_id": 12345, "telegram_api_hash": "12345","telegram_device_model":"12345","telegram_system_version":"12345","telegram_app_version":"12345"}
            :param deauthorize_steam: Finish all Steam sessions after purchase.
            :param hide_bids: Hide your profile when bid on the auction.

            :return: httpx Response object

            """
            path = "/me"
            # Tweak 0
            if disable_steam_guard is True:
                disable_steam_guard = 1
            elif disable_steam_guard is False:
                disable_steam_guard = 0
            if user_allow_ask_discount is True:
                user_allow_ask_discount = 1
            elif user_allow_ask_discount is False:
                user_allow_ask_discount = 0
            if hide_favorites is True:
                hide_favorites = 1
            elif hide_favorites is False:
                hide_favorites = 0
            if vk_show_links is True:
                vk_show_links = 1
            elif vk_show_links is False:
                vk_show_links = 0
            if deauthorize_steam is True:
                deauthorize_steam = 1
            elif deauthorize_steam is False:
                deauthorize_steam = 0
            if hide_bids is True:
                hide_bids = 1
            elif hide_bids is False:
                hide_bids = 0
            params = {
                "disable_steam_guard": disable_steam_guard,
                "user_allow_ask_discount": user_allow_ask_discount,
                "max_discount_percent": max_discount_percent,
                "allow_accept_accounts": allow_accept_accounts,
                "hide_favourites": hide_favorites,
                "vk_ua": vk_ua,
                "show_account_links": vk_show_links,
                "market_custom_title": title,
                "deauthorize_steam": deauthorize_steam,
                "hide_bids": hide_bids,
            }
            if telegram_client:
                for key, value in telegram_client.items():
                    if key not in [
                        "telegram_api_id",
                        "telegram_api_hash",
                        "telegram_device_model",
                        "telegram_system_version",
                        "telegram_app_version",
                    ]:
                        raise Exceptions.UNEXPECTED_ARG(
                            f'Unknown param in telegram_client - "{key}"'
                        )
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/steam"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/steam/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/category_name/games

                Displays a list of games in the category.

                Required scopes: market

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/fortnite"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/mihoyo"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/mihoyo/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __Valorant:
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/valorant"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/valorant/params"
                return _send_request(self=self._api, method="GET", path=path)

        class __LeagueOfLegends:
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/league-of-legends"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/league-of-legends/params"
                return _send_request(self=self._api, method="GET", path=path)

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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/telegram"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/supercell"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/origin"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/origin/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/category_name/games

                Displays a list of games in the category.

                Required scopes: market

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/world-of-tanks"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/wot-blitz"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/wot-blitz/params"
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/epicgames"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/epicgames/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/category_name/games

                Displays a list of games in the category.

                Required scopes: market

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/escape-from-tarkov"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/socialclub"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/socialclub/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/category_name/games

                Displays a list of games in the category.

                Required scopes: market

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/uplay"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/uplay/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/category_name/games

                Displays a list of games in the category.

                Required scopes: market

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/war-thunder"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/discord"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/tiktok"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/instagram"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/battlenet"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/battlenet/params"
                return _send_request(self=self._api, method="GET", path=path)

            @_MainTweaks._CheckScopes(scopes=["market"])
            def games(self) -> httpx.Response:
                """
                GET https://api.lzt.market/category_name/games

                Displays a list of games in the category.

                Required scopes: market

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/vpn"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/cinema"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/cinema/params"
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/spotify"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
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
                order_by: str = None,
                sold_before: bool = None,
                sold_before_by_me: bool = None,
                not_sold_before: bool = None,
                not_sold_before_by_me: bool = None,
                search_params: dict = None,
                **kwargs,
            ) -> httpx.Response:
                """
                GET https://api.lzt.market/categoryName

                Displays a list of accounts in a specific category according to your parameters.

                Required scopes: market

                :param page: The number of the page to display results from
                :param auction: Auction. Can be [yes, no, nomatter].
                :param title: The word or words contained in the account title
                :param pmin: Minimal price of account (Inclusive)
                :param pmax: Maximum price of account (Inclusive)
                :param origin: List of account origins.
                :param not_origin: List of account origins that won't be included.
                :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
                :param sold_before: Sold before.
                :param sold_before_by_me: Sold before by me.
                :param not_sold_before: Not sold before.
                :param not_sold_before_by_me: Not sold before by me.
                :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

                :return: httpx Response object
                """
                path = "/warface"
                if True:  # Tweak market
                    auction = _MainTweaks.market_variable_fix(auction)
                params = {
                    "page": page,
                    "auction": auction,
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
                if search_params is not None:
                    for key, value in search_params.items():
                        params[str(key)] = value
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

                Displays search parameters for a category.

                :return: httpx Response object
                """
                path = "/warface/params"
                return _send_request(self=self._api, method="GET", path=path)

        def __init__(self, _api_self):
            self._api = _api_self
            self.steam = self.__Steam(_api_self)
            self.fortnite = self.__Fortnite(_api_self)
            self.mihoyo = self.__MiHoYo(_api_self)
            self.valorant = self.__Valorant(_api_self)
            self.lol = self.__LeagueOfLegends(_api_self)
            self.telegram = self.__Telegram(_api_self)
            self.supercell = self.__Supercell(_api_self)
            self.origin = self.__Origin(_api_self)
            self.wot = self.__WorldOfTanks(_api_self)
            self.wot_blitz = self.__WorldOfTanksBlitz(_api_self)
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

        @_MainTweaks._CheckScopes(scopes=["market"])
        def get(
            self,
            category_name: str,
            page: int = None,
            auction: str = None,
            title: str = None,
            pmin: int = None,
            pmax: int = None,
            origin: Union[str, list] = None,
            not_origin: Union[str, list] = None,
            order_by: str = None,
            sold_before: bool = None,
            sold_before_by_me: bool = None,
            not_sold_before: bool = None,
            not_sold_before_by_me: bool = None,
            search_params: dict = None,
            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/categoryName

            Displays a list of accounts in a specific category according to your parameters.

            Required scopes: market

            :param page: The number of the page to display results from
            :param auction: Auction. Can be [yes, no, nomatter].
            :param title: The word or words contained in the account title
            :param pmin: Minimal price of account (Inclusive)
            :param pmax: Maximum price of account (Inclusive)
            :param origin: List of account origins.
            :param not_origin: List of account origins that won't be included.
            :param order_by: Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
            :param sold_before: Sold before.
            :param sold_before_by_me: Sold before by me.
            :param not_sold_before: Not sold before.
            :param not_sold_before_by_me: Not sold before by me.
            :param search_params: Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

            :return: httpx Response object
            """
            path = f"/{category_name}"
            if True:  # Tweak market
                auction = _MainTweaks.market_variable_fix(auction)
            params = {
                "page": page,
                "auction": auction,
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
            if search_params is not None:
                for key, value in search_params.items():
                    params[str(key)] = value
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

            Display category list.

            Required scopes: market

            :param top_queries: Display top queries for per category.

            :return: httpx Response object
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

            Required scopes: market

            :param url: Your market search url. It can be https://lzt.market/search_params or https://api.lzt.market/search_params

            :return: httpx Response object
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
            search_params: dict = None,
            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/

            Displays a list of the latest accounts.

            Required scopes: market

            :param page: The number of the page to display results from
            :param title: The word or words contained in the account title
            :param search_params: Search params for your request. Example {"category_id":19} will return only VPN accounts

            :return: httpx Response object

            """
            path = "/"
            params = {"page": page, "title": title}
            if search_params is not None:
                for key, value in search_params.items():
                    params[str(key)] = value
            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def owned(
            self,
            user_id: int = None,
            page: int = None,
            category_id: int = None,
            pmin: int = None,
            pmax: int = None,
            title: str = None,
            status: str = None,
            search_params: dict = None,
            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/user/user_id/items

            Displays a list of owned accounts.

            Category id-names list:

            1 - steam - Steam

            3 - origin - Origin

            4 - warface - Warface

            5 - uplay - Uplay

            7 - socialclub - Social Club

            9 - fortnite - Fortnite

            10 - instagram - Instagram

            11 - battlenet - Battle.net

            12 - epicgames - Epic Games

            13 - valorant - Valorant

            14 - world-of-tanks - World Of Tanks

            16 - wot-blitz - World Of Tanks Blitz

            15 - supercell - Supercell

            17 - genshin-impact - Genshin Impact

            18 - escape-from-tarkov - Escape From Tarkov

            19 - vpn - VPN

            20 - tiktok - TikTok

            22 - discord - Discord

            23 - cinema - Online Cinema

            24 - telegram - Telegram

            26 - spotify - Spotify

            27 - war-thunder - War Thunder

            Required scopes: market

            :param user_id: ID of user.
            :param page: Page
            :param category_id: Accounts category
            :param pmin: Minimal price of account (Inclusive)
            :param pmax: Maximum price of account (Inclusive)
            :param title: The word or words contained in the account title
            :param status: Account status. Can be [active, paid, deleted or awaiting].
            :param search_params: Search params for your request. Example {"category_id":19} will return only VPN accounts

            :return: httpx Response object
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
            if search_params is not None:
                for key, value in search_params.items():
                    params[str(key)] = value
            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def purchased(
            self,
            user_id: int = None,
            page: int = None,
            category_id: int = None,
            pmin: int = None,
            pmax: int = None,
            title: str = None,
            status: str = None,
            search_params: dict = None,
            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/user/user_id/orders

            Displays a list of purchased accounts.

            Category id-names list:

            1 - steam - Steam

            3 - origin - Origin

            4 - warface - Warface

            5 - uplay - Uplay

            7 - socialclub - Social Club

            9 - fortnite - Fortnite

            10 - instagram - Instagram

            11 - battlenet - Battle.net

            12 - epicgames - Epic Games

            13 - valorant - Valorant

            14 - world-of-tanks - World Of Tanks

            16 - wot-blitz - World Of Tanks Blitz

            15 - supercell - Supercell

            17 - genshin-impact - Genshin Impact

            18 - escape-from-tarkov - Escape From Tarkov

            19 - vpn - VPN

            20 - tiktok - TikTok

            22 - discord - Discord

            23 - cinema - Online Cinema

            24 - telegram - Telegram

            26 - spotify - Spotify

            27 - war-thunder - War Thunder

            Required scopes: market

            :param user_id: ID of user.
            :param page: Page
            :param category_id: Accounts category
            :param pmin: Minimal price of account (Inclusive)
            :param pmax: Maximum price of account (Inclusive)
            :param title: The word or words contained in the account title
            :param status: Account status. Can be [active, paid, deleted or awaiting].
            :param search_params: Search params for your request. Example {"category_id":19} will return only VPN accounts

            :return: httpx Response object

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
            if search_params is not None:
                for key, value in search_params.items():
                    params[str(key)] = value
            path = "/user/orders"
            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def favorite(
            self,
            page: int = None,
            status: str = None,
            title: str = None,
            search_params: dict = None,
            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/fave

            Displays a list of favourites accounts.

            Required scopes: market

            :param page: The number of the page to display results from
            :param status: Account status. Can be [active, paid, deleted or awaiting].
            :param search_params: Search params for your request. Example {"category_id":19} will return only VPN accounts
            :param title: The word or words contained in the account title

            :return: httpx Response object

            """
            path = "/fave"
            params = {"page": page, "show": status, "title": title}
            if search_params is not None:
                for key, value in search_params.items():
                    params[str(key)] = value
            if kwargs:
                for kwarg_name, kwarg_value in kwargs.items():
                    params[str(kwarg_name)] = kwarg_value
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def viewed(
            self,
            page: int = None,
            status: str = None,
            title: str = None,
            search_params: dict = None,
            **kwargs,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/viewed

            Displays a list of viewed accounts.

            Required scopes: market

            :param page: The number of the page to display results from
            :param status: Account status. Can be [active, paid, deleted or awaiting].
            :param search_params: Search params for your request. Example {"category_id":19} will return only VPN accounts
            :param title: The word or words contained in the account title

            :return: httpx Response object

            """
            path = "/viewed"
            params = {"page": page, "show": status, "title": title}
            if search_params is not None:
                for key, value in search_params.items():
                    params[str(key)] = value
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
            operation_type: str = None,
            pmin: int = None,
            pmax: int = None,
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
            GET https://api.lzt.market/user/user_id/payments

            Displays info about your profile.

            Required scopes: market

            :param user_id: ID of user.
            :param operation_type: Type of operation. Allowed operation types: income, cost, refilled_balance, withdrawal_balance, paid_item, sold_item, money_transfer, receiving_money, internal_purchase, claim_hold
            :param pmin: Minimal price of operation (Inclusive)
            :param pmax: Maximum price of operation (Inclusive)
            :param page: The number of the page to display results from
            :param operation_id_lt: ID of the operation from which the result begins
            :param receiver: Username of user, which receive money from you
            :param sender: Username of user, which sent money to you
            :param start_date: Start date of operation (RFC 3339 date format)
            :param end_date: End date of operation (RFC 3339 date format)
            :param wallet: Wallet, which used for money payots
            :param comment: Comment for money transfers
            :param is_hold: Display hold operations
            :param show_payments_stats: Display payment stats for selected period (outgoing value, incoming value)

            :return: httpx Response object

            """
            # Tweak 0
            if is_hold is True:
                is_hold = 1
            elif is_hold is False:
                is_hold = 0
            if show_payments_stats is True:
                show_payments_stats = 1
            elif show_payments_stats is False:
                show_payments_stats = 0
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
                "is_hold": is_hold,
                "show_payments_stats": show_payments_stats,
            }
            path = "/user/payments"
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def transfer(
            self,
            amount: int,
            secret_answer: str,
            currency: str = "rub",
            user_id: int = None,
            username: str = None,
            comment: str = None,
            transfer_hold: bool = None,
            hold_length_option: str = None,
            hold_length_value: int = None,
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/balance/transfer

            Send money to any user.

            Required scopes: market

            :param amount: Amount to send in your currency.
            :param secret_answer: Secret answer of your account
            :param currency: Using currency for amount. Allowed values: cny, usd, rub, eur, uah, kzt, byn, gbp ("rub" by default)
            :param user_id: User id of receiver. If user_id specified, username is not required.
            :param username: Username of receiver. If username specified, user_id is not required.
            :param comment: Transfer comment
            :param transfer_hold: Hold transfer or not
            :param hold_length_option: Hold length option. Allowed values: hour, day, week, month, year
            :param hold_length_value: Hold length value

            :return: httpx Response object
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

        @staticmethod
        def generate_link(
            amount: int,
            user_id: int = None,
            username: str = None,
            comment: str = None,
            redirect_url: str = None,
            currency: str = None,
            hold: bool = None,
            hold_length: int = None,
            hold_option: str = None,
        ) -> str:
            """
            Generate payment link

            Required scopes: None

            :param amount: Amount to send in your currency.
            :param user_id: ID of user to transfer money
            :param username: Username to transfer money
            :param comment: Payment comment.
            :param redirect_url: Redirect url. User who paid on this link will be redirected to this url
            :param currency: Using currency for amount. Allowed values: cny, usd, rub, eur, uah, kzt, byn, gbp
            :param hold: Hold transfer or not
            :param hold_length: Hold length ( max 1 month )
            :param hold_option: Hold option. Can be "hours","days","weeks","months"
            :return: string payment url
            """
            # Tweak 0
            if hold is True:
                hold = 1
            elif hold is False:
                hold = 0
            if hold:
                if hold_option in ["hour", "day", "week", "month"]:
                    hold_option += "s"
                if hold_option not in ["hours", "days", "weeks", "months"]:
                    raise Exception(
                        """Invalid hold_option. It can be only "hours","days","weeks" and "months" """
                    )
            params = {
                "user_id": user_id,
                "username": username,
                "amount": amount,
                "comment": comment,
                "redirect": redirect_url,
                "currency": currency,
                "hold": hold,
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

        class __Tag:
            def __init__(self, _api_self):
                self._api = _api_self

            @_MainTweaks._CheckScopes(scopes=["market"])
            def delete(self, item_id: int, tag_id: int) -> httpx.Response:
                """
                DELETE https://api.lzt.market/item_id/tag

                Deletes tag for the account.

                Required scopes: market

                :param item_id: ID of item.
                :param tag_id: Tag id. Tag list is available via api.market.profile.get()

                :return: httpx Response object
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
                POST https://api.lzt.market/item_id/tag

                Adds tag for the account.

                Required scopes: market

                :param item_id: ID of item.
                :param tag_id: Tag id. Tag list is available via api.market.profile.get()

                :return: httpx Response object
                """
                path = f"/{item_id}/tag"
                params = {"tag_id": tag_id}
                return _send_request(
                    self=self._api,
                    method="POST",
                    path=path,
                    params=params,
                )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def get(
            self,
            item_id: int,
            auction: bool = False,
            steam_preview: bool = False,
            preview_type: str = None,
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/item_id
            GET https://api.lzt.market/item_id/steam-preview
            GET https://api.lzt.market/item_id/auction

            Displays account information or returns Steam account html code.

            Required scopes: market

            :param item_id: ID of item.
            :param steam_preview: Set it True if you want to get steam html and False/None if you want to get account info
            :param preview_type: Type of page - profiles or games
            :return: httpx Response object

            """
            path = f"/{item_id}"
            if auction:
                path = f"/{item_id}/auction"
            elif steam_preview:
                path = f"/{item_id}/steam-preview"
            params = {"type": preview_type}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def delete(self, item_id: int, reason: str) -> httpx.Response:
            """
            DELETE https://api.lzt.market/item_id

            Deletes your account from public search. Deletetion type is soft. You can restore account after deletetion if you want.

            Required scopes: market

            :param item_id: ID of item.
            :param reason: Delete reason.

            :return: httpx Response object
            """
            path = f"/{item_id}"
            params = {"reason": reason}
            return _send_request(
                self=self._api, method="DELETE", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def email(self, item_id: int, email: str, login: str) -> httpx.Response:
            """
            GET https://api.lzt.market/email-code

            Gets confirmation code or link.

            Required scopes: market

            :param item_id: ID of item.
            :param email: Account email.

            :return: httpx Response object
            """
            path = "/email-code"
            params = {"email ": email, "login": login, "item_id": item_id}
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def guard(self, item_id: int) -> httpx.Response:
            """
            GET https://api.lzt.market/item_id/guard-code

            Gets confirmation code from MaFile (Only for Steam accounts).

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/guard-code"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def mafile(self, item_id: int) -> httpx.Response:
            """
            GET https://api.lzt.market/item_id/mafile

            Returns mafile in JSON.

            Warning: this action is cancelling active account guarantee.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/mafile"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def password_tm(self, item_id: int) -> httpx.Response:
            """
            GET https://api.lzt.market/item_id/temp-email-password

            Gets password from temp email of account.

            After calling of this method, the warranty will be cancelled, and you cannot automatically resell account.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/temp-email-password"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def refuse_guarantee(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/refuse-guarantee

            Cancel guarantee of account. It can be useful for account reselling.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/refuse-guarantee"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def change_password(self, item_id: int, _cancel: bool = None) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/change-password

            Changes password of account.

            Required scopes: market

            :param item_id: ID of item.
            :param _cancel: Cancel change password recommendation. It will be helpful, if you don't want to change password and get login data

            :return: httpx Response object
            """
            path = f"/{item_id}/change-password"
            # Tweak 0
            if _cancel is True:
                _cancel = 1
            elif _cancel is False:
                _cancel = 0
            params = {"_cancel": _cancel}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def unstick(self, item_id: int) -> httpx.Response:
            """
            DELETE https://api.lzt.market/item_id/stick

            Unstick account of the top of search.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/stick"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def stick(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/stick

            Stick account in the top of search.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/stick"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def unfavorite(self, item_id: int) -> httpx.Response:
            """
            DELETE https://api.lzt.market/item_id/star

            Deletes account from favourites.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/star"
            return _send_request(self=self._api, method="DELETE", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def favorite(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/star

            Adds account to favourites.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/star"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def bump(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/bump

            Bumps account in the search.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/bump"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def change_owner(
            self, item_id: int, username: str, secret_answer: str
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/change-owner

            Change of account owner.

            Required scopes: market

            :param item_id: ID of item.
            :param username: The username of the new account owner
            :param secret_answer: Secret answer of your account

            :return: httpx Response object
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
            price: int = None,
            currency: str = None,
            item_origin: str = None,
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
            PUT https://api.lzt.market/item_id/edit

            Edits any details of account.

            Account origin:

            brute - Account received using Bruteforce

            fishing - Account received from fishing page

            stealer - Account received from stealer logs

            autoreg - Account is automatically registered by a tool

            personal - Account is yours. You created it yourself

            resale - Account received from another seller

            retrive - Account is recovered by email or phone (only for VKontakte category)

            Required scopes: market
            :param item_id: ID of item
            :param price: Account price in your currency.
            :param currency: Using currency. Allowed values: cny, usd, rub, eur, uah, kzt, byn or gbp.
            :param item_origin: Account origin. Where did you get it from.
            :param title: Russian title of account. If title specified and title_en is empty, title_en will be automatically translated to English language.
            :param title_en: English title of account. If title_en specified and title is empty, title will be automatically translated to Russian language.
            :param description: Account public description.
            :param information: Account private information (visible for buyer only if purchased).
            :param email_login_data: Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
            :param email_type: Email type. Allowed values: native, autoreg.
            :param allow_ask_discount: Allow users to ask discount for this account.
            :param proxy_id: Using proxy id for account checking.

            :return: httpx Response object
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

        @_MainTweaks._CheckScopes(scopes=["market"])
        def telegram(self, item_id: int) -> httpx.Response:
            """
            GET https://api.lzt.market/item_id/telegram-login-code

            Gets confirmation code from Telegram.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/telegram-login-code"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def telegram_reset(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/telegram-reset-authorizations

            Resets Telegram authorizations.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/telegram-reset-authorizations"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def update_inventory(self, item_id: int, app_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/update-inventory

            Update inventory value.

            Required scopes: market

            :param item_id: ID of item.
            :param app_id: App id.

            :return: httpx Response object
            """
            params = {"app_id": app_id}
            path = f"/{item_id}/update-inventory"
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def steam_inventory_value(
            self, url: str, app_id: int, currency: str = None, ignore_cache: bool = None
        ) -> httpx.Response:
            """
            GET https://api.lzt.market/steam-value

            Gets steam value.

            Application id list:

            730 - CS2

            578080 - PUBG

            753 - Steam

            570 - Dota 2

            440 - Team Fortress 2

            252490 - Rust

            304930 - Unturned

            232090 - Killing Floor 2

            322330 - Don't Starve Together

            :param url: Link or id of account. Can be [https://lzt.market/{item-id}/, https://steamcommunity.com/id/{steam-name}, https://steamcommunity.com/profiles/{steam-id}, {steam-id}].
            :param app_id: Application id.
            :param currency: Using currency for amount.
            :param ignore_cache: Ignore cache.

            :return: httpx Response object
            """
            params = {
                "link": url,
                "app_id": app_id,
                "currency": currency,
                "ignore_cache": ignore_cache,
            }
            path = "/steam-value"
            return _send_request(self=self._api, method="GET", path=path, params=params)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def confirm_sda(
            self, item_id: int, id: int = None, nonce: int = None
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/confirm-sda

            Confirm steam action.

            Don't set id and nonce parameters to get list of available confirmation requests.

            Warning: this action is cancelling active account guarantee.

            :param item_id: Item id.
            :param id: Confirmation id. (Required along with nonce if you want to confirm action).
            :param nonce: Confirmation nonce. (Required along with id if you want to confirm action).

            :return: httpx Response object
            """
            params = {
                "id": id,
                "nonce": nonce,
            }
            path = f"/{item_id}/confirm-sda"
            return _send_request(
                self=self._api, method="POST", path=path, params=params
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
                self, item_id: int, amount: int, currency: str = None
            ) -> httpx.Response:
                """
                POST https://api.lzt.market/item_id/auction/bid

                Create a new auction bid.

                Required scopes: market

                :param item_id: ID of item.
                :param amount: Amount bid.
                :param currency: Using currency. Can be [rub, uah, kzt, byn, usd, eur, gbp, cny, try].

                :return: httpx Response object
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
                GET https://api.lzt.market/item_id/auction/bid

                Delete your auction bid.

                Required scopes: market

                :param item_id: ID of item.
                :param bid_id: ID of bid.

                :return: httpx Response object
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
        def reserve(self, item_id: int, price: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/reserve

            Reserves account for you. Reserve time - 300 seconds.

            Required scopes: market

            :param item_id: ID of item.
            :param price: Currenct price of account in your currency

            :return: httpx Response object
            """
            path = f"/{item_id}/reserve"
            params = {"price": price}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def reserve_cancel(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/cancel-reserve

            Cancels reserve.

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/cancel-reserve"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def check(self, item_id: int) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/check-account

            Checking account for validity. If the account is invalid, the purchase will be canceled automatically

            Required scopes: market

            :param item_id: ID of item.

            :return: httpx Response object
            """
            path = f"/{item_id}/check-account"
            return _send_request(self=self._api, method="POST", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def confirm(
            self, item_id: int, buy_without_validation: bool = None
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/confirm-buy

            Confirm buy.

            Required scopes: market

            :param item_id: ID of item.
            :param buy_without_validation: Use TRUE if you want to buy account without account data validation (not safe).

            :return: httpx Response object
            """
            path = f"/{item_id}/confirm-buy"
            # Tweak 0
            if buy_without_validation is True:
                buy_without_validation = 1
            elif buy_without_validation is False:
                buy_without_validation = 0
            params = {"buy_without_validation": buy_without_validation}
            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def fast_buy(
            self, item_id: int, price: int, buy_without_validation: bool = None
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/item_id/fast-buy

            Check and buy account.

            Required scopes: market

            :param item_id: ID of item.
            :param price: Current price of account in your currency
            :param buy_without_validation: Use TRUE if you want to buy account without account data validation (not safe).

            :return: httpx Response object
            """
            path = f"/{item_id}/fast-buy"
            if True:  # Tweak 0
                if buy_without_validation is True:
                    buy_without_validation = 1
                elif buy_without_validation is False:
                    buy_without_validation = 0
            params = {
                "price": price,
                "buy_without_validation": buy_without_validation,
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
            GET https://api.lzt.market/item_id/goods/add

            Get info about not published item. For categories, which required temporary email (Steam, Social Club), you will get temporary email in response.

            Required scopes: market

            :param item_id: ID of item.
            :param resell_item_id: Put item id, if you are trying to resell item. This is useful to pass temporary email from reselling item to new item. You will get same temporary email from reselling account.

            :return: httpx Response object
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
            POST https://api.lzt.market/item_id/goods/check

            Check account on validity. If account is valid, account will be published on the market.

            Required scopes: market
            :param item_id: ID for item.
            :param login: Account login (or email)
            :param password: Account password
            :param login_password: Account login data format login:password
            :param close_item: If True, the item will be closed item_state = closed
            :param extra: Extra params for account checking. E.g. you need to put cookies to extra[cookies] if you want to upload TikTok/Fortnite/Epic Games account
            :param resell_item_id: Put item id, if you are trying to resell item.
            :param random_proxy: Pass True, if you get captcha in previous response

            :return: httpx Response object
            """
            path = f"/{item_id}/goods/check"
            if True:  # Tweak 0
                if random_proxy is True:
                    random_proxy = 1
                elif random_proxy is False:
                    random_proxy = 0
                if close_item is True:
                    close_item = 1
                elif close_item is False:
                    close_item = 0
            params = {
                "login": login,
                "password": password,
                "login_password": login_password,
                "close_item": close_item,
                "resell_item_id": resell_item_id,
                "random_proxy": random_proxy,
            }
            data = {}
            if extra is not None:
                if "CREATE_JOB" in locals():
                    data["extra"] = extra  # Костыль CreateJob
                else:
                    for key, value in extra.items():
                        es = f"extra[{key}]"
                        data[es] = value
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
            category_id: int,
            price: int,
            currency: str,
            item_origin: str,
            extended_guarantee: int = None,
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
            auction_duration_option: str = None,
            instabuy_price: int = None,
            not_bids_action: str = None,
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/item/add

            Adds account on the market.

            Account origin:

            brute - Account received using Bruteforce

            fishing - Account received from fishing page

            stealer - Account received from stealer logs

            autoreg - Account is automatically registered by a tool

            personal - Account is yours. You created it yourself

            resale - Account received from another seller

            retrive - Account is recovered by email or phone (only for VKontakte category)

            Required email login data categories:

            9 - Fortnite

            12 - Epic games

            18 - Escape from Tarkov


            Required scopes: market
            :param category_id: Accounts category.
            :param price: Account price in your currency.
            :param currency: Using currency. Allowed values: cny, usd, rub, eur, uah, kzt, byn or gbp.
            :param item_origin: Account origin. Where did you get it from.
            :param extended_guarantee: Guarantee type. Allowed values: -1 -> 12 hours, 0 -> 24 hours, 1 -> 3 days.
            :param title: Russian title of account. If title specified and title_en is empty, title_en will be automatically translated to English language.
            :param title_en: English title of account. If title_en specified and title is empty, title will be automatically translated to Russian language.
            :param description: Account public description.
            :param information: Account private information (visible for buyer only if purchased).
            :param has_email_login_data: Required if a category is one of list of Required email login data categories.
            :param email_login_data: Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
            :param email_type: Email type. Allowed values: native, autoreg.
            :param allow_ask_discount: Allow users to ask discount for this account.
            :param proxy_id: Using proxy id for account checking.
            :param random_proxy: Pass True, if you get captcha in previous response
            :param auction: Pass True if you want to create auction
            :param auction_duration_value: Duration auction value.
            :param auction_duration_option: Duration auction option. Can be [minutes, hours, days].
            :param instabuy_price: The price for which you can instantly redeem your account.
            :param not_bids_action: If you set cancel, at the end of the auction with 0 bids, the account can be purchased at the price you specified as the minimum bid. Can be [close, cancel]

            :return: httpx Response object
            """
            path = "/item/add"
            if True:  # Tweak 0
                if random_proxy is True:
                    random_proxy = 1
                elif random_proxy is False:
                    random_proxy = 0
                if auction is True:
                    type_sell = "auction"
                else:
                    type_sell = "price"
            params = {
                "category_id": category_id,
                "type_sell": type_sell,
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
                "random_proxy": random_proxy,
            }
            if auction is True:
                params["duration_auction_value"] = auction_duration_value
                params["duration_auction_option"] = auction_duration_option
                params["instant_price"] = instabuy_price
                params["not_bids_action"] = not_bids_action

            return _send_request(
                self=self._api, method="POST", path=path, params=params
            )

        @_MainTweaks._CheckScopes(scopes=["market"])
        def fast_sell(
            self,
            category_id: int,
            price: int,
            currency: str,
            item_origin: str,
            extended_guarantee: int = None,
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
            auction_duration_option: str = None,
            instabuy_price: int = None,
            not_bids_action: str = None,
        ) -> httpx.Response:
            """
            POST https://api.lzt.market/item/fast-sell

            Adds and check account on validity. If account is valid, account will be published on the market.

            Account origin:

            brute - Account received using Bruteforce

            fishing - Account received from fishing page

            stealer - Account received from stealer logs

            autoreg - Account is automatically registered by a tool

            personal - Account is yours. You created it yourself

            resale - Account received from another seller

            retrive - Account is recovered by email or phone (only for VKontakte category)

            Required email login data categories:

            9 - Fortnite

            12 - Epic games

            18 - Escape from Tarkov


            Required scopes: market
            :param category_id: Accounts category.
            :param price: Account price in your currency.
            :param currency: Using currency. Allowed values: cny, usd, rub, eur, uah, kzt, byn or gbp.
            :param item_origin: Account origin. Where did you get it from.
            :param extended_guarantee: Guarantee type. Allowed values: -1 -> 12 hours, 0 -> 24 hours, 1 -> 3 days.
            :param title: Russian title of account. If title specified and title_en is empty, title_en will be automatically translated to English language.
            :param title_en: English title of account. If title_en specified and title is empty, title will be automatically translated to Russian language.
            :param description: Account public description.
            :param information: Account private information (visible for buyer only if purchased).
            :param has_email_login_data: Required if a category is one of list of Required email login data categories.
            :param email_login_data: Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
            :param email_type: Email type. Allowed values: native, autoreg.
            :param allow_ask_discount: Allow users to ask discount for this account.
            :param proxy_id: Using proxy id for account checking.
            :param random_proxy: Pass True, if you get captcha in previous response
            :param login: Account login (or email)
            :param password: Account password
            :param login_password: Account login data format login:password
            :param extra: Extra params for account checking. E.g. you need to put cookies to extra[cookies] if you want to upload TikTok/Fortnite/Epic Games account
            :param auction: Pass True if you want to create auction
            :param auction_duration_value: Duration auction value.
            :param auction_duration_option: Duration auction option. Can be [minutes, hours, days].
            :param instabuy_price: The price for which you can instantly redeem your account.
            :param not_bids_action: If you set cancel, at the end of the auction with 0 bids, the account can be purchased at the price you specified as the minimum bid. Can be [close, cancel]

            :return: httpx Response object
            """
            path = "/item/fast-sell"
            # Tweak 0
            if random_proxy is True:
                random_proxy = 1
            elif random_proxy is False:
                random_proxy = 0
            if auction is True:
                type_sell = "auction"
            else:
                type_sell = "price"
            params = {
                "category_id": category_id,
                "price": price,
                "type_sell": type_sell,
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
                "random_proxy": random_proxy,
                "login": login,
                "password": password,
                "login_password": login_password,
            }
            if auction is True:
                params["duration_auction_value"] = auction_duration_value
                params["duration_auction_option"] = auction_duration_option
                params["instant_price"] = instabuy_price
                params["not_bids_action"] = not_bids_action
            data = {}
            if extra is not None:
                if "CREATE_JOB" in locals():
                    data["extra"] = extra  # Костыль CreateJob
                else:
                    for key, value in extra.items():
                        es = f"extra[{key}]"
                        data[es] = value
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

            Gets your proxy list.

            Required scopes: market

            :return: httpx Response object
            """
            path = "/proxy"
            return _send_request(self=self._api, method="GET", path=path)

        @_MainTweaks._CheckScopes(scopes=["market"])
        def delete(
            self, proxy_id: int = None, delete_all: bool = None
        ) -> httpx.Response:
            """
            DELETE https://api.lzt.market/proxy

            Delete single or all proxies.

            Required scopes: market

            :param proxy_id: ID of an existing proxy
            :param delete_all: Use True if you want to delete all proxy

            :return: httpx Response object
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

            Add single proxy or proxy list.

            Required scopes: market

            :param proxy_ip: Proxy ip or host.
            :param proxy_port: Proxy port
            :param proxy_user: Proxy username
            :param proxy_pass: Proxy password
            :param proxy_row: Proxy list in String format ip:port:user:pass. Each proxy must be start with new line (use \n separator)

            :return: httpx Response object
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
        :param token: Your token. You can get in there -> https://zelenka.guru/account/antipublic or in antipublic app
        :param proxy_type: Your proxy type. You can use types ( Constants.Proxy.socks5 or socks4,https,http )
        :param proxy: Proxy string. Example -> ip:port or login:password@ip:port
        """
        self.base_url = "https://antipublic.one"
        self.debug = False
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
        self.custom_params = {}
        self.custom_body = {}
        self.custom_headers = {}
        self._main_headers = {}

        self.info = self.__Info(self)
        self.account = self.__Account(self)

    class __Info:
        def __init__(self, _api_self):
            self._api = _api_self

        def lines_count(self) -> httpx.Response:
            """
            GET https://antipublic.one/api/v2/countLines

            Get count of rows in the AntiPublic db

            :return: httpx Response object
            """

            path = "/api/v2/countLines"
            return _send_request(self=self._api, method="GET", path=path)

        def lines_count_plain(self) -> str:
            """
            GET https://antipublic.one/api/v2/countLinesPlain

            Get count of rows in the AntiPublic db (raw format)

            :return: str
            """

            path = "/api/v2/countLinesPlain"
            return _send_request(self=self._api, method="GET", path=path)

        def version(self) -> httpx.Response:
            """
            GET https://antipublic.one/api/v2/version

            Get current antipublic version, change log and download url

            :return: json {'filename': str, 'version': str, 'changeLog': str, 'url': str}
            """

            path = "/api/v2/version"
            return _send_request(self=self._api, method="GET", path=path)

    class __Account:
        def __init__(self, _api_self):
            self._api = _api_self

        def license(self) -> httpx.Response:
            """
            GET https://antipublic.one/api/v2/checkAccess

            Checks your license

            Token required

            :return: httpx Response object
            """
            path = "/api/v2/checkAccess"
            return _send_request(self=self._api, method="GET", path=path)

        def queries(self) -> httpx.Response:
            """
            GET https://antipublic.one/api/v2/availableQueries

            Get your available queries

            Token required

            :return: httpx Response object
            """
            path = "/api/v2/availableQueries"
            return _send_request(self=self._api, method="GET", path=path)

    def check(self, lines: list[str], insert: bool = None) -> httpx.Response:
        """
        POST https://antipublic.one/api/v2/checkLines

        Check your lines.

        Token required
        :param lines: Lines for check, email:password or login:password
        :param insert: Upload private rows to AntiPublic db

        :return: httpx Response object
        """
        params = {"lines": lines, "insert": insert}
        path = "/api/v2/checkLines"
        return _send_request(self=self, method="POST", path=path, params=params)

    def search(
        self, login: str = None, logins: list[str] = None, limit: int = None
    ) -> httpx.Response:
        """
        POST https://antipublic.one/api/v2/emailSearch
        POST https://antipublic.one/api/v2/emailPasswords

        Get passwords for login's/email's

        Token required

        :param login:
            Email or login for search.
        :param logins:
            Emails or logins for search.

            !!! You need Antupublic Plus subscription to use this param !!!
        :param limit: Result limit (per email).

        :return: httpx Response object
        """
        if logins:
            data = {"emails": logins, "limit": limit}
            path = "/api/v2/emailPasswords"
        elif login:
            data = {"email": login}
            path = "/api/v2/emailSearch"
        else:
            raise KeyError("You need to specify login or logins param")
        return _send_request(self=self, method="POST", path=path, data=data)

import requests
import time
import json


class Market:
    def __init__(self, t):
        self.t = t

    def test(self, params):
        print(self.t.headers)
        print(params)


class lolzteam_api(Market):
    def __init__(self, token: str, bypass_429: bool = True):
        """
        :param token: Your token. You can get in there -> https://zelenka.guru/account/api
        :param bypass_429: Bypass status code 429 by sleep
        """

        self.token = token
        self.bypass_429 = bypass_429
        self.auto_delay_time = time.time() - 3
        self.headers = {'Authorization': f"bearer {self.token}"}

        # child classes (method groups below)
        self.market = Market(self)

    def auto_delay(self):
        """
        Sleep for time difference between the last call and current call if it's less than 3 seconds
        """
        if self.bypass_429:
            current_time = time.time()
            time_diff = current_time - self.auto_delay_time
            if time_diff < 3.0:  # if difference between current and last call > 3 seconds we will sleep the rest of the time

                time.sleep(3.003-time_diff)

    # Start of categories methods
    def get_categories(self, parent_category_id: int = None, parent_forum_id: int = None, order: str = None):
        """
        GET https://api.zelenka.guru/categories

        List of all categories in the system.

        Required scopes: read

        :param parent_category_id: ID of parent category.
        :param parent_forum_id: ID of parent forum.
        :param order: Ordering of categories. Can be [natural, list]
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = "https://api.zelenka.guru/categories"
        params = {
            "parent_category_id": parent_category_id,
            "parent_forum_id": parent_forum_id,
            "order": order
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_category(self, category_id: int):
        """
        GET https://api.zelenka.guru/categories/{category_id}

        Detail information of a category.

        Required scopes: read

        :param category_id: ID of category we want to get
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/categories/{category_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # End of categories methods
    # Start of forums methods
    def get_forums(self, parent_category_id: int = None, parent_forum_id: int = None, order: str = None):
        """
        GET https://api.zelenka.guru/categories/forums

        List of all forums in the system.

        Required scopes: read

        :param parent_category_id: ID of parent category.
        :param parent_forum_id: ID of parent forum.
        :param order: Ordering of categories. Can be [natural, list]
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/categories/forums"
        params = {
            "parent_category_id": parent_category_id,
            "parent_forum_id": parent_forum_id,
            "order": order
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_forum(self, forum_id: int):
        """
        GET https://api.zelenka.guru/forums/{forum_id}

        Detail information of a forum.

        Required scopes: read

        :param forum_id: ID of forum we want to get
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/forums/{forum_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_forum_followers(self, forum_id: int):
        """
        GET https://api.zelenka.guru/forums/{forum_id}/followers

        List of a forum's followers. For privacy reason, only the current user will be included in the list (if the user follows the specified forum).

        Required scopes: read

        :param forum_id: ID of forum we want to get
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/forums/{forum_id}/followers"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def follow_forum(self, forum_id: int, post: bool = None, alert: bool = None, email: bool = None):
        """
        POST https://api.zelenka.guru/forums/{forum_id}/followers
        Follow a forum.

        Required scopes: post

        :param forum_id: ID of forum we want to get
        :param post: Whether to receive notification for post.
        :param alert: Whether to receive notification as alert.
        :param email: Whether to receive notification as email.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/forums/{forum_id}/followers"
        if True:  # Костыль, пока не пофиксят недочет #63
            if post:
                post = 1
            if alert:
                alert = 1
            if email:
                email = 1
        params = {
            "post": post,
            "alert": alert,
            "email": email
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def unfollow_forum(self, forum_id: int):
        """
        DELETE https://api.zelenka.guru/forums/{forum_id}/followers
        Unfollow a forum.

        Required scopes: post

        :param forum_id: ID of forum we want to get

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/forums/{forum_id}/followers"
        params = {
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_followed_forums(self, total: bool = None):
        """
        GET https://api.zelenka.guru/forums/followed

        List of followed forums by current user.

        Required scopes: read

        :param total: If included in the request, only the forum count is returned as forums_total.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/forums/followed"
        if True:  # Костыль, пока не пофиксят недочет #43
            if total:
                total = 1
            else:
                total = 0
        params = {
            "total": total
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # End of forums methods
    # Start of pages methods
    def get_pages(self, parent_page_id: int = None, order: str = None):
        """
        GET https://api.zelenka.guru/pages

        List of all pages in the system.

        Required scopes: read

        :param parent_page_id: ID of parent page. If exists, filter pages that are direct children of that page.
        :param order: Ordering of pages. Can be [natural, list]

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/pages"
        params = {
            "parent_page_id": parent_page_id,
            "order": order
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_page(self, page_id: int):
        """
        GET https://api.zelenka.guru/pages/{page_id}

        Detail information of a page.

        Required scopes: read

        :param page_id: ID of parent page. If exists, filter pages that are direct children of that page.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/pages/{page_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # End of pages methods
    # Start of navigation methods
    def get_navigation(self, parent: int = None):
        """
        GET https://api.zelenka.guru/navigation

        List of navigation elements within the system.

        Required scopes: read

        :param parent: ID of parent element. If exists, filter elements that are direct children of that element.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/navigation"
        params = {
            "parent": parent
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # End of navigation methods
    # Start of threads methods
    def get_threads(self, forum_id: int, thread_ids: str = None, creator_user_id: int = None, sticky: bool = None,
                    thread_prefix_id: int = None, thread_tag_id: int = None, page: int = None, limit: int = None,
                    order: str = None):
        """
        GET https://api.zelenka.guru/threads

        List of threads in a forum (with pagination).

        Required scopes: read

        :param forum_id: ID of the containing forum.
        :param thread_ids: ID's of needed threads (separated by comma). If this parameter is set, all other filtering parameters will be ignored.
        :param creator_user_id: Filter to get only threads created by the specified user.
        :param sticky: Filter to get only sticky <sticky=1> or non-sticky <sticky=0> threads. By default, all threads will be included and sticky ones will be at the top of the result on the first page. In mixed mode, sticky threads are not counted towards threads_total and does not affect pagination.
        :param thread_prefix_id: Filter to get only threads with the specified prefix.
        :param thread_tag_id: Filter to get only threads with the specified tag.
        :param page: Page number of threads.
        :param limit: Number of threads in a page.
        :param order: Can be [natural, thread_create_date, thread_create_date_reverse, thread_update_date, thread_update_date_reverse, thread_view_count, thread_view_count_reverse, thread_post_count, thread_post_count_reverse]
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads"
        if sticky:  # Костыль, пока не пофиксят недочет #43
            sticky = 1
        else:
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
            "order": order
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def create_thread(self, forum_id: int, thread_title: str, post_body: str, thread_prefix_id: int = None,
                      thread_tags: str = None):
        """
        POST https://api.zelenka.guru/threads

        Create a new thread.

        Required scopes: post

        :param forum_id: ID of the target forum.
        :param thread_title: Title of the new thread.
        :param post_body: Content of the new thread.
        :param thread_prefix_id: ID of a prefix for the new thread.
        :param thread_tags: Thread tags for the new thread.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads"
        params = {
            "forum_id": forum_id,
            "thread_title": thread_title,
            "post_body": post_body,
            "thread_prefix_id": thread_prefix_id,
            "thread_tags": thread_tags
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_thread(self, thread_id: int):
        """
        GET https://api.zelenka.guru/threads/{thread_id}

        Detail information of a thread.

        Required scopes: read

        :param thread_id: ID of thread.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/{thread_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def delete_thread(self, thread_id: int, reason: str = None):
        """
        DELETE https://api.zelenka.guru/threads/{thread_id}

        Delete a thread.
         
        Required scopes: post

        :param thread_id: ID of thread.
        :param reason: Reason of the thread removal.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/{thread_id}"
        params = {
            "reason": reason
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_thread_followers(self, thread_id: int):
        """
        GET https://api.zelenka.guru/threads/{thread_id}/followers

        List of a thread's followers. For privacy reason, only the current user will be included in the list.

        Required scopes: read

        :param thread_id: ID of thread.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/{thread_id}/followers"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def follow_thread(self, thread_id: int, email: bool = None):
        """
        POST https://api.zelenka.guru/threads/{thread_id}/followers

        Follow a thread.

        Required scopes: post

        :param thread_id: ID of thread.
        :param email: Whether to receive notification as email.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/{thread_id}/followers"
        if True:  # Костыль, пока не пофиксят недочет #63
            if email:
                email = 1
        params = {
            "email": email
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def unfollow_thread(self, thread_id: int):
        """
        DELETE https://api.zelenka.guru/threads/{thread_id}/followers

        Unfollow a thread.

        Required scopes: post

        :param thread_id: ID of thread.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/{thread_id}/followers"
        params = {
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_followed_threads(self, total: bool = None):
        """
        GET https://api.zelenka.guru/forums/followed

        List of followed forums by current user.

        Required scopes: read

        :param total: If included in the request, only the forum count is returned as forums_total.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/forums/followed"
        if True:  # Костыль, пока не пофиксят недочет #43
            if total:
                total = 1
            else:
                total = 0
        params = {
            "total": total
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_thread_navigation(self, thread_id: int):
        """
        GET https://api.zelenka.guru/threads/{thread_id}/navigaion

        List of navigation elements to reach the specified thread.

        Required scopes: read

        :param thread_id: ID of thread.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/{thread_id}/navigaion"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_thread_vote(self, thread_id: int):
        """
        GET https://api.zelenka.guru/threads/{thread_id}/pool

        Detail information of a poll.

        Required scopes: read

        :param thread_id: ID of thread.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/{thread_id}/pool"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def post_thread_vote(self, thread_id: int, response_id: int = None, response_ids: list[int] = None):
        """
        GET https://api.zelenka.guru/threads/{thread_id}/pool

        Vote on a thread poll.

        Required scopes: post

        :param thread_id: ID of thread.
        :param response_id: The id of the response to vote for. Can be skipped if response_ids set.
        :param response_ids: An array of ids of responses (if the poll allows multiple choices).

        :return: json server response
        """
        url = f"https://api.zelenka.guru/threads/{thread_id}/poll/votes"
        if type(response_ids) == list:
            for element in response_ids:
                if not isinstance(element, int):
                    raise TypeError("All response_ids need to be integer")
            if self.bypass_429:
                lolzteam_api.auto_delay(self)
            params = {
                "response_ids[]": response_ids
            }
            response = requests.post(url=url, params=params, headers=self.headers)
            self.auto_delay_time = time.time()
            response_json = response.json()
            return response_json
        else:
            if self.bypass_429:
                lolzteam_api.auto_delay(self)
            params = {
                "response_id": response_id
            }
            response = requests.post(url=url, params=params, headers=self.headers)
            self.auto_delay_time = time.time()
            response_json = response.json()
            return response_json

    def get_new_threads(self, forum_id: int = None, limit: int = None, data_limit: int = None):
        """
        GET https://api.zelenka.guru/threads/new

        List of unread threads (must be logged in).

        Required scopes: read

        :param forum_id: ID of the container forum to search for threads. Child forums of the specified forum will be included in the search.
        :param limit: Maximum number of result threads. The limit may get decreased if the value is too large (depending on the system configuration).
        :param data_limit: Number of thread data to be returned. Default value is 20.
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/new"
        params = {
            "forum_id": forum_id,
            "limit": limit,
            "data_limit": data_limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_recent_threads(self, days: int = None, forum_id: int = None, limit: int = None, data_limit: int = None):
        """
        GET https://api.zelenka.guru/threads/recent

        List of recent threads.

        Required scopes: read

        :param days: Maximum number of days to search for threads.
        :param forum_id: ID of the container forum to search for threads. Child forums of the specified forum will be included in the search.
        :param limit: Maximum number of result threads. The limit may get decreased if the value is too large (depending on the system configuration).
        :param data_limit: Number of thread data to be returned. Default value is 20.
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/recent"
        params = {
            "days": days,
            "forum_id": forum_id,
            "limit": limit,
            "data_limit": data_limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def bump_thread(self, thread_id: int):
        """
        POST https://api.zelenka.guru/threads/{thread_id}/bump

        Bump a thread.

        Required scopes: post

        :param thread_id: ID of thread.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/threads/{thread_id}/bump"
        params = {
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # End of threads methods
    # Start of posts methods
    def get_posts(self, thread_id: int, page_of_post_id: int = None, post_ids: str = None, page: int = None,
                  limit: int = None, order: int = None):
        """
        GET https://api.zelenka.guru/posts

        List of posts in a thread (with pagination).

        Required scopes: read

        :param thread_id: ID of the containing thread.
        :param page_of_post_id: ID of a post, posts that are in the same page with the specified post will be returned. thread_id may be skipped.
        :param post_ids: ID's of needed posts (separated by comma). If this parameter is set, all other filtering parameters will be ignored.
        :param page: Page number of posts.
        :param limit: Number of posts in a page. Default value depends on the system configuration.
        :param order: Ordering of posts. Can be [natural, natural_reverse, post_create_date, post_create_date_reverse].
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts"
        params = {
            "thread_id": thread_id,
            "page_of_post_id": page_of_post_id,
            "post_ids": post_ids,
            "page": page,
            "limit": limit,
            "order": order
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def create_post(self, post_body: str, thread_id: int = None, quote_post_id: int = None):
        """
        POST https://api.zelenka.guru/threads

        Create a new thread.

        Required scopes: post

        :param post_body: Content of the new post.
        :param thread_id: ID of the target thread.
        :param quote_post_id: ID of the quote post. It's possible to skip thread_id if this parameter is provided. An extra check is performed if both parameters exist and does not match.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts"
        params = {
            "post_body": post_body,
            "thread_id": thread_id,
            "quote_post_id": quote_post_id,

        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_post(self, post_id: int):
        """
        GET https://api.zelenka.guru/posts/post_id

        Detail information of a post.

        Required scopes: read

        :param post_id: ID of post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def edit_post(self, post_id: int, thread_title: str = None, thread_prefix_id: int = None, thread_tags: str = None,
                  thread_node_id: int = None, post_body: str = None):
        """
        PUT https://api.zelenka.guru/posts/post_id

        Edit a post.

        Required scopes: post

        :param post_id: ID of post.
        :param thread_title: New title of the thread (only used if the post is the first post in the thread and the authenticated user can edit thread).
        :param thread_prefix_id: New id of the thread's prefix (only used if the post is the first post in the thread and the authenticated user can edit thread).
        :param thread_tags: New tags of the thread (only used if the post is the first post in the thread and the authenticated user can edit thread tags).
        :param thread_node_id: Move thread to new forum if the post is first post and the authenticated user can move thread.
        :param post_body: New content of the post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}"
        params = {
            "thread_title": thread_title,
            "thread_prefix_id": thread_prefix_id,
            "thread_tags": thread_tags,
            "thread_node_id": thread_node_id,
            "post_body": post_body
        }
        response = requests.put(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def delete_post(self, post_id: int, reason: str = None):
        """
        DELETE https://api.zelenka.guru/posts/post_id

        Delete a post.

        Required scopes: post

        :param post_id: ID of post.
        :param reason: Reason of the post removal.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}"
        params = {
            "reason": reason
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_post_likes(self, post_id: int, page: int = None, limit: int = None):
        """
        GET https://api.zelenka.guru/posts/post_id/likes

        List of users who liked a post.

        Required scopes: read

        :param post_id: ID of post.
        :param page: Page number of users.
        :param limit: Number of users in a page. Default value depends on the system configuration.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}/likes"
        params = {
            "page": page,
            "limit": limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def like_post(self, post_id: int):
        """
        POST https://api.zelenka.guru/posts/post_id

        Like a post.

        Required scopes: post

        :param post_id: ID of post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}"
        params = {
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def unlike_post(self, post_id: int):
        """
        DELETE https://api.zelenka.guru/posts/post_id

        Unlike a post.

        Required scopes: post

        :param post_id: ID of post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}"
        params = {
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def report_post(self, post_id: int, message: str):
        """
        POST https://api.zelenka.guru/posts/post_id/report

        Report a post.

        Required scopes: post

        :param post_id: ID of post.
        :param message: Reason of the report.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}/report"
        params = {
            "message": message
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_post_comments(self, post_id: int, before: int = None):
        """
        GET https://api.zelenka.guru/posts/post_id/comments

        List of post comments in a thread (with pagination).

        Required scopes: read

        :param post_id: ID of post.
        :param before: The time in milliseconds (e.g. 1652177794083) before last comment date

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}/comments"
        params = {
            "before": before
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def create_post_comment(self, post_id: int, comment_body: str = None):
        """
        POST https://api.zelenka.guru/posts/post_id/comments

        Create a new post comment.

        Required scopes: post

        :param post_id: ID of post.
        :param comment_body: Content of the new post

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/posts/{post_id}/comments"
        params = {
            "comment_body": comment_body
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # End of posts methods
    # Start of tagging method
    def get_tags_popular(self):
        """
        GET https://api.zelenka.guru/tags

        List of popular tags (no pagination).

        Required scopes: get

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/tags"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_tags(self, page: int = None):
        """
        GET https://api.zelenka.guru/tags/list

        List of tags.

        Required scopes: post

        :param page: Page number of tags list.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/tags/list"
        params = {
            "page": page
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_tagged_content(self, tag_id: int, page: int = None, limit: int = None):
        """
        GET https://api.zelenka.guru/tags/tag_id

        List of tagged contents.

        Required scopes: read

        :param tag_id:
        :param page: Page number of tags list.
        :param limit:

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/tags/{tag_id}"
        params = {
            "page": page,
            "limit": limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def search_tags(self, tag: str):
        """
        GET https://api.zelenka.guru/tags/find

        Filtered list of tags.

        Required scopes: read

        :param tag: tag to filter. Tags start with the query will be returned.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/tags/find"
        params = {
            "tag": tag
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # End of tagging methods
    # Start of users methods
    def get_users(self, page: int = None, limit: int = None):
        """
        GET https://api.zelenka.guru/users

        List of users (with pagination).

        Required scopes: read

        :param page: Page number of users.
        :param limit: Number of users in a page.
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users"
        params = {
            "page": page,
            "limit": limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_user_fields(self):
        """
        GET https://api.zelenka.guru/users/fields

        List of user fields.

        Required scopes: read

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/fields"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def search_users(self, username: str = None, user_email: str = None, custom_fields: dict = None):
        """
        GET https://api.zelenka.guru/users/find

        List of users (with pagination).

        Required scopes: read / admincp

        :param username: Username to filter. Usernames start with the query will be returned.
        :param user_email: Email to filter. Requires admincp scope.
        :param custom_fields: Custom fields to filter. Example: {"telegram": "Telegram_Login"}

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/find"
        params = {
            "username": username,
            "user_email": user_email,
        }
        for key, value in custom_fields.items():
            cf = f"custom_fields[{key}]"
            params[cf] = value
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_user(self, user_id: int = None):
        """
        GET https://api.zelenka.guru/users/user_id

        Detail information of a user.

        Required scopes: read

        :param user_id: ID of user
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def edit_user(self, user_id: int, password: str = None, password_old: str = None, password_algo: str = None,
                  user_email: str = None, username: str = None, user_title: str = None, primary_group_id: int = None,
                  secondary_group_ids: list[int] = None, user_dob_day: int = None, user_dob_month: int = None,
                  user_dob_year: int = None, fields: dict = None):
        """
        PUT https://api.zelenka.guru/users/user_id

        Edit a user.

        Encryption:
        For sensitive information like password, encryption can be used to increase data security. For all encryption with key support, the client_secret will be used as the key. List of supported encryptions:
        aes128: AES 128-bit encryption (mode: ECB, padding: PKCS#7). Because of algorithm limitation, the binary md5 hash of key will be used instead of the key itself.

        Required scopes: read / admincp

        :param user_id: ID of user
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

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}"
        params = {
            "password": password,
            "password_old": password_old,
            "password_algo": password_algo,
            "user_email": user_email,
            "username": username,
            "user_title": user_title,
            "primary_group_id": primary_group_id,
            "secondary_group_ids[]": secondary_group_ids,
            "user_dob_day": user_dob_day,
            "user_dob_month": user_dob_month,
            "user_dob_year": user_dob_year,
        }
        for key, value in fields.items():
            field = f"fields[{key}]"
            params[field] = value
        response = requests.put(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def upload_avatar(self, user_id: int, avatar: bytes):
        """
        POST https://api.zelenka.guru/users/user_id/avatar

        Upload avatar for a user.

        Required scopes: post / admincp

        :param user_id: ID of user
        :param avatar: Binary data of the avatar.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/avatar"
        params = {
        }
        files = {
            "avatar": avatar
        }
        response = requests.post(url=url, params=params, files=files, headers=self.headers)
        self.auto_delay_time = time.time()
        print(response.text)
        response_json = response.json()
        return response_json

    def delete_avatar(self, user_id: int):
        """
        DELETE https://api.zelenka.guru/users/user_id/avatar

        Delete avatar for a user.

        Required scopes: post / admincp

        :param user_id: ID of user

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/avatar"
        params = {
        }

        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        print(response.text)
        response_json = response.json()
        return response_json

    def get_user_followers(self, user_id: int, order: str = None, page: int = None, limit: int = None):
        """
        GET https://api.zelenka.guru/users/user_id/followers

        List of users (with pagination).

        Required scopes: read

        :param user_id: ID of user
        :param order: Ordering of followers. Support: natural, follow_date, follow_date_reverse
        :param page: Page number of followers.
        :param limit: Number of followers in a page.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/followers"
        params = {
            "order": order,
            "page": page,
            "limit": limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def follow_user(self, user_id: int):
        """
        POST https://api.zelenka.guru/users/user_id/followers

        Follow a user.

        Required scopes: post

        :param user_id: ID of user

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/followers"
        params = {
        }

        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        print(response.text)
        response_json = response.json()
        return response_json

    def unfollow_user(self, user_id: int):
        """
        DELETE https://api.zelenka.guru/users/user_id/followers

        Unfollow a user.

        Required scopes: post

        :param user_id: ID of user

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/followers"
        params = {
        }

        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        print(response.text)
        response_json = response.json()
        return response_json

    def get_user_followings(self, user_id: int, order: str = None, page: int = None, limit: int = None):
        """
        GET https://api.zelenka.guru/users/user_id/followings

        List of users whom are followed by a user.

        Required scopes: read

        :param user_id: ID of user
        :param order: Ordering of users. Support: natural, follow_date, follow_date_reverse
        :param page: Page number of users.
        :param limit: Number of users in a page.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/followings"
        params = {
            "order": order,
            "page": page,
            "limit": limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_ignored_users(self, total: bool = None):
        """
        GET https://api.zelenka.guru/users/ignored

        List of ignored users of current user.

        Required scopes: read

        :param total: If included in the request, only the user count is returned as users_total.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/ignored"
        if True:  # Костыль, пока не пофиксят недочет #43
            if total:
                total = 1
            else:
                total = 0
        params = {
            "total": total
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def ignore_user(self, user_id: int):
        """
        POST https://api.zelenka.guru/users/user_id/ignore

        Ignore a user.

        Required scopes: post

        :param user_id: ID of user

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/ignore"
        params = {
        }

        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        print(response.text)
        response_json = response.json()
        return response_json

    def unignore_user(self, user_id: int):
        """
        DELETE https://api.zelenka.guru/users/user_id/ignore

        Ignore a user.

        Required scopes: post

        :param user_id: ID of user

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/ignore"
        params = {
        }

        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        print(response.text)
        response_json = response.json()
        return response_json

    def get_user_groups(self, user_id: int = None):
        """
        GET https://api.zelenka.guru/users/user_id/groups

        List of a user's groups.

        Required scopes: read / admincp

        :param user_id: ID of user

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        if type(user_id) is None:
            url = f"https://api.zelenka.guru/users/groups"
        else:
            url = f"https://api.zelenka.guru/users/{user_id}/groups"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # End of users methods
    # Start of profile posts methods
    def get_user_contents(self, user_id: int, page: int = None, limit: int = None):
        """
        GET https://api.zelenka.guru/users/user_id/timeline

        List of contents created by user (with pagination).

        Required scopes: read

        :param user_id: ID of user
        :param page: Page number of contents.
        :param limit: Number of contents in a page.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/timeline"
        params = {
            "page": page,
            "limit": limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def create_profile_post(self, user_id: int, post_body: str):
        """
        POST https://api.zelenka.guru/users/user_id/timeline

        Create a new profile post on a user timeline.

        Required scopes: post

        :param user_id: ID of user
        :param post_body: Content of the new profile post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/users/{user_id}/timeline"
        params = {
            "post_body": post_body
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_profile_post(self, profile_post_id: int):
        """
        GET https://api.zelenka.guru/profile-posts/profile_post_id

        Detail information of a profile post.

        Required scopes: read

        :param profile_post_id: ID of profile post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def edit_profile_post(self, profile_post_id: int, post_body: str):
        """
        PUT https://api.zelenka.guru/profile-posts/profile_post_id

        Edit a profile post.

        Required scopes: post

        :param profile_post_id: ID of profile post.
        :param post_body: New content of the profile post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}"
        params = {
            "post_body": post_body
        }
        response = requests.put(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def delete_profile_post(self, profile_post_id: int, reason: str = None):
        """
        DELETE https://api.zelenka.guru/profile-posts/profile_post_id

        Delete a profile post.

        Required scopes: post

        :param profile_post_id: ID of profile post.
        :param reason: Reason of the profile post removal.


        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}"
        params = {
            "reason": reason
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_profile_post_likes(self, profile_post_id: int):
        """
        GET https://api.zelenka.guru/profile-posts/profile_post_id/likes

        List of users who liked a profile post.

        Required scopes: read

        :param profile_post_id: ID of profile post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}/likes"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def like_profile_post(self, profile_post_id: int):
        """
        POST https://api.zelenka.guru/profile-posts/profile_post_id/likes

        Like a profile post.

        Required scopes: post

        :param profile_post_id: ID of profile post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}/likes"
        params = {
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def unlike_profile_post(self, profile_post_id: int):
        """
        DELETE https://api.zelenka.guru/profile-posts/profile_post_id/likes

        Unlike a profile post.

        Required scopes: post

        :param profile_post_id: ID of profile post.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}/likes"
        params = {
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def report_profile_post(self, profile_post_id: int, message: str):
        """
        POST https://api.zelenka.guru/profile-posts/profile_post_id

        Report a profile post.

        Required scopes: post

        :param profile_post_id: ID of profile post.
        :param message: Reason of the report.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}"
        params = {
            "message": message
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # END of profile posts methods
    # Start of profile posts comments methods
    def get_profile_post_comments(self, profile_post_id: int, before: int = None, limit: int = None):
        """
        GET https://api.zelenka.guru/profile-posts/profile_post_id/comments

        List of comments of a profile post.

        Required scopes: read

        :param profile_post_id: ID of profile post.
        :param before: Date to get older comments. Please note that this entry point does not support the page parameter, but it still does support limit.
        :param limit: Number of profile posts in a page.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}/comments"
        params = {
            "before": before,
            "limit": limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def create_profile_post_comment(self, profile_post_id: int, comment_body: str):
        """
        POST https://api.zelenka.guru/profile-posts/profile_post_id/comments

        Create a new profile post comment.

        Required scopes: post

        :param profile_post_id: ID of profile post.
        :param comment_body: Content of the new profile post comment.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}/comments"
        params = {
            "comment_body": comment_body,
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_profile_post_comment(self, profile_post_id: int, comment_id: int):
        """
        GET https://api.zelenka.guru/profile-posts/profile_post_id/comments/comment_id

        Detail information of a profile post comment.

        Required scopes: read

        :param profile_post_id: ID of profile post.
        :param comment_id: ID of profile post comment

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}/comments/{comment_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def delete_profile_post_comment(self, profile_post_id: int, comment_id: int, reason: str = None):
        """
        DELETE https://api.zelenka.guru/profile-posts/profile_post_id/comments/comment_id

        Delete a profile post's comment.

        Required scopes: post

        :param profile_post_id: ID of profile post.
        :param comment_id: ID of profile post comment
        :param reason: Reason of the report.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/profile-posts/{profile_post_id}/comments/{comment_id}"
        params = {
            "reason": reason
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # END of profile posts comments methods
    # Start of Conversations methods
    def get_conversations(self, page: int = None, limit: int = None):
        """
        GET https://api.zelenka.guru/conversations

        List of conversations (with pagination).

        Required scopes: conversate, read

        :param page: Page number of conversations.
        :param limit: Number of conversations in a page.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversations"
        params = {
            "page": page,
            "limit": limit
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_conversation(self, conversation_id: int):
        """
        GET https://api.zelenka.guru/conversations/conversation_id

        Detail information of a conversation.

        Required scopes: conversate, read

        :param conversation_id: ID of conversation.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversations/{conversation_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def delete_conversation(self, conversation_id: int):
        """
        DELETE https://api.zelenka.guru/conversations/conversation_id

        Delete a conversation.

        Required scopes: conversate, post

        :param conversation_id: ID of conversation.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversations/{conversation_id}"
        params = {
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_conversation_messages(self, conversation_id: int, page: int = None, limit: int = None, order: str = None,
                                  before: int = None, after: int = None):
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

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversation-messages"
        params = {
            "conversation_id": conversation_id,
            "page": page,
            "limit": limit,
            "order": order,
            "before": before,
            "after": after
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def create_conversation_message(self, conversation_id: int, message_body: str):
        """
        POST https://api.zelenka.guru/conversation-messages

        Create a new conversation message.

        Required scopes: conversate, post

        :param conversation_id: ID of conversation.
        :param message_body: Content of the new message.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversation-messages"
        params = {
            "conversation_id": conversation_id,
            "message_body": message_body
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_conversation_message(self, message_id: int):
        """
        GET https://api.zelenka.guru/conversation-messages/message_id

        Detail information of a message.

        Required scopes: conversate, read

        :param message_id: ID of conversation message.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversation-messages/{message_id}"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def edit_conversation_message(self, message_id: int, message_body: str):
        """
        PUT https://api.zelenka.guru/conversation-messages/message_id

        Edit a message.

        Required scopes: conversate, post

        :param message_id: ID of conversation message.
        :param message_body: New content of the message.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversation-messages/{message_id}"
        params = {
            "message_body": message_body
        }
        response = requests.put(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def delete_conversation_message(self, message_id: int):
        """
        DELETE https://api.zelenka.guru/conversation-messages/message_id

        Delete a message.

        Required scopes: conversate, post

        :param message_id: ID of conversation message.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversation-messages/{message_id}"
        params = {
        }
        response = requests.delete(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def report_conversation_message(self, message_id: int, message: str = None):
        """
        POST https://api.zelenka.guru/conversation-messages/message_id/report

        Create a new conversation message.

        Required scopes: conversate, post

        :param message_id: ID of conversation message.
        :param message : Reason of the report.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/conversation-messages/{message_id}/report"
        params = {
            "message": message
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # END of Conversations  methods
    # Start of Notifications methods
    def get_notifications(self):
        """
        GET https://api.zelenka.guru/notifications

        List of notifications (both read and unread).

        Required scopes: read

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/notifications"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def get_notification(self, notification_id: int):
        """
        GET https://api.zelenka.guru/notifications

        Get associated content of notification. The response depends on the content type.

        Required scopes: read
        :param notification_id: ID of notification.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/notifications/{notification_id}/content"
        params = {
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def read_notification(self, notification_id: int = None):
        """
        POST https://api.zelenka.guru/notifications/read

        Mark single notification or all existing notifications read.

        Required scopes: post
        :param notification_id: ID of notification. If notification_id is omitted, it's mark all existing notifications as read.

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/notifications/read"
        params = {
            "notification_id": notification_id
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def send_custom_notification(self, user_id: int = None, username: str = None, message: str = None,
                                 message_html: str = None, notification_type: str = None, extra_data: str = None):
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

        :return: json server response
        """
        # По приколу добавил получается. Шанс того, что это заюзает реквест, томмас или григорий крайне мал
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/notifications/custom"
        params = {
            "user_id": user_id,
            "username": username,
            "message": message,
            "message_html": message_html,
            "notification_type": notification_type,
            "extra_data": extra_data
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # END of Notifications  methods
    # Start of Searching methods
    def search_thread(self, q: str = None, tag: str = None, forum_id: int = None, user_id: int = None, page: int = None,
                      limit: int = None, data_limit: int = None):
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

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/search/threads"
        params = {
            "q": q,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit,
            "data_limit": data_limit
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def search_post(self, q: str = None, tag: str = None, forum_id: int = None, user_id: int = None, page: int = None,
                    limit: int = None, data_limit: int = None):
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

        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/search/posts"
        params = {
            "q": q,
            "tag": tag,
            "forum_id": forum_id,
            "user_id": user_id,
            "page": page,
            "limit": limit,
            "data_limit": data_limit
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    def search_tagged(self, tag: str = None, tags: list[str] = None, page: int = None, limit: int = None):
        """
        POST https://api.zelenka.guru/search/tagged

        Search for tagged contents.

        Required scopes: post
        :param tag: Tag to search for tagged contents.
        :param tags: Array of tags to search for tagged contents.
        :param page: Page number of results.
        :param limit: Number of results in a page.
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/search/tagged"
        params = {
            "tag": tag,
            "tags[]": tags,
            "page": page,
            "limit": limit,
        }
        response = requests.post(url=url, params=params, headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json

    # END of Searching  methods
    # Start of Batch requests methods
    def batch(self, request_body: list[dict]):
        """
        POST https://api.zelenka.guru/batch

        Execute multiple API requests at once.(10 max)

        Example scheme:

        [
            {
            "id": "1",
            "uri": "https://api.zelenka.guru/users/2410024",
            "method": "GET",
            "params": {}
            }
        ]
        :param request_body: Use scheme above
        :return: json server response
        """
        lolzteam_api.auto_delay(self)
        url = f"https://api.zelenka.guru/batch"
        params = {
        }
        response = requests.post(url=url, params=params, data=json.dumps(request_body), headers=self.headers)
        self.auto_delay_time = time.time()
        response_json = response.json()
        return response_json
    # END of Batch requests  methods

<font size=6 style="margin: auto"> <center>

[Market docs](https://github.com/AS7RIDENIED/Lolzteam_Python_Api/blob/main/Documentation/Market.md) - [Antipublic Docs](https://github.com/AS7RIDENIED/Lolzteam_Python_Api/blob/main/Documentation/Antipublic.md)

</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

* [Threads](#threads)
  * [Contests](#contests)
    * [Create upgrade contest (time)](#create-upgrade-contest-time)
    * [Create upgrade contest (count)](#create-upgrade-contest-count)
    * [Create money contest (time)](#create-money-contest-time)
    * [Create money contest (count)](#create-money-contest-count)
  * [Get threads](#get-threads)
  * [Create thread](#create-thread)
  * [Get thread](#get-thread)
  * [Delete thread](#delete-thread)
  * [Get thread followers](#get-thread-followers)
  * [Get followed threads](#get-followed-threads)
  * [Follow thread](#follow-thread)
  * [Unfollow thread](#unfollow-thread)
  * [Get thread navigation](#get-thread-navigation)
  * [Get thread votes](#get-thread-votes)
  * [Thread vote](#thread-vote)
  * [Get new threads](#get-new-threads)
  * [Get recent threads](#get-recent-threads)
  * [Bump thread](#bump-thread)
* [Posts](#posts)
  * [Post comments](#post-comments)
    * [Get post comment](#get-post-comment)
    * [Create post comment](#create-post-comment)
  * [Get posts](#get-posts)
  * [Get post](#get-post)
  * [Create post](#create-post)
  * [Edit post](#edit-post)
  * [Delete post](#delete-post)
  * [Get post likes](#get-post-likes)
  * [Like post](#like-post)
  * [Unlike post](#unlike-post)
  * [Report post](#report-post)
* [Forums](#forums)
  * [Get forums](#get-forums)
  * [Get forum](#get-forum)
  * [Get forum followers](#get-forum-followers)
  * [Get followed forums](#get-followed-forums)
  * [Follow forum](#follow-forum)
  * [Unfollow forum](#unfollow-forum)
* [Users](#users)
  * [Avatar](#avatar)
    * [Upload avatar](#upload-avatar)
    * [Delete avatar](#delete-avatar)
  * [Get users](#get-users)
  * [Get user](#get-user)
  * [Edit user](#edit-user)
  * [Get user fields](#get-user-fields)
  * [Search users](#search-users)
  * [Lost password](#lost-password)
  * [Get user followings](#get-user-followings)
  * [Get user followers](#get-user-followers)
  * [Follow user](#follow-user)
  * [Unfollow user](#unfollow-user)
  * [Get ignored users](#get-ignored-users)
  * [Ignore user](#ignore-user)
  * [Unignore user](#unignore-user)
  * [Get user groups](#get-user-groups)
* [Profile posts](#profile-posts)
  * [Profile post comments](#profile-post-comments)
    * [Get profile post comments](#get-profile-post-comments)
    * [Get profile post comment](#get-profile-post-comment)
    * [Create profile post comment](#create-profile-post-comment)
    * [Delete profile post comment](#delete-profile-post-comment)
  * [Get profile post](#get-profile-post)
  * [Create profile post](#create-profile-post)
  * [Edit profile post](#edit-profile-post)
  * [Delete profile post](#delete-profile-post)
  * [Get profile post likes](#get-profile-post-likes)
  * [Like profile post](#like-profile-post)
  * [Unlike profile post](#unlike-profile-post)
  * [Report profile post](#report-profile-post)
* [Conversations](#conversations)
  * [Conversation messages](#conversation-messages)
    * [Get conversation messages](#get-conversation-messages)
    * [Get conversation message](#get-conversation-message)
    * [Send conversation message](#send-conversation-message)
    * [Edit conversation message](#edit-conversation-message)
    * [Delete conversation message](#delete-conversation-message)
    * [Report conversation message](#report-conversation-message)
  * [Get conversations](#get-conversations)
  * [Get conversation](#get-conversation)
  * [Create conversation](#create-conversation)
  * [Create group conversation](#create-group-conversation)
  * [Leave from conversation](#leave-from-conversation)
* [Notifications](#notifications)
  * [Get notifications](#get-notifications)
  * [Get notification](#get-notification)
  * [Read notification/s](#read-notifications)
  * [Send custom notification](#send-custom-notificaton)
* [Categories](#categories)
  * [Get categories](#get-categories)
  * [Get category](#get-category)
* [Pages](#pages)
  * [Get pages](#get-pages)
  * [Get page](#get-page)
* [Tags](#tags)
  * [Get popular tags](#get-popular-tags)
  * [Get tags](#get-tags)
  * [Tagged contents](#tagged-contents)
  * [Find tags](#find-tags)
* [Search](#search)
  * [Search for threads](#search-for-threads)
  * [Search for posts](#search-for-posts)
  * [Search for all types of content](#search-for-all-types-of-content)
  * [Search for tagged](#search-for-tagged)
  * [Search indexing](#search-indexing)
* [Oauth](#oauth)
  * [Facebook oauth](#facebook-oauth)
  * [Twitter oauth](#twitter-oauth)
  * [Google oauth](#google-oauth)
  * [Associate oauth](#associate-oauth)
  * [Admin oauth](#admin-oauth)
* [Navigation](#navigation)
* [Get batch job](#get-batch-job)
* [Batch](#batch)

</details>

# Quickstart

You need to create class instance to use library

```
from LolzteamApi import LolzteamApi
api = LolzteamApi(token="Your_token", language="en")
```

**Parameters:**

- **token** (str): Your token.
  > You can get in there -> https://zelenka.guru/account/api
- **bypass_429** (bool): Bypass status code 429 by sleep
  > It's True by default. You can skip it or set False if you want
- **language** (str): Language for your api responses. 
  > Pass "en" if you want to get responses in english or pass "ru" if you want to get responses in russian.
- **proxy_type** (str): Your proxy type. 
  > You can use types ( Types.Proxy.socks5 or socks4,https,http )
- **proxy** (str): Proxy string. 
  > Example -> ip:port or login:password@ip:port

# Threads

*Methods for getting, creating threads*

---

## Contests

*Methods for creating contests*

### Create upgrade contest (time)

*Create upgrade contest by time.*

**Parameters:**

- **thread_title** (str): Title of the new thread.
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
- **thread_prefix_id** (int): ID of a prefix for the new thread.
- **thread_tags** (str): Thread tags for the new thread.

**Example:**

```python
data = api.forum.threads.contests.upgrade.create_by_time(thread_title="Api example", post_body="Api example",
                                                         prize_data_upgrade=Types.Forum.Contests.Upgrade_prizes.uniq,
                                                         count_winners=1, length_value=3,
                                                         length_option=Types.Forum.Contests.Length.days,
                                                         require_like_count=1, require_total_like_count=1,
                                                         secret_answer="Secret answer")
print(data)
```

```python
{'thread': {'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create upgrade contest (count)

*Create upgrade contest by members count.*

**Parameters:**

- **thread_title** (str): Title of the new thread.
- **post_body** (str): Content of the new thread.
- **prize_data_upgrade** (int): Which upgrade will each winner receive.
- **count_winners** (int): Winner count (prize count).
  > The maximum value is 100.
- **needed_members** (int): Max member count.
- **require_like_count** (int): Sympathies for this week.
- **require_total_like_count** (int): Symapthies for all time.
- **secret_answer** (str): Secret answer of your account.
- **thread_prefix_id** (int): ID of a prefix for the new thread.
- **thread_tags** (str): Thread tags for the new thread.

**Example:**

```python
data = api.forum.threads.contests.upgrade.create_by_count(thread_title="Api example", post_body="Api example",
                                                          prize_data_upgrade=Types.Forum.Contests.Upgrade_prizes.uniq,
                                                          count_winners=1, needed_members=300, require_like_count=1,
                                                          require_total_like_count=1, secret_answer="Secret answer")
print(data)
```

```python
{'thread': {'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create money contest (time)

*Create money contest by time.*

**Parameters:**

- **thread_title** (str): Title of the new thread.
- **post_body** (str): Content of the new thread.
- **prize_data_money** (int): How much money will each winner receive.
- **count_winners** (int): Winner count (prize count). 
  > The maximum value is 100.
- **length_value** (int): Giveaway duration value.
  > The maximum duration is 3 days.
- **length_option** (str): Giveaway duration type. 
  > Can be [minutes, hours, days]. The maximum duration is 3 days.
- **require_like_count** (int): Sympathies for this week.
- **require_total_like_count** (int): Symapthies for all time.
- **secret_answer** (str): Secret answer of your account.
- **thread_prefix_id** (int): ID of a prefix for the new thread.
- **thread_tags** (str): Thread tags for the new thread.

**Example:**

```python
data = api.forum.threads.contests.money.create_by_time(thread_title="Api example", post_body="Api example",
                                                       prize_data_money=500,
                                                       count_winners=1, length_value=3,
                                                       length_option=Types.Forum.Contests.Length.days,
                                                       require_like_count=1, require_total_like_count=1,
                                                       secret_answer="Secret answer")
print(data)
```

```python
{'thread': {'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create money contest (count)

*Create money contest by members count.*

**Parameters:**

- **thread_title** (str): Title of the new thread.
- **post_body** (str): Content of the new thread.
- **prize_data_money** (int): How much money will each winner receive.
- **count_winners** (int): Winner count (prize count).
  > The maximum value is 100.
- **needed_members** (int): Max member count.
- **require_like_count** (int): Sympathies for this week.
- **require_total_like_count** (int): Symapthies for all time.
- **secret_answer** (str): Secret answer of your account.
- **thread_prefix_id** (int): ID of a prefix for the new thread.
- **thread_tags** (str): Thread tags for the new thread.

**Example:**

```python
data = api.forum.threads.contests.money.create_by_count(thread_title="Api example", post_body="Api example",
                                                        prize_data_money=500,
                                                        count_winners=1, needed_members=300, require_like_count=1,
                                                        require_total_like_count=1, secret_answer="Secret answer")
print(data)
```

```python
{'thread': {'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Get threads

*List of threads in a forum (with pagination).*

**Parameters:**

- **forum_id** (int): ID of the containing forum.
- **thread_ids** (str): ID's of needed threads (separated by comma).
  > If this parameter is set, all other filtering parameters will be ignored.
- **creator_user_id** (int): Filter to get only threads created by the specified user.
- **sticky** (bool): Filter to get only sticky <sticky=1> or non-sticky <sticky=0> threads. 
  > By default, all threads will be included and sticky ones will be at the top of the result on the first page. In mixed mode, sticky threads are not counted towards threads_total and does not affect pagination.
- **thread_prefix_id** (int): Filter to get only threads with the specified prefix.
- **thread_tag_id** (int): Filter to get only threads with the specified tag.
- **page** (int): Page number of threads.
- **limit** (int): Number of threads in a page.
- **order** (str): Threads sorting order.
  > Can be [natural, thread_create_date, thread_create_date_reverse, thread_update_date, thread_update_date_reverse, thread_view_count, thread_view_count_reverse, thread_post_count, thread_post_count_reverse]

**Example:**

```python
data = api.forum.threads.get_threads(forum_id=876)
print(data)
```

```python
{'threads': [{'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create thread

*Create a new thread.*

**Parameters:**

- **forum_id** (int): ID of the target forum.
- **thread_title** (str): Title of the new thread.
- **post_body** (str): Content of the new thread.
- **thread_prefix_id** (int): ID of a prefix for the new thread.
- **thread_tags** (str): Thread tags for the new thread.

**Example:**

```python
data = api.forum.threads.create(forum_id=876, thread_title="Api example", post_body="Api example", )
print(data)
```

```python
{'thread': {'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get thread

*Detail information of a thread.*

**Parameters:**

- **thread_id** (int): ID of thread.

**Example:**

```python
data = api.forum.threads.get(thread_id=5523020)
print(data)
```

```python
{'thread': {'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete thread

*Delete a thread.*

**Parameters:**

- **thread_id** (int): ID of thread.
- **reason** (str): Reason of the thread removal.

**Example:**

```python
data = api.forum.threads.delete(thread_id=5523020, reason="No reason :c")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Get thread followers

*List of a thread's followers. For privacy reason, only the current user will be included in the list.*

**Parameters:**

- **thread_id** (int): ID of thread.

**Example:**

```python
data = api.forum.threads.followers(thread_id=5523020)
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string', 'follow': {'alert': True, 'email': True}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get followed threads

*List of followed threads by current user.*

**Parameters:**

- **total** (bool): If included in the request, only the thread count is returned as threads_total.

**Example:**

```python
data = api.forum.threads.followed()
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Follow thread

*Follow a thread.*

**Parameters:**

- **thread_id** (int): ID of thread.
- **email** (bool): Whether to receive notification as email.

**Example:**

```python
data = api.forum.threads.follow(thread_id=5523020)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Unfollow thread

*Unfollow a thread.*

**Parameters:**

- **thread_id** (int): ID of thread.

**Example:**

```python
data = api.forum.threads.unfollow(thread_id=5523020)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Get thread navigation

*List of navigation elements to reach the specified thread.*

**Parameters:**

- **thread_id** (int): ID of thread.

**Example:**

```python
data = api.forum.threads.navigation(thread_id=5523020)
print(data)
```

```python
{'elements': [{'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'sub-elements': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'navigation_type': 'string', 'navigation_id': 0, 'navigation_depth': 0, 'navigation_parent_id': 0, 'has_sub_elements': True, 'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'forum_is_followed': True}], 'elements_count': 0, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get thread votes

*Detail information of a poll.*

**Parameters:**

- **thread_id** (int): ID of thread.

**Example:**

```python
data = api.forum.threads.votes(thread_id=5523020)
print(data)
```

```python
{'poll_id': 0, 'poll_question': 'string', 'poll_vote_count': 0, 'poll_is_open': True, 'poll_is_voted': True, 'poll_max_votes': 0, 'responses': [{'response_id': 0, 'response_answer': 'string', 'response_is_voted': True, 'response_vote_count': 0, 'voters': [{'user_id': 0, 'username': 'string'}]}], 'permissions': {'vote': True, 'result': True}, 'links': {'votes': 'string'}}
```

### Thread vote

*Vote on a thread poll.*

**Parameters:**

- **thread_id** (int): ID of thread.
- **response_id** (int): The id of the response to vote for. 
  > Can be skipped if response_ids set.
- **response_ids** (list[int]): An array of ids of responses (if the poll allows multiple choices).

**Example:**

```python
data = api.forum.threads.vote(thread_id=5523020, response_id=264758)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Get new threads

*List of unread threads (must be logged in).*

**Parameters:**

- **forum_id** (int): ID of the container forum to search for threads.
  > Child forums of the specified forum will be included in the search.
- **limit** (int): Maximum number of result threads. 
  > The limit may get decreased if the value is too large (depending on the system configuration).
- **data_limit** (int): Number of thread data to be returned. 
  > Default value is 20.

**Example:**

```python
data = api.forum.threads.new()
print(data)
```

```python
{'threads': [{'thread_id': 0}], 'data': [{'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get recent threads

*List of recent threads.*

**Parameters:**

- **days** (int): Maximum number of days to search for threads.
- **forum_id** (int): ID of the container forum to search for threads. 
  > Child forums of the specified forum will be included in the search.
- **limit** (int): Maximum number of result threads. 
  > The limit may get decreased if the value is too large (depending on the system configuration).
- **data_limit** (int): Number of thread data to be returned. 
  > Default value is 20.

**Example:**

```python
data = api.forum.threads.recent()
print(data)
```

```python
{'threads': [{'thread_id': 0}], 'data': [{'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Bump thread

*Bump a thread.*

**Parameters:**

- **thread_id** (int): ID of thread.

**Example:**

```python
data = api.forum.threads.bump(thread_id=5523020)
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Posts

*Methods for getting and creating posts*

---

## Post comments

*Methods for getting and creating post comments*

### Get post comment

*List of post comments in a thread (with pagination).*

**Parameters:**

- **post_id** (int): ID of post.
- **before** (int): The time in milliseconds (e.g. 1652177794083) before last comment date

**Example:**

```python
data = api.forum.posts.comments.get(post_id=39769208)
print(data)
```

```python
{'comments': {'111': {'post_comment_id': 0, 'post_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_comment_body': 'string', 'post_comment_body_html': 'string', 'post_comment_body_plain_text': 'string', 'post_comment_like_count': 0, 'user_is_ignored': True, 'post_comment_is_published': True, 'post_comment_is_deleted': True, 'post_comment_update_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'post': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True}}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create post comment

*Create a new post comment.*

**Parameters:**

- **post_id** (int): ID of post.
- **comment_body** (str): Content of the new post

**Example:**

```python
data = api.forum.posts.comments.create(post_id=39769208, comment_body="Api example")
print(data)
```

```python
{'comment': {'post_comment_id': 0, 'post_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_comment_body': 'string', 'post_comment_body_html': 'string', 'post_comment_body_plain_text': 'string', 'post_comment_like_count': 0, 'user_is_ignored': True, 'post_comment_is_published': True, 'post_comment_is_deleted': True, 'post_comment_update_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'post': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Get posts

*List of posts in a thread (with pagination).*

**Parameters:**

- **thread_id** (int): ID of the containing thread.
- **page_of_post_id** (int): ID of a post, posts that are in the same page with the specified post will be returned. 
  > thread_id may be skipped.
- **post_ids** (list): ID's of needed posts. 
  > If this parameter is set, all other filtering parameters will be ignored.
- **page** (int): Page number of posts.
- **limit** (int): Number of posts in a page.
  > Default value depends on the system configuration.
- **order** (int): Ordering of posts.
  > Can be [natural, natural_reverse, post_create_date, post_create_date_reverse].

**Example:**

```python
data = api.forum.posts.get_posts(thread_id=5523020)
print(data)
```

```python
{'posts': [{'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}], 'posts_total': 0, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get post

*Detail information of a post.*

**Parameters:**

- **post_id** (int): ID of post.

**Example:**

```python
data = api.forum.posts.get(post_id=39769208)
print(data)
```

```python
{'post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create post

*Create a new post.*

**Parameters:**

- **post_body** (str): Content of the new post.
- **thread_id** (int): ID of the target thread.
- **quote_post_id** (int): ID of the quote post. 
  > It's possible to skip thread_id if this parameter is provided. An extra check is performed if both parameters exist and does not match.

**Example:**

```python
data = api.forum.posts.create(thread_id=5523020, post_body="Good library, awesome author")
print(data)
```

```python
{'post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Edit post

*Edit a post.*

**Parameters:**

- **post_id** (int): ID of post.
- **thread_title** (str): New title of the thread (only used if the post is the first post in the thread and the authenticated user can edit thread).
- **thread_prefix_id** (int): New id of the thread's prefix (only used if the post is the first post in the thread and the authenticated user can edit thread).
- **thread_tags** (str): New tags of the thread (only used if the post is the first post in the thread and the authenticated user can edit thread tags).
- **thread_node_id** (int): Move thread to new forum if the post is first post and the authenticated user can move thread.
- **post_body** (str): New content of the post.

**Example:**

```python
data = api.forum.posts.edit(post_id=39769208,thread_title="Библиотека для упрощения работы с API | LolzteamApi Forum/Market/Antipublic Python")
print(data)
```

```python
{'post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete post

*Delete a post.*

**Parameters:**

- **post_id** (int): ID of post.
- **reason** (str): Reason of the post removal.

**Example:**

```python
data = api.forum.posts.delete(post_id=39769208, reason="No reason :c")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Get post likes

*List of users who liked a post.*

**Parameters:**

- **post_id** (int): ID of post.
- **page** (int): Page number of users.
- **limit** (int): Number of users in a page. 
  > Default value depends on the system configuration.

**Example:**

```python
data = api.forum.posts.likes(post_id=39769208, limit=10, page=2)
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string'}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Like post

*Like a post.*

**Parameters:**

- **post_id** (int): ID of post.

**Example:**

```python
data = api.forum.posts.like(post_id=39769208)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Unlike post

*Unlike a post.*

**Parameters:**

- **post_id** (int): ID of post.

**Example:**

```python
data = api.forum.posts.unlike(post_id=39769208)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Report post

*Report a post.*

**Parameters:**

- **post_id** (int): ID of post.
- **message** (str): Reason of the report.

**Example:**

```python
data = api.forum.posts.report(post_id=39769208, message="No report message :c")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

# Forums

*Methods for getting information about forums*

### Get forums

*List of all forums in the system.*

**Parameters:**

- **parent_category_id** (int): ID of parent category.
- **parent_forum_id** (int): ID of parent forum.
- **order** (str): Ordering of categories. 
  > Can be [natural, list]

**Example:**

```python
data = api.forum.forums.get_forums()
print(data)
```

```python
{'forums': [{'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}], 'forums_total': 0, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get forum

*Detail information of a forum.*

**Parameters:**

- **forum_id** (int): ID of forum.    

**Example:**

```python
data = api.forum.forums.get_forum(forum_id=969)
print(data)
```

```python
{'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get forum followers

*List of a forum's followers. For privacy reason, only the current user will be included in the list (if the user follows the specified forum).*

**Parameters:**

- **forum_id** (int): ID of forum.    

**Example:**

```python
data = api.forum.forums.followers(forum_id=969)
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string', 'follow': {'post': True, 'alert': True, 'email': True}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get followed forums

*List of followed forums by current user.*

**Parameters:**

- **total** (bool): If included in the request, only the forum count is returned as forums_total.

**Example:**

```python
data = api.forum.forums.followed(total=True)
print(data)
```

```python
{'forums': [{'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True, 'follow': {'post': True, 'alert': True, 'email': True}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```


### Follow forum

*Follow a forum.*

**Parameters:**

- **forum_id** (int): ID of forum we want to get
- **post** (bool): Whether to receive notification for post.
- **alert** (bool): Whether to receive notification as alert.
- **email** (bool): Whether to receive notification as email.

**Example:**

```python
data = api.forum.forums.follow(forum_id=969, post=True, alert=True)
print(data)
```

```python
{'status': 'ok', 'message': 'Изменения сохранены', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Unfollow forum

*Unfollow a forum.*

**Parameters:**

- **forum_id** (int): ID of forum.

**Example:**

```python
data = api.forum.forums.unfollow(forum_id=969)
print(data)
```

```python
{'status': 'ok', 'message': 'Изменения сохранены', 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Users

---

## Avatar

### Upload avatar

*Upload avatar for a user.*

**Parameters:**

- **avatar** (bytes): Binary data of the avatar.
- **user_id** (int): ID of user. If you do not specify the user_id, then you will change the avatar of the current user

**Example:**

```python
with open("avatar.png", 'rb') as f:
    avatar = f.read()
data = api.forum.users.avatar.upload(user_id=2410024, avatar=avatar)
print(data)
```

```python
{'status': 'ok', 'message': 'Upload completed successfully'}
```

### Delete avatar

*Delete avatar for a user.*

**Parameters:**

- **user_id** (int): ID of user. If you do not specify the user_id, then you will delete the avatar of the current user

**Example:**

```python
data = api.forum.users.avatar.delete(user_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

---

### Get users

*List of users (with pagination).*

**Parameters:**

- **page** (int): Page number of users.
- **limit** (int): Number of users in a page.

**Example:**

```python
data = api.forum.users.users(page=1)
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}], 'users_total': 0, 'links': {'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get user

*Detail information of a user.*

**Parameters:**

- **user_id** (int): ID of user. If you do not specify the user_id, you will get info about current user

**Example:**

```python
data = api.forum.users.get(user_id=2410024)
print(data)
```

```python
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Edit user

*Edit a user.*

**Parameters:**

- **user_id** (int): ID of user. If you do not specify the user_id, you will edit current user
- **password** (str): New password.
- **password_old** (str): Data of the existing password, it is not required if (1) the current authenticated user has user admin permission, (2) the admincp scope is granted and (3) the user being edited is not the current authenticated user.
- **password_algo** (str): Algorithm used to encrypt the password and password_old parameters.
- **user_email** (str): New email of the user.
- **username** (str): New username of the user. 
  > Changing username requires Administrator permission.
- **user_title** (str): New custom title of the user.
- **primary_group_id** (int): ID of new primary group.
- **secondary_group_ids** (list[int]): Array of ID's of new secondary groups.
- **user_dob_day** (int): Date of birth (day) of the new user.
- **user_dob_month** (int): Date of birth (month) of the new user.
- **user_dob_year** (int): Date of birth (year) of the new user.
- **fields** (dict): Array of values for user fields.

**Example:**

```python
data = api.forum.users.edit(user_id=2410024, user_title="LolzteamAPI python -> zelenka.guru/threads/5523020")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Get user fields

*List of user fields.*

**Example:**

```python
data = api.forum.users.fields()
print(data)
```

```python
{'fields': [{'id': 'string', 'title': 'string', 'description': 'string', 'position': 'string', 'is_required': True, 'is_multi_choice': True, 'choices': [{'key': 'string', 'value': 'string'}]}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Search users

*Filtered list of users by username, email or custom fields.*

**Parameters:**

- **username** (str): Username to filter. Usernames start with the query will be returned.
- **user_email** (str): Email to filter. Requires admincp scope.
- **custom_fields** (dict): Custom fields to filter. Example

**Example:**

```python
data = api.forum.users.search(username=2410024)
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Lost password

*Request a password reset via email. Either username or email parameter must be provided. If both are provided, username will be used.*

**Parameters:**

- **oauth_token** (str): A valid one time token.
- **username** (str): Username
- **email** (str): Email

**Example:**

```python
data = api.forum.users.lost_password(oauth_token=oauth, username="AS7RID")
print(data)
```

```python
{'status': 'ok', 'message': 'A password reset request has been emailed to you. Please follow the instructions in that email.'}
```

### Get user followings

*List of users whom are followed by a user.*

**Parameters:**

- **user_id** (int): ID of user. If you do not specify the user_id, you will get followings users by current user
- **order** (str): Ordering of users. Support
- **page** (int): Page number of users.
- **limit** (int): Number of users in a page.

**Example:**

```python
data = api.forum.users.followings(user_id=2410024)
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}], 'users_total': 0, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get user followers

*List of a user's followers.*

**Parameters:**

- **user_id** (int): ID of user.
  > If you do not specify the user_id, you will get followers of current user
- **order** (str): Ordering of followers. 
- **page** (int): Page number of followers.
- **limit** (int): Number of followers in a page.

**Example:**

```python
data = api.forum.users.followers(user_id=2410024)
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}], 'users_total': 0, 'links': {'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Follow user

*Follow a user.*

**Parameters:**

- **user_id** (int): ID of user

**Example:**

```python
data = api.forum.users.follow(user_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Unfollow user

*Unfollow a user.*

**Parameters:**

- **user_id** (int): ID of user

**Example:**

```python
data = api.forum.users.unfollow(user_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Get ignored users

*List of ignored users of current user.*

**Parameters:**

- **total** (bool): If included in the request, only the user count is returned as users_total.

**Example:**

```python
data = api.forum.users.ignored()
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string'}]}
```

### Ignore user

*Ignore a user.*

**Parameters:**

- **user_id** (int): ID of user

**Example:**

```python
data = api.forum.users.ignore(user_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Unignore user

*Unignore a user.*

**Parameters:**

- **user_id** (int): ID of user

**Example:**

```python
data = api.forum.users.unignore(user_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Get user groups

*List of a user's groups.*
  > You can get groups only for current user. 
  > 
  > If you want to get another user groups you need scope admincp
  >
  > You can get main user group with "[Get user](#get-user)" method

**Parameters:**

- **user_id** (int): ID of user. If user_id skipped, method will return current user groups

**Example:**

```python
data = api.forum.users.groups(user_id=2410024)
print(data)
```

```python
{'user_groups': [{'user_group_id': 0, 'user_group_title': 'string', 'is_primary_group': True}], 'user_id': 0}
```

# Profile posts

---

## Profile post comments

### Get profile post comments

*List of comments of a profile post.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.
- **before** (int): Date to get older comments. 
  > Please note that this entry point does not support the page parameter, but it still does support limit.
- **limit** (int): Number of profile posts in a page.

**Example:**

```python
data = api.forum.profile_posts.comments.comments(profile_post_id=3223590)
print(data)
```

```python
{'comments': [{'comment_id': 0, 'profile_post_id': 0, 'comment_user_id': 0, 'comment_username': 'string', 'comment_create_date': 0, 'comment_body': 'string', 'user_is_ignored': True, 'timeline_user_id': 0, 'links': {'detail': 'string', 'profile_post': 'string', 'timeline': 'string', 'timeline_user': 'string', 'poster': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'delete': True}}], 'comments_total': 0, 'profile_post': {'profile_post_id': 0, 'timeline_user_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_like_count': 0, 'post_comment_count': 0, 'timeline_username': 'string', 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'links': {'permalink': 'string', 'detail': 'string', 'timeline': 'string', 'timeline_user': 'string', 'poster': 'string', 'likes': 'string', 'comments': 'string', 'report': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'like': True, 'comment': True, 'report': True}}, 'timeline_user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get profile post comment

*Detail information of a profile post comment.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.
- **comment_id** (int): ID of profile post comment

**Example:**

```python
data = api.forum.profile_posts.comments.get(profile_post_id=3223590,comment_id=1780307)
print(data)
```

```python
{'comment': {'comment_id': 0, 'profile_post_id': 0, 'comment_user_id': 0, 'comment_username': 'string', 'comment_create_date': 0, 'comment_body': 'string', 'user_is_ignored': True, 'timeline_user_id': 0, 'links': {'detail': 'string', 'profile_post': 'string', 'timeline': 'string', 'timeline_user': 'string', 'poster': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create profile post comment

*Create a new profile post comment.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.
- **comment_body** (str): Content of the new profile post comment.

**Example:**

```python
data = api.forum.profile_posts.comments.create(profile_post_id=3223590,comment_body="Api example")
print(data)
```

```python
{'comment': {'comment_id': 0, 'profile_post_id': 0, 'comment_user_id': 0, 'comment_username': 'string', 'comment_create_date': 0, 'comment_body': 'string', 'user_is_ignored': True, 'timeline_user_id': 0, 'links': {'detail': 'string', 'profile_post': 'string', 'timeline': 'string', 'timeline_user': 'string', 'poster': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete profile post comment

*Delete a profile post's comment.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.
- **comment_id** (int): ID of profile post comment
- **reason** (str): Reason of the report.

**Example:**

```python
data = api.forum.profile_posts.comments.delete(profile_post_id=3223590,comment_id=1780307,reason="No reason:c")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

---

### Get profile post

*Detail information of a profile post.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.

**Example:**

```python
data = api.forum.profile_posts.get(profile_post_id=2667951)
print(data)
```

```python
{'profile_post': {'profile_post_id': 0, 'timeline_user_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_like_count': 0, 'post_comment_count': 0, 'timeline_username': 'string', 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'links': {'permalink': 'string', 'detail': 'string', 'timeline': 'string', 'timeline_user': 'string', 'poster': 'string', 'likes': 'string', 'comments': 'string', 'report': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'like': True, 'comment': True, 'report': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create profile post

*Create a new profile post on a user timeline.*

**Parameters:**

- **post_body** (str): Content of the new profile post.
- **user_id** (int): ID of user. If you do not specify the user_id, you will create profile post in current user's timeline

**Example:**

```python
data = api.forum.profile_posts.create(user_id=2410024,post_body="Api example")
print(data)
```

```python
{'data': {'content_type': 'string', 'content_id': 0, 'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}, 'thread': {'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'thread_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}], 'thread_tags': {'3': 'string', '49306': 'string'}, 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True}}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Edit profile post

*Edit a profile post.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.
- **post_body** (str): New content of the profile post.

**Example:**

```python
data = api.forum.profile_posts.edit(profile_post_id=2667951,post_body="Api example")
print(data)
```

```python
{'profile_post': {'profile_post_id': 0, 'timeline_user_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_like_count': 0, 'post_comment_count': 0, 'timeline_username': 'string', 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'links': {'permalink': 'string', 'detail': 'string', 'timeline': 'string', 'timeline_user': 'string', 'poster': 'string', 'likes': 'string', 'comments': 'string', 'report': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'like': True, 'comment': True, 'report': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete profile post

*Delete a profile post.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.
- **reason** (str): Reason of the profile post removal.

**Example:**

```python
data = api.forum.profile_posts.delete(profile_post_id=2667951,reason="No reason:c")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Get profile post likes

*List of users who liked a profile post.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.

**Example:**

```python
data = api.forum.profile_posts.likes(profile_post_id=2667951)
print(data)
```

```python
{'users': [{'user_id': 0, 'username': 'string'}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Like profile post

*Like a profile post.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.

**Example:**

```python
data = api.forum.profile_posts.like(profile_post_id=2667951)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Unlike profile post

*Unlike a profile post.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.

**Example:**

```python
data = api.forum.profile_posts.unlike(profile_post_id=2667951)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Report profile post

*Report a profile post.*

**Parameters:**

- **profile_post_id** (int): ID of profile post.
- **message** (str): Reason of the report.

**Example:**

```python
data = api.forum.profile_posts.report(profile_post_id=2667951, message="No reason:c")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

# Conversations

---

## Conversation messages

### Get conversation messages

*List of messages in a conversation (with pagination).*

**Parameters:**

- **conversation_id** (int): ID of conversation.
- **page** (int): Page number of messages.
- **limit** (int): Number of messages in a page.
- **order** (str): Ordering of messages. Can be [natural, natural_reverse].
- **before** (int): Date to get older messages.
- **after** (int): Date to get newer messages.

**Example:**

```python
data = api.forum.conversations.messages.get_all(conversation_id=17312)
print(data)
```

```python
{'message': {'message_id': 0, 'conversation_id': 0, 'creator_user_id': 0, 'creator_username': 'string', 'message_create_date': 0, 'message_body': 'string', 'message_body_html': 'string', 'message_body_plain_text': 'string', 'message_attachment_count': 0, 'user_is_ignored': True, 'links': {'detail': 'string', 'conversation': 'string', 'creator': 'string', 'creator_avatar': 'string', 'report': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'upload_attachment': True, 'report': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get conversation message

*Detail information of a message.*

**Parameters:**

- **message_id** (int): ID of conversation message.

**Example:**

```python
data = api.forum.conversations.messages.get(message_id=1731221)
print(data)
```

```python
{'message': {'message_id': 0, 'conversation_id': 0, 'creator_user_id': 0, 'creator_username': 'string', 'message_create_date': 0, 'message_body': 'string', 'message_body_html': 'string', 'message_body_plain_text': 'string', 'message_attachment_count': 0, 'user_is_ignored': True, 'links': {'detail': 'string', 'conversation': 'string', 'creator': 'string', 'creator_avatar': 'string', 'report': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'upload_attachment': True, 'report': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Send conversation message

*Create a new conversation message.*

**Parameters:**

- **conversation_id** (int): ID of conversation.
- **message_body** (str): Content of the new message.

**Example:**

```python
data = api.forum.conversations.messages.create(conversation_id=17312,message_body="Api example")
print(data)
```

```python
{'message': {'message_id': 0, 'conversation_id': 0, 'creator_user_id': 0, 'creator_username': 'string', 'message_create_date': 0, 'message_body': 'string', 'message_body_html': 'string', 'message_body_plain_text': 'string', 'message_attachment_count': 0, 'user_is_ignored': True, 'links': {'detail': 'string', 'conversation': 'string', 'creator': 'string', 'creator_avatar': 'string', 'report': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'upload_attachment': True, 'report': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Edit conversation message

*Edit a message.*

**Parameters:**

- **message_id** (int): ID of conversation message.
- **message_body** (str): New content of the message.

**Example:**

```python
data = api.forum.conversations.messages.edit(message_id=1731221, message_body="Api example1")
print(data)
```

```python
{'message': {'message_id': 0, 'conversation_id': 0, 'creator_user_id': 0, 'creator_username': 'string', 'message_create_date': 0, 'message_body': 'string', 'message_body_html': 'string', 'message_body_plain_text': 'string', 'message_attachment_count': 0, 'user_is_ignored': True, 'links': {'detail': 'string', 'conversation': 'string', 'creator': 'string', 'creator_avatar': 'string', 'report': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'upload_attachment': True, 'report': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete conversation message

*Delete a message.*

**Parameters:**

- **message_id** (int): ID of conversation message.

**Example:**

```python
data = api.forum.conversations.messages.delete(message_id=1731221)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Report conversation message

*Create a new conversation message.*

**Parameters:**

- **message_id** (int): ID of conversation message.
- **message** (str): Reason of the report.

**Example:**

```python
data = api.forum.conversations.messages.report(message_id=1731221,message="No reason:c")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

---

### Get conversations

*List of conversations (with pagination).*

**Parameters:**

- **page** (int): Page number of conversations.
- **limit** (int): Number of conversations in a page.

**Example:**

```python
data = api.forum.conversations.get_all()
print(data)
```

```python
{'conversations': [{'conversation_id': 0, 'conversation_title': 'string', 'creator_user_id': 0, 'creator_username': 'string', 'creator_username_html': 'string', 'conversation_create_date': 0, 'conversation_update_date': 0, 'is_starred': 0, 'is_group': 0, 'user_is_ignored': True, 'conversation_message_count': 0, 'conversation_has_new_message': True, 'links': {'permalink': 'string', 'detail': 'string', 'messages': 'string'}, 'permissions': {'reply': True, 'delete': True, 'upload_attachment': True}, 'first_message': {'message_id': 0, 'conversation_id': 0, 'creator_user_id': 0, 'creator_username': 'string', 'creator_username_html': 'string', 'message_create_date': 0, 'message_body': 'string', 'message_body_html': 'string', 'message_body_plain_text': 'string', 'message_attachment_count': 0, 'user_is_ignored': True, 'links': {'detail': 'string', 'conversation': 'string', 'creator': 'string', 'creator_avatar': 'string', 'report': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'upload_attachment': True, 'report': True}}, 'recipients': [{'user_id': 0, 'username': 'string', 'username_html': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'last_activity': 0, 'is_online': True}]}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get conversation

*Detail information of a conversation.*

**Parameters:**

- **conversation_id** (int): ID of conversation.

**Example:**

```python
data = api.forum.conversations.get(conversation_id=17312)
print(data)
```

```python
{'conversation': {'conversation_id': 0, 'conversation_title': 'string', 'creator_user_id': 0, 'creator_username': 'string', 'creator_username_html': 'string', 'conversation_create_date': 0, 'conversation_update_date': 0, 'is_starred': 0, 'is_group': 0, 'user_is_ignored': True, 'conversation_message_count': 0, 'conversation_has_new_message': True, 'links': {'permalink': 'string', 'detail': 'string', 'messages': 'string'}, 'permissions': {'reply': True, 'delete': True, 'upload_attachment': True}, 'first_message': {'message_id': 0, 'conversation_id': 0, 'creator_user_id': 0, 'creator_username': 'string', 'creator_username_html': 'string', 'message_create_date': 0, 'message_body': 'string', 'message_body_html': 'string', 'message_body_plain_text': 'string', 'message_attachment_count': 0, 'user_is_ignored': True, 'links': {'detail': 'string', 'conversation': 'string', 'creator': 'string', 'creator_avatar': 'string', 'report': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'upload_attachment': True, 'report': True}}, 'recipients': [{'user_id': 0, 'username': 'string', 'username_html': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'last_activity': 0, 'is_online': True}]}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create conversation

*Create a new conversation.*

**Parameters:**

- **recipient_id** (int): ID of recipient.
- **message** (str): First message in conversation.
- **open_invite** (bool): Allow invites in conversation.
- **conversation_locked** (bool): Is conversation locked.
- **allow_edit_messages** (bool): Allow edit messages.

**Example:**

```python
data = api.forum.conversations.create(recipient_id=2410024, message="Api example")
print(data)
```

```python
{'conversation': {'conversation_id': 0, 'conversation_title': 'string', 'creator_user_id': 0, 'creator_username': 'string', 'creator_username_html': 'string', 'conversation_create_date': 0, 'conversation_update_date': 0, 'is_starred': 0, 'is_group': 0, 'user_is_ignored': True, 'conversation_message_count': 0, 'conversation_has_new_message': True, 'links': {'permalink': 'string', 'detail': 'string', 'messages': 'string'}, 'permissions': {'reply': True, 'delete': True, 'upload_attachment': True}, 'first_message': {'message_id': 0, 'conversation_id': 0, 'creator_user_id': 0, 'creator_username': 'string', 'creator_username_html': 'string', 'message_create_date': 0, 'message_body': 'string', 'message_body_html': 'string', 'message_body_plain_text': 'string', 'message_attachment_count': 0, 'user_is_ignored': True, 'links': {'detail': 'string', 'conversation': 'string', 'creator': 'string', 'creator_avatar': 'string', 'report': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'upload_attachment': True, 'report': True}}, 'recipients': [{'user_id': 0, 'username': 'string', 'username_html': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'last_activity': 0, 'is_online': True}]}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Create group conversation

*Create a new group conversation.*

**Parameters:**

- **recipients** (str): List of usernames (Separated by comma. Example -> "RaysMorgan,Thomas,Requeste")
- **title** (str): The title of new conversation.
- **message** (str): First message in conversation.
- **open_invite** (bool): Allow invites in conversation.
- **conversation_locked** (bool): Is conversation locked.
- **allow_edit_messages** (bool): Allow edit messages.

**Example:**

```python
data = api.forum.conversations.create_group(recipients="AS7RID", message="Api example")
print(data)
```

```python
{'conversation': {'conversation_id': 0, 'conversation_title': 'string', 'creator_user_id': 0, 'creator_username': 'string', 'creator_username_html': 'string', 'conversation_create_date': 0, 'conversation_update_date': 0, 'is_starred': 0, 'is_group': 0, 'user_is_ignored': True, 'conversation_message_count': 0, 'conversation_has_new_message': True, 'links': {'permalink': 'string', 'detail': 'string', 'messages': 'string'}, 'permissions': {'reply': True, 'delete': True, 'upload_attachment': True}, 'first_message': {'message_id': 0, 'conversation_id': 0, 'creator_user_id': 0, 'creator_username': 'string', 'creator_username_html': 'string', 'message_create_date': 0, 'message_body': 'string', 'message_body_html': 'string', 'message_body_plain_text': 'string', 'message_attachment_count': 0, 'user_is_ignored': True, 'links': {'detail': 'string', 'conversation': 'string', 'creator': 'string', 'creator_avatar': 'string', 'report': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'upload_attachment': True, 'report': True}}, 'recipients': [{'user_id': 0, 'username': 'string', 'username_html': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'last_activity': 0, 'is_online': True}]}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Leave from conversation

*Leave from conversation*

**Parameters:**

- **conversation_id** (int): ID of conversation.

**Example:**

```python
data = api.forum.conversations.leave(conversation_id=17312)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

# Notifications

### Get notifications

*List of notifications (both read and unread).*

**Example:**

```python
data = api.forum.notifications.get_all()
print(data)
```

```python
{'notifications': [{'notification_id': 0, 'notification_create_date': 0, 'content_type': 'string', 'content_id': 0, 'content_action': 'string', 'notification_is_unread': True, 'creator_user_id': 0, 'creator_username': 'string', 'notification_type': 'string', 'links': {'content': 'string', 'creator_avatar': 'string'}, 'notification_html': 'string'}], 'notifications_total': 0, 'links': {'read': 'string', 'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get notification

*Get associated content of notification. The response depends on the content type.*

**Parameters:**

- **notification_id** (int): ID of notification.

**Example:**

```python
data = api.forum.notifications.get(notification_id=1590600042)
print(data)
```

```python
{'notification': {'notification_id': 0, 'notification_create_date': 0, 'content_type': 'string', 'content_id': 0, 'content_action': 'string', 'notification_is_unread': True, 'creator_user_id': 0, 'creator_username': 'string', 'notification_type': 'string', 'links': {'content': 'string', 'creator_avatar': 'string'}, 'notification_html': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Read notification/s

*Mark single notification or all existing notifications read.*

**Parameters:**

- **notification_id** (int): ID of notification. If notification_id is omitted, it's mark all existing notifications as read.

**Example:**

```python
data = api.forum.notifications.read(notification_id=1590600042)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Send custom notificaton

*Send a custom alert.*
  > The current user must have the [bd] API: Send custom alert permission
  > 
  > You can't use that method :c

**Parameters:**

- **user_id** (int): The alert receiver.
- **username** (str): The alert receiver.
- **message** (str): The alert message.
- **message_html** (str): The alert message.
- **notification_type** (str): The notification type.
- **extra_data** (str): Extra data when sending alert. Предположительно это словарик, но я не уверен

**Example:**

```python
data = api.forum.notifications.custom(user_id=1, message="Hello grisha", notification_type="user")
print(data)
```

```python
string
```

# Categories

### Get categories

*List of all categories in the system.*

**Parameters:**

- **parent_category_id** (int): ID of parent category.
- **parent_forum_id** (int): ID of parent forum.
- **order** (str): Ordering of categories.

**Example:**

```python
data = api.forum.categories.get_categories()
print(data)
```

```python
{'categories': [{'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}], 'categories_total': 0, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get category

*Detail information of a category.*

**Parameters:**

- **category_id** (int): ID of category

**Example:**

```python
data = api.forum.categories.get_category(category_id=103)
print(data)
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Pages

### Get pages

*List of all pages in the system.*

**Parameters:**

- **parent_page_id** (int): ID of parent page. If exists, filter pages that are direct children of that page.
- **order** (str): Ordering of pages. Can be [natural, list]

**Example:**

```python
data = api.forum.pages.get_pages()
print(data)
```

```python
{'pages': [{'page_id': 0, 'page_title': 'string', 'page_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-pages': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}], 'pages_total': 0, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get page

*Detail information of a page.*

**Parameters:**

- **page_id** (int): ID of parent page. If exists, filter pages that are direct children of that page.

**Example:**

```python
data = api.forum.pages.get_page(page_id=693)
print(data)
```

```python
{'page': {'page_id': 0, 'page_title': 'string', 'page_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-pages': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Tags

### Get popular tags

*List of popular tags (no pagination).*

**Parameters:**


**Example:**

```python
data = api.forum.tags.popular()
print(data)
```

```python
{'tag': {'1': 'string', '2': 'string', '3': 'string', '4': 'string', '5': 'string', '6': 'string', '7': 'string', '8': 'string', '9': 'string', '10': 'string', '11': 'string', '12': 'string', '14': 'string', '15': 'string', '16': 'string', '17': 'string', '18': 'string', '19': 'string', '20': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get tags

*List of tags.*

**Parameters:**

- **page** (int): Page number of tags list.
- **limit** (int): Limit of tags on a page.

**Example:**

```python
data = api.forum.tags.tags(page=7)
print(data)
```

```python
{'tags': {'1': 'string', '2': 'string', '3': 'string', '4': 'string', '5': 'string', '6': 'string', '7': 'string', '8': 'string', '9': 'string', '10': 'string', '11': 'string', '12': 'string', '14': 'string', '15': 'string', '16': 'string', '17': 'string', '18': 'string', '19': 'string', '20': 'string'}, 'tags_total': 0, 'links': {'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Tagged contents

*List of tagged contents.*

**Parameters:**

- **tag_id** (int): Id of tag.
- **page** (int): Page number of tags list.
- **limit** (int): Number of tagged contents in a page.

**Example:**

```python
data = api.forum.tags.tagged(tag_id=20)
print(data)
```

```python
{'tag': {'tag_id': 0, 'tag_text': 'string', 'tag_use_count': 0, 'links': {'permalink': 'string', 'detail': 'string'}}, 'tagged': [{'content_type': 'string', 'content_id': 0, 'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': ['string'], 'thread_tags': {'14': 'string', '101': 'string', '355': 'string', '1097': 'string'}, 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': ['string'], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}], 'tagged_total': 0, 'links': {'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Find tags

*Filtered list of tags.*

**Parameters:**

- **tag** (str): tag to filter. Tags start with the query will be returned.

**Example:**

```python
data = api.forum.tags.find(tag="LolzteamApi")
print(data)
```

```python
{'tags': ['string'], 'ids': [0], 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Search

### Search for threads

*Search for threads.*

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
data = api.forum.search.thread(q="LolzteamApi")
print(data)
```

```python
{'threads': [{'thread_id': 0}], 'data': [{'content_type': 'string', 'content_id': 0, 'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}], 'links': {'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Search for posts

*Search for posts.*

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
data = api.forum.search.post(q="LolzteamApi")
print(data)
```

```python
{'posts': [{'thread_id': 0, 'post_id': 0}], 'data': [{'content_type': 'string', 'content_id': 0, 'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}], 'links': {'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Search for all types of content

*Search for threads.*

**Parameters:**

- **q** (str): Search query. 
  > Can be skipped if user_id is set.
- **tag** (str): Tag to search for tagged contents.
- **forum_id** (int): ID of the container forum to search for contents. 
  > Child forums of the specified forum will be included in the search.
- **user_id** (int): ID of the creator to search for contents.
- **page** (int): Page number of results.
- **limit** (int): Number of results in a page.

**Example:**

```python
data = api.forum.search.post(q="LolzteamApi")
print(data)
```

```python
{'posts': [{'thread_id': 0, 'post_id': 0}], 'data': [{'content_type': 'string', 'content_id': 0, 'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}], 'links': {'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Search for tagged

*Search for tagged contents.*

**Parameters:**

- **tag** (str): Tag to search for tagged contents.
- **tags** (list[str]): Array of tags to search for tagged contents.
- **page** (int): Page number of results.
- **limit** (int): Number of results in a page.

**Example:**

```python
data = api.forum.search.tag(tag="LolzteamApi")
print(data)
```

```python
{'posts': [{'thread_id': 0, 'post_id': 0}], 'data': [{'content_type': 'string', 'content_id': 0, 'thread_id': 0, 'forum_id': 0, 'thread_title': 'string', 'thread_view_count': 0, 'creator_user_id': 0, 'creator_username': 'string', 'thread_create_date': 0, 'thread_update_date': 0, 'user_is_ignored': True, 'thread_post_count': 0, 'thread_is_published': True, 'thread_is_deleted': True, 'thread_is_sticky': True, 'thread_is_followed': True, 'first_post': {'post_id': 0, 'thread_id': 0, 'poster_user_id': 0, 'poster_username': 'string', 'post_create_date': 0, 'post_body': 'string', 'post_body_html': 'string', 'post_body_plain_text': 'string', 'signature': 'string', 'signature_html': 'string', 'signature_plain_text': 'string', 'post_like_count': 0, 'post_attachment_count': 0, 'like_users': [{'user_id': 0, 'username': 'string', 'display_style_group_id': 0, 'is_banned': 0, 'uniq_username_css': 'string'}], 'user_is_ignored': True, 'post_is_published': True, 'post_is_deleted': True, 'post_update_date': 0, 'post_is_first_post': True, 'links': {'permalink': 'string', 'detail': 'string', 'thread': 'string', 'poster': 'string', 'likes': 'string', 'report': 'string', 'attachments': 'string', 'poster_avatar': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'reply': True, 'like': True, 'report': True, 'upload_attachment': True}}, 'thread_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}], 'thread_tags': ['string'], 'links': {'permalink': 'string', 'detail': 'string', 'followers': 'string', 'forum': 'string', 'posts': 'string', 'first_poster': 'string', 'first_poster_avatar': 'string', 'first_post': 'string', 'last_poster': 'string', 'last_post': 'string'}, 'permissions': {'view': True, 'delete': True, 'follow': True, 'post': True, 'upload_attachment': True, 'edit': True}, 'forum': {'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': [{'group_title': 'string', 'group_prefixes': [{'prefix_id': 0, 'prefix_title': 'string'}]}], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'forum_is_followed': True}}], 'links': {'pages': 0, 'page': 0, 'next': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Search indexing

*Index external content data into search system to be searched later.*

**Parameters:**

- **content_type** (str): The type of content being indexed.
- **content_id** (str):  The unique id for the content.
- **title** (str):  Content title.
- **body** (str):  Content body.
- **link** (str):  Link related to content.
- **date** (int): Unix timestamp in second of the content. If missing, current time will be used.

**Example:**

```python
data = api.forum.search.indexing(content_type="post",content_id=40767586,title="LolzteamApi Python",body="Body",link="https://zelenka.guru/threads/5523020/")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

# Oauth

### Facebook oauth

*Request API access token using Facebook access token. Please note that because Facebook uses app-scoped user_id, it is not possible to recognize user across different Facebook Applications.*

**Parameters:**

- **client_id** (int): ID of facebook client.
- **client_secret** (str): Secret phrase of facebook client.
- **facebook_token** (str): Facebook token.

**Example:**

```python
data = api.forum.oauth.facebook(client_id="client_id",client_secret="client_secret",facebook_token="fb_token")
print(data)
```

```python
string
```

### Twitter oauth

*Request API access token using Twitter access token. The twitter_uri and twitter_auth parameters are similar to X-Auth-Service-Provider and X-Verify-Credentials-Authorization as specified in Twitter's OAuth Echo specification.*

**Parameters:**

- **client_id** (int): ID of twitter client.
- **client_secret** (str): Secret phrase of twitter client.
- **twitter_url** (str): "the full /account/verify_credentials.json uri that has been used to calculate OAuth signature. For security reason, the uri must use HTTPS protocol and the hostname must be either "twitter.com" or "api.twitter.com"."
- **twitter_auth** (str): the complete authentication header that starts with "OAuth". Consult Twitter document for more information.

**Example:**

```python
data = api.forum.oauth.twitter(client_id="client_id",client_secret="client_secret",twitter_url="https://twitter_url",twitter_auth="twitter_auth")
print(data)
```

```python
string
```

### Google oauth

*Request API access token using Google access token.*

**Parameters:**

- **client_id** (int): ID of facebook client.
- **client_secret** (str): Secret phrase of facebook client.
- **google_token** (str): Google token.

**Example:**

```python
data = api.forum.oauth.google(client_id="client_id",client_secret="client_secret",google_token="google_token")
print(data)
```

```python
string
```

### Associate oauth

*Request API access token and associate social account with an existing user account.*

**Parameters:**

- **client_id** (int): ID of associate client.
- **user_id** (str): ID of user.
- **password** (str): Can be used with password_algo for better security. See Encryption section for more information.
- **extra_data** (str): Extra data
- **extra_timestamp** (int): Extra timestamp

**Example:**

```python
data = api.forum.oauth.associate(client_id="client_id",client_secret="client_secret",user_id="user_id",password="user_pass", extra_data="data",extra_timestamp="timestamp")
print(data)
```

```python
string
```

### Admin oauth

*Request API access token for another user.*
  > This requires admincp scope and the current user must have sufficient system permissions.*

**Parameters:**

- **user_id** (int): ID of the user that needs access token.

**Example:**

```python
data = api.forum.oauth.admin(user_id=1)
print(data)
```

```python
string
```

# Navigation

*List of navigation elements within the system.*

**Parameters:**

- **parent** (int): ID of parent element.
  > If exists, filter elements that are direct children of that element.

**Example:**

```python
data = api.forum.navigation()
print(data)
```

```python
{'elements': [{'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string', 'sub-elements': 'string', 'threads': 'string', 'followers': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True, 'create_thread': True, 'upload_attachment': True, 'tag_thread': True, 'follow': True}, 'navigation_type': 'string', 'navigation_id': 0, 'navigation_parent_id': 0, 'has_sub_elements': True, 'forum_id': 0, 'forum_title': 'string', 'forum_description': 'string', 'forum_thread_count': 0, 'forum_post_count': 0, 'forum_prefixes': ['string'], 'thread_default_prefix_id': 0, 'thread_prefix_is_required': True, 'forum_is_followed': True}]}
```

# Get batch job

*Creates batch job for Batch method*

**Parameters:**

- **func** (function): Needed method pointer
- **job_name** (str): Job name
- ****kwargs** (str): Arguments for needed method

**Example:**

```python
jobs = [
    api.get_batch_job(api.forum.users.search, job_name="1", custom_fields={"telegram": "AS7RID"}),
    api.get_batch_job(api.forum.users.get, job_name="2", user_id=1),
    api.get_batch_job(api.forum.threads.get, job_name="3", thread_id=5523020),
    api.get_batch_job(api.forum.threads.create, job_name="4", forum_id=876, thread_title="Api batch example",post_body="Api batch example body", thread_tags="LolzteamApi")
]
for job in jobs:
    print(job)
```

```python
{'id': '1', 'uri': 'https://api.zelenka.guru/users/find', 'method': 'GET', 'params': {'username': None, 'user_email': None, 'custom_fields[telegram]': 'AS7RID', 'custom_fields': {'telegram': 'AS7RID'}, 'locale': 'en'}, 'data': {'username': None, 'user_email': None, 'custom_fields[telegram]': 'AS7RID', 'custom_fields': {'telegram': 'AS7RID'}}, 'files': None}
{'id': '2', 'uri': 'https://api.zelenka.guru/users/1', 'method': 'GET', 'params': {'locale': 'en'}, 'data': {}, 'files': None}
{'id': '3', 'uri': 'https://api.zelenka.guru/threads/5523020', 'method': 'GET', 'params': {'locale': 'en'}, 'data': {}, 'files': None}
{'id': '4', 'uri': 'https://api.zelenka.guru/threads', 'method': 'POST', 'params': {'forum_id': 876, 'thread_prefix_id': None, 'thread_tags': 'LolzteamApi', 'thread_title': 'Api batch example', 'post_body': 'Api batch example body', 'locale': 'en'}, 'data': {'thread_title': 'Api batch example', 'post_body': 'Api batch example body', 'forum_id': 876, 'thread_prefix_id': None, 'thread_tags': 'LolzteamApi'}, 'files': None}
```

# Batch

*Execute multiple API requests at once.*

  > Maximum batch jobs is 10.
  >
  > Forum batch can only proceed with forum url's. If you want to use batch with market url's try [this](https://github.com/AS7RIDENIED/Lolzteam_Python_Api/blob/main/Documentation/Market.md#batch)

**Parameters:**

- **request_body** (list[dict]): List of batch jobs.

**Example:**

```python
jobs = [
    api.get_batch_job(api.forum.users.search, job_name="1", custom_fields={"telegram": "AS7RID"}),
    api.get_batch_job(api.forum.users.get, job_name="2", user_id=1),
    api.get_batch_job(api.forum.threads.get, job_name="3", thread_id=5523020),
    api.get_batch_job(api.forum.threads.create, job_name="4", forum_id=876, thread_title="Api batch example",post_body="Api batch example body", thread_tags="LolzteamApi")
]
data = api.forum.batch(request_body=jobs)
for job_name, job_data in data["jobs"].items():
    print(job_data)
```

```python
{'_job_result': 'ok', 'users': [{'user_id': 2410024, 'username': 'AS7RID', 'username_html': '<span  class="style22">AS7RID</span>', 'user_message_count': 1089, 'user_register_date': 1560282271, 'user_like_count': 2949, 'short_link': 'as7rid', ... }
{'_job_result': 'ok', 'user': {'user_id': 1, 'username': 'RaysMorgan', 'username_html': '<span  class="style3">RaysMorgan</span>', 'user_message_count': 12104, 'user_register_date': 1362675475, 'user_like_count': 44351, 'short_link': 'rays',  ... }
{'_job_result': 'ok', 'thread': {'thread_id': 5523020, 'forum_id': 976, 'thread_title': 'Библиотека для упрощения работы с API | LolzteamApi Forum/Market/Antipublic Python', 'thread_view_count': 715, 'creator_user_id': 2410024, 'creator_usern ... }
{'_job_result': 'ok', 'thread': {'thread_id': 5907641, 'forum_id': 876, 'thread_title': 'Api batch example', 'thread_view_count': 1, 'creator_user_id': 2410024, 'creator_username': 'AS7RID', 'creator_username_html': '<span  class="style22">AS ... }
```

<font size=6 style="margin: auto"> <center>
[Market docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Market.md) - [Antipublic Docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Antipublic.md)
[Utility docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Utils.md)
</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

* [Categories](#categories)
  * [List](#list)
  * [Get](#get)
* [Forums](#forums)
  * [List](#list-1)
  * [Get](#get-1)
  * [Follow](#follow)
  * [Unfollow](#unfollow)
  * [Followers](#followers)
  * [Followed](#followed)
* [Pages](#pages)
  * [List](#list-2)
  * [Get](#get-2)
* [Posts](#posts)
  * [Posts Comments](#posts-comments)
    * [Get](#get-3)
    * [Create](#create)
  * [List](#list-3)
  * [Get](#get-4)
  * [Create](#create-1)
  * [Edit](#edit)
  * [Delete](#delete)
  * [Likes](#likes)
  * [Like](#like)
  * [Unlike](#unlike)
  * [Report](#report)
* [Threads](#threads)
  * [Contests](#contests)
    * [Money](#money)
      * [Create By Time](#create-by-time)
      * [Create By Count](#create-by-count)
    * [Upgrade](#upgrade)
      * [Create By Time](#create-by-time-1)
      * [Create By Count](#create-by-count-1)
  * [Arbitrage](#arbitrage)
    * [Market](#market)
    * [Non Market](#non-market)
  * [List](#list-4)
  * [Get](#get-5)
  * [Create](#create-2)
  * [Edit](#edit-1)
  * [Move](#move)
  * [Delete](#delete-1)
  * [Followers](#followers-1)
  * [Followed](#followed-1)
  * [Follow](#follow-1)
  * [Unfollow](#unfollow-1)
  * [Navigation](#navigation)
  * [Votes](#votes)
  * [Vote](#vote)
  * [New](#new)
  * [Recent](#recent)
  * [Bump](#bump)
* [Tags](#tags)
  * [Popular](#popular)
  * [List](#list-5)
  * [Tagged](#tagged)
  * [Find](#find)
* [Users](#users)
  * [Avatar](#avatar)
    * [Upload](#upload)
    * [Delete](#delete-2)
    * [Crop](#crop)
  * [List](#list-6)
  * [Fields](#fields)
  * [Search](#search)
  * [Get](#get-6)
  * [Timeline](#timeline)
  * [Edit](#edit-2)
  * [Follow](#follow-2)
  * [Unfollow](#unfollow-2)
  * [Followers](#followers-2)
  * [Followings](#followings)
  * [Ignored](#ignored)
  * [Ignore](#ignore)
  * [Unignore](#unignore)
  * [Groups](#groups)
* [Profile Posts](#profile-posts)
  * [Profile Posts Comments](#profile-posts-comments)
    * [List](#list-7)
    * [Get](#get-7)
    * [Create](#create-3)
  * [List](#list-8)
  * [Get](#get-8)
  * [Create](#create-4)
  * [Edit](#edit-3)
  * [Delete](#delete-3)
  * [Likes](#likes-1)
  * [Like](#like-1)
  * [Unlike](#unlike-1)
  * [Report](#report-1)
* [Search](#search-1)
  * [All](#all)
  * [Thread](#thread)
  * [Post](#post)
  * [Tag](#tag)
  * [Profile Posts](#profile-posts)
* [Notifications](#notifications)
  * [List](#list-9)
  * [Get](#get-9)
  * [Read](#read)
* [Conversations](#conversations)
  * [Conversations Messages](#conversations-messages)
    * [List](#list-10)
    * [Get](#get-10)
    * [Create](#create-5)
    * [Edit](#edit-4)
    * [Delete](#delete-4)
    * [Report](#report-2)
  * [List](#list-11)
  * [Get](#get-11)
  * [Leave](#leave)
  * [Create](#create-6)
  * [Create Group](#create-group)
* [Navigation](#navigation-1)
* [Batch](#batch)


</details>

# Quickstart

You need to create class instance to use library

```
from LOLZTEAM import AutoUpdate
from LOLZTEAM import Constants
from LOLZTEAM.API import Forum, Market
from LOLZTEAM.Tweaks import DelaySync, SendAsAsync, CreateJob

token = "your_token"

market = Market(token=token, language="en")
forum = Forum(token=token, language="en")
```

**Parameters:**

- **token** (str): Your token.
  > You can get it [there](https://zelenka.guru/account/api)
- **bypass_429** (bool): Bypass status code 429 by sleep
- **language** (str): Language for your api responses.
- **proxy_type** (str): Your proxy type.
- **proxy** (str): Proxy string.
- **reset_custom_variables** (bool): Reset custom variables.
- **timeout** (int): Request timeout.
# Categories

## List

GET https://api.zelenka.guru/categories

*List of all categories in the system.*

Required scopes: *read*

**Parameters:**

- **parent_category_id** (int): ID of parent category.
- **parent_forum_id** (int): ID of parent forum.
- **order** (str): Ordering of categories.
    > Can be [natural, list]

**Example:**

```python
forum.categories.list()
```


## Get

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


# Forums

## List

GET https://api.zelenka.guru/forums

*List of all forums in the system.*

Required scopes: *read*

**Parameters:**

- **parent_category_id** (int): ID of parent category.
- **parent_forum_id** (int): ID of parent forum.
- **order** (str): Ordering of categories.
    > Can be [natural, list]

**Example:**

```python
response = forum.forums.list()
print(response.json())
```


## Get

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


## Follow

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


## Unfollow

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


## Followers

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


## Followed

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


# Pages

## List

GET https://api.zelenka.guru/pages

*List of all pages in the system.*

Required scopes: *read*

**Parameters:**

- **parent_page_id** (int): ID of parent page.
    > If exists, filter pages that are direct children of that page.
- **order** (str): Ordering of pages.
    > Can be [natural, list]

**Example:**

```python
response = forum.pages.list()
print(response.json())
```


## Get

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


# Posts

## Comments

### Get

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


### Create

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


## List

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
    > Can be [natural, natural_reverse, post_create_date, post_create_date_reverse].

**Example:**

```python
response = forum.posts.list(thread_id=1000000)
print(response.json())
```


## Get

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


## Create

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


## Edit

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


## Delete

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


## Likes

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


## Like

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


## Unlike

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


## Report

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


# Threads

## Contests

### Money

#### Create By Time

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


#### Create By Count

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


### Upgrade

#### Create By Time

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


#### Create By Count

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


## Arbitrage

### Market

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


### Non Market

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


## List

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


## Get

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


## Create

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


## Edit

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


## Move

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


## Delete

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


## Followers

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


## Followed

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


## Follow

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


## Unfollow

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


## Navigation

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


## Votes

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


## Vote

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


## New

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


## Recent

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


## Bump

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


# Tags

## Popular

GET https://api.zelenka.guru/tags

*List of popular tags (no pagination).*

Required scopes: *read*

**Example:**

```python
response = forum.tags.popular()
print(response.json())
```


## List

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


## Tagged

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


## Find

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


# Users

## Avatar

### Upload

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


### Delete

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


### Crop

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


## List

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


## Fields

GET https://api.zelenka.guru/users/fields

*List of user fields.*

Required scopes: *read*

**Example:**

```python
response = forum.users.fields()
print(response.json())
```


## Search

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


## Get

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


## Timeline

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


## Edit

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


## Follow

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


## Unfollow

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


## Followers

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


## Followings

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


## Ignored

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


## Ignore

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


## Unignore

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


## Groups

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


# Posts

## Comments

### List

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


### Get

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


### Create

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


## List

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


## Get

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


## Create

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


## Edit

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


## Delete

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


## Likes

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


## Like

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


## Unlike

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


## Report

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


# Search

## All

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


## Thread

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


## Post

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


## Tag

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


## Profile Posts

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


# Notifications

## List

GET https://api.zelenka.guru/notifications

*List of notifications (both read and unread).*

Required scopes: *read*

**Example:**

```python
response = forum.notifications.list()
print(response.json())
```


## Get

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


## Read

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


# Conversations

## Messages

### List

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


### Get

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


### Create

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


### Edit

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


### Delete

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


### Report

POST https://api.zelenka.guru/conversation-messages/{message_id}/report

*Create a new conversation message.*

Required scopes: *conversate*, *post*

**Parameters:**

- **message_id** (int): ID of conversation message.
- **message** (str): Reason of the report.

**Example:**

```python
response = forum.conversations.messages.report(message_id=1000000, reason="Reason")
print(response.json())
```


## List

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


## Get

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


## Leave

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


## Create

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


## Create Group

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


# Navigation

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


# Batch

POST https://api.zelenka.guru/batch

*Execute multiple API requests at once. Maximum batch jobs is 10.*

**Example jobs scheme:**

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



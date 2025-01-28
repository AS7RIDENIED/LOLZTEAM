<div style="display: flex; gap: 5px; justify-content: center;">
<a href="https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/Documentation/Market.md" style="background-color: #2bad72; color: white; padding: 5px 10px; text-decoration: none; border-radius: 7px; font-weight: bold; transition: all 0.3s ease;">Market docs</a><a href="https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/Documentation/Antipublic.md" style="background-color: #2bad72; color: white; padding: 5px 10px; text-decoration: none; border-radius: 7px; font-weight: bold; transition: all 0.3s ease;">Antipublic Docs</a>
</div>

<details>

<summary><font size="4">Method tree</font></summary>

* [Quickstart](#quickstart)
* [Categories](#categories)
  * [List](#list)
  * [Get](#get)
* [Forums](#forums)
  * [List](#list-1)
  * [Get](#get-1)
  * [Followers](#followers)
  * [Followed](#followed)
  * [Follow](#follow)
  * [Unfollow](#unfollow)
* [Pages](#pages)
  * [List](#list-2)
  * [Get](#get-2)
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
  * [Poll](#poll)
    * [Get](#get-3)
    * [Vote](#vote)
  * [List Unread](#list-unread)
  * [List Recent](#list-recent)
  * [List](#list-3)
  * [Get](#get-4)
  * [Create](#create)
  * [Edit](#edit)
  * [Delete](#delete)
  * [Bump](#bump)
  * [Move](#move)
  * [Followers](#followers-1)
  * [Followed](#followed-1)
  * [Follow](#follow-1)
  * [Unfollow](#unfollow-1)
  * [Navigation](#navigation)
* [Posts](#posts)
  * [Comments](#comments)
    * [List](#list-4)
    * [Create](#create-1)
  * [List](#list-5)
  * [Get](#get-5)
  * [Create](#create-2)
  * [Edit](#edit-1)
  * [Delete](#delete-1)
  * [Likes](#likes)
  * [Like](#like)
  * [Unlike](#unlike)
  * [Report](#report)
* [Users](#users)
  * [Avatar](#avatar)
    * [Upload](#upload)
    * [Delete](#delete-2)
    * [Crop](#crop)
  * [Background](#background)
    * [Upload](#upload-1)
    * [Delete](#delete-3)
    * [Crop](#crop-1)
  * [Profile Posts](#profile-posts)
    * [Comments](#comments-1)
      * [List](#list-6)
      * [Get](#get-6)
      * [Create](#create-3)
    * [List](#list-7)
    * [Get](#get-7)
    * [Create](#create-4)
    * [Edit](#edit-2)
    * [Delete](#delete-4)
    * [Likes](#likes-1)
    * [Like](#like-1)
    * [Unlike](#unlike-1)
  * [List](#list-8)
  * [Search](#search)
  * [Get](#get-8)
  * [Edit](#edit-3)
  * [Fields](#fields)
  * [Followers](#followers-2)
  * [Followed](#followed-2)
  * [Follow](#follow-2)
  * [Unfollow](#unfollow-2)
  * [Ignored](#ignored)
  * [Ignore](#ignore)
  * [Unignore](#unignore)
  * [Content](#content)
* [Conversations](#conversations)
  * [Messages](#messages)
    * [List](#list-9)
    * [Get](#get-9)
    * [Create](#create-5)
    * [Edit](#edit-4)
  * [List](#list-10)
  * [Get](#get-10)
  * [Create](#create-6)
  * [Create Group](#create-group)
  * [Leave](#leave)
* [Notifications](#notifications)
  * [List](#list-11)
  * [Get](#get-11)
  * [Read](#read)
* [Tags](#tags)
  * [List](#list-12)
  * [Get](#get-12)
  * [Popular](#popular)
  * [Search](#search-1)
* [Search](#search-2)
  * [All](#all)
  * [Threads](#threads-1)
  * [Posts](#posts-1)
  * [Profile Posts](#profile-posts-1)
  * [Tagged](#tagged)
* [Navigation](#navigation-1)
* [Batch](#batch)


</details>

# Quickstart

LOLZTEAM Forum API Client

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


# Categories

## List

GET https://api.zelenka.guru/categories

*Get categories.*

**Parameters:**

- **parent_category_id** (int): Parent category ID.
- **parent_forum_id** (int): Parent forum ID.
- **order** (str): Order of the categories.

**Example:**

```python
response = forum.categories.list(parent_category_id=1, parent_forum_id=1, order="natural")
print(response.json())
```


## Get

GET https://api.zelenka.guru/categories/{category_id}

*Get category.*

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

*Get forums.*

**Parameters:**

- **parent_category_id** (int): Parent category ID.
- **parent_forum_id** (int): Parent forum ID.
- **order** (str): Order of the forums.

**Example:**

```python
response = forum.forums.list()
print(response.json())
```


## Get

GET https://api.zelenka.guru/forums/{forum_id}

*Get forum.*

**Parameters:**

- **forum_id** (int): Forum ID.

**Example:**

```python
response = forum.forums.get(forum_id=876)
print(response.json())
```


## Followers

GET https://api.zelenka.guru/forums/{forum_id}/followers

*Get forum followers.*

**Parameters:**

- **forum_id** (int): Forum ID.

**Example:**

```python
response = forum.forums.followers(forum_id=876)
print(response.json())
```


## Followed

GET https://api.zelenka.guru/forums/followed

*Get followed forums.*

**Parameters:**

- **total** (bool): Get total count of followed forums.

**Example:**

```python
response = forum.forums.followed(total=True)
print(response.json())
```


## Follow

POST https://api.zelenka.guru/forums/{forum_id}/followers

*Follow forum.*

**Parameters:**

- **post** (bool): Get post notifications.
- **alert** (bool): Get alert notifications.
- **email** (bool): Get email notifications.
- **prefix_ids** (list[int]): Prefix IDs.
- **minimal_contest_amount** (float): Minimal contest amount.

**Example:**

```python
response = forum.forums.follow(forum_id=876, post=True, alert=True, email=False)
print(response.json())
```


## Unfollow

DELETE https://api.zelenka.guru/forums/{forum_id}/followers

*Unfollow forum.*

**Parameters:**

- **forum_id** (int): Forum ID.

**Example:**

```python
response = forum.forums.unfollow(forum_id=876)
print(response.json())
```


# Pages

## List

GET https://api.zelenka.guru/pages

*Get pages.*

**Example:**

```python
response = forum.pages.list()
print(response.json())
```


## Get

GET https://api.zelenka.guru/pages/{page_id}

*Get page.*

**Parameters:**

- **page_id** (int): Page ID.

**Example:**

```python
response = forum.pages.get(page_id=1)
print(response.json())
```


# Threads

## Contests

### Money

#### Create By Time

POST https://api.zelenka.guru/threads

*Create a money contest.*

**Parameters:**

- **post_body** (str): Content of the new contest.
- **prize_amount** (float): How much money will each winner receive.
- **winners_count** (int): Winner count (prize count).
    > The maximum value is 100.
- **length** (int): Contest duration value.
    > The maximum duration is 3 days.
- **length_option** (str): Contest duration type.
    > Can be [minutes, hours, days]. The maximum duration is 3 days.
- **require_week_sympathy** (int): Sympathies for this week.
- **require_total_sympathy** (int): Symapthies for all time.
- **secret_answer** (str): Secret answer of your account.
- **reply_group** (int): Allow to reply only users with chosen or higher group.
- **title** (str): Thread title.
    > Can be skipped if title_en set.
- **title_en** (str): Thread title in english.
    > Can be skipped if title set.
- **tags** (list[str]): Thread tags.
- **hide_contacts** (bool): Hide contacts.
- **allow_ask_hidden_content** (bool): Allow ask hidden content.
- **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
- **dont_alert_followers** (bool): Don't alert followers.
- **forum_notifications** (bool): Get forum notifications.
- **email_notifications** (bool): Get email notifications.

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


#### Create By Count

POST https://api.zelenka.guru/threads

*Create a money contest.*

**Parameters:**

- **post_body** (str): Content of the new contest.
- **prize_amount** (float): How much money will each winner receive.
- **winners_count** (int): Winner count (prize count).
- **needed_members** (int): Max member count.
- **require_week_sympathy** (int): Sympathies for this week.
- **require_total_sympathy** (int): Symapthies for all time.
- **secret_answer** (str): Secret answer of your account.
- **reply_group** (int): Allow to reply only users with chosen or higher group.
- **title** (str): Thread title.
    > Can be skipped if title_en set.
- **title_en** (str): Thread title in english.
    > Can be skipped if title set.
- **tags** (list[str]): Thread tags.
- **hide_contacts** (bool): Hide contacts.
- **allow_ask_hidden_content** (bool): Allow ask hidden content.
- **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
- **dont_alert_followers** (bool): Don't alert followers.
- **forum_notifications** (bool): Get forum notifications.
- **email_notifications** (bool): Get email notifications.

**Example:**

```python
response = forum.threads.contests.money.create_by_count(post_body="Contest", prize_amount=500, winners_count=1,
                                                       needed_members=300, require_week_sympathy=1, require_total_sympathy=50,
                                                       secret_answer="My secret answer", title="Contest")
print(response.json())
```


### Upgrade

#### Create By Time

POST https://api.zelenka.guru/threads

*Create a new contest.*

**Parameters:**

- **post_body** (str): Content of the new contest.
- **prize_group** (Constants.Forum.Contests.UpgradePrize._Literal): Which upgrade will each winner receive.
- **winners_count** (int): Winner count (prize count).
    > The maximum value is 100.
- **length** (int): Contest duration value.
    > The maximum duration is 3 days.
- **length_option** (Constants.Forum.Contests.Length._Literal): Contest duration type.
    > Can be [minutes, hours, days]. The maximum duration is 3 days.
- **require_week_sympathy** (int): Sympathies for this week.
- **require_total_sympathy** (int): Sympathies for all time.
- **secret_answer** (str): Secret answer of your account.
- **reply_group** (Constants.Forum.ReplyGroups._Literal): Allow to reply only users with chosen or higher group.
- **title** (str): Thread title.
    > Can be skipped if title_en set.
- **title_en** (str): Thread title in english.
    > Can be skipped if title set.
- **tags** (list[str]): Thread tags.
- **hide_contacts** (bool): Hide contacts.
- **allow_ask_hidden_content** (bool): Allow ask hidden content.
- **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
- **dont_alert_followers** (bool): Don't alert followers.
- **forum_notifications** (bool): Get forum notifications.
- **email_notifications** (bool): Get email notifications.

**Example:**

```python
response = forum.threads.contests.upgrade.create_by_time(post_body="Contest", prize_group=1, winners_count=1,
                                                       length=3, length_option="days", require_week_sympathy=1,
                                                       require_total_sympathy=50, secret_answer="My secret answer", title="Contest")
print(response.json())
```


#### Create By Count

POST https://api.zelenka.guru/threads

*Create a new contest.*

**Parameters:**

- **post_body** (str): Content of the new contest.
- **prize_group** (Constants.Forum.Contests.UpgradePrize._Literal): Which upgrade will each winner receive.
- **winners_count** (int): Winner count (prize count).
    > The maximum value is 100.
- **needed_members** (int): Max member count.
- **require_week_sympathy** (int): Sympathies for this week.
- **require_total_sympathy** (int): Sympathies for all time.
- **secret_answer** (str): Secret answer of your account.
- **reply_group** (Constants.Forum.ReplyGroups._Literal): Allow to reply only users with chosen or higher group.
- **title** (str): Thread title.
    > Can be skipped if title_en set.
- **title_en** (str): Thread title in english.
    > Can be skipped if title set.
- **tags** (list[str]): Thread tags.
- **hide_contacts** (bool): Hide contacts.
- **allow_ask_hidden_content** (bool): Allow ask hidden content.
- **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
- **dont_alert_followers** (bool): Don't alert followers.
- **forum_notifications** (bool): Get forum notifications.
- **email_notifications** (bool): Get email notifications.

**Example:**

```python
response = forum.threads.contests.upgrade.create_by_count(post_body="Contest", prize_group=1, winners_count=1,
                                                       needed_members=300, require_week_sympathy=1,
                                                       require_total_sympathy=50, secret_answer="My secret answer", title="Contest")
print(response.json())
```


## Arbitrage

### Market

POST https://api.zelenka.guru/claims

*Create a Arbitrage.*

**Parameters:**

- **responder** (str): To whom the complaint is filed. Specify a nickname or a link to the profile.
- **item_id** (str|int): Write account link or item_id.
- **amount** (float): Amount by which the responder deceived you.
- **post_body** (str): You should describe what's happened.
- **currency** (str): Currency of Arbitrage.
- **conversation_screenshot** (str): Screenshot showing the respondent's Telegram login. If the correspondence was conducted in Telegram, upload screenshot that will display the respondent's Telegram login against the background of your dialogue. The screenshot must be uploaded to Imgur. If the correspondence was conducted elsewhere, write "no".
- **tags** (list[str]): Thread tags.
- **hide_contacts** (bool): Hide contacts.
- **allow_ask_hidden_content** (bool): Allow ask hidden content.
- **dont_alert_followers** (bool): Don't alert followers.
- **forum_notifications** (bool): Get forum notifications.
- **email_notifications** (bool): Get email notifications.

**Example:**

```python
response = forum.threads.arbitrage.market(responder="AS7RID", item_id=1000000, amount=1000,
                                          post_body="Arbitrage test", currency="rub")
print(response.json())
```


### Non Market

POST https://api.zelenka.guru/claims

*Create a Arbitrage.*


**Parameters:**

- **responder** (str): To whom the complaint is filed. Specify a nickname or a link to the profile.
- **amount** (float): Amount by which the responder deceived you.
- **receipt** (str): Funds transfer recipient. Upload a receipt for the transfer of funds, use the "View receipt" button in your wallet. Must be uploaded to Imgur. Write "no" if you have not paid.
- **post_body** (str): You should describe what's happened.
- **pay_claim** (str): If you set this parameter to "now" forum will automatically calculate the amount and debit it from your account.
    > For filing claims, it is necessary to make a contribution in the amount of 5% of the amount of damage (but not less than 50 rubles and not more than 5000 rubles). For example, for an amount of damage of 300 rubles, you will need to pay 50 rubles, for 2,000 and 10,000 rubles - 100 and 500 rubles, respectively).
- **conversation_screenshot** (str): Screenshot showing the respondent's Telegram login. If the correspondence was conducted in Telegram, upload screenshot that will display the respondent's Telegram login against the background of your dialogue. The screenshot must be uploaded to Imgur. If the correspondence was conducted elsewhere, write "no".
- **responder_data** (str): Contacts and wallets of the responder. Specify the known data about the responder (Skype, Vkontakte, Qiwi, WebMoney, etc.), if any.
- **currency** (str): Currency of Arbitrage.
- **transfer_type** (str): The transaction took place through a guarantor or there was a transfer to the market with a hold?
- **tags** (list[str]): Thread tags.
- **hide_contacts** (bool): Hide contacts.
- **allow_ask_hidden_content** (bool): Allow ask hidden content.
- **comment_ignore_group** (bool): Allow commenting if user can't post in thread.
- **dont_alert_followers** (bool): Don't alert followers.
- **reply_group** (int): Allow to reply only users with chosen or higher group.
- **forum_notifications** (bool): Get forum notifications.
- **email_notifications** (bool): Get email notifications.

**Example:**

```python
response = forum.threads.arbitrage.non_market(responder="AS7RID", amount=100, currency="rub", receipt="no",
                                              post_body="Non market arbitrage", pay_claim="now", transfer_type="notsafe")
print(response.json())
```


## Poll

### Get

GET https://api.zelenka.guru/threads/{thread_id}/poll

*Get poll.*

**Parameters:**

- **thread_id** (int): Thread ID.

**Example:**

```python
response = forum.threads.poll.get(thread_id=5523020)
print(response.json())
```


### Vote

POST https://api.zelenka.guru/threads/{thread_id}/poll/votes

*Vote in poll.*

**Parameters:**

- **thread_id** (int): Thread ID.
- **option_ids** (list[int] | int): Option IDs.

**Example:**

```python
response = forum.threads.poll.vote(thread_id=5523020, option_ids=[1, 2, 3])
print(response.json())
```


## List Unread

GET https://api.zelenka.guru/threads/new

*Get unread threads.*

**Parameters:**

- **forum_id** (int): Forum ID.
- **limit** (int): Limit of threads.
- **data_limit** (int): Limit of data.

**Example:**

```python
response = forum.threads.list_unread(forum_id=876, limit=10, data_limit=10)
print(response.json())
```


## List Recent

GET https://api.zelenka.guru/threads/recent

*Get recent threads.*

**Parameters:**

- **days** (int): Maximum number of days to search for threads.
- **forum_id** (int): Forum ID.
- **limit** (int): Limit of threads.
- **data_limit** (int): Limit of data.

**Example:**

```python
response = forum.threads.list_recent(days=1, forum_id=876, limit=10, data_limit=10)
print(response.json())
```


## List

GET https://api.zelenka.guru/threads

*Get threads.*

**Parameters:**

- **forum_id** (int): Forum ID.
- **user_id** (int): Filter to get only threads created by the specified user.
- **prefix_id** (int): Filter to get only threads with the specified prefix.
- **tag_id** (int): Filter to get only threads with the specified tag.
- **page** (int): Page.
- **limit** (int): Limit of threads.
- **order** (str): Order of threads.

**Example:**


## Get

GET https://api.zelenka.guru/threads/{thread_id}

*Get thread.*

**Parameters:**

- **thread_id** (int): Thread ID.

**Example:**

```python
response = forum.threads.get(thread_id=5523020)
print(response.json())
```


## Create

POST https://api.zelenka.guru/threads

*Create a thread.*

**Parameters:**

- **forum_id** (int): Forum ID.
- **post_body** (str): Content of the new thread.
- **title** (str): Title.
- **title_en** (str): Title in English.
- **prefix_ids** (list[int]): Prefix IDs.
- **tags** (list[int]): Tags.
- **reply_group** (int): Reply group.
- **hide_contacts** (bool): Hide contacts.
- **allow_ask_hidden_content** (bool): Allow ask hidden content.
- **comment_ignore_group** (bool): Comment ignore group.
- **dont_alert_followers** (bool): Don't alert followers.
- **forum_notifications** (bool): Get forum notifications.
- **email_notifications** (bool): Get email notifications.

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


## Edit

PUT https://api.zelenka.guru/threads/{thread_id}

*Edit a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.
- **title** (str): Title.
- **title_en** (str): Title in English.
- **post_body** (str): Post body.
- **prefix_ids** (list[int]): Prefix IDs.
- **tags** (list[int]): Tags.
- **discussion_state** (bool): Discussion state.
- **hide_contacts** (bool): Hide contacts.
- **allow_ask_hidden_content** (bool): Allow ask hidden content.
- **reply_group** (int): Reply group.
- **comment_ignore_group** (bool): Comment ignore group.

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


## Delete

DELETE https://api.zelenka.guru/threads/{thread_id}

*Delete a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.
- **reason** (str): Reason.

**Example:**

```python
response = forum.threads.delete(thread_id=5523020, reason="Test reason")
print(response.json())
```


## Bump

POST https://api.zelenka.guru/threads/{thread_id}/bump

*Bump a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.

**Example:**

```python
response = forum.threads.bump(thread_id=5523020)
print(response.json())
```


## Move

POST https://api.zelenka.guru/threads/{thread_id}/move

*Move a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.
- **forum_id** (int): Target forum ID.
- **title** (str): Title.
- **title_en** (str): Title in English.
- **prefix_ids** (list[int]): Prefix IDs.
- **send_alert** (bool): Send alert.

**Example:**

```python
response = forum.threads.move(thread_id=5523020, forum_id=876, title="Test thread", title_en="Test thread", prefix_ids=[1, 2, 3], send_alert=True)
print(response.json())
```


## Followers

GET https://api.zelenka.guru/threads/{thread_id}/followers

*Get followers of a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.

**Example:**

```python
response = forum.threads.followers(thread_id=5523020)
print(response.json())
```


## Followed

GET https://api.zelenka.guru/threads/{thread_id}/followed

*Get followed users of a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.
- **total** (bool): Total.

**Example:**

```python
response = forum.threads.followed(thread_id=5523020, total=True)
print(response.json())
```


## Follow

POST https://api.zelenka.guru/threads/{thread_id}/followers

*Follow a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.
- **email** (bool): Email.

**Example:**

```python
response = forum.threads.follow(thread_id=5523020, email=True)
print(response.json())
```


## Unfollow

DELETE https://api.zelenka.guru/threads/{thread_id}/followers

*Unfollow a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.

**Example:**

```python
response = forum.threads.unfollow(thread_id=5523020)
print(response.json())
```


## Navigation

GET https://api.zelenka.guru/threads/{thread_id}/navigation

*Get navigation of a thread.*

**Parameters:**

- **thread_id** (int): Thread ID.

**Example:**

```python
response = forum.threads.navigation(thread_id=5523020)
print(response.json())
```


# Posts

## Comments

### List

GET https://api.zelenka.guru/posts/{post_id}/comments

*Get comments of a post.*

**Parameters:**

- **post_id** (int): Post ID.
- **before_comment** (int): Parse comments before this comment.
- **before** (int): Parse comments before this timestamp.

**Example:**

```python
response = forum.posts.comments.list(post_id=5523020, before_comment=100)
print(response.json())
```


### Create

POST https://api.zelenka.guru/posts/{post_id}/comments

*Create a comment.*

**Parameters:**

- **post_id** (int): Post ID.
- **post_body** (str): Post body.

**Example:**

```python
response = forum.posts.comments.create(post_id=5523020, post_body="Test comment")
print(response.json())
```


## List

GET https://api.zelenka.guru/posts

*Get posts.*

**Parameters:**

- **thread_id** (int): Thread ID.
- **post_id** (int): Parse posts from page of this post.
- **page** (int): Page.
- **limit** (int): Posts limit per page.
- **order** (str): Posts order.

**Example:**

```python
response = forum.posts.list(thread_id=5523020, page=1, limit=10, order="natural")
print(response.json())
```


## Get

GET https://api.zelenka.guru/posts/{post_id}

*Get a post.*

**Parameters:**

- **post_id** (int): Post ID.

**Example:**

```python
response = forum.posts.get(post_id=5523020)
print(response.json())
```


## Create

POST https://api.zelenka.guru/posts

*Create a post.*

**Parameters:**

- **post_body** (str): Post body.
- **thread_id** (int): Thread ID.
- **quote_post_id** (int): Quote post ID.

**Example:**

```python
response = forum.posts.create(post_body="Test post", thread_id=5523020, quote_post_id=1234567)
print(response.json())
```


## Edit

PUT https://api.zelenka.guru/posts/{post_id}

*Edit a post.*

**Parameters:**

- **post_id** (int): Post ID.
- **post_body** (str): Post body.

**Example:**

```python
response = forum.posts.edit(post_id=5523020, post_body="Test post")
print(response.json())
```


## Delete

DELETE https://api.zelenka.guru/posts/{post_id}

*Delete a post.*

**Parameters:**

- **post_id** (int): Post ID.
- **reason** (str): Reason.

**Example:**

```python
response = forum.posts.delete(post_id=5523020, reason="Test reason")
print(response.json())
```


## Likes

GET https://api.zelenka.guru/posts/{post_id}/likes

*Get likes of a post.*

**Parameters:**

- **post_id** (int): Post ID.
- **page** (int): Page.
- **limit** (int): Likes limit per page.

**Example:**

```python
response = forum.posts.likes(post_id=5523020, page=1, limit=10)
print(response.json())
```


## Like

POST https://api.zelenka.guru/posts/{post_id}/likes

*Like a post.*

**Parameters:**

- **post_id** (int): Post ID.

**Example:**

```python
response = forum.posts.like(post_id=5523020)
print(response.json())
```


## Unlike

DELETE https://api.zelenka.guru/posts/{post_id}/likes

*Unlike a post.*

**Parameters:**

- **post_id** (int): Post ID.

**Example:**

```python
response = forum.posts.unlike(post_id=5523020)
print(response.json())
```


## Report

POST https://api.zelenka.guru/posts/{post_id}/report

*Report a post.*

**Parameters:**

- **post_id** (int): Post ID.
- **reason** (str): Reason.

**Example:**

```python
response = forum.posts.report(post_id=5523020, reason="Test reason")
print(response.json())
```


# Users

## Avatar

### Upload

POST https://api.zelenka.guru/users/me/avatar

*Upload an avatar.*
> You can't create batch job for this method

**Parameters:**

- **file** (bytes): Avatar bytes.
- **x** (int): X.
- **y** (int): Y.
- **size** (int): Selection size.
  > Minimum value - 16.

**Example:**

```python
with open("avatar.png", "rb") as file:
    response = forum.users.avatar.upload(file=file.read(), x=100, y=100, size=100)
print(response.json())
```


### Delete

DELETE https://api.zelenka.guru/users/me/avatar

**Delete an avatar.**

**Example:**

```python
response = forum.users.avatar.delete()
print(response.json())
```


### Crop

POST https://api.zelenka.guru/users/me/avatar/crop

*Crop an avatar.*

**Parameters:**

- **x** (int): X.
- **y** (int): Y.
- **size** (int): Selection size.
  > Minimum value - 16.

**Example:**

```python
response = forum.users.avatar.crop(x=100, y=100, size=100)
print(response.json())
```


## Background

### Upload

POST https://api.zelenka.guru/users/me/background

*Upload a background.*
> You can't create batch job for this method

**Parameters:**

- **file** (bytes): Background bytes.
- **x** (int): X.
- **y** (int): Y.
- **size** (int): Selection size.
  > Minimum value - 100.

**Example:**

```python
with open("background.png", "rb") as file:
    response = forum.users.background.upload(file=file.read(), x=100, y=100, size=100)
print(response.json())
```


### Delete

DELETE https://api.zelenka.guru/users/me/background

**Delete a background.**

**Example:**

```python
response = forum.users.background.delete()
print(response.json())
```


### Crop

POST https://api.zelenka.guru/users/me/background/crop

*Crop a background.*

**Parameters:**

- **x** (int): X.
- **y** (int): Y.
- **size** (int): Selection size.
  > Minimum value - 100.

**Example:**

```python
response = forum.users.background.crop(x=100, y=100, size=100)
print(response.json())
```


## Posts

### Comments

#### List

GET https://api.zelenka.guru/profile-posts/{post_id}/comments

*Get comments of a profile post.*

**Parameters:**

- **post_id** (int): Profile post ID.
- **before** (int): Parse comments before this timestamp.
- **limit** (int): Comments limit per page.

**Example:**

```python
response = forum.users.profile_posts.comments.list(post_id=5523020, before=100, limit=10)
print(response.json())
```


#### Get

GET https://api.zelenka.guru/profile-posts/{post_id}/comments/{comment_id}

*Get a comment of a profile post.*

**Parameters:**

- **post_id** (int): Profile post ID.
- **comment_id** (int): Comment ID.

**Example:**

```python
response = forum.users.profile_posts.comments.get(post_id=5523020, comment_id=1)
print(response.json())
```


#### Create

POST https://api.zelenka.guru/profile-posts/{post_id}/comments

*Create a comment of a profile post.*

**Parameters:**

- **post_id** (int): Profile post ID.
- **post_body** (str): Comment body.

**Example:**

```python
response = forum.users.profile_posts.comments.create(post_id=5523020, post_body="Test comment")
print(response.json())
```


### List

GET https://api.zelenka.guru/users/{user_id}/profile-posts

*Get profile posts of a user.*

**Parameters:**

- **user_id** (int): User ID.
- **page** (int): Page.
- **limit** (int): Posts limit per page.

**Example:**

```python
response = forum.users.profile_posts.list(user_id=2410024, page=1, limit=10)
print(response.json())
```


### Get

GET https://api.zelenka.guru/profile-posts/{post_id}

*Get a profile post.*

**Parameters:**

- **post_id** (int): Profile post ID.

**Example:**

```python
response = forum.users.profile_posts.get(post_id=5523020)
print(response.json())
```


### Create

POST https://api.zelenka.guru/users/{user_id}/profile-posts

*Create a profile post.*

**Parameters:**

- **user_id** (int): User ID.
- **post_body** (str): Post body.

**Example:**

```python
response = forum.users.profile_posts.create(user_id=2410024, post_body="Test post")
print(response.json())
```


### Edit

PUT https://api.zelenka.guru/profile-posts/{post_id}

*Edit a profile post.*

**Parameters:**

- **post_id** (int): Profile post ID.
- **post_body** (str): Post body.

**Example:**

```python
response = forum.users.profile_posts.edit(post_id=5523020, post_body="Test post")
print(response.json())
```


### Delete

DELETE https://api.zelenka.guru/profile-posts/{post_id}

**Delete a profile post.**

**Parameters:**

- **post_id** (int): Profile post ID.
- **reason** (str): Delete reason.

**Example:**

```python
response = forum.users.profile_posts.delete(post_id=5523020, reason="Test reason")
print(response.json())
```


### Likes

GET https://api.zelenka.guru/profile-posts/{post_id}/likes

*Get likes of a profile post.*

**Parameters:**

- **post_id** (int): Profile post ID.

**Example:**

```python
response = forum.users.profile_posts.likes.list(post_id=5523020)
print(response.json())
```


### Like

POST https://api.zelenka.guru/profile-posts/{post_id}/likes

**Like a profile post.**

**Example:**

```python
response = forum.users.profile_posts.likes.like(post_id=5523020)
print(response.json())
```


### Unlike

DELETE https://api.zelenka.guru/profile-posts/{post_id}/likes

**Unlike a profile post.**

**Example:**

```python
response = forum.users.profile_posts.likes.unlike(post_id=5523020)
print(response.json())
```


## List

GET https://api.zelenka.guru/users

*Get users.*

**Parameters:**

- **page** (int): Page.
- **limit** (int): Users limit per page.

**Example:**

```python
response = forum.users.list(page=1, limit=10)
print(response.json())
```


## Search

GET https://api.zelenka.guru/users/find

*Search users.*

**Parameters:**

- **username** (str): Username of the user.
- **fields** (dict[str, str]): Custom fields.

**Example:**

```python
response = forum.users.search(username="test", fields={"field1": "value1", "field2": "value2"})
print(response.json())
```


## Get

GET https://api.zelenka.guru/users/{user_id}

*Get a user.*

**Parameters:**

- **user_id** (int): User ID.

**Example:**

```python
response = forum.users.get(user_id=2410024)
print(response.json())
```


## Edit

PUT https://api.zelenka.guru/users/me

*Edit a user.*

**Parameters:**

- **title** (str): Title.
- **display_group_id** (int): Display group ID.
- **dob** (tuple[int, int, int]): Date of birth.
- **fields** (dict[str, str]): Custom fields.

**Example:**

```python
response = forum.users.edit(title="Test title", display_group_id=1, dob=(1, 1, 2000), fields={"_4": "My new interests", "occupation": "My new occupation"})
print(response.json())
```


## Fields

GET https://api.zelenka.guru/users/fields

*Get your fields.*

**Example:**

```python
response = forum.users.fields()
print(response.json())
```


## Followers

GET https://api.zelenka.guru/users/{user_id}/followers

*Get followers of a user.*

**Parameters:**

- **user_id** (int): User ID.
- **order** (str): Order.
- **page** (int): Page.
- **limit** (int): Followers limit per page.

**Example:**

```python
response = forum.users.followers(user_id=2410024, order="follow_date", page=1, limit=10)
print(response.json())
```


## Followed

GET https://api.zelenka.guru/users/{user_id}/followings

*Get followed users of a user.*

**Parameters:**

- **user_id** (int): User ID.
- **order** (str): Order.
- **page** (int): Page.
- **limit** (int): Followed users limit per page.

**Example:**

```python
response = forum.users.followed(user_id=2410024, order="follow_date", page=1, limit=10)
print(response.json())
```


## Follow

POST https://api.zelenka.guru/users/{user_id}/followers

**Follow a user.**

**Example:**

```python
response = forum.users.follow(user_id=2410024)
print(response.json())
```


## Unfollow

DELETE https://api.zelenka.guru/users/{user_id}/followers

**Unfollow a user.**

**Example:**

```python
response = forum.users.unfollow(user_id=2410024)
print(response.json())
```


## Ignored

GET https://api.zelenka.guru/users/ignored

*Get ignored users.*

**Example:**

```python
response = forum.users.ignored()
print(response.json())
```


## Ignore

POST https://api.zelenka.guru/users/{user_id}/ignore

**Ignore a user.**

**Example:**

```python
response = forum.users.ignore(user_id=2410024)
print(response.json())
```


## Unignore

DELETE https://api.zelenka.guru/users/{user_id}/ignore

**Unignore a user.**

**Example:**

```python
response = forum.users.unignore(user_id=2410024)
print(response.json())
```


## Content

GET https://api.zelenka.guru/users/{user_id}/timeline

*Get timeline of a user.*

**Example:**

```python
response = forum.users.content(user_id=2410024, page=1, limit=10)
print(response.json())
```


# Conversations

## Messages

### List

GET https://api.zelenka.guru/conversation-messages

*Get messages of a conversation.*


### Get

GET https://api.zelenka.guru/conversation-messages/{message_id}

*Get a message.*

**Parameters:**

- **message_id** (int): Message ID.

**Example:**

```python
response = forum.conversations.messages.get(message_id=123456)
print(response.json())
```


### Create

POST https://api.zelenka.guru/conversation-messages

**Create a message.**

**Parameters:**

- **conversation_id** (int): Conversation ID.
- **message** (str): Message.

**Example:**

```python
response = forum.conversations.messages.create(conversation_id=123456, message="Hello, world!")
print(response.json())
```


### Edit

PUT https://api.zelenka.guru/conversation-messages/{message_id}

**Edit a message.**

**Parameters:**

- **message_id** (int): Message ID.
- **message** (str): Message.

**Example:**

```python
response = forum.conversations.messages.edit(message_id=123456, message="Hello, world!")
print(response.json())
```


## List

GET https://api.zelenka.guru/conversations

*Get conversations.*

**Parameters:**

- **page** (int): Page.
- **limit** (int): Limit.

**Example:**

```python
response = forum.conversations.list(page=1, limit=10)
print(response.json())
```


## Get

GET https://api.zelenka.guru/conversations/{conversation_id}

*Get a conversation.*

**Parameters:**

- **conversation_id** (int): Conversation ID.

**Example:**

```python
response = forum.conversations.get(conversation_id=123456)
print(response.json())
```


## Create

POST https://api.zelenka.guru/conversations

**Create a conversation.**

**Parameters:**

- **user_id** (int): User ID.
- **message** (str): Message.

**Example:**

```python
response = forum.conversations.create(user_id=2410024, message="Hello, world!")
print(response.json())
```


## Create Group

POST https://api.zelenka.guru/conversations

**Create a group conversation.**

**Parameters:**

- **usernames** (list[str]): Usernames.
- **message** (str): Message.
- **title** (str): Title.
- **open_invite** (bool): Open invite.
- **conversation_locked** (bool): Conversation locked.
- **allow_edit_messages** (bool): Allow edit messages.

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


## Leave

DELETE https://api.zelenka.guru/conversations/{conversation_id}

**Leave from a conversation.**

**Parameters:**

- **conversation_id** (int): Conversation ID.
- **leave_type** (str): Leave type.

**Example:**

```python
response = forum.conversations.leave(conversation_id=123456, leave_type="delete")
print(response.json())
```


# Notifications

## List

GET https://api.zelenka.guru/notifications

*Get notifications.*

**Example:**

```python
response = forum.notifications.list()
print(response.json())
```


## Get

GET https://api.zelenka.guru/notifications/{notification_id}

*Get a notification.*

**Parameters:**

- **notification_id** (int): Notification ID.

**Example:**

```python
response = forum.notifications.get(notification_id=123456)
print(response.json())
```


## Read

POST https://api.zelenka.guru/notifications/read

**Read a notification.**

**Parameters:**

- **notification_id** (int): Notification ID.

**Example:**

```python
response = forum.notifications.read()
print(response.json())
```


# Tags

## List

GET https://api.zelenka.guru/tags/list

*Get tags.*

**Parameters:**

- **page** (int): Page.
- **limit** (int): Limit.

**Example:**

```python
response = forum.tags.list(page=1, limit=10)
print(response.json())
```


## Get

GET https://api.zelenka.guru/tags/{tag_id}

*Get a tag.*

**Parameters:**

- **tag_id** (int): Tag ID.
- **page** (int): Page.
- **limit** (int): Limit.

**Example:**

```python
response = forum.tags.get(tag_id=123456, page=1, limit=10)
print(response.json())
```


## Popular

GET https://api.zelenka.guru/tags/popular

*Get popular tags.*

**Example:**

```python
response = forum.tags.popular()
print(response.json())
```


## Search

GET https://api.zelenka.guru/tags/find

**Search for a tag.**

**Parameters:**

- **tag** (str): Tag.

**Example:**

```python
response = forum.tags.search(tag="example")
print(response.json())
```


# Search

## All

POST https://api.zelenka.guru/search

**Search for all types of content.**

**Parameters:**

- **query** (str): Query.
- **user_id** (int): User ID.
- **tag** (str): Tag.
- **forum_id** (int): Forum ID.
- **page** (int): Page.
- **limit** (int): Limit.

**Example:**

```python
response = forum.search.all(user_id=2410024, forum_id=876, page=1, limit=10)
print(response.json())
```


## Threads

POST https://api.zelenka.guru/search/threads

**Search for threads.**

**Parameters:**

- **query** (str): Query.
- **user_id** (int): User ID.
- **page** (int): Page.
- **limit** (int): Limit.

**Example:**

```python
response = forum.search.threads(user_id=2410024, page=1, limit=10)
print(response.json())
```


## Posts

POST https://api.zelenka.guru/search/posts

**Search for posts.**

**Parameters:**

- **query** (str): Query.
- **user_id** (int): User ID.
- **page** (int): Page.
- **limit** (int): Limit.

**Example:**

```python
response = forum.search.posts(user_id=2410024, page=1, limit=10)
print(response.json())
```


## Profile Posts

POST https://api.zelenka.guru/search/profile-posts

**Search for profile posts.**

**Parameters:**

- **query** (str): Query.
- **user_id** (int): User ID.
- **page** (int): Page.
- **limit** (int): Limit.

**Example:**

```python
response = forum.search.profile_posts(user_id=2410024, page=1, limit=10)
print(response.json())
```


## Tagged

POST https://api.zelenka.guru/search/tagged

**Search for tagged content.**

**Parameters:**

- **tag** (str): Tag.
- **tags** (list[str]): Tags.
- **page** (int): Page.
- **limit** (int): Limit.

**Example:**

```python
response = forum.search.tagged(tag="example", tags=["example", "example2"], page=1, limit=10)
print(response.json())
```


# Navigation

GET https://api.zelenka.guru/navigation

*Get navigation.*

**Parameters:**

- **parent** (int): Parent ID.

**Example:**

```python
response = forum.navigation()
print(response.json())
```


# Batch

POST https://api.zelenka.guru/batch

*Batch requests.*

**Parameters:**

- **jobs** (list[dict[str, str]]): Batch jobs.

**Example:**

```python
response = forum.batch(jobs=[{"method": "GET", "url": "/users/2410024", "params": {}}])
#  Also you can create jobs for almost all functions like this:
#  job = forum.users.get.job(user_id=2410024)
print(response.json())
```



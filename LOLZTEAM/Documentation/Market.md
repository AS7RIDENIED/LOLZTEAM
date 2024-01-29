<font size=6 style="margin: auto"> <center>

[Forum docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Forum.md) - [Antipublic Docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Antipublic.md)

</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

* [Profile](#profile)
  * [Get profile](#get-profile)
  * [Edit profile](#edit-profile)
* [List](#list)
  * [Category](#category)
    * [Steam](#steam)
      * [Get](#get)
      * [Params](#params)
      * [Games](#games)
    * [Fortnite](#fortnite)
      * [Get](#get-1)
      * [Params](#params-1)
    * [VK](#vk)
      * [Get](#get-2)
      * [Params](#params-2)
    * [Genshin Impact](#genshin-impact)
      * [Get](#get-3)
      * [Params](#params-3)
    * [Valorant](#valorant)
      * [Get](#get-4)
      * [Params](#params-4)
    * [League of Legends](#league-of-legends)
      * [Get](#get-5)
      * [Params](#params-5)
    * [Telegram](#telegram)
      * [Get](#get-6)
      * [Params](#params-6)
    * [Supercell](#supercell)
      * [Get](#get-7)
      * [Params](#params-7)
    * [Origin](#origin)
      * [Get](#get-8)
      * [Params](#params-8)
      * [Games](#games-1)
    * [World of Tanks](#world-of-tanks)
      * [Get](#get-9)
      * [Params](#params-9)
    * [World of Tanks Blitz](#world-of-tanks-blitz)
      * [Get](#get-10)
      * [Params](#params-10)
    * [Epicgames](#epicgames)
      * [Get](#get-11)
      * [Params](#params-11)
      * [Games](#games-2)
    * [Escape from Tarkov](#escape-from-tarkov)
      * [Get](#get-12)
      * [Params](#params-12)
    * [Social Club](#social-club)
      * [Get](#get-13)
      * [Params](#params-13)
    * [Uplay](#uplay)
      * [Get](#get-14)
      * [Params](#params-14)
      * [Games](#games-3)
    * [War Thunder](#war-thunder)
      * [Get](#get-15)
      * [Params](#params-15)
    * [Discord](#discord)
      * [Get](#get-16)
      * [Params](#params-16)
    * [Tiktok](#tiktok)
      * [Get](#get-17)
      * [Params](#params-17)
    * [Instagram](#instagram)
      * [Get](#get-18)
      * [Params](#params-18)
    * [Battle Net](#battle-net)
      * [Get](#get-19)
      * [Params](#params-19)
      * [Games](#games-4)
    * [VPN](#vpn)
      * [Get](#get-20)
      * [Params](#params-20)
    * [Cinema](#cinema)
      * [Get](#get-21)
      * [Params](#params-21)
    * [Spotify](#spotify)
      * [Get](#get-22)
      * [Params](#params-22)
    * [Warface](#warface)
      * [Get](#get-23)
      * [Params](#params-23)
    * [Youtube](#youtube)
      * [Get](#get-24)
      * [Params](#params-24)
  * [Get item](#get-item)
  * [Latest items](#latest-items)
  * [From url](#from-url)
  * [Viewed accounts](#viewed-accounts)
  * [Favorite accounts](#favorite-accounts)
  * [Purchased accounts](#purchased-accounts)
  * [Owned accounts](#owned-accounts)
* [Purchasing](#purchasing)
  * [Auction](#auction)
    * [Get auction bids](#get-auction-bids) 
    * [Place auction bid](#place-auction-bid)
    * [Delete auction bid](#delete-auction-bid)
  * [Fast buy](#fast-buy)
  * [Check](#check)
  * [Confirm buy](#confirm-buy)
  * [Reserve](#reserve)
  * [Cancel reserve](#cancel-reserve)
* [Publishing](#publishing)
  * [Fast sell](#fast-sell)
  * [Add](#add)
  * [Check](#check-1)
  * [Info](#info)
* [Managing](#managing)
  * [Tag](#tag)
    * [Add tag](#add-tag)
    * [Delete tag](#delete-tag)
  * [Edit](#edit-)
  * [Delete](#delete)
  * [Steam inventory value](#steam-inventory-value)
  * [Change owner](#change-owner)
  * [Change password](#change-password)
  * [Bump](#bump)
  * [Get email code](#get-email-code)
  * [Get steam guard](#get-steam-guard)
  * [Get mafile](#get-mafile)
  * [Get temp mail password](#get-temp-mail-password)
  * [Get telegram confirmation code](#get-telegram-confirmation-code)
  * [Reset telegram authorizations](#reset-telegram-authorizations)
  * [Refuse guaranteee](#refuse-guarantee)
  * [Favorite](#favorite)
  * [Unfavorite](#unfavorite)
  * [Stick](#stick)
  * [Unstick](#unstick)
* [Payments](#payments)
  * [History](#history)
  * [Transfer](#transfer)
  * [Generate payment link](#generate-payment-link)
* [Proxy](#proxy)
  * [Get proxies](#get-proxies)
  * [Add proxy](#add-proxy)
  * [Delete proxy](#delete-proxy)
* [Get batch job](#get-batch-job)
* [Batch](#batch)
* [Send async](#send-async)

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
  > You can get in there -> https://zelenka.guru/account/api
- **bypass_429** (bool): Bypass status code 429 by sleep
  > It's True by default. You can skip it or set False if you want
- **language** (str): Language for your api responses. 
  > Pass "en" if you want to get responses in english or pass "ru" if you want to get responses in russian.
- **proxy_type** (str): Your proxy type. 
  > You can use types ( Constants.Proxy.socks5 or socks4,https,http )
- **proxy** (str): Proxy string. 
  > Example -> ip:port or login:password@ip:port

# Profile

*Methods to get and edit profile info*

### Get profile

*Displays info about your profile.*

*[Official documentation reference](https://lzt-market.readme.io/reference/marketprofilesettingsgetinfo)*

**Example:**

```python
response = market.profile.get()
print(response.json())
```

```python
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_email': 'string', 'user_unread_notification_count': 0, 'user_dob_day': 0, 'user_dob_month': 0, 'user_dob_year': 0, 'user_title': 'string', 'user_last_seen_date': 0, 'balance': 0, 'hold': 0, 'system_info': {'visitor_id': 0, 'time': 0}}}
```

### Edit profile

*Change settings about your profile on the market.*

*[Official documentation reference](https://lzt-market.readme.io/reference/marketprofilesettingsgetsettings)*

**Parameters:**

- **disable_steam_guard** (bool): Disable Steam Guard on account purchase moment
- **deauthorize_steam** (bool): Finish all Steam sessions after purchase
- **user_allow_ask_discount** (bool): Allow users ask discount for your accounts
- **max_discount_percent** (int): Maximum discount percents for your accounts
- **allow_accept_accounts** (str): Usernames who can transfer market accounts to you. Separate values with a comma.
- **hide_favourites** (bool): Hide your profile info when you add an account to favorites
- **hide_bids** (bool): Hide your profile when bid on the auction
- **vk_ua** (str): Your vk useragent to accounts.
- **title** (str): Market title.
- **telegram_client** (dict): Telegram client. It should be {"telegram_api_id": 12345, "telegram_api_hash": "12345","telegram_device_model":"12345","telegram_system_version":"12345","telegram_app_version":"12345"}

**Example:**

```python
response = market.profile.edit(user_allow_ask_discount=True)
print(response.json())
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

# List

*Methods for getting account lists*

---

## Category

---

### Steam

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.steam.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.steam.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

#### Games

*Displays a list of games in the category.*

**Example:**

```python
response = market.list.category.steam.games()
print(response.json())
```

```python
{'games': [{'app_id': 'string', 'title': 'string', 'abbr': 'string', 'category_id': 0, 'img': 'string', 'url': 'string', 'ru': ['string']}], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': True, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---


### Fortnite

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.fortnite.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.fortnite.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### VK

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.vk.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.vk.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Genshin impact

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.genshin.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.genshin.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Valorant

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.valorant.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.valorant.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### League of Legends

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.lol.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.lol.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Telegram

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.telegram.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.telegram.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Supercell

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.supercell.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.supercell.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Origin

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.origin.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.origin.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

#### Games

*Displays a list of games in the category.*

**Example:**

```python
response = market.list.category.origin.games()
print(response.json())
```

```python
{'games': [{'app_id': 'string', 'title': 'string', 'abbr': 'string', 'category_id': 0, 'img': 'string', 'url': 'string', 'ru': ['string']}], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': True, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### World of Tanks

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.wot.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.wot.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### World of Tanks Blitz

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.wot_blitz.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.steam.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Epicgames

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.epicgames.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.epicgames.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

#### Games

*Displays a list of games in the category.*

**Example:**

```python
response = market.list.category.epicgames.games()
print(response.json())
```

```python
{'games': [{'app_id': 'string', 'title': 'string', 'abbr': 'string', 'category_id': 0, 'img': 'string', 'url': 'string', 'ru': ['string']}], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': True, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Escape from Tarkov

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.eft.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.eft.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Social Club

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.socialclub.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.socialclub.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

#### Games

*Displays a list of games in the category.*

**Example:**

```python
response = market.list.category.socialclub.games()
print(response.json())
```

```python
{'games': [{'app_id': 'string', 'title': 'string', 'abbr': 'string', 'category_id': 0, 'img': 'string', 'url': 'string', 'ru': ['string']}], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': True, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Uplay

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.uplay.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.uplay.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

#### Games

*Displays a list of games in the category.*

**Example:**

```python
response = market.list.category.uplay.games()
print(response.json())
```

```python
{'games': [{'app_id': 'string', 'title': 'string', 'abbr': 'string', 'category_id': 0, 'img': 'string', 'url': 'string', 'ru': ['string']}], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': True, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### War Thunder

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.war_thunder.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.war_thunder.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Discord

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.discord.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.discord.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### TikTok

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.tiktok.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.tiktok.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Instagram

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.instagram.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.instagram.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Battle Net

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.battlenet.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.battlenet.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

#### Games

*Displays a list of games in the category.*

**Example:**

```python
response = market.list.category.battlenet.games()
print(response.json())
```

```python
{'games': [{'app_id': 'string', 'title': 'string', 'abbr': 'string', 'category_id': 0, 'img': 'string', 'url': 'string', 'ru': ['string']}], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': True, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### VPN

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.vpn.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.vpn.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Cinema

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.cinema.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.cinema.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Spotify

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.spotify.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.spotify.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Warface

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.warface.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.warface.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### YouTube

#### Get

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **auction** (str): Auction. Can be [yes, no, nomatter].
- **title** (str): The word or words contained in the account title
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **origin** (strorlist): List of account origins.
- **not_origin** (strorlist): List of account origins that won't be included.
- **order_by** (str): Order by. Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **sold_before** (bool): Sold before.
- **sold_before_by_me** (bool): Sold before by me.
- **not_sold_before** (bool): Not sold before.
- **not_sold_before_by_me** (bool): Not sold before by me.
- **search_params** (dict): Search params for your request. Example {"mafile":"yes"} in steam category will return accounts that have mafile

**Example:**

```python
response = market.list.category.youtube.get(pmax=50, origin=[Constants.Market.ItemOrigin.brute, Constants.Market.ItemOrigin.retrieve])
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

#### Params

*Displays search parameters for a category.*

**Example:**

```python
response = market.list.category.youtube.params()
print(response.json())
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Get categories

*Display category list.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountspublishinggetcategories)*

**Parameters:**

- **top_queries** (bool): Display top queries for per category.

**Example:**

```python
response = market.list.category.list()
print(response.json())
```

```python
{'0': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Get item

*Displays item information or returns Steam account html code.*

*[Official documentation reference (item info)](https://lzt-market.readme.io/reference/accountslistgetinformation)*
*[Official documentation reference (steam html)](https://lzt-market.readme.io/reference/accountslistgetsteamhtml)*

**Parameters:**

- **item_id** (int): ID of item.
- **steam_preview** (bool): Steam preview
  > Set it True if you want to get steam html and False/None if you want to get item info
- **preview_type** (str): Type of page. 
  > Can be "profiles" or "games"

**Example:**

```python
response = market.list.get(item_id=2410024)
print(response.json())
```

```python
{'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'seller': {'user_id': 0, 'username': 'string', 'avatar_date': 0, 'user_group_id': 0, 'secondary_group_ids': 'string', 'display_style_group_id': 0, 'uniq_username_css': 'string'}}
```

### Latest items

*Displays a list of the latest accounts.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountslistgetlatest)*

**Parameters:**

- **page** (int): The number of the page to display results from
- **title** (str): The word or words contained in the account title
- **search_params** (dict): Search params for your request.
  > Example {"category_id":19} will return only VPN accounts

**Example:**

```python
response = market.list.new()
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### From url

*Displays a list of the latest accounts from your market url with search params.*

**Parameters:**

- **url** (str): Your market search url.
  > It can be https://lzt.market or https://lzt.market

**Example:**

```python
response = market.list.from_url(url="https://lzt.market/steam/cs-go-prime?origin[]=fishing&eg=1")
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### Viewed accounts

*Displays a list of viewed accounts.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountslistgetviewed)*

**Parameters:**

- **page** (int): The number of the page to display results from
- **status** (str): Account status.
  > Can be [active, paid, deleted or awaiting].

  > You also can use types - Constants.Market.ItemStatus
- **title** (str): The word or words contained in the account title
- **search_params** (dict): Search params for your request. 
  > Example {"category_id":19} will return only VPN accounts

**Example:**

```python
response = market.list.viewed()
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### Favorite accounts

*Displays a list of favorite accounts.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountslistgetfavorite)*

**Parameters:**

- **page** (int): The number of the page to display results from
- **status** (str): Account status.
  > Can be [active, paid, deleted or awaiting].

  > You also can use types - Constants.Market.ItemStatus
- **title** (str): The word or words contained in the account title
- **search_params** (dict): Search params for your request.
  > Example {"category_id":19} will return only VPN accounts

**Example:**
```python
response = market.list.favorite()
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}

```

### Purchased accounts

*Displays a list of purchased accounts.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountslistgetpurchased)*

**Parameters:**

- **user_id** (int): ID of user.
- **page** (int): Page
- **category_id** (int): Accounts category
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **title** (str): The word or words contained in the account title
- **search_params** (dict): Search params for your request. 
  > Example {"category_id":19} will return only VPN accounts
- **status** (str): Account status.
  > Can be [active, paid, deleted or awaiting].

  > You also can use types - Constants.Market.ItemStatus
- **order** (str): Order type.
  > Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_up, pdate_to_down_upload, pdate_to_up_upload].

  >You also can use types - Constants.Market.Order

**Example:**

```python
response = market.list.purchased()
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### Owned accounts

*Displays a list of owned accounts.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountslistgetowned)*

**Parameters:**

- **user_id** (int): ID of user.
  > It will set automatically if you didn't but take addictional 3 seconds
- **page** (int): Page
- **category_id** (int): Accounts category
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **title** (str): The word or words contained in the account title
- **search_params** (dict): Search params for your request. 
  > Example {"category_id":19} will return only VPN accounts
- **status** (str): Account status. 
  > Can be [active, paid, deleted or awaiting].

  > You also can use types - Constants.Market.ItemStatus
- **order** (str): Order type.
  > Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_up, pdate_to_down_upload, pdate_to_up_upload].

  >You also can use types - Constants.Market.Order

**Example:**

```python
response = market.list.owned()
print(response.json())
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

# Purchasing

*Methods for item purchasing*

## Auction

---

### Get auction bids

*Display a list of bids in the auction.*

*[Official documentation reference](https://lzt-market.readme.io/reference/auctionget)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.purchasing.auction.get(item_id=2410024)
print(response.json())
```

```python
{'itemId': 0, 'bids': [{'bid_id': 0, 'bid_value': {'rub': 'string', 'uah': 'string', 'kzt': 'string', 'byn': 'string', 'usd': 'string', 'eur': 'string', 'gbp': 'string', 'cny': 'string', 'try': 'string'}, 'minAllowedBidValue': {'rub': 0, 'uah': 0, 'kzt': 0, 'byn': 0, 'usd': 0, 'eur': 0, 'gbp': 0, 'cny': 0, 'try': 0}, 'bid_previous_value': {'rub': 'string', 'uah': 'string', 'kzt': 'string', 'byn': 'string', 'usd': 'string', 'eur': 'string', 'gbp': 'string', 'cny': 'string', 'try': 'string'}, 'user': {'user_id': 0, 'avatar': 'string', 'usernameHtml': 'string'}, 'bid_date': 0, 'canCancelBid': False, 'endTimeAuction': 0}], 'is_finished': 0, 'endTime': 0, 'currencies': {'{currency}': {'title': 'string', 'symbol': 'string', 'rate': {'Value': 0, 'Nominal': 0}}}, 'userCurrency': 'string', 'minAllowedBidValue': {'rub': 0, 'uah': 0, 'kzt': 0, 'byn': 0, 'usd': 0, 'eur': 0, 'gbp': 0, 'cny': 0, 'try': 0}, 'startValue': {'rub': 0, 'uah': 0, 'kzt': 0, 'byn': 0, 'usd': 0, 'eur': 0, 'gbp': 0, 'cny': 0, 'try': 0}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Place auction bid

*Create a new auction bid.*

*[Official documentation reference](https://lzt-market.readme.io/reference/auctionpostbid)*

**Parameters:**

- **item_id** (int): ID of item.
- **amount** (int): Amount bid.
- **currency** (str): Bid currency.
  > Can be [rub, uah, kzt, byn, usd, eur, gbp, cny, try].

**Example:**

```python
response = market.purchasing.auction.place_bid(item_id=2410024, amount=250)
print(response.json())
```

```python
{'status': 'ok', 'bid': {'bid_id': 0, 'bid_value': {'rub': 'string', 'uah': 'string', 'kzt': 'string', 'byn': 'string', 'usd': 'string', 'eur': 'string', 'gbp': 'string', 'cny': 'string', 'try': 'string'}, 'minAllowedBidValue': {'rub': 0, 'uah': 0, 'kzt': 0, 'byn': 0, 'usd': 0, 'eur': 0, 'gbp': 0, 'cny': 0, 'try': 0}, 'bid_previous_value': {'rub': 'string', 'uah': 'string', 'kzt': 'string', 'byn': 'string', 'usd': 'string', 'eur': 'string', 'gbp': 'string', 'cny': 'string', 'try': 'string'}, 'user': {'user_id': 0, 'avatar': 'string', 'usernameHtml': 'string'}, 'bid_date': 0, 'canCancelBid': False, 'endTimeAuction': 0}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete auction bid

*Delete your auction bid.*

*[Official documentation reference](https://lzt-market.readme.io/reference/auctiondeletebid)*

**Parameters:**

- **item_id** (int): ID of item.
- **bid_id** (int): ID of bid.

**Example:**

```python
response = market.purchasing.auction.delete_bid(item_id=2410024, bid_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'The bid success deleted', 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Fast buy

*Check and buy account.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountspurchasingcheckbuy)*

**Parameters:**

- **item_id** (int): ID of item.
- **price** (int): Current price of account in your currency
- **buy_without_validation** (bool): Buy account without validation
  > Use TRUE if you want to buy account without account data validation (not safe)

**Example:**

```python
response = market.purchasing.fast_buy(item_id=2410024,price=10)
print(response.json())
```

```python
{'status': 'ok', 'reserve_end_date': 0, 'item': {'account': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Check

*Checking account for validity. If the account is invalid, the purchase will be canceled automatically.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountspurchasingcheck)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.purchasing.check(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'item': {'account': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Confirm buy

*Confirm buy.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountspurchasingconfirmbuy)*

**Parameters:**

- **item_id** (int): ID of item.
- **buy_without_validation** (bool): Buy account without validation
  > Use TRUE if you want to buy account without account data validation (not safe)

**Example:**

```python
response = market.purchasing.confirm(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'item': {'account': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Reserve

*Reserves account for you.*
  > Reserve time - 300 seconds.

*[Official documentation reference](https://lzt-market.readme.io/reference/accountspurchasingsetreserve)*

**Parameters:**

- **item_id** (int): ID of item.
- **price** (int): Current price of account in your currency

*Example:*

```python
response = market.purchasing.reserve(item_id=2410024,price=10)
print(response.json())
```

```python
{'status': 'ok', 'reserve_end_date': 0, 'item': {'account': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Cancel reserve

*Cancels reserve.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountspurchasingcancelreserve)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.purchasing.reserve_cancel(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

# Publishing

*Methods for item publishing*

### Fast sell

*Adds and check account on validity. If account is valid, account will be published on the market.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountpublishingfastsell)*

**Parameters:**

- **category_id** (int): Accounts category.
- **price** (int): Account price in your currency.
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
- **email_login_data** (str): Required if a category is one of list of Required email login data categories. 
  > Email login data (login:pass format).
- **email_type** (str): Email type.
  > Use types -> Constants.Market.ItemOrigin
- **allow_ask_discount** (bool): Allow users to ask discount for this account.
- **proxy_id** (int): Using proxy id for account checking.
- **random_proxy** (bool): Pass True, if you get captcha in previous response
- **login** (str): Account login (or email)
- **password** (str): Account password
- **login_password** (str): Account login data
  > Format - login:password
- **extra** (dict): Extra params for account checking.
  > E.g. you need to put cookies to extra (extra={"cookies": cookies}) if you want to upload TikTok/Fortnite/Epic Games account
- **auction** (bool): Pass True if you want to create auction
- **auction_duration_value** (int): Duration auction value.
- **auction_duration_option** (str): Duration auction option. Can be [minutes, hours, days].
- **instabuy_price** (int): The price for which you can instantly redeem your account.
- **not_bids_action** (str): If you set cancel, at the end of the auction with 0 bids, the account can be purchased at the price you specified as the minimum bid. Can be [close, cancel]

**Example:**

```python
response = market.publishing.fast_sell(category_id=Constants.Market.CategoryID.vk, price=10,
                                       currency=Constants.Market.Currency.rub, item_origin=Constants.Market.ItemOrigin.autoreg,
                                       extended_guarantee=Constants.Market.Guarantee.day, title="Acc vk",
                                       allow_ask_discount=True, login_password="Login:password")
print(response.json())
```

```python
{'status': 'ok', 'message': 'string', 'item': {'item_id': 0, 'item_state': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Add

*Adds account on the market.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountpublishingadditem)*

**Parameters:**

- **category_id** (int): Accounts category.
- **price** (int): Account price in your currency.
- **currency** (str): Using currency.
- **item_origin** (str): Account origin.
- **extended_guarantee** (int): Guarantee type.
- **title** (str): Russian title of account.
  > If title specified and title_en is empty, title_en will be automatically translated to English language.
- **title_en** (str): English title of account. 
  > If title_en specified and title is empty, title will be automatically translated to Russian language.
- **description** (str): Account public description.
- **information** (str): Account private information (visible for buyer only if purchased).
- **has_email_login_data** (bool): Required if a category is one of list of Required email login data categories.
- **email_login_data** (str): Required if a category is one of list of Required email login data categories. 
  > Email login data (login:pass format).
- **email_type** (str): Email type.
- **allow_ask_discount** (bool): Allow users to ask discount for this account.
- **proxy_id** (int): Using proxy id for account checking.
- **random_proxy** (bool): Pass True, if you get captcha in previous response
- **auction** (bool): Pass True if you want to create auction
- **auction_duration_value** (int): Duration auction value.
- **auction_duration_option** (str): Duration auction option. Can be [minutes, hours, days].
- **instabuy_price** (int): The price for which you can instantly redeem your account.
- **not_bids_action** (str): If you set cancel, at the end of the auction with 0 bids, the account can be purchased at the price you specified as the minimum bid. Can be [close, cancel]

**Example:**

```python
response = market.publishing.add(category_id=Constants.Market.CategoryID.vk, price=10,
                                 currency=Constants.Market.Currency.rub, item_origin=Constants.Market.ItemOrigin.autoreg,
                                 extended_guarantee=Constants.Market.Guarantee.day, title="Acc vk",
                                 allow_ask_discount=True)
print(response.json())
```

```python
{'status': 'ok', 'item': {'item_id': 0, 'item_state': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Check

*Check and put up to sale not published account OR update account information existing account.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountspublishingchecknotpublic)*

**Parameters:**

- **item_id** (int): ID for item.
- **login** (str): Account login (or email)
- **password** (str): Account password
- **login_password** (str): Account login data 
  > Format login:password
- **close_item** (bool): Close item or not.
  > If True, the item will be closed item_state = closed
- **extra** (dict): Extra params for account checking. 
  > E.g. you need to put cookies to extra[cookies] if you want to upload TikTok/Fortnite/Epic Games account
- **resell_item_id** (int): Resell item id
  > Put item id, if you are trying to resell item.
- **random_proxy** (bool): Use random proxy
  > Pass True, if you get captcha in previous response

**Example:**

```python
response = market.publishing.check(item_id=2410024,login_password="Login:password")
print(response.json())
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Info

*Get info about not published item. For categories, which required temporary email (Steam, Social Club), you will get temporary email in response.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountspublishinggetinfonotpublic)*

**Parameters:**

- **item_id** (int): ID of item.
- **resell_item_id** (int): Put item id, if you are trying to resell item.
  > This is useful to pass temporary email from reselling item to new item. 
  
  > You will get same temporary email from reselling account.

**Example:**

```python
response = market.publishing.info(item_id=2410024)
print(response.json())
```

```python
{'status': 'string', 'item': {'item_id': 0, 'item_state': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}, 'temp_email': 'string', 'sessionLoginData': ['string'], 'ignoreCookieUpload': True}
```

# Managing

*Methods for account managing*

---

## Tag

*Methods for items tagging*

### Add tag

*Adds tag for the account.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingaddtag)*

**Parameters:**

- **item_id** (int): ID of item.
- **tag_id** (int): Tag id. Tag list is available via market.profile.get()

**Example:**

```python
response = market.managing.tag.add(item_id=2410024, tag_id=1)
print(response.json())
```

```python
{'itemId': 0, 'tag': {'tag_id': 0, 'title': 'string', 'isDefault': True, 'forOwnedAccountsOnly': True, 'bc': 'string'}, 'addedTagId': 0, 'deleteTags': [0], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete tag

*Deletes tag for the account.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingdeletetag)*

**Parameters:**

- **item_id** (int): ID of item.
- **tag_id** (int): Tag id. Tag list is available via market.profile.get()

**Example:**

```python
response = market.managing.tag.delete(item_id=2410024, tag_id=1)
print(response.json())
```

```python
{'itemId': 0, 'tag': {'tag_id': 0, 'title': 'string', 'isDefault': True, 'forOwnedAccountsOnly': True, 'bc': 'string'}, 'addedTagId': 0, 'deleteTags': [0], 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Edit 

*Edits any details of account.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingedit)*

**Parameters:**

- **item_id** (int): ID of item.
- **price** (int): Account price in your currency.
- **currency** (str): Using currency. 
- **item_origin** (str): Account origin. Where did you get it from.
- **title** (str): Russian title of account. 
  > If title specified and title_en is empty, title_en will be automatically translated to English language.
- **title_en** (str): English title of account.
  > If title_en specified and title is empty, title will be automatically translated to Russian language.
- **description** (str): Account public description.
- **information** (str): Account private information (visible for buyer only if purchased).
- **email_login_data** (str): Required if a category is one of list of Required email login data categories. 
  > Email login data (login:pass format).
- **email_type** (str): Email type.
- **allow_ask_discount** (bool): Allow users to ask discount for this account.
- **proxy_id** (int): Using proxy id for account checking.

**Example:**

```python
response = market.managing.edit(item_id=2410024,price=777)
print(response.json())
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete

*Deletes your account from public search. Deletion type is soft. You can restore account after deletion if you want.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingdelete)*

**Parameters:**

- **item_id** (int): ID of item.
- **reason** (str): Delete reason.

**Example:**

```python
response = market.managing.delete(item_id=2410024,reason="Im gay")
print(response.json())
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Steam inventory value

*Gets steam value.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanaginggetsteamvalue)*

**Parameters:**

- **url** (str): Link or id of account. 
  > Can be [https://lzt.market/{item-id}/, https://steamcommunity.com/id/{steam-name}, https://steamcommunity.com/profiles/{steam-id}, {steam-id}].
- **app_id** (int): Application id.
  > You can use Types. Check example below
- **currency** (str): Using currency for amount.
  > You can use Types. Check example below
- **ignore_cache** (bool): Ignore cache.
  > If you pass False (default) market api will take inventory from cache (Inventory can be outdated). If you pass True inventory will reparse and you get price at current moment

**Example:**

```python
response = market.managing.steam_inventory_value(url="https://steamcommunity.com/id/AS7RID",currency=Constants.Market.Currency.rub,app_id=Constants.Market.AppID.CSGO)
print(response.json())
```

```python
{'query': 'https://steamcommunity.com/id/AS7RID', 'data': {'items': {'5189384637': {'classid': '5189384637', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQNqhpOSV-fRPasw8rsUFJ5KBFZv668FFQynaHMJT9B74-ywtjYxfOmMe_Vx28AucQj3brAoYrz3Fay_kY4MG_wdYeLMlhpLMaM-1U', 'title': 'Revolution Case', 'price': 112.3, 'count': '1', 'stickers': None, 'type': 'Base Grade Container', 'market_hash_name': 'Revolution%20Case', 'fraudwarnings': None}, '3946324730': {'classid': '3946324730', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQNqhpOSV-fRPasw8rsUFJ5KBFZv668FFU2nfGaJG0btN2wwYHfxa-hY-uFxj4Dv50nj7uXpI7w3AewrhBpMWH6d9CLMlhpEbAe-Zk', 'title': 'Fracture Case', 'price': 59.05, 'count': '1', 'stickers': None, 'type': 'Base Grade Container', 'market_hash_name': 'Fracture%20Case', 'fraudwarnings': None}, '3220810394': {'classid': '3220810394', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou6ryFAR17P7YJgJQ7d-9kZSOkuXLPr7Vn35cppB0ievCp9322VKyrkVrN2z6dtOSdVQ8MAyD-QC6lb26gZe7tZrMmnF9-n51z91ErA0', 'title': 'StatTrak™ MP7 | Mischief (Field-Tested)', 'price': 46.47, 'count': '1', 'stickers': None, 'type': 'StatTrak™ Mil-Spec Grade SMG', 'market_hash_name': 'StatTrak%E2%84%A2%20MP7%20%7C%20Mischief%20%28Field-Tested%29', 'fraudwarnings': None}, '3591173339': {'classid': '3591173339', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposbaqKAxf0Ob3djFN79eJkIWKg__gPLfdqWZU7Mxkh6eToY2l3wy2rkFkNmj0JYaTcQY8YV-BqATrweu615-4u5zLnHVl6CJz-z-DyCIevZ0V', 'title': 'Glock-18 | Catacombs (Field-Tested)', 'price': 24.2, 'count': '1', 'stickers': {'stickerCount': 4, 'patchCount': 0, 'count': 4, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Mil-Spec Grade Pistol', 'market_hash_name': 'Glock-18%20%7C%20Catacombs%20%28Field-Tested%29', 'fraudwarnings': None}, '3035569050': {'classid': '3035569050', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLOzLhRlxfbGTjVb09ijl5SYqPDmNr7fqWdY781lxL-Zoo-hiVC1_BJsam37I4TAJ1Q7M1zYqQPol-2618fvupWYwSZk73Q8pSGKLd3ROFw', 'title': 'Five-SeveN | Coolant (Factory New)', 'price': 6.78, 'count': '1', 'stickers': None, 'type': 'Consumer Grade Pistol', 'market_hash_name': 'Five-SeveN%20%7C%20Coolant%20%28Factory%20New%29', 'fraudwarnings': None}, '3035569189': {'classid': '3035569189', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou6r8FA957ODYfTxW-Nmkx7-HnvD8J_XUzjwJupdw3-rA8I6jiQPl80I5Yzz7IoCTcwRtZl3VrFa2l-jp18O9ot2XnhWS9Knh', 'title': 'MP9 | Slide (Minimal Wear)', 'price': 4.84, 'count': '1', 'stickers': None, 'type': 'Consumer Grade SMG', 'market_hash_name': 'MP9%20%7C%20Slide%20%28Minimal%20Wear%29', 'fraudwarnings': None}, '3035580092': {'classid': '3035580092', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpoo7e1f1Jf2-r3czFX6cyknY6fqPX4Jr7Dk29u4MBwnPCP8d-iilGwqhVpYzzwLIeVcgNoY1zSq1bqlOm5hJ687ZzJmHVkvXN2tmGdwUIRV2k43w', 'title': 'UMP-45 | Facility Dark (Battle-Scarred)', 'price': 3.87, 'count': '1', 'stickers': None, 'type': 'Consumer Grade SMG', 'market_hash_name': 'UMP-45%20%7C%20Facility%20Dark%20%28Battle-Scarred%29', 'fraudwarnings': None}, '310777179': {'classid': '310777179', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpouLWzKjhz3MzbcDNG09GzkImemrnwYOOGwjIJ7JB1j-3D9Nms0FDh_0tqYjulLNCWdFNvZl7QrlPswOu6m9bi6_rlVdP1', 'title': 'Nova | Sand Dune (Field-Tested)', 'price': 3.87, 'count': '1', 'stickers': None, 'type': 'Consumer Grade Shotgun', 'market_hash_name': 'Nova%20%7C%20Sand%20Dune%20%28Field-Tested%29', 'fraudwarnings': None}, '1989297441': {'classid': '1989297441', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0su2fDm25bWCWeXKPT1sxTLBaYDrb-GX2t7_BQ2rOFbotEVhXLKoCpzBJNciBOQx9itAdqGq0mFZwCxo8e9VKaVLjnSBHZelHVPZFwA', 'title': 'Sealed Graffiti | Sorry (Brick Red)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20Sorry%20%28Brick%20Red%29', 'fraudwarnings': None}, '1989279141': {'classid': '1989279141', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0suOBCG25Pm-Te3WBHg84T7ZdPT6N-WChtOqVE2vAEuglSwECf_cM9mIdbprYPgx9itAdqGq0mFZwCxo8e9VKaVK4m3dCMuyaadCusA', 'title': 'Sealed Graffiti | NaCl (Shark White)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20NaCl%20%28Shark%20White%29', 'fraudwarnings': None}, '1989299897': {'classid': '1989299897', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0o_ePHnjyVzPBLiWXSgw9TrMMY2jbqGCm5OvCF27BF-4tRFtVfqoApzJNNc7YPRo60IQN8iuomUM7HRkkfddLZQOvw2QfKOAhnCJLcMkz1YlJgQ', 'title': 'Sealed Graffiti | Death Sentence (Tracer Yellow)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20Death%20Sentence%20%28Tracer%20Yellow%29', 'fraudwarnings': None}, '1989288246': {'classid': '1989288246', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0rO2BBTqjOWGReHiLGV9uH7ZbY2ve9zKtsemWRG3BEuotQg9Ve6pX-m1IPMGNIVJjg5FYpGm3hUloEgIhYslfLVm-nnJKNxikjmox', 'title': 'Sealed Graffiti | Toasted (Monster Purple)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20Toasted%20%28Monster%20Purple%29', 'fraudwarnings': None}, '1989276589': {'classid': '1989276589', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0pO-CI3DyeyfFJjOXS1s9SOJZZ2rb9zXx5OrAFjDOE-1_R1pQKaNW8TUbOs-LPxJo1I8JqiuomUM7HRkkfddLZQOvw2QfKOAhnCJLcMm5ggoI_A', 'title': 'Sealed Graffiti | QQ (Tracer Yellow)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20QQ%20%28Tracer%20Yellow%29', 'fraudwarnings': None}, '4302203091': {'classid': '4302203091', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9QVcJY8gulRPQV6CF7b9mNvbRRMjdgIO5ez2flZj0qTKI24TuNi1x9bexqakZe2JzjIIuMMh2rHEotqgxkS6rPdFh4ZR', 'title': 'Sticker | 100 Thieves | 2020 RMR', 'price': 2.9, 'count': 24, 'stickers': None, 'type': 'High Grade Sticker', 'market_hash_name': 'Sticker%20%7C%20100%20Thieves%20%7C%202020%20RMR', 'fraudwarnings': None}, '1989287941': {'classid': '1989287941', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0ovCCC3q5bDOdLCSNHgpqT7JdNDzf_jH05-jCRDmcQ-t4Q1tRLqZW-mVBa8_YOQx9itAdqGq0mFZwCxo8e9VKaVLtzyAVaLvjeQiSVQ', 'title': 'Sealed Graffiti | King Me (Monster Purple)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20King%20Me%20%28Monster%20Purple%29', 'fraudwarnings': None}, '3496846827': {'classid': '3496846827', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaO1U1g72Ycz4bvYzvxdLakfWnYuPQxWlTuZ133O_ArN6j0Qa3_BI9Z2rwJoaQbEZgNvzyEwH0', 'title': 'P250', 'price': None, 'count': '1', 'stickers': {'stickerCount': 3, 'patchCount': 0, 'count': 3, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Pistol', 'market_hash_name': 'P250', 'fraudwarnings': None}, '3515046014': {'classid': '3515046014', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaOBRng6uGI2oT7YTjwobex_HwZbrSxzsAvJYi3rmYrY6kiQDnr0VtMT2ndo6ccBh-Pw_WKbm-EQ', 'title': 'SSG 08', 'price': None, 'count': '1', 'stickers': {'stickerCount': 3, 'patchCount': 0, 'count': 3, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Sniper Rifle', 'market_hash_name': 'SSG%2008', 'fraudwarnings': None}, '3528419424': {'classid': '3528419424', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaLAZs2v_JY3NAtIjnwdPdwq_1Nb_TwW9SupNw07GUoYmg3gKyrxZvNTr3JtWXcFNofxiOrQoC97_e', 'title': 'Galil AR', 'price': None, 'count': '1', 'stickers': {'stickerCount': 3, 'patchCount': 0, 'count': 3, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Rifle', 'market_hash_name': 'Galil%20AR', 'fraudwarnings': None}, '1989274499': {'classid': '1989274499', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0ovCCC3q5bDOdLCSNHgpqT7JdNDzf_jH05-jCRDmcQ-t4Q1tRLqZW-mVBa8_YOQx9itAdqGq0mFZwCxo8e9VKaVK4m3dCMuyX6bcTBg', 'title': 'Graffiti | King Me (Shark White)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20King%20Me%20%28Shark%20White%29', 'fraudwarnings': None}, '1989275289': {'classid': '1989275289', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0tuuDG2e5P2DBfnWMGg0_RLtbND6N-WDwse2VSmmdE74oEF0CdKUB-jcYbMuBagx9itAdqGq0mFZwCxo8e9VKaVK4m3dCMuyY2Tc6Pw', 'title': 'Graffiti | Take Flight (Shark White)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20Take%20Flight%20%28Shark%20White%29', 'fraudwarnings': None}, '1989275676': {'classid': '1989275676', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0pveDD3n4YzKKdieBTAhpH7ZbMD3R_Gfx5L6cFDrNQu8uEgFRe_NXoDAfPcuAPRM80ZlLpWL-lEtxEQQlZ8lSeR-30ykQYL50y3ClvG56Ng', 'title': 'Graffiti | Quickdraw (Shark White)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20Quickdraw%20%28Shark%20White%29', 'fraudwarnings': None}, '1989270691': {'classid': '1989270691', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0pe2BEHXlJjadf3HcTQswSrJbPD6IrTak5O6dQDjPRbklQVpSf_BR9zAfPsiNPRIjlNlc7Wa3m0tvEwMkZsxWfBbmniVEMOkkivTsgr4', 'title': 'Graffiti | Keep the Change (Jungle Green)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20Keep%20the%20Change%20%28Jungle%20Green%29', 'fraudwarnings': None}, '3653202725': {'classid': '3653202725', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fVOG_wcbQVmJ5IABWuoX3e1Uw7P_efWwMudjnzNaJlKH3Zu2EkDMGv8ByjuiToI2tigbg-kplYj3xdY6cIFVtM0aQpAYy5bU4zQ', 'title': '2020 Service Medal', 'price': None, 'count': '1', 'stickers': None, 'type': 'Extraordinary Collectible', 'market_hash_name': '2020%20Service%20Medal', 'fraudwarnings': None}, '1989274048': {'classid': '1989274048', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0pO-CI2P4eiXdYSKKHQw9TLNZNGvYrGL25-WTQTmfRu0rRgsDffRQp2BBPMGIPhY93Y8Vu2u_0UdyEhk6f9BKZAarxm1ONOkmyyVHBfEvLrw', 'title': 'Graffiti | Worry (War Pig Pink)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20Worry%20%28War%20Pig%20Pink%29', 'fraudwarnings': None}, '1989271413': {'classid': '1989271413', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0ovCCC3q5bDOdLCSNHgpqT7JdNDzf_jH05-jCRDmcQ-t4Q1tRLqZW-mVBa8_YOQx9itAdqGq0mFZwCxo8e9VKaVLvzyMVMORPsBckkw', 'title': 'Graffiti | King Me (Monarch Blue)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20King%20Me%20%28Monarch%20Blue%29', 'fraudwarnings': None}, '3500707668': {'classid': '3500707668', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaKhBwnaGQKGRHvd_gx9TekvOkZr-HxGlV6sAg27vF99332QXjr0NuYTz3I4GLMlhpm0KUJjU', 'title': 'AWP', 'price': None, 'count': '1', 'stickers': {'stickerCount': 4, 'patchCount': 0, 'count': 4, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Sniper Rifle', 'market_hash_name': 'AWP', 'fraudwarnings': None}, '3494936622': {'classid': '3494936622', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaPhRw7ODBfThM79mk2tbbz_KlY-OHxDMJvZUp3uvDpI_wiwHhr0trMTj2cYCcdlRoNV7S-wWggbC4gMgSD1s', 'title': 'USP-S', 'price': None, 'count': '1', 'stickers': {'stickerCount': 4, 'patchCount': 0, 'count': 4, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Pistol', 'market_hash_name': 'USP-S', 'fraudwarnings': None}, '1989272030': {'classid': '1989272030', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0qe6yGX3wYCPGLi3VUgluTOVdNDvf_WH05ezFS2nIROp_Fg0CL_cE-jYdOJraPBQ5htQD_zL2h0p6WBUnfspUfRq33n0DPaR4zXURJs9XfaeMfrs', 'title': 'Graffiti | 8-Ball (War Pig Pink)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%208-Ball%20%28War%20Pig%20Pink%29', 'fraudwarnings': None}}, 'steamId': '76561198993773915', 'steam_id': '76561198993773915', 'appId': 730, 'appTitle': 'CS:GO', 'totalValue': 348.38, 'itemCount': 51, 'marketableItemCount': 38, 'currency': 'rub', 'currencyIcon': '₽', 'language': 'english', 'time': 1695207618, 'cache': True}, 'appId': 730, 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695587503}}
```

### Change owner

*Change of account owner.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingchangeowner)*

**Parameters:**

- **item_id** (int): ID of item.
- **username** (str): The username of the new account owner
- **secret_answer** (str): Secret answer of your account

**Example:**

```python
response = market.managing.change_owner(item_id=2410024,username="AS7RID",secret_answer="Denyak net")
print(response.json())
```

```python
{'status': 'ok', 'message': 'string'}
```

### Change password

*Changes password of account.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingchangepassword)*

**Parameters:**

- **item_id** (int): ID of item.
- **_cancel** (bool): Cancel change password recommendation. It will be helpful, if you don't want to change password and get login data

**Example:**

```python
response = market.managing.change_password(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'Changes Saved', 'new_password': 'string'}
```

### Bump

*Bumps account in the search.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingbump)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.bump(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get email code

*Gets confirmation code or link.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanaginggetemailcode)*

**Parameters:**

- **item_id** (int): ID of item.
- **email** (str): Account email.

**Example:**

```python
response = market.managing.email(item_id=2410024,email="as7rid@zelenka.guru")
print(response.json())
```

```python
{'item': {'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'seller': {'user_id': 0, 'username': 'string', 'avatar_date': 0, 'user_group_id': 0, 'secondary_group_ids': 'string', 'display_style_group_id': 0, 'uniq_username_css': 'string'}}, 'codeData': {'code': 'string', 'date': 0, 'textPlain': 'string'}}
```

### Get steam guard

*Gets confirmation code from MaFile (Only for Steam accounts).*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanaginggetmafilecode)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.guard(item_id=2410024)
print(response.json())
```

```python
{'item': {'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'seller': {'user_id': 0, 'username': 'string', 'avatar_date': 0, 'user_group_id': 0, 'secondary_group_ids': 'string', 'display_style_group_id': 0, 'uniq_username_css': 'string'}}, 'codeData': {'code': 'string', 'date': 0, 'textPlain': 'string'}}
```

### Get mafile

*Returns mafile in JSON.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanaginggetmafilejson)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.mafile(item_id=2410024)
print(response.json())
```

```python
{'maFile': {}}
```

### Get temp mail password

*Gets password from temp email of account.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanaginggetpasswordemail)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.password_tm(item_id=2410024)
print(response.json())
```

```python
{'item': {'account': 'string'}}
```

### Get telegram confirmation code

*Gets confirmation code from Telegram.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanaginggettelegramcode)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.telegram(item_id=2410024)
print(response.json())
```

```python
{'item': {'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'seller': {'user_id': 0, 'username': 'string', 'avatar_date': 0, 'user_group_id': 0, 'secondary_group_ids': 'string', 'display_style_group_id': 0, 'uniq_username_css': 'string'}}, 'codes': {'code': 'string', 'date': 0}}
```

### Reset telegram authorizations

*Resets Telegram authorizations.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingtelegramresetauth)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.telegram_reset(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Refuse guarantee

*Cancel guarantee of account. It can be useful for account reselling.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingcancelguarantee)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.refuse_guarantee(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Favorite

*Adds account to favourites.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingaddfavorite)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.favorite(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Unfavorite

*Deletes account from favourites.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingdeletefavorite)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.unfavorite(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Stick

*Stick account in the top of search.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingstick)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.stick(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'string'}
```

### Unstick

*Unstick account of the top of search.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingunstick)*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = market.managing.unstick(item_id=2410024)
print(response.json())
```

```python
{'status': 'ok', 'message': 'string'}
```

### Update inventory value

*Update inventory value.*

*[Official documentation reference](https://lzt-market.readme.io/reference/accountsmanagingupdateinventoryvalue)*

**Parameters:**

- **item_id** (int): Item id.
- **app_id** (int): App id.

**Example:**

```python
response = market.managing.update_inventory(item_id=2410024, app_id=730)
print(response.json())
```

```python
{'status': 'ok', 'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Payments

*Methods to transfer market balance and check payments history*

### History

*Displays list of your payments.*

*[Official documentation reference](https://lzt-market.readme.io/reference/paymentslisthistory)*

**Parameters:**

- **user_id** (int): ID of user.
- **operation_type** (str): Type of operation. Allowed operation types
- **pmin** (int): Minimal price of operation (Inclusive)
- **pmax** (int): Maximum price of operation (Inclusive)
- **page** (int): The number of the page to display results from
- **operation_id_lt** (int): ID of the operation from which the result begins
- **receiver** (str): Username of user, which receive money from you
- **sender** (str): Username of user, which sent money to you
- **start_date** (str): Start date of operation (RFC 3339 date format)
- **end_date** (str): End date of operation (RFC 3339 date format)
- **wallet** (str): Wallet, which used for money payots
- **comment** (str): Comment for money transfers
- **is_hold** (bool): Display hold operations
- **show_payments_stats** (bool): Display payment stats for selected period (outgoing value, incoming value)

**Example:**

```python
response = market.payments.history(user_id=2410024,sender="root")
print(response.json())
```

```python
{'payments': {'payment': 'string'}, 'hasNextPage': True, 'lastOperationId': 0, 'nextPageHref': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Transfer

*Send money to any user.*

*[Official documentation reference](https://lzt-market.readme.io/reference/paymentslistsendmoney)*

**Parameters:**

- **amount** (int): Amount to send in your currency.
- **secret_answer** (str): Secret answer of your account
- **currency** (str): Using currency for amount.
- **user_id** (int): User id of receiver. 
  > If user_id specified, username is not required.
- **username** (str): Username of receiver. 
  > If username specified, user_id is not required.
- **comment** (str): Transfer comment
- **transfer_hold** (bool): Hold transfer or not
- **hold_length_option** (str): Hold length option.
- **hold_length_value** (int): Hold length value

**Example:**

```python
response = market.payments.transfer(user_id=2410024, amount=250, currency=Constants.Market.Currency.rub, secret_answer="Secret answer")
print(response.json())
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Generate payment link

*Generates payment link*

**Parameters:**

- **amount** (int): Amount to send in your currency.
- **user_id** (int): ID of user to transfer money
- **username** (str): Username to transfer money
- **comment** (str): Payment comment.
- **redirect_url** (str): Redirect url. User who paid on this link will be redirected to this url
- **currency** (str): Using currency for amount. Allowed values
- **hold** (bool): Hold transfer or not
- **hold_length** (int): Hold length ( max 1 month )
- **hold_option** (str): Hold option. Can be "hours","days","weeks","months"

**Example:**

```python
response = market.payments.generate_link(user_id=2410024, comment="LOLZTEAM example", currency=Constants.Market.Currency.rub, amount=250)
print(response.json())
```

```python
https://lzt.market/balance/transfer?user_id=2410024&amount=250&comment=LOLZTEAM+example&currency=rub&hold=0
```

# Proxy

*Methods to add/delete and get your market proxies*

### Get proxies

*Gets your proxy list.*

*[Official documentation reference](https://lzt-market.readme.io/reference/proxysettingsget)*

**Example:**

```python
response = market.proxy.get()
print(response.json())
```

```python
{'proxies': [{'proxy': {'proxy_id': 0, 'user_id': 0, 'proxy_ip': 'string', 'proxy_port': 0, 'proxy_user': 'string', 'proxy_pass': 'string', 'proxyString': 'string'}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Add proxy

*Add single proxy or proxy list.*

*[Official documentation reference](https://lzt-market.readme.io/reference/proxysettingsadd)*

**Parameters:**

- **proxy_ip** (str): Proxy ip or host.
- **proxy_port** (int): Proxy port
- **proxy_user** (str): Proxy username
- **proxy_pass** (str): Proxy password
- **proxy_row** (str): Proxy list in String format ip:port:user:pass. 
  > Each proxy must be start with new line (use \n separator)

**Example:**

```python
response = market.proxy.add(proxy_ip="192.168.1.1",proxy_port="5000",proxy_user="Login",proxy_pass="Password")
print(response.json())
```

```python
{'status': 'ok', 'message': 'Changes Saved', 'system_info': {'visitor_id': 2410024, 'time': 1695586117}}
```

### Delete proxy

*Delete single or all proxies.*

*[Official documentation reference](https://lzt-market.readme.io/reference/proxysettingsdelete)*

**Parameters:**

- **proxy_id** (int): ID of an existing proxy
- **delete_all** (bool): Use True if you want to delete all proxy

**Example:**

```python
response = market.proxy.delete(delete_all=True)
print(response.json())
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
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
    get_batch_job(market.list.favorite, job_name="1", page=1),
    get_batch_job(market.payments.history, job_name="2", user_id=2410024, sender="root"),
    get_batch_job(market.steam_value, job_name="3", url="https://steamcommunity.com/id/AS7RID", app_id=Constants.Market.AppID.CS2, currency=Constants.Market.Currency.usd)
]
for job in jobs:
    print(job)
```

```python
{'id': '1', 'uri': 'https://lzt.market/fave', 'method': 'GET', 'params': {'page': 1, 'locale': 'en'}, 'data': {'page': 1}, 'files': None}
{'id': '2', 'uri': 'https://lzt.market/user/2410024/payments', 'method': 'GET', 'params': {'user_id': 2410024, 'operation_type': None, 'pmin': None, 'pmax': None, 'page': None, 'operation_id_lt': None, 'receiver': None, 'sender': 'root', 'start_date': None, 'end_date': None, 'wallet': None, 'comment': None, 'is_hold': 0, 'show_payments_stats': 0, 'locale': 'en'}, 'data': {'user_id': 2410024, 'operation_type': None, 'pmin': None, 'pmax': None, 'page': None, 'operation_id_lt': None, 'receiver': None, 'sender': 'root', 'start_date': None, 'end_date': None, 'wallet': None, 'comment': None, 'is_hold': 0, 'show_payments_stats': 0}, 'files': None}
{'id': '3', 'uri': 'https://lzt.market/steam-value', 'method': 'GET', 'params': {'link': 'https://steamcommunity.com/id/AS7RID', 'app_id': 730, 'currency': 'usd', 'ignore_cache': None, 'locale': 'en'}, 'data': {'link': 'https://steamcommunity.com/id/AS7RID', 'app_id': 730, 'currency': 'usd', 'ignore_cache': None}, 'files': None}
```

# Batch

*Execute multiple API requests at once.*

  > Maximum batch jobs is 10.
  >
  > Market batch can only proceed with market url's. If you want to use batch with forum url's try [this](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/Documentation/Forum.md#batch)

*[Official documentation reference](https://lzt-market.readme.io/reference/batchrequestsexecute)*

**Parameters:**

- **jobs** (list[dict]): List of batch jobs.

**Example:**

```python
jobs = [
    get_batch_job(market.list.favorite, job_name="1", page=1),
    get_batch_job(market.payments.history, job_name="2", user_id=2410024, sender="root"),
    get_batch_job(market.steam_value, job_name="3", url="https://steamcommunity.com/id/AS7RID", app_id=Constants.Market.AppID.CS2, currency=Constants.Market.Currency.usd)
]
response = market.batch(jobs=jobs)
for job_name, job_data in data["jobs"].items():
    print(job_data)
```

```python
{'_job_result': 'ok', 'items': [], 'totalItems': 0, 'totalItemsPrice': None, 'perPage': 40, 'page': 1, 'searchUrl': '/fave', 'stickyItems': []}
{'_job_result': 'ok', 'payments': {'121540810': {'operation_id': 121540810, 'operation_date': 1694350167, 'operation_type': 'receiving_money', 'outgoing_sum': 0, 'incoming_sum': 777,  ... }
{'_job_result': 'ok', 'query': 'https://steamcommunity.com/id/AS7RID', 'data': {'items': {'5189384637': {'classid': '5189384637', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dl ... }
```

# Send async

*Send request as async*

**Parameters:**

- **func** (function): Target function.
- ****kwargs** (any): Target function parameters.

**Example:**

```python
response = await send_as_async(func=market.profile.get, user_id=2410024)
print(response.json())
```

```python
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_email': 'string', 'user_unread_notification_count': 0, 'user_dob_day': 0, 'user_dob_month': 0, 'user_dob_year': 0, 'user_title': 'string', 'user_last_seen_date': 0, 'balance': 0, 'hold': 0, 'system_info': {'visitor_id': 0, 'time': 0}}}
```
<font size=6 style="margin: auto"> <center>

[Forum docs](https://github.com/AS7RIDENIED/Lolzteam_Python_Api/blob/main/Documentation/Forum.md) - [Antipublic Docs](https://github.com/AS7RIDENIED/Lolzteam_Python_Api/blob/main/Documentation/Antipublic.md)

</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

* [Profile](#profile)
  * [Get profile](#get-profile)
  * [Edit profile](#edit-profile)
* [List](#list)
  * [Categories](#categories)
    * [Get accounts in category](#get-accounts-in-category)
    * [Get categories](#get-categories)
    * [Get search params](#get-search-params)
    * [Get category games](#get-category-games)
  * [Get item](#get-item)
  * [New items](#new-items)
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
  * [Edit](#edit)
  * [Info](#info)
* [Managing](#managing)
  * [Tag](#tag)
    * [Add tag](#add-tag)
    * [Delete tag](#delete-tag)
  * [Edit](#edit-)
  * [Delete](#delete)
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
* [Steam inventory value](#steam-inventory-value)
* [Send async](#send-async)

</details>


# Quickstart

You need to create class instance to use library

```
from LolzteamApi import LolzteamApi, Types
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

# Profile

*Methods to get and edit profile info*

### Get profile

*Displays info about your profile.*

**Example:**

```python
data = api.market.profile.get()
print(data)
```

```python
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_email': 'string', 'user_unread_notification_count': 0, 'user_dob_day': 0, 'user_dob_month': 0, 'user_dob_year': 0, 'user_title': 'string', 'user_last_seen_date': 0, 'balance': 0, 'hold': 0, 'system_info': {'visitor_id': 0, 'time': 0}}}
```

### Edit profile

*Change settings about your profile on the market.*

**Parameters:**

- **disable_steam_guard** (bool): Disable Steam Guard on account purchase moment
- **user_allow_ask_discount** (bool): Allow users ask discount for your accounts
- **max_discount_percent** (int): Maximum discount percents for your accounts
- **allow_accept_accounts** (str): Usernames who can transfer market accounts to you. Separate values with a comma.
- **hide_favourites** (bool): Hide your profile info when you add an account to favorites
- **vk_ua** (str): Your vk useragent to accounts

**Example:**

```python
data = api.market.profile.edit(user_allow_ask_discount=True)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

# List

*Methods for getting account lists*

---

## Categories

### Get accounts in category

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **category_name** (str): Name of category.
- **pmin** (int): Minimal price of account (Inclusive)
- **pmax** (int): Maximum price of account (Inclusive)
- **title** (str): The word or words contained in the account title
- **parse_sticky_items** (bool): If true, API will return stickied accounts in results
- **parse_same_items** (bool): If true, API will return account history in results
- **games** (list[int] or int): The ID of a game found on the account
- **page** (int): The number of the page to display results from
- **auction** (str): Auction. 
  > Can be [yes, no, nomatter].
- **order_by** (str): Order by. 
  > Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_down_upload, pdate_to_up, pdate_to_up_upload].
- **search_params** (dict): Search params for your request.
  > Example {"origin":"autoreg"} will return only "autoreg" accounts

**Example:**

```python
data = api.market.list.categories.get(category_name=Types.Market.Categories.vk,pmax=10)
print(data)
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### Get categories

*Display category list.*

**Parameters:**

- **top_queries** (bool): Display top queries for per category.

**Example:**

```python
data = api.market.list.categories.categories()
print(data)
```

```python
{'0': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get search params

*Displays search parameters for a category.*

**Parameters:**

- **category_name** (str): Name of category.

**Example:**

```python
data = api.market.list.categories.params(category_name=Types.Market.Categories.vk)
print(data)
```

```python
{'category': {'category_id': 0, 'category_title': 'string', 'category_description': 'string', 'links': {'permalink': 'string', 'detail': 'string', 'sub-categories': 'string', 'sub-forums': 'string'}, 'permissions': {'view': True, 'edit': True, 'delete': True}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get category games

*Displays a list of games in the category.*

**Parameters:**

- **category_name** (str): Name of category.

**Example**:

```python
data = api.market.list.categories.games(category_name=Types.Market.Categories.steam)
print(data)
```

```python
{'games': [{'app_id': 'string', 'title': 'string', 'abbr': 'string', 'category_id': 0, 'img': 'string', 'url': 'string', 'ru': ['string']}], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': True, 'system_info': {'visitor_id': 0, 'time': 0}}
```
---

### Get item

*Displays item information or returns Steam account html code.*

**Parameters:**

- **item_id** (int): ID of item.
- **steam_preview** (bool): Steam preview
  > Set it True if you want to get steam html and False/None if you want to get item info
- **preview_type** (str): Type of page. 
  > Can be "profiles" or "games"

**Example:**

```python
data = api.market.list.get(item_id=2410024)
print(data)
```

```python
{'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'seller': {'user_id': 0, 'username': 'string', 'avatar_date': 0, 'user_group_id': 0, 'secondary_group_ids': 'string', 'display_style_group_id': 0, 'uniq_username_css': 'string'}}
```
### New items

*Displays a list of the latest accounts.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **title** (str): The word or words contained in the account title
- **search_params** (dict): Search params for your request.
  > Example {"category_id":19} will return only VPN accounts

**Example:**

```python
data = api.market.list.new()
print(data)
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### From url

*Displays a list of the latest accounts from your market url with search params.*

**Parameters:**

- **url** (str): Your market search url.
  > It can be https://lzt.market or https://api.lzt.market

**Example:**

```python
data = api.market.list.from_url(url="https://lzt.market/steam/cs-go-prime?origin[]=fishing&eg=1")
print(data)
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### Viewed accounts

*Displays a list of viewed accounts.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **status** (str): Account status.
  > Can be [active, paid, deleted or awaiting].

  > You also can use types - Types.Market.Item_status
- **title** (str): The word or words contained in the account title
- **search_params** (dict): Search params for your request. 
  > Example {"category_id":19} will return only VPN accounts

**Example:**

```python
data = api.market.list.viewed()
print(data)
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### Favorite accounts

*Displays a list of favorite accounts.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **status** (str): Account status.
  > Can be [active, paid, deleted or awaiting].

  > You also can use types - Types.Market.Item_status
- **title** (str): The word or words contained in the account title
- **search_params** (dict): Search params for your request.
  > Example {"category_id":19} will return only VPN accounts

**Example:**
```python
data = api.market.list.favorite()
print(data)
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}

```

### Purchased accounts

*Displays a list of purchased accounts.*

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

  > You also can use types - Types.Market.Item_status
- **order** (str): Order type.
  > Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_up, pdate_to_down_upload, pdate_to_up_upload].

  >You also can use types - Types.Market.Order

**Example:**

```python
data = api.market.list.purchased()
print(data)
```

```python
{'items': ['string'], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 0, 'page': 0, 'searchUrl': 'string'}
```

### Owned accounts

*Displays a list of owned accounts.*

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

  > You also can use types - Types.Market.Item_status
- **order** (str): Order type.
  > Can be [price_to_up, price_to_down, pdate_to_down, pdate_to_up, pdate_to_down_upload, pdate_to_up_upload].

  >You also can use types - Types.Market.Order

**Example:**

```python
data = api.market.list.owned()
print(data)
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

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
response = api.market.purchasing.auction.get(item_id=2410024)
print(response)
```

```python
{'itemId': 0, 'bids': [{'bid_id': 0, 'bid_value': {'rub': 'string', 'uah': 'string', 'kzt': 'string', 'byn': 'string', 'usd': 'string', 'eur': 'string', 'gbp': 'string', 'cny': 'string', 'try': 'string'}, 'minAllowedBidValue': {'rub': 0, 'uah': 0, 'kzt': 0, 'byn': 0, 'usd': 0, 'eur': 0, 'gbp': 0, 'cny': 0, 'try': 0}, 'bid_previous_value': {'rub': 'string', 'uah': 'string', 'kzt': 'string', 'byn': 'string', 'usd': 'string', 'eur': 'string', 'gbp': 'string', 'cny': 'string', 'try': 'string'}, 'user': {'user_id': 0, 'avatar': 'string', 'usernameHtml': 'string'}, 'bid_date': 0, 'canCancelBid': False, 'endTimeAuction': 0}], 'is_finished': 0, 'endTime': 0, 'currencies': {'{currency}': {'title': 'string', 'symbol': 'string', 'rate': {'Value': 0, 'Nominal': 0}}}, 'userCurrency': 'string', 'minAllowedBidValue': {'rub': 0, 'uah': 0, 'kzt': 0, 'byn': 0, 'usd': 0, 'eur': 0, 'gbp': 0, 'cny': 0, 'try': 0}, 'startValue': {'rub': 0, 'uah': 0, 'kzt': 0, 'byn': 0, 'usd': 0, 'eur': 0, 'gbp': 0, 'cny': 0, 'try': 0}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Place auction bid

*Create a new auction bid.*

**Parameters:**

- **item_id** (int): ID of item.
- **amount** (int): Amount bid.
- **currency** (str): Using currency.
  > Can be [rub, uah, kzt, byn, usd, eur, gbp, cny, try].

**Example:**

```python
response = api.market.purchasing.auction.place_bid(item_id=2410024, amount=250, currency=Types.Market.Currency.rub)
print(response)
```

```python
{'status': 'ok', 'bid': {'bid_id': 0, 'bid_value': {'rub': 'string', 'uah': 'string', 'kzt': 'string', 'byn': 'string', 'usd': 'string', 'eur': 'string', 'gbp': 'string', 'cny': 'string', 'try': 'string'}, 'minAllowedBidValue': {'rub': 0, 'uah': 0, 'kzt': 0, 'byn': 0, 'usd': 0, 'eur': 0, 'gbp': 0, 'cny': 0, 'try': 0}, 'bid_previous_value': {'rub': 'string', 'uah': 'string', 'kzt': 'string', 'byn': 'string', 'usd': 'string', 'eur': 'string', 'gbp': 'string', 'cny': 'string', 'try': 'string'}, 'user': {'user_id': 0, 'avatar': 'string', 'usernameHtml': 'string'}, 'bid_date': 0, 'canCancelBid': False, 'endTimeAuction': 0}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete auction bid

*Delete your auction bid.*

**Parameters:**

- **item_id** (int): ID of item.
- **bid_id** (int): ID of bid.

**Example:**

```python
response = api.market.purchasing.auction.delete_bid(item_id=2410024, bid_id=2410024)
print(response)
```

```python
{'status': 'ok', 'message': 'The bid success deleted', 'system_info': {'visitor_id': 0, 'time': 0}}
```

---

### Fast buy

*Check and buy account.*

**Parameters:**

- **item_id** (int): ID of item.
- **price** (int): Current price of account in your currency
- **buy_without_validation** (bool): Buy account without validation
  > Use TRUE if you want to buy account without account data validation (not safe)

**Example:**

```python
data = api.market.purchasing.fast_buy(item_id=2410024,price=10)
print(data)
```

```python
{'status': 'ok', 'reserve_end_date': 0, 'item': {'account': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```
### Check

*Checking account for validity. If the account is invalid, the purchase will be canceled automatically.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.purchasing.check(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'item': {'account': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Confirm buy

*Confirm buy.*

**Parameters:**

- **item_id** (int): ID of item.
- **buy_without_validation** (bool): Buy account without validation
  > Use TRUE if you want to buy account without account data validation (not safe)

**Example:**

```python
data = api.market.purchasing.confirm(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'item': {'account': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Reserve

*Reserves account for you.*
  > Reserve time - 300 seconds.

**Parameters:**

- **item_id** (int): ID of item.
- **price** (int): Current price of account in your currency

*Example:*

```python
data = api.market.purchasing.reserve(item_id=2410024,price=10)
print(data)
```

```python
{'status': 'ok', 'reserve_end_date': 0, 'item': {'account': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Cancel reserve

*Cancels reserve.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.purchasing.reserve_cancel(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

# Publishing

*Methods for item publishing*

### Fast sell

*Adds and check account on validity. If account is valid, account will be published on the market.*

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
  > Use types -> Types.Market.Item_origin
- **allow_ask_discount** (bool): Allow users to ask discount for this account.
- **proxy_id** (int): Using proxy id for account checking.
- **random_proxy** (bool): Pass True, if you get captcha in previous response
- **login** (str): Account login (or email)
- **password** (str): Account password
- **login_password** (str): Account login data
  > Format - login:password
- **extra** (dict): Extra params for account checking.
  > E.g. you need to put cookies to extra (extra={"cookies": cookies}) if you want to upload TikTok/Fortnite/Epic Games account

**Example:**

```python
data = api.market.publishing.fast_sell(category_id=Types.Market.Categories_ID.vk, price=10,
                                       currency=Types.Market.Currency.rub, item_origin=Types.Market.Item_origin.autoreg,
                                       extended_guarantee=Types.Market.Guarantee.day, title="Acc vk",
                                       allow_ask_discount=True, login_password="Login:password")
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'item': {'item_id': 0, 'item_state': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Add

*Adds account on the market.*

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

**Example:**

```python
data = api.market.publishing.add(category_id=Types.Market.Categories_ID.vk, price=10,
                                 currency=Types.Market.Currency.rub, item_origin=Types.Market.Item_origin.autoreg,
                                 extended_guarantee=Types.Market.Guarantee.day, title="Acc vk",
                                 allow_ask_discount=True)
print(data)
```

```python
{'status': 'ok', 'item': {'item_id': 0, 'item_state': 'string'}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Check

*Check and put up to sale not published account OR update account information existing account.*

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
data = api.market.publishing.check(item_id=2410024,login_password="Login:password")
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Edit

*Edits any details of account.*

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
data = api.market.publishing.edit(item_id=2410024,price=777)
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Info

*Get info about not published item. For categories, which required temporary email (Steam, Social Club), you will get temporary email in response.*

**Parameters:**

- **item_id** (int): ID of item.
- **resell_item_id** (int): Put item id, if you are trying to resell item.
  >This is useful to pass temporary email from reselling item to new item. 
  
  > You will get same temporary email from reselling account.

**Example:**

```python
data = api.market.publishing.info(item_id=2410024)
print(data)
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

**Parameters:**

- **item_id** (int): ID of item.
- **tag_id** (int): Tag id. Tag list is available via api.market.profile.get()

**Example:**

```python
data = api.market.managing.tag.add(item_id=2410024, tag_id=1)
print(data)
```

```python
{'itemId': 0, 'tag': {'tag_id': 0, 'title': 'string', 'isDefault': True, 'forOwnedAccountsOnly': True, 'bc': 'string'}, 'addedTagId': 0, 'deleteTags': [0], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete tag

*Deletes tag for the account.*

**Parameters:**

- **item_id** (int): ID of item.
- **tag_id** (int): Tag id. Tag list is available via api.market.profile.get()

**Example:**

```python
data = api.market.managing.tag.delete(item_id=2410024, tag_id=1)
print(data)
```

```python
{'itemId': 0, 'tag': {'tag_id': 0, 'title': 'string', 'isDefault': True, 'forOwnedAccountsOnly': True, 'bc': 'string'}, 'addedTagId': 0, 'deleteTags': [0], 'system_info': {'visitor_id': 0, 'time': 0}}
```

---
### Edit 

*Edits any details of account.*

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
data = api.market.managing.edit(item_id=2410024,price=777)
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Delete

*Deletes your account from public search. Deletion type is soft. You can restore account after deletion if you want.*

**Parameters:**

- **item_id** (int): ID of item.
- **reason** (str): Delete reason.

**Example:**

```python
data = api.market.managing.delete(item_id=2410024,reason="Im gay")
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Change owner

*Change of account owner.*

**Parameters:**

- **item_id** (int): ID of item.
- **username** (str): The username of the new account owner
- **secret_answer** (str): Secret answer of your account

**Example:**

```python
data = api.market.managing.change_owner(item_id=2410024,username="AS7RID",secret_answer="Denyak net")
print(data)
```

```python
{'status': 'ok', 'message': 'string'}
```

### Change password

*Changes password of account.*

**Parameters:**

- **item_id** (int): ID of item.
- **_cancel** (bool): Cancel change password recommendation. It will be helpful, if you don't want to change password and get login data

**Example:**

```python
data = api.market.managing.change_password(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved', 'new_password': 'string'}
```

### Bump

*Bumps account in the search.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.bump(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Get email code

*Gets confirmation code or link.*

**Parameters:**

- **item_id** (int): ID of item.
- **email** (str): Account email.

**Example:**

```python
data = api.market.managing.email(item_id=2410024,email="as7rid@zelenka.guru")
print(data)
```

```python
{'item': {'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'seller': {'user_id': 0, 'username': 'string', 'avatar_date': 0, 'user_group_id': 0, 'secondary_group_ids': 'string', 'display_style_group_id': 0, 'uniq_username_css': 'string'}}, 'codeData': {'code': 'string', 'date': 0, 'textPlain': 'string'}}
```

### Get steam guard

*Gets confirmation code from MaFile (Only for Steam accounts).*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.guard(item_id=2410024)
print(data)
```

```python
{'item': {'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'seller': {'user_id': 0, 'username': 'string', 'avatar_date': 0, 'user_group_id': 0, 'secondary_group_ids': 'string', 'display_style_group_id': 0, 'uniq_username_css': 'string'}}, 'codeData': {'code': 'string', 'date': 0, 'textPlain': 'string'}}
```

### Get mafile

*Returns mafile in JSON.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.mafile(item_id=2410024)
print(data)
```

```python
{'maFile': {}}
```

### Get temp mail password

*Gets password from temp email of account.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.password_tm(item_id=2410024)
print(data)
```

```python
{'item': {'account': 'string'}}
```

### Get telegram confirmation code

*Gets confirmation code from Telegram.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.telegram(item_id=2410024)
print(data)
```

```python
{'item': {'item': {'item_id': 0, 'item_state': 'string', 'published_date': 'string', 'title': 'string', 'description': 'string', 'price': 0, 'update_stat_date': 0, 'refreshed_date': 0, 'login': 'string', 'temp_email': 'string', 'view_count': 0, 'information': 'string', 'item_origin': 'string'}, 'seller': {'user_id': 0, 'username': 'string', 'avatar_date': 0, 'user_group_id': 0, 'secondary_group_ids': 'string', 'display_style_group_id': 0, 'uniq_username_css': 'string'}}, 'codes': {'code': 'string', 'date': 0}}
```

### Reset telegram authorizations

*Resets Telegram authorizations.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.telegram_reset(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Refuse guarantee

*Cancel guarantee of account. It can be useful for account reselling.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.refuse_guarantee(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved'}
```

### Favorite

*Adds account to favourites.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.favorite(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Unfavorite

*Deletes account from favourites.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.unfavorite(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Stick

*Stick account in the top of search.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.stick(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'string'}
```

### Unstick

*Unstick account of the top of search.*

**Parameters:**

- **item_id** (int): ID of item.

**Example:**

```python
data = api.market.managing.unstick(item_id=2410024)
print(data)
```

```python
{'status': 'ok', 'message': 'string'}
```

# Payments

*Methods to transfer market balance and check payments history*

### History

*Displays list of your payments.*

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
data = api.market.payments.history(user_id=2410024,sender="root")
print(data)
```

```python
{'payments': {'payment': 'string'}, 'hasNextPage': True, 'lastOperationId': 0, 'nextPageHref': 'string', 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Transfer

*Send money to any user.*

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
data = api.market.payments.transfer(user_id=2410024, amount=250, currency=Types.Market.Currency.rub, secret_answer="Secret answer")
print(data)
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
data = api.market.payments.generate_link(user_id=2410024, comment="LolzteamApi example", currency=Types.Market.Currency.rub, amount=250)
print(data)
```

```python
https://lzt.market/balance/transfer?user_id=2410024&amount=250&comment=LolzteamApi+example&currency=rub&hold=0
```

# Proxy

*Methods to add/delete and get your market proxies*

### Get proxies

*Gets your proxy list.*

**Example:**

```python
data = api.market.proxy.get()
print(data)
```

```python
{'proxies': [{'proxy': {'proxy_id': 0, 'user_id': 0, 'proxy_ip': 'string', 'proxy_port': 0, 'proxy_user': 'string', 'proxy_pass': 'string', 'proxyString': 'string'}}], 'system_info': {'visitor_id': 0, 'time': 0}}
```

### Add proxy

*Add single proxy or proxy list.*

**Parameters:**

- **proxy_ip** (str): Proxy ip or host.
- **proxy_port** (int): Proxy port
- **proxy_user** (str): Proxy username
- **proxy_pass** (str): Proxy password
- **proxy_row** (str): Proxy list in String format ip:port:user:pass. 
  > Each proxy must be start with new line (use separator)

**Example:**

```python
data = api.market.proxy.add(proxy_ip="192.168.1.1",proxy_port="5000",proxy_user="Login",proxy_pass="Password")
print(data)
```

```python
{'status': 'ok', 'message': 'Changes Saved', 'system_info': {'visitor_id': 2410024, 'time': 1695586117}}
```

### Delete proxy

*Delete single or all proxies.*

**Parameters:**

- **proxy_id** (int): ID of an existing proxy
- **delete_all** (bool): Use True if you want to delete all proxy

**Example:**

```python
data = api.market.proxy.delete(delete_all=True)
print(data)
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
    api.get_batch_job(api.market.list.favorite, job_name="1", page=1),
    api.get_batch_job(api.market.payments.history, job_name="2", user_id=2410024, sender="root"),
    api.get_batch_job(api.market.steam_value, job_name="3", url="https://steamcommunity.com/id/AS7RID", app_id=Types.Market.App_Ids.CS2, currency=Types.Market.Currency.usd)
]
for job in jobs:
    print(job)
```

```python
{'id': '1', 'uri': 'https://api.lzt.market/fave', 'method': 'GET', 'params': {'page': 1, 'locale': 'en'}, 'data': {'page': 1}, 'files': None}
{'id': '2', 'uri': 'https://api.lzt.market/user/2410024/payments', 'method': 'GET', 'params': {'user_id': 2410024, 'operation_type': None, 'pmin': None, 'pmax': None, 'page': None, 'operation_id_lt': None, 'receiver': None, 'sender': 'root', 'start_date': None, 'end_date': None, 'wallet': None, 'comment': None, 'is_hold': 0, 'show_payments_stats': 0, 'locale': 'en'}, 'data': {'user_id': 2410024, 'operation_type': None, 'pmin': None, 'pmax': None, 'page': None, 'operation_id_lt': None, 'receiver': None, 'sender': 'root', 'start_date': None, 'end_date': None, 'wallet': None, 'comment': None, 'is_hold': 0, 'show_payments_stats': 0}, 'files': None}
{'id': '3', 'uri': 'https://api.lzt.market/steam-value', 'method': 'GET', 'params': {'link': 'https://steamcommunity.com/id/AS7RID', 'app_id': 730, 'currency': 'usd', 'ignore_cache': None, 'locale': 'en'}, 'data': {'link': 'https://steamcommunity.com/id/AS7RID', 'app_id': 730, 'currency': 'usd', 'ignore_cache': None}, 'files': None}
```

# Batch

*Execute multiple API requests at once.*

  > Maximum batch jobs is 10.
  >
  > Market batch can only proceed with market url's. If you want to use batch with forum url's try [this](https://github.com/AS7RIDENIED/Lolzteam_Python_Api/blob/main/Documentation/Forum.md#batch)

**Parameters:**

- **jobs** (list[dict]): List of batch jobs.

**Example:**

```python
jobs = [
    api.get_batch_job(api.market.list.favorite, job_name="1", page=1),
    api.get_batch_job(api.market.payments.history, job_name="2", user_id=2410024, sender="root"),
    api.get_batch_job(api.market.steam_value, job_name="3", url="https://steamcommunity.com/id/AS7RID", app_id=Types.Market.App_Ids.CS2, currency=Types.Market.Currency.usd)
]
data = api.market.batch(jobs=jobs)
for job_name, job_data in data["jobs"].items():
    print(job_data)
```

```python
{'_job_result': 'ok', 'items': [], 'totalItems': 0, 'totalItemsPrice': None, 'perPage': 40, 'page': 1, 'searchUrl': '/fave', 'stickyItems': []}
{'_job_result': 'ok', 'payments': {'121540810': {'operation_id': 121540810, 'operation_date': 1694350167, 'operation_type': 'receiving_money', 'outgoing_sum': 0, 'incoming_sum': 777,  ... }
{'_job_result': 'ok', 'query': 'https://steamcommunity.com/id/AS7RID', 'data': {'items': {'5189384637': {'classid': '5189384637', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dl ... }
```

# Steam inventory value

*Gets steam value.*

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
data = api.market.steam_value(url="https://steamcommunity.com/id/AS7RID",currency=Types.Market.Currency.rub,app_id=Types.Market.App_Ids.CSGO)
print(data)
```

```python
{'query': 'https://steamcommunity.com/id/AS7RID', 'data': {'items': {'5189384637': {'classid': '5189384637', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQNqhpOSV-fRPasw8rsUFJ5KBFZv668FFQynaHMJT9B74-ywtjYxfOmMe_Vx28AucQj3brAoYrz3Fay_kY4MG_wdYeLMlhpLMaM-1U', 'title': 'Revolution Case', 'price': 112.3, 'count': '1', 'stickers': None, 'type': 'Base Grade Container', 'market_hash_name': 'Revolution%20Case', 'fraudwarnings': None}, '3946324730': {'classid': '3946324730', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQNqhpOSV-fRPasw8rsUFJ5KBFZv668FFU2nfGaJG0btN2wwYHfxa-hY-uFxj4Dv50nj7uXpI7w3AewrhBpMWH6d9CLMlhpEbAe-Zk', 'title': 'Fracture Case', 'price': 59.05, 'count': '1', 'stickers': None, 'type': 'Base Grade Container', 'market_hash_name': 'Fracture%20Case', 'fraudwarnings': None}, '3220810394': {'classid': '3220810394', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou6ryFAR17P7YJgJQ7d-9kZSOkuXLPr7Vn35cppB0ievCp9322VKyrkVrN2z6dtOSdVQ8MAyD-QC6lb26gZe7tZrMmnF9-n51z91ErA0', 'title': 'StatTrak™ MP7 | Mischief (Field-Tested)', 'price': 46.47, 'count': '1', 'stickers': None, 'type': 'StatTrak™ Mil-Spec Grade SMG', 'market_hash_name': 'StatTrak%E2%84%A2%20MP7%20%7C%20Mischief%20%28Field-Tested%29', 'fraudwarnings': None}, '3591173339': {'classid': '3591173339', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposbaqKAxf0Ob3djFN79eJkIWKg__gPLfdqWZU7Mxkh6eToY2l3wy2rkFkNmj0JYaTcQY8YV-BqATrweu615-4u5zLnHVl6CJz-z-DyCIevZ0V', 'title': 'Glock-18 | Catacombs (Field-Tested)', 'price': 24.2, 'count': '1', 'stickers': {'stickerCount': 4, 'patchCount': 0, 'count': 4, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Mil-Spec Grade Pistol', 'market_hash_name': 'Glock-18%20%7C%20Catacombs%20%28Field-Tested%29', 'fraudwarnings': None}, '3035569050': {'classid': '3035569050', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLOzLhRlxfbGTjVb09ijl5SYqPDmNr7fqWdY781lxL-Zoo-hiVC1_BJsam37I4TAJ1Q7M1zYqQPol-2618fvupWYwSZk73Q8pSGKLd3ROFw', 'title': 'Five-SeveN | Coolant (Factory New)', 'price': 6.78, 'count': '1', 'stickers': None, 'type': 'Consumer Grade Pistol', 'market_hash_name': 'Five-SeveN%20%7C%20Coolant%20%28Factory%20New%29', 'fraudwarnings': None}, '3035569189': {'classid': '3035569189', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou6r8FA957ODYfTxW-Nmkx7-HnvD8J_XUzjwJupdw3-rA8I6jiQPl80I5Yzz7IoCTcwRtZl3VrFa2l-jp18O9ot2XnhWS9Knh', 'title': 'MP9 | Slide (Minimal Wear)', 'price': 4.84, 'count': '1', 'stickers': None, 'type': 'Consumer Grade SMG', 'market_hash_name': 'MP9%20%7C%20Slide%20%28Minimal%20Wear%29', 'fraudwarnings': None}, '3035580092': {'classid': '3035580092', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpoo7e1f1Jf2-r3czFX6cyknY6fqPX4Jr7Dk29u4MBwnPCP8d-iilGwqhVpYzzwLIeVcgNoY1zSq1bqlOm5hJ687ZzJmHVkvXN2tmGdwUIRV2k43w', 'title': 'UMP-45 | Facility Dark (Battle-Scarred)', 'price': 3.87, 'count': '1', 'stickers': None, 'type': 'Consumer Grade SMG', 'market_hash_name': 'UMP-45%20%7C%20Facility%20Dark%20%28Battle-Scarred%29', 'fraudwarnings': None}, '310777179': {'classid': '310777179', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpouLWzKjhz3MzbcDNG09GzkImemrnwYOOGwjIJ7JB1j-3D9Nms0FDh_0tqYjulLNCWdFNvZl7QrlPswOu6m9bi6_rlVdP1', 'title': 'Nova | Sand Dune (Field-Tested)', 'price': 3.87, 'count': '1', 'stickers': None, 'type': 'Consumer Grade Shotgun', 'market_hash_name': 'Nova%20%7C%20Sand%20Dune%20%28Field-Tested%29', 'fraudwarnings': None}, '1989297441': {'classid': '1989297441', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0su2fDm25bWCWeXKPT1sxTLBaYDrb-GX2t7_BQ2rOFbotEVhXLKoCpzBJNciBOQx9itAdqGq0mFZwCxo8e9VKaVLjnSBHZelHVPZFwA', 'title': 'Sealed Graffiti | Sorry (Brick Red)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20Sorry%20%28Brick%20Red%29', 'fraudwarnings': None}, '1989279141': {'classid': '1989279141', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0suOBCG25Pm-Te3WBHg84T7ZdPT6N-WChtOqVE2vAEuglSwECf_cM9mIdbprYPgx9itAdqGq0mFZwCxo8e9VKaVK4m3dCMuyaadCusA', 'title': 'Sealed Graffiti | NaCl (Shark White)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20NaCl%20%28Shark%20White%29', 'fraudwarnings': None}, '1989299897': {'classid': '1989299897', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0o_ePHnjyVzPBLiWXSgw9TrMMY2jbqGCm5OvCF27BF-4tRFtVfqoApzJNNc7YPRo60IQN8iuomUM7HRkkfddLZQOvw2QfKOAhnCJLcMkz1YlJgQ', 'title': 'Sealed Graffiti | Death Sentence (Tracer Yellow)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20Death%20Sentence%20%28Tracer%20Yellow%29', 'fraudwarnings': None}, '1989288246': {'classid': '1989288246', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0rO2BBTqjOWGReHiLGV9uH7ZbY2ve9zKtsemWRG3BEuotQg9Ve6pX-m1IPMGNIVJjg5FYpGm3hUloEgIhYslfLVm-nnJKNxikjmox', 'title': 'Sealed Graffiti | Toasted (Monster Purple)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20Toasted%20%28Monster%20Purple%29', 'fraudwarnings': None}, '1989276589': {'classid': '1989276589', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0pO-CI3DyeyfFJjOXS1s9SOJZZ2rb9zXx5OrAFjDOE-1_R1pQKaNW8TUbOs-LPxJo1I8JqiuomUM7HRkkfddLZQOvw2QfKOAhnCJLcMm5ggoI_A', 'title': 'Sealed Graffiti | QQ (Tracer Yellow)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20QQ%20%28Tracer%20Yellow%29', 'fraudwarnings': None}, '4302203091': {'classid': '4302203091', 'tradable': 1, 'marketable': 1, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9QVcJY8gulRPQV6CF7b9mNvbRRMjdgIO5ez2flZj0qTKI24TuNi1x9bexqakZe2JzjIIuMMh2rHEotqgxkS6rPdFh4ZR', 'title': 'Sticker | 100 Thieves | 2020 RMR', 'price': 2.9, 'count': 24, 'stickers': None, 'type': 'High Grade Sticker', 'market_hash_name': 'Sticker%20%7C%20100%20Thieves%20%7C%202020%20RMR', 'fraudwarnings': None}, '1989287941': {'classid': '1989287941', 'tradable': 1, 'marketable': 1, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0ovCCC3q5bDOdLCSNHgpqT7JdNDzf_jH05-jCRDmcQ-t4Q1tRLqZW-mVBa8_YOQx9itAdqGq0mFZwCxo8e9VKaVLtzyAVaLvjeQiSVQ', 'title': 'Sealed Graffiti | King Me (Monster Purple)', 'price': 2.9, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Sealed%20Graffiti%20%7C%20King%20Me%20%28Monster%20Purple%29', 'fraudwarnings': None}, '3496846827': {'classid': '3496846827', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaO1U1g72Ycz4bvYzvxdLakfWnYuPQxWlTuZ133O_ArN6j0Qa3_BI9Z2rwJoaQbEZgNvzyEwH0', 'title': 'P250', 'price': None, 'count': '1', 'stickers': {'stickerCount': 3, 'patchCount': 0, 'count': 3, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Pistol', 'market_hash_name': 'P250', 'fraudwarnings': None}, '3515046014': {'classid': '3515046014', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaOBRng6uGI2oT7YTjwobex_HwZbrSxzsAvJYi3rmYrY6kiQDnr0VtMT2ndo6ccBh-Pw_WKbm-EQ', 'title': 'SSG 08', 'price': None, 'count': '1', 'stickers': {'stickerCount': 3, 'patchCount': 0, 'count': 3, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Sniper Rifle', 'market_hash_name': 'SSG%2008', 'fraudwarnings': None}, '3528419424': {'classid': '3528419424', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaLAZs2v_JY3NAtIjnwdPdwq_1Nb_TwW9SupNw07GUoYmg3gKyrxZvNTr3JtWXcFNofxiOrQoC97_e', 'title': 'Galil AR', 'price': None, 'count': '1', 'stickers': {'stickerCount': 3, 'patchCount': 0, 'count': 3, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Rifle', 'market_hash_name': 'Galil%20AR', 'fraudwarnings': None}, '1989274499': {'classid': '1989274499', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0ovCCC3q5bDOdLCSNHgpqT7JdNDzf_jH05-jCRDmcQ-t4Q1tRLqZW-mVBa8_YOQx9itAdqGq0mFZwCxo8e9VKaVK4m3dCMuyX6bcTBg', 'title': 'Graffiti | King Me (Shark White)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20King%20Me%20%28Shark%20White%29', 'fraudwarnings': None}, '1989275289': {'classid': '1989275289', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0tuuDG2e5P2DBfnWMGg0_RLtbND6N-WDwse2VSmmdE74oEF0CdKUB-jcYbMuBagx9itAdqGq0mFZwCxo8e9VKaVK4m3dCMuyY2Tc6Pw', 'title': 'Graffiti | Take Flight (Shark White)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20Take%20Flight%20%28Shark%20White%29', 'fraudwarnings': None}, '1989275676': {'classid': '1989275676', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0pveDD3n4YzKKdieBTAhpH7ZbMD3R_Gfx5L6cFDrNQu8uEgFRe_NXoDAfPcuAPRM80ZlLpWL-lEtxEQQlZ8lSeR-30ykQYL50y3ClvG56Ng', 'title': 'Graffiti | Quickdraw (Shark White)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20Quickdraw%20%28Shark%20White%29', 'fraudwarnings': None}, '1989270691': {'classid': '1989270691', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0pe2BEHXlJjadf3HcTQswSrJbPD6IrTak5O6dQDjPRbklQVpSf_BR9zAfPsiNPRIjlNlc7Wa3m0tvEwMkZsxWfBbmniVEMOkkivTsgr4', 'title': 'Graffiti | Keep the Change (Jungle Green)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20Keep%20the%20Change%20%28Jungle%20Green%29', 'fraudwarnings': None}, '3653202725': {'classid': '3653202725', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fVOG_wcbQVmJ5IABWuoX3e1Uw7P_efWwMudjnzNaJlKH3Zu2EkDMGv8ByjuiToI2tigbg-kplYj3xdY6cIFVtM0aQpAYy5bU4zQ', 'title': '2020 Service Medal', 'price': None, 'count': '1', 'stickers': None, 'type': 'Extraordinary Collectible', 'market_hash_name': '2020%20Service%20Medal', 'fraudwarnings': None}, '1989274048': {'classid': '1989274048', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0pO-CI2P4eiXdYSKKHQw9TLNZNGvYrGL25-WTQTmfRu0rRgsDffRQp2BBPMGIPhY93Y8Vu2u_0UdyEhk6f9BKZAarxm1ONOkmyyVHBfEvLrw', 'title': 'Graffiti | Worry (War Pig Pink)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20Worry%20%28War%20Pig%20Pink%29', 'fraudwarnings': None}, '1989271413': {'classid': '1989271413', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0ovCCC3q5bDOdLCSNHgpqT7JdNDzf_jH05-jCRDmcQ-t4Q1tRLqZW-mVBa8_YOQx9itAdqGq0mFZwCxo8e9VKaVLvzyMVMORPsBckkw', 'title': 'Graffiti | King Me (Monarch Blue)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%20King%20Me%20%28Monarch%20Blue%29', 'fraudwarnings': None}, '3500707668': {'classid': '3500707668', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaKhBwnaGQKGRHvd_gx9TekvOkZr-HxGlV6sAg27vF99332QXjr0NuYTz3I4GLMlhpm0KUJjU', 'title': 'AWP', 'price': None, 'count': '1', 'stickers': {'stickerCount': 4, 'patchCount': 0, 'count': 4, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Sniper Rifle', 'market_hash_name': 'AWP', 'fraudwarnings': None}, '3494936622': {'classid': '3494936622', 'tradable': 0, 'marketable': 0, 'image_url': '-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQh5hlcX0nvUOGsx8DdQBJjIAVHubSaPhRw7ODBfThM79mk2tbbz_KlY-OHxDMJvZUp3uvDpI_wiwHhr0trMTj2cYCcdlRoNV7S-wWggbC4gMgSD1s', 'title': 'USP-S', 'price': None, 'count': '1', 'stickers': {'stickerCount': 4, 'patchCount': 0, 'count': 4, 'images': [], 'title': 'Sticker: DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019, DeadFox | Berlin 2019'}, 'type': 'Stock Pistol', 'market_hash_name': 'USP-S', 'fraudwarnings': None}, '1989272030': {'classid': '1989272030', 'tradable': 0, 'marketable': 0, 'image_url': 'IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0qe6yGX3wYCPGLi3VUgluTOVdNDvf_WH05ezFS2nIROp_Fg0CL_cE-jYdOJraPBQ5htQD_zL2h0p6WBUnfspUfRq33n0DPaR4zXURJs9XfaeMfrs', 'title': 'Graffiti | 8-Ball (War Pig Pink)', 'price': None, 'count': '1', 'stickers': None, 'type': 'Base Grade Graffiti', 'market_hash_name': 'Graffiti%20%7C%208-Ball%20%28War%20Pig%20Pink%29', 'fraudwarnings': None}}, 'steamId': '76561198993773915', 'steam_id': '76561198993773915', 'appId': 730, 'appTitle': 'CS:GO', 'totalValue': 348.38, 'itemCount': 51, 'marketableItemCount': 38, 'currency': 'rub', 'currencyIcon': '₽', 'language': 'english', 'time': 1695207618, 'cache': True}, 'appId': 730, 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695587503}}
```

# Send async

*Send request as async*

**Parameters:**

- **func** (function): Target function.
- ****kwargs** (any): Target function parameters.

**Example:**

```python
response = await api.send_as_async(func=api.market.profile.get, user_id=2410024)
print(response)
```

```python
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_email': 'string', 'user_unread_notification_count': 0, 'user_dob_day': 0, 'user_dob_month': 0, 'user_dob_year': 0, 'user_title': 'string', 'user_last_seen_date': 0, 'balance': 0, 'hold': 0, 'system_info': {'visitor_id': 0, 'time': 0}}}
```
<font size=6 style="margin: auto"><center>
[Forum docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Forum.md) - [Antipublic Docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Antipublic.md)
[Utility docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Utils.md)
</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

* [Batch](#batch)
* [Profile](#profile)
  * [Get](#get)
  * [Edit](#edit)
* [Category](#category)
  * [Steam](#steam)
    * [Get](#get-1)
    * [Params](#params)
    * [Games](#games)
  * [Fortnite](#fortnite)
    * [Get](#get-2)
    * [Params](#params-1)
  * [Mihoyo](#mihoyo)
    * [Get](#get-3)
    * [Params](#params-2)
  * [Riot](#riot)
    * [Get](#get-4)
    * [Params](#params-3)
    * [Valorant Data](#valorant-data)
  * [Telegram](#telegram)
    * [Get](#get-5)
    * [Params](#params-4)
  * [Supercell](#supercell)
    * [Get](#get-6)
    * [Params](#params-5)
  * [Origin](#origin)
    * [Get](#get-7)
    * [Params](#params-6)
    * [Games](#games-1)
  * [Worldoftanks](#worldoftanks)
    * [Get](#get-8)
    * [Params](#params-7)
  * [Worldoftanksblitz](#worldoftanksblitz)
    * [Get](#get-9)
    * [Params](#params-8)
  * [Gifts](#gifts)
    * [Get](#get-10)
    * [Params](#params-9)
  * [Epicgames](#epicgames)
    * [Get](#get-11)
    * [Params](#params-10)
    * [Games](#games-2)
  * [Escapefromtarkov](#escapefromtarkov)
    * [Get](#get-12)
    * [Params](#params-11)
  * [Socialclub](#socialclub)
    * [Get](#get-13)
    * [Params](#params-12)
    * [Games](#games-3)
  * [Uplay](#uplay)
    * [Get](#get-14)
    * [Params](#params-13)
    * [Games](#games-4)
  * [Warthunder](#warthunder)
    * [Get](#get-15)
    * [Params](#params-14)
  * [Discord](#discord)
    * [Get](#get-16)
    * [Params](#params-15)
  * [Tiktok](#tiktok)
    * [Get](#get-17)
    * [Params](#params-16)
  * [Instagram](#instagram)
    * [Get](#get-18)
    * [Params](#params-17)
  * [Battlenet](#battlenet)
    * [Get](#get-19)
    * [Params](#params-18)
    * [Games](#games-5)
  * [Vpn](#vpn)
    * [Get](#get-20)
    * [Params](#params-19)
  * [Cinema](#cinema)
    * [Get](#get-21)
    * [Params](#params-20)
  * [Roblox](#roblox)
    * [Get](#get-22)
    * [Params](#params-21)
  * [Spotify](#spotify)
    * [Get](#get-23)
    * [Params](#params-22)
  * [Warface](#warface)
    * [Get](#get-24)
    * [Params](#params-23)
  * [Minecraft](#minecraft)
    * [Get](#get-25)
    * [Params](#params-24)
  * [Get](#get-26)
  * [List](#list)
* [List](#list)
  * [From Url](#from-url)
  * [Latest](#latest)
  * [Owned](#owned)
  * [Purchased](#purchased)
  * [Favorite](#favorite)
  * [Viewed](#viewed)
* [Payments](#payments)
  * [History](#history)
  * [Transfer](#transfer)
  * [Fee](#fee)
  * [Generate Link](#generate-link)
* [Managing](#managing)
  * [Tag](#tag)
    * [Delete](#delete)
    * [Add](#add)
  * [Steamman](#steamman)
    * [Guard](#guard)
    * [Mafile](#mafile)
    * [Update Inventory](#update-inventory)
    * [Inventory Value](#inventory-value)
    * [Confirm Sda](#confirm-sda)
  * [Telegramman](#telegramman)
    * [Code](#code)
    * [Reset Auth](#reset-auth)
  * [Password Temp Mail](#password-temp-mail)
  * [Get](#get-27)
  * [Bulk Get](#bulk-get)
  * [Delete](#delete-1)
  * [Email](#email)
  * [Refuse Guarantee](#refuse-guarantee)
  * [Check Guarantee](#check-guarantee)
  * [Change Password](#change-password)
  * [Stick](#stick)
  * [Unstick](#unstick)
  * [Favorite](#favorite-1)
  * [Unfavorite](#unfavorite)
  * [Bump](#bump)
  * [Change Owner](#change-owner)
  * [Edit](#edit-1)
  * [Arbitrage](#arbitrage)
* [Purchasing](#purchasing)
  * [Auction](#auction)
    * [Place Bid](#place-bid)
    * [Delete Bid](#delete-bid)
  * [Check](#check)
  * [Confirm](#confirm)
  * [Fast Buy](#fast-buy)
* [Publishing](#publishing)
  * [Info](#info)
  * [Check](#check-1)
  * [Add](#add-1)
  * [Fast Sell](#fast-sell)
* [Proxy](#proxy)
  * [Get](#get-28)
  * [Delete](#delete-2)
  * [Add](#add-2)


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
# Batch

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


# Profile

## Get

GET https://api.lzt.market/me

*Displays info about your profile.*

Required scopes: *market*

**Example:**

```python
response = market.profile.get()
print(response.json())
```


## Edit

PUT https://api.lzt.market/me

*Change settings about your profile on the market.*

Required scopes: *market*

**Parameters:**

- **disable_steam_guard** (INSERT_HERE): Disable Steam Guard on account purchase moment
- **user_allow_ask_discount** (INSERT_HERE): Allow users ask discount for your accounts
- **max_discount_percent** (INSERT_HERE): Maximum discount percents for your accounts
- **allow_accept_accounts** (INSERT_HERE): Usernames who can transfer market accounts to you. Separate values with a comma.
- **hide_favourites** (INSERT_HERE): Hide your profile info when you add an account to favorites
- **title** (INSERT_HERE): Market title.
- **telegram_client** (INSERT_HERE): Telegram client. It should be {"telegram_api_id"
- **deauthorize_steam** (INSERT_HERE): Finish all Steam sessions after purchase.
- **hide_bids** (INSERT_HERE): Hide your profile when bid on the auction.

**Example:**

```python
response = market.profile.edit(user_allow_ask_discount=True, max_discount_percent=25, title="Selling some stuff")
print(response.json())
```


# Category

## Steam

### Get

GET https://api.lzt.market/steam

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.steam.get()
print(response.json())
```


### Params

GET https://api.lzt.market/steam/params

*Displays search parameters for a category.*

Required scopes: *market*

**Example:**

```python
response = market.category.steam.params()
print(response.json())
```


### Games

GET https://api.lzt.market/steam/games

*Displays a list of games in the category.*

Required scopes: *market*

**Example:**

```python
response = market.category.steam.games()
print(response.json())
```


## Fortnite

### Get

GET https://api.lzt.market/fortnite

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.fortnite.get()
print(response.json())
```


### Params

GET https://api.lzt.market/fortnite/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.fortnite.params()
print(response.json())
```


## Mihoyo

### Get

GET https://api.lzt.market/mihoyo

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.mihoyo.get()
print(response.json())
```


### Params

GET https://api.lzt.market/mihoyo/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.mihoyo.params()
print(response.json())
```


## Riot

### Get

GET https://api.lzt.market/riot

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.riot.get()
print(response.json())
```


### Params

GET https://api.lzt.market/riot/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.riot.params()
print(response.json())
```


### Valorant Data

GET https://api.lzt.market/data/valorant

*Displays data for specified type in valorant category.*

**Example:**

```python
response = market.category.riot.valorant_data(data_type="Agent")
print(response.json())
```


## Telegram

### Get

GET https://api.lzt.market/telegram

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.telegram.get()
print(response.json())
```


### Params

GET https://api.lzt.market/telegram/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.telegram.params()
print(response.json())
```


## Supercell

### Get

GET https://api.lzt.market/supercell

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.supercell.get()
print(response.json())
```


### Params

GET https://api.lzt.market/supercell/params

*Displays search parameters for a category.*

**Example:**

```python
response = INSERT_HERE
print(response.json())
```


## Origin

### Get

GET https://api.lzt.market/origin

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.origin.get()
print(response.json())
```


### Params

GET https://api.lzt.market/origin/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.origin.params()
print(response.json())
```


### Games

GET https://api.lzt.market/origin/games

*Displays a list of games in the category.*

Required scopes: *market*

**Example:**

```python
response = market.category.origin.games()
print(response.json())
```


## Worldoftanks

### Get

GET https://api.lzt.market/world-of-tanks

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.wot.get()
print(response.json())
```


### Params

GET https://api.lzt.market/world-of-tanks/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.wot.params()
print(response.json())
```


## Worldoftanksblitz

### Get

GET https://api.lzt.market/wot-blitz

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.wot_blitz.get()
print(response.json())
```


### Params

GET https://api.lzt.market/wot-blitz/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.wot_blitz.params()
print(response.json())
```


## Gifts

### Get

GET https://api.lzt.market/gifts

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.gifts.get()
print(response.json())
```


### Params

GET https://api.lzt.market/gifts/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.gitfs.params()
print(response.json())
```


## Epicgames

### Get

GET https://api.lzt.market/epicgames

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.epicgames.get()
print(response.json())
```


### Params

GET https://api.lzt.market/epicgames/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.epicgames.params()
print(response.json())
```


### Games

GET https://api.lzt.market/epicgames/games

*Displays a list of games in the category.*

Required scopes: *market*

**Example:**

```python
response = market.category.epicgames.games()
print(response.json())
```


## Escapefromtarkov

### Get

GET https://api.lzt.market/espace-from-tarkov

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.eft.get()
print(response.json())
```


### Params

GET https://api.lzt.market/escape-from-tarkov/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.eft.params()
print(response.json())
```


## Socialclub

### Get

GET https://api.lzt.market/socialclub

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.socialclub.get()
print(response.json())
```


### Params

GET https://api.lzt.market/socialclub/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.socialclub.params()
print(response.json())
```


### Games

GET https://api.lzt.market/socialclub/games

*Displays a list of games in the category.*

Required scopes: *market*

**Example:**

```python
response = market.category.socialclub.games()
print(response.json())
```


## Uplay

### Get

GET https://api.lzt.market/uplay

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.uplat.get()
print(response.json())
```


### Params

GET https://api.lzt.market/uplay/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.uplay.params()
print(response.json())
```


### Games

GET https://api.lzt.market/uplay/games

*Displays a list of games in the category.*

Required scopes: *market*

**Example:**

```python
response = market.category.uplay.games()
print(response.json())
```


## Warthunder

### Get

GET https://api.lzt.market/war-thunder

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.war_thunder.get()
print(response.json())
```


### Params

GET https://api.lzt.market/war-thunder/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.war_thunder.params()
print(response.json())
```


## Discord

### Get

GET https://api.lzt.market/discord

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.discord.get()
print(response.json())
```


### Params

GET https://api.lzt.market/discord/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.discord.params()
print(response.json())
```


## Tiktok

### Get

GET https://api.lzt.market/tiktok

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.tiktok.get()
print(response.json())
```


### Params

GET https://api.lzt.market/tiktok/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.tiktok.params()
print(response.json())
```


## Instagram

### Get

GET https://api.lzt.market/telegram

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.telegram.get()
print(response.json())
```


### Params

GET https://api.lzt.market/telegram/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.telegram.params()
print(response.json())
```


## Battlenet

### Get

GET https://api.lzt.market/battlenet

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.battlenet.get()
print(response.json())
```


### Params

GET https://api.lzt.market/battlenet/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.battlenet.params()
print(response.json())
```


### Games

GET https://api.lzt.market/battlenet/games

*Displays a list of games in the category.*

Required scopes: *market*

**Example:**

```python
response = market.category.battlenet.games()
print(response.json())
```


## Vpn

### Get

GET https://api.lzt.market/vpn

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.vpn.get()
print(response.json())
```


### Params

GET https://api.lzt.market/vpn/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.vpn.params()
print(response.json())
```


## Cinema

### Get

GET https://api.lzt.market/cinema

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.cinema.get()
print(response.json())
```


### Params

GET https://api.lzt.market/cinema/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.cinema.params()
print(response.json())
```


## Roblox

### Get

GET https://api.lzt.market/roblox

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.roblox.get()
print(response.json())
```


### Params

GET https://api.lzt.market/roblox/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.roblox.params()
print(response.json())
```


## Spotify

### Get

GET https://api.lzt.market/spotify

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.spotify.get()
print(response.json())
```


### Params

GET https://api.lzt.market/spotify/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.spotify.params()
print(response.json())
```


## Warface

### Get

GET https://api.lzt.market/warface

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.warface.get()
print(response.json())
```


### Params

GET https://api.lzt.market/warface/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.warface.params()
print(response.json())
```


## Minecraft

### Get

GET https://api.lzt.market/minecraft

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.minecraft.get()
print(response.json())
```


### Params

GET https://api.lzt.market/minecraft/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.minecraft.params()
print(response.json())
```


## Get

GET https://api.lzt.market/{category_name}

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **category_name** (str): Category name.
- **page** (INSERT_HERE): The number of the page to display results from
- **auction** (INSERT_HERE): Auction.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **origin** (INSERT_HERE): List of account origins.
- **not_origin** (INSERT_HERE): List of account origins that won't be included.
- **order_by** (INSERT_HERE): Item order.
- **sold_before** (INSERT_HERE): Sold before.
- **sold_before_by_me** (INSERT_HERE): Sold before by me.
- **not_sold_before** (INSERT_HERE): Not sold before.
- **not_sold_before_by_me** (INSERT_HERE): Not sold before by me.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.category.get(category_name="telegram")
print(response.json())
```


## List

GET https://api.lzt.market/category

*Display category list.*

Required scopes: *market*

**Parameters:**

- **top_queries** (INSERT_HERE): Display top queries for per category.

**Example:**

```python
response = market.category.list()
print(response.json())
```


# List

## From Url

Displays a list of the latest accounts from your market url with search params

Required scopes: *market**

**Parameters:**

- **url** (INSERT_HERE): Your market search url.
    > It can be *https://lzt.market/search_params* or *https://api.lzt.market/search_params*

**Example:**

```python
response = market.list.from_url(url="https://lzt.market/steam?origin[]=fishing&eg=1")
print(response.json())
```


## Latest

GET https://api.lzt.market/

*Displays a list of the latest accounts.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **title** (INSERT_HERE): The word or words contained in the account title.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.list.latest()
print(response.json())
```


## Owned

GET https://api.lzt.market/user/{user_id}/items

*Displays a list of owned accounts.*

Required scopes: *market*

**Parameters:**

- **user_id** (INSERT_HERE): ID of user.
- **page** (INSERT_HERE): Page
- **category_id** (INSERT_HERE): Accounts category
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **title** (INSERT_HERE): The word or words contained in the account title.
- **status** (INSERT_HERE): Account status. Can be [active, paid, deleted or awaiting].
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.list.owned()
print(response.json())
```


## Purchased

GET https://api.lzt.market/user/{user_id}/orders

*Displays a list of purchased accounts.*

Required scopes: *market*

**Parameters:**

- **user_id** (INSERT_HERE): ID of user.
- **page** (INSERT_HERE): Page
- **category_id** (INSERT_HERE): Accounts category
- **pmin** (INSERT_HERE): Minimal price of account (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of account (Inclusive).
- **title** (INSERT_HERE): The word or words contained in the account title.
- **status** (INSERT_HERE): Account status. Can be [active, paid, deleted or awaiting].
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.list.orders()
print(response.json())
```


## Favorite

GET https://api.lzt.market/fave

*Displays a list of favourites accounts.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **status** (INSERT_HERE): Account status.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.list.favorite()
print(response.json())
```


## Viewed

GET https://api.lzt.market/viewed

*Displays a list of viewed accounts.*

Required scopes: *market*

**Parameters:**

- **page** (INSERT_HERE): The number of the page to display results from
- **status** (INSERT_HERE): Account status.
- **title** (INSERT_HERE): The word or words contained in the account title.
- **kwargs** (INSERT_HERE): Additional search parameters for your request.

**Example:**

```python
response = market.list.viewed()
print(response.json())
```


# Payments

## History

GET https://api.lzt.market/user/{user_id}/payments

*Displays info about your profile.*

Required scopes: *market*

**Parameters:**

- **user_id** (INSERT_HERE): ID of user.
- **operation_type** (INSERT_HERE): Type of operation.
- **pmin** (INSERT_HERE): Minimal price of operation (Inclusive).
- **pmax** (INSERT_HERE): Maximum price of operation (Inclusive).
- **page** (INSERT_HERE): The number of the page to display results from.
- **operation_id_lt** (INSERT_HERE): ID of the operation from which the result begins.
- **receiver** (INSERT_HERE): Username of user, which receive money from you.
- **sender** (INSERT_HERE): Username of user, which sent money to you.
- **start_date** (INSERT_HERE): Start date of operation (RFC 3339 date format).
- **end_date** (INSERT_HERE): End date of operation (RFC 3339 date format).
- **wallet** (INSERT_HERE): Wallet, which used for money payots.
- **comment** (INSERT_HERE): Comment for money transfers.
- **is_hold** (INSERT_HERE): Display hold operations.
- **show_payments_stats** (INSERT_HERE): Display payment stats for selected period (outgoing value, incoming value).

**Example:**

```python
response = market.payments.history()
print(response.json())
```


## Transfer

POST https://api.lzt.market/balance/transfer

*Send money to any user.*

Required scopes: *market*

**Parameters:**

- **amount** (INSERT_HERE): Amount to send in your currency.
- **secret_answer** (INSERT_HERE): Secret answer of your account.
- **currency** (INSERT_HERE): Using currency for amount.
- **user_id** (INSERT_HERE): User id of receiver. If user_id specified, username is not required.
- **username** (INSERT_HERE): Username of receiver. If username specified, user_id is not required.
- **comment** (INSERT_HERE): Transfer comment.
- **transfer_hold** (INSERT_HERE): Hold transfer or not.
- **hold_length_option** (INSERT_HERE): Hold length option.
- **hold_length_value** (INSERT_HERE): Hold length value.

**Example:**

```python
response = market.payments.transfer(user_id=2410024, amount=250, currency="rub", secret_answer="My secret answer")
print(response.json())
```


## Fee

GET https://api.lzt.market/balance/transfer/fee

*Get transfer limits and get fee amount for transfer.*

Required scopes: *market*

**Parameters:**

- **amount** (INSERT_HERE): Amount to send in your currency.

**Example:**

```python
response = market.payments.fee(amount=250)
print(response.json())
```


## Generate Link

*Generate payment link.*

**Parameters:**

- **amount** (INSERT_HERE): Amount to send in your currency.
- **user_id** (INSERT_HERE): ID of user to transfer money.
- **username** (INSERT_HERE): Username to transfer money.
- **comment** (INSERT_HERE): Payment comment.
- **redirect_url** (INSERT_HERE): Redirect url. User who paid on this link will be redirected to this url.
- **currency** (INSERT_HERE): Using currency for amount.
- **hold** (INSERT_HERE): Hold transfer or not.
- **hold_length** (INSERT_HERE): Hold length.
    > Max - 1 month.
- **hold_period** (INSERT_HERE): Hold option.

**Example:**

```python
payment_link = market.payments.generate_link(user_id=2410024, amount=250, comment="Comment", redirect_url="https://example.com")
print(payment_link)
```


# Managing

## Tag

### Delete

DELETE https://api.lzt.market/{item_id}/tag

*Deletes tag for the account.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **tag_id** (INSERT_HERE): Tag id.
    > Tag list is available via market.profile.get()

**Example:**

```python
response = market.managing.tag.delete(item_id=1000000, tag_id=1000)
print(response.json())
```


### Add

POST https://api.lzt.market/{item_id}/tag

*Adds tag for the account.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **tag_id** (INSERT_HERE): Tag id.
    > Tag list is available via market.profile.get()

**Example:**

```python
response = market.managing.tag.add(item_id=1000000, tag_id=1000)
print(response.json())
```


## Steamman

### Guard

GET https://api.lzt.market/{item_id}/guard-code

*Gets confirmation code from MaFile (Only for Steam accounts).*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.steam.guard(item_id=1000000)
print(response.json())
```


### Mafile

GET https://api.lzt.market/{item_id}/mafile

*Returns mafile in JSON.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.steam.mafile(item_id=1000000)
print(response.json())
```


### Update Inventory

POST https://api.lzt.market/{item_id}/update-inventory

*Update inventory value.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **app_id** (INSERT_HERE): App id.

**Example:**

```python
response = market.managing.steam.update_inventory(item_id=1000000, app_id=730)
print(response.json())
```


### Inventory Value

GET https://api.lzt.market/steam-value

*Gets steam value.*

**Parameters:**

- **url** (INSERT_HERE): Link or id of account.
    > Can be [https://lzt.market/{item-id}/, https://steamcommunity.com/id/{steam-name}, https://steamcommunity.com/profiles/{steam-id}, {steam-id}].
- **item_id** (INSERT_HERE): Item id.
- **app_id** (INSERT_HERE): Application id.
- **currency** (INSERT_HERE): Using currency for amount.
- **ignore_cache** (INSERT_HERE): Ignore cache.

**Example:**

```python
response = market.managing.steam.inventory_value(item_id=1000000, app_id=730)
print(response.json())
```


### Confirm Sda

POST https://api.lzt.market/{item_id}/confirm-sda

*Confirm steam action.*
> Don't set id and nonce parameters to get list of available confirmation requests.

**Parameters:**

- **item_id** (INSERT_HERE): Item id.
- **id** (INSERT_HERE): Confirmation id.
    > Required along with **nonce** if you want to confirm action.
- **nonce** (INSERT_HERE): Confirmation nonce.
    > Required along with **id** if you want to confirm action.

**Example:**

```python
response = market.managing.steam.confirm_sda(item_id=1000000)
print(response.json())
```


## Telegramman

### Code

GET https://api.lzt.market/{item_id}/telegram-login-code

*Gets confirmation code from Telegram.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.telegram.code(item_id=1000000)
print(response.json())
```


### Reset Auth

POST https://api.lzt.market/{item_id}/telegram-reset-authorizations

*Resets Telegram authorizations.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.telegram.reset_auth(item_id=1000000)
print(response.json())
```


## Password Temp Mail

GET https://api.lzt.market/{item_id}/temp-email-password

*Gets password from temp email of account.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.password_temp_mail(item_id=1000000)
print(response.json())
```


## Get

GET https://api.lzt.market/{item_id}
GET https://api.lzt.market/{item_id}/steam-preview
GET https://api.lzt.market/{item_id}/auction

*Displays account information or returns Steam account html code.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **steam_preview** (INSERT_HERE): Set it True if you want to get steam html and False/None if you want to get account info
- **preview_type** (INSERT_HERE): Type of page - profiles or games

**Example:**

```python
response = market.managing.get(item_id=1000000)
print(response.json())
```


## Bulk Get

POST https://api.lzt.market/bulk/items

*Bulk get up to 250 accounts.*

Required scopes: *market*

**Parameters:**

- **item_ids** (INSERT_HERE): Item ids.

**Example:**

```python
response = market.managing.bulk_get(item_ids=[1000000, 2000000, 3000000, 4000000, 500000])
print(response.json())
```


## Delete

DELETE https://api.lzt.market/{item_id}

*Deletes your account from public search. Deletetion type is soft. You can restore account after deletetion if you want.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **reason** (INSERT_HERE): Delete reason.

**Example:**

```python
response = market.managing.delete(item_id=1000000)
print(response.json())
```


## Email

GET https://api.lzt.market/email-code

*Gets confirmation code or link.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **email** (INSERT_HERE): Account email.
- **login** (INSERT_HERE): Account login.

**Example:**

```python
response = market.managing.email(item_id=1000000)
print(response.json())
```


## Refuse Guarantee

POST https://api.lzt.market/{item_id}/refuse-guarantee

*Cancel guarantee of account. It can be useful for account reselling.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.refuse_guarantee(item_id=1000000)
print(response.json())
```


## Check Guarantee

POST https://api.lzt.market/{item_id}/check-guarantee

*Checks the guarantee and cancels it if there are reasons to cancel it.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.check_guarantee(item_id=1000000)
print(response.json())
```


## Change Password

POST https://api.lzt.market/{item_id}/change-password

*Changes password of account.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **_cancel** (INSERT_HERE): Cancel change password recommendation. It will be helpful, if you don't want to change password and get login data

**Example:**

```python
response = market.managing.change_password(item_id=1000000)
print(response.json())
```


## Stick

POST https://api.lzt.market/{item_id}/stick

*Stick account in the top of search.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.stick(item_id=1000000)
print(response.json())
```


## Unstick

DELETE https://api.lzt.market/{item_id}/stick

*Unstick account of the top of search.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.unstick(item_id=1000000)
print(response.json())
```


## Favorite

 POST https://api.lzt.market/{item_id}/star

*Adds account to favourites.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.favorite(item_id=1000000)
print(response.json())
```


## Unfavorite

DELETE https://api.lzt.market/{item_id}/star

*Deletes account from favourites.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.unfavorite(item_id=1000000)
print(response.json())
```


## Bump

POST https://api.lzt.market/{item_id}/bump

*Bumps account in the search.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.managing.bump(item_id=1000000)
print(response.json())
```


## Change Owner

POST https://api.lzt.market/{item_id}/change-owner

*Change of account owner.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **username** (INSERT_HERE): The username of the new account owner.
- **secret_answer** (INSERT_HERE): Secret answer of your account.

**Example:**

```python
response = market.managing.change_owner(item_id=1000000, username="AS7RID", secret_answer="My secret answer")
print(response.json())
```


## Edit

PUT https://api.lzt.market/{item_id}/edit

*Edits any details of account.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item
- **price** (INSERT_HERE): Account price in your currency.
- **currency** (INSERT_HERE): Using currency.
- **item_origin** (INSERT_HERE): Account origin.
- **title** (INSERT_HERE): Russian title of account.
    > If title specified and title_en is empty, title_en will be automatically translated to English language.
- **title_en** (INSERT_HERE): English title of account.
    > If title_en specified and title is empty, title will be automatically translated to Russian language.
- **description** (INSERT_HERE): Account public description.
- **information** (INSERT_HERE): Account private information (visible for buyer only if purchased).
- **email_login_data** (INSERT_HERE): Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
- **email_type** (INSERT_HERE): Email type.
- **allow_ask_discount** (INSERT_HERE): Allow users to ask discount for this account.
- **proxy_id** (INSERT_HERE): Using proxy id for account checking.

**Example:**

```python
response = market.managing.edit(item_id=1000000, price=1000)
print(response.json())
```


## Arbitrage

POST https://api.lzt.market/{item_id}/claims

*Create a Arbitrage.*

Required scopes: *post*

**Parameters:**

- **post_body** (INSERT_HERE): You should describe what's happened.

**Example:**

```python
response = market.managing.arbitrage(item_id=1000000, post_body="There i'am discribe what's happened.")
print(response.json())
```


# Purchasing

## Auction

### Place Bid

POST https://api.lzt.market/{item_id}/auction/bid

*Create a new auction bid.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **amount** (INSERT_HERE): Amount bid.
- **currency** (INSERT_HERE): Using currency.

**Example:**

```python
response = market.purchasing.auction.place_bid(item_id=1000000, amount=1000)
print(response.json())
```


### Delete Bid

GET https://api.lzt.market/{item_id}/auction/bid

*Delete your auction bid.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **bid_id** (INSERT_HERE): ID of bid.

**Example:**

```python
response = market.purchasing.auction.delete_bid(item_id=1000000, bid_id=1000)
print(response.json())
```


## Check

POST https://api.lzt.market/{item_id}/check-account

*Checking account for validity. If the account is invalid, the purchase will be canceled automatically*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.

**Example:**

```python
response = market.purchasing.check(item_id=1000000)
print(response.json())
```


## Confirm

POST https://api.lzt.market/{item_id}/confirm-buy

*Confirm buy.*

Required scopes: *market*

**Example:**

```python
response = market.purchasing.confirm(item_id=1000000)
print(response.json())
```


## Fast Buy

POST https://api.lzt.market/{item_id}/fast-buy

*Check and buy account.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **price** (INSERT_HERE): Current price of account in your currency.
- **buy_without_validation** (INSERT_HERE): Use TRUE if you want to buy account without account data validation (not safe).

**Example:**

```python
response = market.purchasing.fast_buy(item_id=1000000, price=1000)
print(response.json())
```


# Publishing

## Info

GET https://api.lzt.market/{item_id}/goods/add

*Get info about not published item. For categories, which required temporary email (Steam, Social Club), you will get temporary email in response.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID of item.
- **resell_item_id** (INSERT_HERE): Put item id, if you are trying to resell item. This is useful to pass temporary email from reselling item to new item. You will get same temporary email from reselling account.

**Example:**

```python
response = market.publishing.info(item_id=1000000)
print(response.json())
```


## Check

POST https://api.lzt.market/{item_id}/goods/check

*Check account on validity. If account is valid, account will be published on the market.*

Required scopes: *market*

**Parameters:**

- **item_id** (INSERT_HERE): ID for item.
- **login** (INSERT_HERE): Account login (or email).
- **password** (INSERT_HERE): Account password.
- **login_password** (INSERT_HERE): Account login data format login:password.
- **close_item** (INSERT_HERE): If True, the item will be closed item_state = closed.
- **extra** (INSERT_HERE): Extra params for account checking.
- **resell_item_id** (INSERT_HERE): Put item id, if you are trying to resell item.
- **random_proxy** (INSERT_HERE): Pass True, if you get captcha in previous response.

**Example:**

```python
response = market.publishing.check(item_id=1000000, login="login", password="password")
print(response.json())
```


## Add

POST https://api.lzt.market/item/add

*Adds account on the market.*

Required scopes: *market*

**Parameters:**

- **category_id** (INSERT_HERE): Accounts category.
- **price** (INSERT_HERE): Account price in your currency.
- **currency** (INSERT_HERE): Using currency.
- **item_origin** (INSERT_HERE): Account origin. Where did you get it from.
- **extended_guarantee** (INSERT_HERE): Guarantee type.
- **title** (INSERT_HERE): Russian title of account.
    > If title specified and title_en is empty, title_en will be automatically translated to English language.
- **title_en** (INSERT_HERE): English title of account.
    > If title_en specified and title is empty, title will be automatically translated to Russian language.
- **description** (INSERT_HERE): Account public description.
- **information** (INSERT_HERE): Account private information (visible for buyer only if purchased).
- **has_email_login_data** (INSERT_HERE): Required if a category is one of list of Required email login data categories.
- **email_login_data** (INSERT_HERE): Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
- **email_type** (INSERT_HERE): Email type.
- **allow_ask_discount** (INSERT_HERE): Allow users to ask discount for this account.
- **proxy_id** (INSERT_HERE): Using proxy id for account checking.
- **random_proxy** (INSERT_HERE): Pass True, if you get captcha in previous response
- **auction** (INSERT_HERE): Pass True if you want to create auction
- **auction_duration_value** (INSERT_HERE): Duration auction value.
- **auction_duration_option** (INSERT_HERE): Duration auction option.
- **instabuy_price** (INSERT_HERE): The price for which you can instantly redeem your account.
- **not_bids_action** (INSERT_HERE): If you set cancel, at the end of the auction with 0 bids, the account can be purchased at the price you specified as the minimum bid. Can be [close, cancel]

**Example:**

```python
response = market.publishing.add(category_id=24, price=100, currency="rub", item_origin="stealer", title="Telegram")
print(response.json())
```


## Fast Sell

POST https://api.lzt.market/item/fast-sell

*Adds and check account on validity. If account is valid, account will be published on the market.*

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


Required scopes: *market*
**Parameters:**

- **category_id** (INSERT_HERE): Accounts category.
- **price** (INSERT_HERE): Account price in your currency.
- **currency** (INSERT_HERE): Using currency.
- **item_origin** (INSERT_HERE): Account origin. Where did you get it from.
- **extended_guarantee** (INSERT_HERE): Guarantee type.
- **title** (INSERT_HERE): Russian title of account.
    > If title specified and title_en is empty, title_en will be automatically translated to English language.
- **title_en** (INSERT_HERE): English title of account.
    > If title_en specified and title is empty, title will be automatically translated to Russian language.
- **description** (INSERT_HERE): Account public description.
- **information** (INSERT_HERE): Account private information (visible for buyer only if purchased).
- **has_email_login_data** (INSERT_HERE): Required if a category is one of list of Required email login data categories.
- **email_login_data** (INSERT_HERE): Required if a category is one of list of Required email login data categories. Email login data (login:pass format).
- **email_type** (INSERT_HERE): Email type.
- **allow_ask_discount** (INSERT_HERE): Allow users to ask discount for this account.
- **proxy_id** (INSERT_HERE): Using proxy id for account checking.
- **random_proxy** (INSERT_HERE): Pass True, if you get captcha in previous response.
- **login** (INSERT_HERE): Account login (or email).
- **password** (INSERT_HERE): Account password.
- **login_password** (INSERT_HERE): Account login data format login:password.
- **extra** (INSERT_HERE): Extra params for account checking.
- **auction** (INSERT_HERE): Pass True if you want to create auction.
- **auction_duration_value** (INSERT_HERE): Duration auction value.
- **auction_duration_option** (INSERT_HERE): Duration auction option.
- **instabuy_price** (INSERT_HERE): The price for which you can instantly redeem your account.
- **not_bids_action** (INSERT_HERE): If you set cancel, at the end of the auction with 0 bids, the account can be purchased at the price you specified as the minimum bid. Can be [close, cancel]

**Example:**

```python
response = market.publishing.add(category_id=24, price=100, currency="rub", item_origin="stealer", login="auth_key", password="dc_id", title="Telegram")
print(response.json())
```


# Proxy

## Get

GET https://api.lzt.market/proxy

*Gets your proxy list.*

Required scopes: *market*

**Example:**

```python
response = market.proxy.get()
print(response.json())
```


## Delete

DELETE https://api.lzt.market/proxy

*Delete single or all proxies.*

Required scopes: *market*

**Parameters:**

- **proxy_id** (INSERT_HERE): ID of an existing proxy.
- **delete_all** (INSERT_HERE): Use True if you want to delete all proxy.

**Example:**

```python
response = market.proxy.delete(delete_all=True)
print(response.json())
```


## Add

POST https://api.lzt.market/proxy

*Add single proxy or proxy list.*

Required scopes: *market*

**Parameters:**

- **proxy_ip** (INSERT_HERE): Proxy ip or host.
- **proxy_port** (INSERT_HERE): Proxy port
- **proxy_user** (INSERT_HERE): Proxy username
- **proxy_pass** (INSERT_HERE): Proxy password
- **proxy_row** (INSERT_HERE): Proxy list in String format ip:port:user:pass.
    > Each proxy must be start with new line (use *\n* separator)

**Example:**

```python
response = market.proxy.add(proxy_row="192.168.1.1:8080:login:password
192.168.2.2:8080:login:password")
print(response.json())
```



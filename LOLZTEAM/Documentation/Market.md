<font size=6 style="margin: auto"><center>
[Forum docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Forum.md) - [Antipublic Docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Antipublic.md)
[Utility docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Utils.md)
</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

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
* [List](#list-1)
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
  * [Transfer Cancel](#transfer-cancel)
  * [Generate Link](#generate-link)
* [Managing](#managing)
  * [Tag](#tag)
    * [Delete](#delete)
    * [Add](#add)
  * [Steam](#steam-1)
    * [Guard](#guard)
    * [Mafile](#mafile)
    * [Update Inventory](#update-inventory)
    * [Inventory Value](#inventory-value)
    * [Confirm Sda](#confirm-sda)
  * [Telegram](#telegram-1)
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
  * [Note](#note)
  * [Change Owner](#change-owner)
  * [Edit](#edit-1)
  * [Arbitrage](#arbitrage)
* [Purchasing](#purchasing)
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

- **disable_steam_guard** (bool): Disable Steam Guard on account purchase moment
- **user_allow_ask_discount** (bool): Allow users ask discount for your accounts
- **max_discount_percent** (int): Maximum discount percents for your accounts
- **allow_accept_accounts** (str): Usernames who can transfer market accounts to you. Separate values with a comma.
- **hide_favorites** (bool): Hide your profile info when you add an account to favorites
- **title** (str): Market title.
- **telegram_client** (dict): Telegram client. It should be {"telegram_api_id"
- **deauthorize_steam** (bool): Finish all Steam sessions after purchase.

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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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


### Params

GET https://api.lzt.market/supercell/params

*Displays search parameters for a category.*

**Example:**

```python
response = market.category.supercell.params()
print(response.json())
```


## Origin

### Get

GET https://api.lzt.market/origin

*Displays a list of accounts in a specific category according to your parameters.*

Required scopes: *market*

**Parameters:**

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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

- **page** (int): The number of the page to display results from
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
- **page** (int): The number of the page to display results from
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


## List

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


# List

## From Url

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


## Latest

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


## Owned

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


## Purchased

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


## Favorite

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


## Viewed

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


# Payments

## History

GET https://api.lzt.market/user/payments

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


## Transfer

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


## Fee

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


## Transfer Cancel

POST https://api.lzt.market/balance/transfer/cancel

*Cancels a transfer with a hold that was sent to your account.*

Required scopes: *market*

**Parameters:**

- **payment_id** (int): Payment id.

**Example:**

```python
response = market.payments.transfer_cancel(payment_id=2410024)
print(response.json())
```


## Generate Link

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


# Managing

## Tag

### Delete

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


### Add

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


## Steam

### Guard

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


### Mafile

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


### Update Inventory

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


### Inventory Value

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


### Confirm Sda

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


## Telegram

### Code

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


### Reset Auth

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


## Password Temp Mail

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


## Get

GET https://api.lzt.market/{item_id}
GET https://api.lzt.market/{item_id}/steam-preview

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


## Bulk Get

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


## Delete

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


## Email

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


## Refuse Guarantee

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


## Check Guarantee

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


## Change Password

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


## Stick

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


## Unstick

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


## Favorite

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
            

## Unfavorite

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


## Bump

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


## Note

POST https://api.lzt.market/{item_id}/note-save

*Edits a note for the account.*

Required scopes: *market*

**Parameters:**

- **item_id** (int): ID of item.
- **text** (str): Text of note.

**Example:**

```python
response = market.managing.note(item_id=1000000, text="Good account")
print(response.json())
```


## Change Owner

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


## Edit

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


## Arbitrage

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


# Purchasing

## Check

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

- **item_id** (int): ID of item.
- **price** (float): Current price of account in your currency.
- **buy_without_validation** (bool): Use TRUE if you want to buy account without account data validation (not safe).

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

- **item_id** (int): ID of item.
- **resell_item_id** (int): Put item id, if you are trying to resell item. This is useful to pass temporary email from reselling item to new item. You will get same temporary email from reselling account.

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

- **item_id** (int): ID for item.
- **login** (str): Account login (or email).
- **password** (str): Account password.
- **login_password** (str): Account login data format login:password.
- **close_item** (bool): If True, the item will be closed item_state = closed.
- **extra** (str): Extra params for account checking.
- **resell_item_id** (int): Put item id, if you are trying to resell item.
- **random_proxy** (bool): Pass True, if you get captcha in previous response.
- **proxy** (str): Proxy line format ip:port:user:pass (prioritize over proxy_id parameter).

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
- **instabuy_price** (float): The price for which you can instantly redeem your account.

**Example:**

```python
response = market.publishing.add(category_id=24, price=100, currency="rub", item_origin="stealer", title="Telegram")
print(response.json())
```


## Fast Sell

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
- **close_item** (bool): If True, the item will be closed item_state = closed.
- **proxy** (str): Proxy line format ip:port:user:pass (prioritize over proxy_id parameter).

**Example:**

```python
response = market.publishing.fast_sell(category_id=24, price=100, currency="rub", item_origin="stealer", login="auth_key", password="dc_id", title="Telegram")
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

- **proxy_id** (int): ID of an existing proxy.
- **delete_all** (bool): Use True if you want to delete all proxy.

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

- **proxy_ip** (str): Proxy ip or host.
- **proxy_port** (str): Proxy port
- **proxy_user** (str): Proxy username
- **proxy_pass** (str): Proxy password
- **proxy_row** (str): Proxy list in String format ip:port:user:pass.
    > Each proxy must be start with new line (use *\n* separator)

**Example:**

```python
response = market.proxy.add(proxy_row="192.168.1.1:8080:login:password
192.168.2.2:8080:login:password")
print(response.json())
```


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



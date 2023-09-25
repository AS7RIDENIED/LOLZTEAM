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

### Get

*Displays info about your profile.*

**Example:**

```python
data = api.market.profile.get()
print(data)
```

```python
{'user': {'user_id': 2410024, 'username': 'AS7RID', 'username_html': '<span  class="style22">AS7RID</span>', 'user_message_count': 1067, 'user_register_date': 1560282271, 'user_like_count': 2932, ...}
```

### Edit

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
{'status': 'ok', 'message': 'Changes Saved', 'system_info': {'visitor_id': 2410024, 'time': 1695564377}}
```

# List

*Methods for getting account lists*

---

## Categories

### Get

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
- **search_params** (dict): Search params for your request.
  > Example {"origin":"autoreg"} will return only "autoreg" accounts

**Example:**

```python
data = api.market.list.categories.get(category_name=Types.Market.Categories.vk,pmax=10)
print(data)
```

```python
{'items': [item1, item2, item3, ...], 'totalItems': 6479, 'totalItemsPrice': None, 'perPage': 40, 'page': 1, 'cacheTTL': 1695568336, 'lastModified': 1695568306, 'searchUrl': '/vkontakte?pmax=10&locale=en', 'stickyItems': [], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695568306}}
```

### Categories

*Display category list.*

**Parameters:**

- **top_queries** (bool): Display top queries for per category.

**Example:**

```python
data = api.market.list.categories.categories()
print(data)
```

```python
{'0': {'category_id': 1, 'sub_category_id': 1, 'category_order': 10, 'category_title': 'Steam', 'category_name': 'steam', 'category_url': 'steam', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты steam с %s, а так же у нас есть продажа аккаунтов стим с %s.', 'category_login_url': 'https://steamcommunity.com/login/home/', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 1, 'has_account_link': 1, 'require_temp_email': 1, 'recovery_link': 'https://help.steampowered.com/en/wizard/HelpWithLoginInfo?accountsearch=1', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 1, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '1': {'category_id': 9, 'sub_category_id': 1, 'category_order': 20, 'category_title': 'Fortnite', 'category_name': 'fortnite', 'category_url': 'fortnite', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести аккаунты фортнайт по низкой цене со скинами и pve', 'category_login_url': 'https://www.epicgames.com/id/login/epic?redirect_uri=https%3A%2F%2Fwww.epicgames.com%2Faccount%2Fpersonal%3FproductName%3Dfortnite%26lang%3Dru', 'add_item_available': 1, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': 'https://www.epicgames.com/id/login/forgot-password', 'check_button_enabled': 0, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 1, 'require_email_login_data': 1, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 1, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 1, 'cookies': 'required', 'login_type': 'email', 'guest_hidden': 0, 'available_temp_email': 1, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '2': {'category_id': 2, 'sub_category_id': 1, 'category_order': 30, 'category_title': 'VKontakte', 'category_name': 'vk', 'category_url': 'vkontakte', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты VKontakte с подписчиками, друзьями, а так же у нас есть продажа аккаунтов ВК с голосами.', 'category_login_url': 'https://vk.com/login', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 1, 'require_video_recording': 0, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '2', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '3': {'category_id': 17, 'sub_category_id': 1, 'category_order': 40, 'category_title': 'Genshin Impact', 'category_name': 'genshin', 'category_url': 'genshin-impact', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты геншин импакт с легендарными персонажами, много созвездий и легендарных оружий', 'category_login_url': 'https://account.mihoyo.com/?lang=en#/account/safetySettings', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '4': {'category_id': 13, 'sub_category_id': 1, 'category_order': 50, 'category_title': 'Valorant', 'category_name': 'valorant', 'category_url': 'valorant', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести качественные аккаунты валорант бета без привязок по низким ценам', 'category_login_url': 'https://account.riotgames.com/', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '4', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'username', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '5': {'category_id': 29, 'sub_category_id': 1, 'category_order': 55, 'category_title': 'League of Legends', 'category_name': 'lol', 'category_url': 'league-of-legends', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести качественные аккаунты League of Legends без привязок по низким ценам', 'category_login_url': '', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': 'League of Legends', 'account_price_min': 1, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '4', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'username', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '6': {'category_id': 24, 'sub_category_id': 1, 'category_order': 60, 'category_title': 'Telegram', 'category_name': 'telegram', 'category_url': 'telegram', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести аккаунт Telegram оптом, с отлежкой, в комплекте идет tdata, широкий выбор стран: Россия, Украина, США, а также авторег телеграм аккаунты', 'category_login_url': '', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': 'Telegram', 'category_h1_html_en': 'Telegram', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 90, 'buy_without_validation': 1}, '7': {'category_id': 6, 'sub_category_id': 1, 'category_order': 60, 'category_title': 'Diamond RP', 'category_name': 'diamondrp', 'category_url': 'diamondrp', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести аккаунты даймонд рп по низкой цене с деньгами и без привязки', 'category_login_url': 'https://diamondrp.ru/cabinet/login', 'add_item_available': 0, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 0, 'support_personal_proxy': 0, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 0, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '8': {'category_id': 15, 'sub_category_id': 1, 'category_order': 70, 'category_title': 'Supercell', 'category_name': 'supercell', 'category_url': 'supercell', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести аккаунт Brawl Stars, Clash of Clans или Clash Royale. Есть аккаунты с дорогими бравлерами, есть дешевые и прокаченные акки', 'category_login_url': '', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'email', 'guest_hidden': 0, 'available_temp_email': 1, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '9': {'category_id': 3, 'sub_category_id': 1, 'category_order': 80, 'category_title': 'Origin (EA)', 'category_name': 'ea', 'category_url': 'origin', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты origin с батлой 1, фифой 18, а так же у нас есть продажа аккаунтов origin с играми.', 'category_login_url': 'https://www.origin.com/rus/ru-ru/store', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 1, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'required', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '10': {'category_id': 14, 'sub_category_id': 1, 'category_order': 90, 'category_title': 'World of Tanks', 'category_name': 'wot', 'category_url': 'world-of-tanks', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты ворлд оф тэнкс с золотом, много боев, без привязок по очень низким ценам', 'category_login_url': 'https://ru.wargaming.net/id/signin/', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '4', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '11': {'category_id': 16, 'sub_category_id': 1, 'category_order': 95, 'category_title': 'World of Tanks Blitz', 'category_name': 'wot', 'category_url': 'wot-blitz', 'category_description_html': 'Аккаунты World of Tanks Blitz без привязки с золотом и техникой', 'category_login_url': 'https://ru.wargaming.net/id/signin/', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '4', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '12': {'category_id': 12, 'sub_category_id': 1, 'category_order': 100, 'category_title': 'Epic Games', 'category_name': 'eg', 'category_url': 'epicgames', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести качественные аккаунты epic games по низким ценам, а также с игрой Metro Exodus, RDR 2, World War Z, Borderlands 3', 'category_login_url': 'https://www.epicgames.com/id/login/epic?redirect_uri=https%3A%2F%2Fwww.epicgames.com%2Faccount%2Fpersonal%3FproductName%3Dfortnite%26lang%3Dru', 'add_item_available': 1, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': 'https://www.epicgames.com/id/login/forgot-password', 'check_button_enabled': 0, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 1, 'require_email_login_data': 1, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 1, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'email', 'guest_hidden': 0, 'available_temp_email': 1, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '13': {'category_id': 18, 'sub_category_id': 1, 'category_order': 110, 'category_title': 'Escape from Tarkov', 'category_name': 'tarkov', 'category_url': 'escape-from-tarkov', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести качественные аккаунты Escape From Tarkov с валютой и прокаченным персонажем.', 'category_login_url': 'https://www.escapefromtarkov.com/login', 'add_item_available': 1, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 1, 'require_email_login_data': 1, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 1, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1,2', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'email', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '14': {'category_id': 21, 'sub_category_id': 1, 'category_order': 120, 'category_title': 'Twitter', 'category_name': 'twitter', 'category_url': '', 'category_description_html': '', 'category_login_url': '', 'add_item_available': 0, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 0, 'support_personal_proxy': 0, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 0, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 1, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '15': {'category_id': 7, 'sub_category_id': 1, 'category_order': 120, 'category_title': 'Social Club', 'category_name': 'socialclub', 'category_url': 'socialclub', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты сошл клаб с гта 5 без бана и привязки.', 'category_login_url': 'https://ru.socialclub.rockstargames.com/profile/signin', 'add_item_available': 1, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 1, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 1, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 1, 'cookies': 'required', 'login_type': 'email', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '16': {'category_id': 5, 'sub_category_id': 1, 'category_order': 130, 'category_title': 'Uplay', 'category_name': 'uplay', 'category_url': 'uplay', 'category_description_html': "На нашем сайте предоставляется уникальная возможность купить аккаунты assassin's creed origins, с the crew а так же у нас есть продажа аккаунтов uplay с far cry", 'category_login_url': 'https://support.ubi.com/ru-RU/Cases/New', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'email', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '17': {'category_id': 27, 'sub_category_id': 1, 'category_order': 140, 'category_title': 'War Thunder', 'category_name': 'wt', 'category_url': 'war-thunder', 'category_description_html': '', 'category_login_url': 'https://login.gaijin.net/ru/', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '18': {'category_id': 22, 'sub_category_id': 1, 'category_order': 150, 'category_title': 'Discord', 'category_name': 'ds', 'category_url': 'discord', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести дискорд токены по низкой цене, проспам, чистые токены, с биллингом', 'category_login_url': '', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': 'Discord', 'category_h1_html_en': 'Discord', 'account_price_min': 1, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 0, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '19': {'category_id': 20, 'sub_category_id': 1, 'category_order': 170, 'category_title': 'TikTok', 'category_name': 'tt', 'category_url': 'tiktok', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты тикток с подписчиками, лайками, а так же у нас есть продажа аккаунтов тикток для рекламы и с отлежкой.', 'category_login_url': 'https://www.tiktok.com/login', 'add_item_available': 1, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '123', 'account_price_min': 5, 'require_video_recording': 1, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'required', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '20': {'category_id': 10, 'sub_category_id': 1, 'category_order': 180, 'category_title': 'Instagram', 'category_name': 'instagram', 'category_url': 'instagram', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести качественные аккаунты instagram по низкой цене с подписчиками, а также пустые, автореги, брут, с большим количеством публикаций', 'category_login_url': 'https://www.instagram.com/accounts/login/?source=auth_switcher', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 1, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '5', 'support_temp_email': 0, 'cookies': 'available', 'login_type': 'username', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '21': {'category_id': 11, 'sub_category_id': 1, 'category_order': 190, 'category_title': 'Battle.net', 'category_name': 'battlenet', 'category_url': 'battlenet', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести качественные аккаунты батл нет за 10 рублей, а также с овервотчем', 'category_login_url': 'https://www.blizzard.com/login', 'add_item_available': 1, 'mass_upload_item_available': 0, 'has_guarantee': 1, 'has_account_link': 1, 'require_temp_email': 1, 'recovery_link': 'https://eu.battle.net/account/recovery/en-us/identify-account.html?requestType=PASSWORD_RESET', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 1, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 1, 'cookies': 'none', 'login_type': 'email', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '22': {'category_id': 19, 'sub_category_id': 1, 'category_order': 200, 'category_title': 'VPN', 'category_name': 'vpn', 'category_url': 'vpn', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты впн сервисов, такие как Vypr VPN, Surfshark VPN, IpVanish, Windscribe VPN Pro, а также vpn аккаунты ZenMate, TunnelBear VPN\r\n', 'category_login_url': '1', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 0, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '23': {'category_id': 23, 'sub_category_id': 1, 'category_order': 210, 'category_title': 'Streaming media services', 'category_name': 'cinema', 'category_url': 'cinema', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность приобрести аккаунт онлайн кинотеатра: окко, иви, кинопоиск, мегого и другие', 'category_login_url': '', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 0, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 1, 'require_video_recording': 0, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 1, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '24': {'category_id': 26, 'sub_category_id': 1, 'category_order': 220, 'category_title': 'Spotify', 'category_name': 'spotify', 'category_url': 'spotify', 'category_description_html': '', 'category_login_url': 'https://www.spotify.com/int/login/?continue=https%3A%2F%2Fopen.spotify.com%2F__noul__%3Fl2l%3D1%26nd%3D1', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': 'Spotify', 'account_price_min': 1, 'require_video_recording': 0, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '25': {'category_id': 4, 'sub_category_id': 1, 'category_order': 230, 'category_title': 'Warface', 'category_name': 'wf', 'category_url': 'warface', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты warface без привязки, с донатом а так же у нас есть продажа аккаунтов варфейс альфа, чарли без обмана.', 'category_login_url': 'https://wf.mail.ru/', 'add_item_available': 4, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 0, 'support_personal_proxy': 0, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 5, 'require_video_recording': 1, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '4', 'support_temp_email': 0, 'cookies': 'required', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '26': {'category_id': 25, 'sub_category_id': 1, 'category_order': 240, 'category_title': 'YouTube', 'category_name': 'youtube', 'category_url': 'youtube', 'category_description_html': '', 'category_login_url': '', 'add_item_available': 1, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 1, 'require_video_recording': 1, 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'required', 'login_type': 'any', 'guest_hidden': 1, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, '27': {'category_id': 28, 'sub_category_id': 1, 'category_order': 260, 'category_title': 'Minecraft', 'category_name': 'minecraft', 'category_url': 'minecraft', 'category_description_html': 'minecraft', 'category_login_url': '', 'add_item_available': 0, 'mass_upload_item_available': 0, 'has_guarantee': 0, 'has_account_link': 0, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 0, 'checker_enabled': 0, 'support_personal_proxy': 0, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 0, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 1, 'require_video_recording': 0, 'require_eld_for_native_accs': 1, 'can_be_resold': 1, 'proxy_type': '1', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'email', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695568463}}
```

### Params

*Displays search parameters for a category.*

**Parameters:**

- **category_name** (str): Name of category.

**Example:**

```python
data = api.market.list.categories.params(category_name=Types.Market.Categories.vk)
print(data)
```

```python
{'category': {'category_id': 2, 'sub_category_id': 1, 'category_order': 30, 'category_title': 'VKontakte', 'category_name': 'vk', 'category_url': 'vkontakte', 'category_description_html': 'На нашем сайте предоставляется уникальная возможность купить аккаунты VKontakte с подписчиками, друзьями, а так же у нас есть продажа аккаунтов ВК с голосами.', 'category_login_url': 'https://vk.com/login', 'add_item_available': 1, 'mass_upload_item_available': 1, 'has_guarantee': 0, 'has_account_link': 1, 'require_temp_email': 0, 'recovery_link': '', 'check_button_enabled': 1, 'checker_enabled': 1, 'support_personal_proxy': 1, 'support_email_login_data': 0, 'require_email_login_data': 0, 'display_in_list': 1, 'category_description_html_en': '', 'category_h1_html_en': '', 'account_price_min': 1, 'require_video_recording': 0, 'top_queries': '[{"category_id":2,"order_by":"price_to_up","tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?order_by=price_to_up"},{"category_id":2,"pmax":10,"tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?pmax=10"},{"category_id":2,"tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"sex":"woman","relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?sex=woman"},{"category_id":2,"order_by":"price_to_up","tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"tel":"yes","relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?tel=yes&order_by=price_to_up"},{"category_id":2,"pmax":15,"tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?pmax=15"},{"category_id":2,"pmax":7,"tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?pmax=7"},{"category_id":2,"pmax":8,"tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?pmax=8"},{"category_id":2,"pmax":10,"order_by":"price_to_up","tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"tel":"yes","relation":[],"admin_level":0,"reg":10,"reg_period":"day","mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte?oauth_token=a539e7f3ff17179e7a0eeb7c2c84dcc3071a4ef5&pmax=10&reg=10&reg_period=day&tel=yes&order_by=price_to_up"},{"category_id":2,"order_by":"pdate_to_down_upload","tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?order_by=pdate_to_down_upload"},{"category_id":2,"order_by":"price_to_down","tag_id":[],"not_tag_id":[],"origin":[],"not_origin":[],"user_id":0,"nsb_by_me":false,"sb_by_me":false,"hide_viewed":false,"email_login_data":false,"email_type":[],"search_id":0,"vk_country":[],"vk_city":[],"relation":[],"admin_level":0,"mcountry":[],"not_mcountry":[],"opened_profile":false,"userItems":false,"userOrders":false,"searchUrl":"\\/vkontakte\\/?order_by=price_to_down"}]', 'require_eld_for_native_accs': 0, 'can_be_resold': 1, 'proxy_type': '2', 'support_temp_email': 0, 'cookies': 'none', 'login_type': 'any', 'guest_hidden': 0, 'available_temp_email': 0, 'resale_duration_limit_days': 30, 'buy_without_validation': 1}, 'params': [{'name': 'vk_country', 'input': 'array', 'description': 'List of allowed countries'}, {'name': 'vk_city', 'input': 'array', 'description': 'List of allowed cities'}, {'name': 'vk_friend_min', 'input': 'number', 'description': 'Minimum number of friends'}, {'name': 'vk_friend_max', 'input': 'number', 'description': 'Maximum number of friends'}, {'name': 'vk_follower_min', 'input': 'number', 'description': 'Minimum number of followers'}, {'name': 'vk_follower_max', 'input': 'number', 'description': 'Maximum number of followers'}, {'name': 'vk_vote_min', 'input': 'number', 'description': 'Minimum number of votes'}, {'name': 'vk_vote_max', 'input': 'number', 'description': 'Maximum number of votes'}, {'name': 'sex', 'input': 'string', 'description': 'Sex of account', 'values': ['man', 'woman']}, {'name': 'tel', 'input': 'yesno', 'description': 'Has linked mobile', 'values': ['yes', 'no', 'nomatter']}, {'name': 'email', 'input': 'yesno', 'description': 'Has linked email', 'values': ['yes', 'no', 'nomatter']}, {'name': 'tfa', 'input': 'yesno', 'description': 'Has enabled 2FA', 'values': ['yes', 'no', 'nomatter']}, {'name': 'relation', 'input': 'array', 'description': 'Relationship', 'values': [0, 1, 2, 3, 4, 5, 6, 7, 8]}, {'name': 'group_follower_min', 'input': 'number', 'description': 'Minimum number of group followers'}, {'name': 'group_follower_max', 'input': 'number', 'description': 'Maximum number of group followers'}, {'name': 'groups_min', 'input': 'number', 'description': 'Minimum number of groups'}, {'name': 'groups_max', 'input': 'number', 'description': 'Maximum number of groups'}, {'name': 'admin_level', 'input': 'number', 'description': 'Admin group level', 'values': [4, 3, 2, 1]}, {'name': 'min_age', 'input': 'number', 'description': 'Minimum age'}, {'name': 'max_age', 'input': 'number', 'description': 'Maximum age'}, {'name': 'dig_min', 'input': 'number', 'description': 'Minimum number of digits in ID'}, {'name': 'dig_max', 'input': 'number', 'description': 'Maximum number of digits in ID'}, {'name': 'conversations_min', 'input': 'number', 'description': 'Minimum number of conversations'}, {'name': 'conversations_max', 'input': 'number', 'description': 'Maximum number of conversations'}, {'name': 'reg', 'input': 'number', 'description': 'How old is the account'}, {'name': 'reg_period', 'input': 'string', 'description': 'In what notation is time measured', 'values': ['day', 'month', 'year']}, {'name': 'mcountry', 'input': 'array', 'description': 'List of allowed countries of phone number'}, {'name': 'not_mcountry', 'input': 'array', 'description': 'List of excluded countries of phone number'}, {'name': 'opened_profile', 'input': 'boolean', 'description': 'Opened account profile'}, {'name': 'verified', 'input': 'yesno', 'description': 'Has verification', 'values': ['yes', 'no', 'nomatter']}], 'base_params': {'0': {'name': 'pmin', 'input': 'number', 'description': 'Minimum price'}, '1': {'name': 'pmax', 'input': 'number', 'description': 'Maximum price'}, '2': {'name': 'title', 'input': 'string', 'description': 'Title'}, '3': {'name': 'order_by', 'input': 'string', 'description': 'Order by', 'values': ['price_to_up', 'price_to_down', 'pdate_to_down', 'pdate_to_down_upload', 'pdate_to_up', 'pdate_to_up_upload']}, '4': {'name': 'show', 'input': 'string', 'description': 'Type of account', 'values': ['active', 'closed', 'awaiting', 'deleted']}, '5': {'name': 'tag_id', 'input': 'array', 'description': 'List of tag ids'}, '6': {'name': 'not_tag_id', 'input': 'array', 'description': "List of tag ids that won't be included"}, '7': {'name': 'origin', 'input': 'array', 'description': 'List of account origins', 'values': ['brute', 'fishing', 'stealer', 'personal', 'resale', 'autoreg']}, '8': {'name': 'not_origin', 'input': 'array', 'description': "List of account origins that won't be included"}, '9': {'name': 'user_id', 'input': 'number', 'description': 'Search accounts of user'}, '10': {'name': 'nsb', 'input': 'boolean', 'description': 'Not sold before'}, '11': {'name': 'sb', 'input': 'boolean', 'description': 'Sold before'}, '12': {'name': 'nsb_by_me', 'input': 'boolean', 'description': 'Not sold by me before'}, '13': {'name': 'sb_by_me', 'input': 'boolean', 'description': 'Sold by me before'}, '14': {'name': 'eg', 'input': 'string', 'description': 'Guarantee period. -1 = 12 hours, 0 = 24 hours, 1 = 72 hours', 'values': ['-1', '0', '1']}, '15': {'name': 'hide_viewed', 'input': 'boolean', 'description': 'Hide viewed accounts'}, '16': {'name': 'currency', 'input': 'string', 'description': 'Currency in which the cost of the account will be shown. ISO 3166'}, '17': {'name': 'email_login_data', 'input': 'boolean', 'description': 'Has email login data'}, '18': {'name': 'item_domain', 'input': 'boolean', 'description': 'Domain of native/autoreg email'}, '19': {'name': 'email_type', 'input': 'array', 'description': 'Email type', 'values': ['market', 'autoreg', 'native', 'no']}, '22': {'name': 'delete_reason', 'input': 'string', 'description': 'Delete reason of account (Works only for owned deleted accounts)'}}, 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695568625}}
```

### Games

*Displays a list of games in the category.*

**Parameters:**

- **category_name** (str): Name of category.

**Example**:

```python
data = api.market.list.categories.games(category_name=Types.Market.Categories.steam)
print(data)
```

```python
{'games': [game1, game2, game3, ...], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695568884}}

```
---

### Get

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
{'item': {'item_id': 2410024, 'item_state': 'paid', 'category_id': 2, 'published_date': 1566068135, 'title': 'Вк по 10', 'description': '', 'price': 14, 'update_stat_date': 0, 'refreshed_date': 1566068135, 'view_count': 10, 'is_sticky': 0, 'item_origin': 'brute', 'extended_guarantee': 0, 'nsb': -1, 'allow_ask_discount': 1, 'title_en': '', 'description_en': '', 'email_type': '', 'is_reserved': 0, 'item_domain': '', 'active_auction': 0, 'note_text': None, 'user_allow_ask_discount': 1, 'max_discount_percent': 30, 'market_custom_title': '', 'buyer_avatar_date': 1658531718, 'buyer_user_group_id': 2, 'buyer_secondary_group_ids': '93', 'is_fave': None, 'in_cart': None, 'cart_price': None, 'vk_item_id': 2410024, 'vk_id_count': 9, 'vk_friend_count': 347, 'vk_follower_count': 65, 'vk_admin_groups': [], 'vk_max_group_follower_count': 0, 'vk_vote_count': 0, 'vk_country': 'Russia', 'vk_sex': '1', 'vk_mobile': '1', 'vk_register_date': 1484575264, 'vk_age': 0, 'vk_city': '', 'vk_email': -1, 'vk_mobile_country': 7, 'vk_tfa': -1, 'vk_is_closed': '-1', 'vk_relation': 0, 'vk_count_conversations': 0, 'vk_is_verified': 0, 'canResellItem': False, 'canViewLoginData': False, 'canUpdateItemStats': False, 'showGetEmailCodeButton': False, 'buyer': {'user_id': 500113, 'operation_date': 1566070679, 'visitorIsBuyer': False, 'username': 'Джон1234', 'is_banned': 0, 'display_style_group_id': 2, 'uniq_username_css': '', 'secondary_group_ids': '93', 'user_group_id': 2}, 'isPersonalAccount': False, 'rub_price': 14, 'price_currency': 'rub', 'canValidateAccount': False, 'canResellItemAfterPurchase': True, 'vkMobileCountry': 'Russia', 'vk_sex_phrase': 'Female', 'vk_relation_phrase': 'Not specified', 'canViewAccountLink': False, 'itemOriginPhrase': 'Bruteforce', 'visitorIsAuthor': False, 'canAskDiscount': False, 'canCheckGuarantee': False, 'tags': [], 'customFields': [], 'externalAuth': [], 'isTrusted': False, 'isIgnored': False, 'deposit': 0, 'extraPrices': [{'currency': 'usd', 'price': 0.15}, {'currency': 'eur', 'price': 0.14}], 'canViewAccountLoginAndTempEmail': False, 'bumpSettings': {'canBumpItem': False, 'canBumpItemGlobally': False, 'shortErrorPhrase': None, 'errorPhrase': None}, 'auction': None, 'reserve': {'reserve_user_id': 0, 'reserve_date': 0}, 'description_html': '', 'description_html_en': '', 'seller': {'user_id': 2510063, 'username': 'HamHD', 'avatar_date': 1658573040, 'is_banned': 0, 'display_style_group_id': 2, 'joined_date': 1564564116, 'sold_items_count': 47, 'active_items_count': 0, 'restore_data': '', 'effective_last_activity': 1584966749, 'restore_percents': None, 'isOnline': False}}, 'canStickItem': False, 'canUnstickItem': False, 'canBuyItem': False, 'cannotBuyItemError': 'This item is sold', 'canCloseItem': False, 'canOpenItem': False, 'canReportItem': True, 'canEditItem': False, 'canDeleteItem': False, 'canCancelConfirmedBuy': False, 'canViewItemHistory': False, 'faveCount': False, 'isVisibleItem': True, 'canViewLoginData': False, 'sameItems': {'2385292': {'item_id': 2385292, 'item_state': 'paid', 'category_id': 2, 'published_date': 1565601107, 'title': 'Вк (жён.муж,брут) по 25 рублей + свежие не проверенные аккаунты, нечего не чекал! разбирайте!', 'description': '', 'price': 25, 'update_stat_date': 0, 'refreshed_date': 1565601107, 'view_count': 12, 'is_sticky': 0, 'item_origin': 'brute', 'extended_guarantee': 0, 'nsb': -1, 'allow_ask_discount': 1, 'title_en': '', 'description_en': '', 'email_type': '', 'is_reserved': 0, 'item_domain': '', 'active_auction': 0, 'vk_item_id': 2385292, 'vk_id_count': 9, 'vk_friend_count': 338, 'vk_follower_count': 64, 'vk_admin_groups': 'a:0:{}', 'vk_max_group_follower_count': 0, 'vk_vote_count': 0, 'vk_country': 'Россия', 'vk_sex': '1', 'vk_mobile': '1', 'vk_register_date': 1484575264, 'vk_age': 0, 'vk_city': '', 'vk_email': -1, 'vk_mobile_country': 7, 'vk_tfa': -1, 'vk_is_closed': '-1', 'vk_relation': 0, 'vk_count_conversations': 0, 'vk_is_verified': 0, 'buyer_avatar_date': 1683398067, 'buyer_user_group_id': 2, 'buyer_secondary_group_ids': '21,22,23,38,93', 'isCurrent': False, 'buyer': {'user_id': 2536632, 'operation_date': 1565609166, 'visitorIsBuyer': False, 'username': 'zorononame', 'is_banned': 0, 'display_style_group_id': 23, 'uniq_username_css': '', 'secondary_group_ids': '21,22,23,38,93', 'user_group_id': 2}, 'rub_price': 25, 'reserve': {'reserve_user_id': 0, 'reserve_date': 0}, 'description_html': '', 'description_html_en': '', 'seller': {'user_id': 2463802, 'username': 'Linus28', 'avatar_date': 1658570843, 'is_banned': 1, 'display_style_group_id': 2}}, '2410024': {'item_id': 2410024, 'item_state': 'paid', 'category_id': 2, 'published_date': 1566068135, 'title': 'Вк по 10', 'description': '', 'price': 14, 'update_stat_date': 0, 'refreshed_date': 1566068135, 'view_count': 10, 'is_sticky': 0, 'item_origin': 'brute', 'extended_guarantee': 0, 'nsb': -1, 'allow_ask_discount': 1, 'title_en': '', 'description_en': '', 'email_type': '', 'is_reserved': 0, 'item_domain': '', 'active_auction': 0, 'vk_item_id': 2410024, 'vk_id_count': 9, 'vk_friend_count': 347, 'vk_follower_count': 65, 'vk_admin_groups': 'a:0:{}', 'vk_max_group_follower_count': 0, 'vk_vote_count': 0, 'vk_country': 'Россия', 'vk_sex': '1', 'vk_mobile': '1', 'vk_register_date': 1484575264, 'vk_age': 0, 'vk_city': '', 'vk_email': -1, 'vk_mobile_country': 7, 'vk_tfa': -1, 'vk_is_closed': '-1', 'vk_relation': 0, 'vk_count_conversations': 0, 'vk_is_verified': 0, 'buyer_avatar_date': 1658531718, 'buyer_user_group_id': 2, 'buyer_secondary_group_ids': '93', 'isCurrent': True, 'buyer': {'user_id': 500113, 'operation_date': 1566070679, 'visitorIsBuyer': False, 'username': 'Джон1234', 'is_banned': 0, 'display_style_group_id': 2, 'uniq_username_css': '', 'secondary_group_ids': '93', 'user_group_id': 2}, 'rub_price': 14, 'reserve': {'reserve_user_id': 0, 'reserve_date': 0}, 'description_html': '', 'description_html_en': '', 'seller': {'user_id': 2510063, 'username': 'HamHD', 'avatar_date': 1658573040, 'is_banned': 0, 'display_style_group_id': 2}}, '4315777': {'item_id': 4315777, 'item_state': 'paid', 'category_id': 2, 'published_date': 1583507005, 'title': 'Вк актив', 'description': '', 'price': 8, 'update_stat_date': 0, 'refreshed_date': 1583507005, 'view_count': 3, 'is_sticky': 0, 'item_origin': 'resale', 'extended_guarantee': 0, 'nsb': -1, 'allow_ask_discount': 1, 'title_en': '', 'description_en': '', 'email_type': '', 'is_reserved': 0, 'item_domain': '', 'active_auction': 0, 'vk_item_id': 4315777, 'vk_id_count': 9, 'vk_friend_count': 409, 'vk_follower_count': 0, 'vk_admin_groups': 'a:0:{}', 'vk_max_group_follower_count': 0, 'vk_vote_count': 0, 'vk_country': 'Россия', 'vk_sex': '1', 'vk_mobile': '1', 'vk_register_date': 1484575264, 'vk_age': 13, 'vk_city': '', 'vk_email': -1, 'vk_mobile_country': 7, 'vk_tfa': -1, 'vk_is_closed': '-1', 'vk_relation': 0, 'vk_count_conversations': 0, 'vk_is_verified': 0, 'buyer_avatar_date': 1658237012, 'buyer_user_group_id': 2, 'buyer_secondary_group_ids': '38,54', 'isCurrent': False, 'buyer': {'user_id': 2323269, 'operation_date': 1583507203, 'visitorIsBuyer': False, 'username': 'Quntum23', 'is_banned': 0, 'display_style_group_id': 2, 'uniq_username_css': '', 'secondary_group_ids': '38,54', 'user_group_id': 2}, 'rub_price': 8, 'reserve': {'reserve_user_id': 0, 'reserve_date': 0}, 'description_html': '', 'description_html_en': '', 'seller': {'user_id': 3013283, 'username': 'Moonbringer', 'avatar_date': 1658575938, 'is_banned': 0, 'display_style_group_id': 21}}, '5177318': {'item_id': 5177318, 'item_state': 'paid', 'category_id': 2, 'published_date': 1589537028, 'title': 'Vk с фишинга 5р', 'description': '', 'price': 5, 'update_stat_date': 0, 'refreshed_date': 1589537028, 'view_count': 2, 'is_sticky': 0, 'item_origin': 'fishing', 'extended_guarantee': 0, 'nsb': -1, 'allow_ask_discount': 1, 'title_en': '', 'description_en': '', 'email_type': '', 'is_reserved': 0, 'item_domain': '', 'active_auction': 0, 'vk_item_id': 5177318, 'vk_id_count': 9, 'vk_friend_count': 408, 'vk_follower_count': 75, 'vk_admin_groups': 'a:1:{i:186017783;a:5:{s:4:"name";s:25:"Компания arifleim";s:11:"screen_name";s:13:"club186017783";s:11:"admin_level";i:3;s:13:"members_count";i:21;s:9:"photo_100";s:45:"https://vk.com/images/community_100.png?ava=1";}}', 'vk_max_group_follower_count': 0, 'vk_vote_count': 0, 'vk_country': 'Россия', 'vk_sex': '1', 'vk_mobile': '1', 'vk_register_date': 1484575264, 'vk_age': 13, 'vk_city': '', 'vk_email': 0, 'vk_mobile_country': 7, 'vk_tfa': 0, 'vk_is_closed': '-1', 'vk_relation': 0, 'vk_count_conversations': 0, 'vk_is_verified': 0, 'buyer_avatar_date': 0, 'buyer_user_group_id': 2, 'buyer_secondary_group_ids': '', 'isCurrent': False, 'buyer': None, 'rub_price': 5, 'reserve': {'reserve_user_id': 0, 'reserve_date': 0}, 'description_html': '', 'description_html_en': '', 'seller': {'user_id': 172866, 'username': 'ProVanbI4', 'avatar_date': 1658531161, 'is_banned': 1, 'display_style_group_id': 18}}}, 'sameItemsCount': 3, 'showToFavouritesButton': True, 'itemLink': 'https://lzt.market/2410024/?_apiLanguageId=1695652294+NibCWoB%2BsjcAvSCzer3PJA%3D%3D', 'canChangeOwner': False, 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695565894}}
```
### New

*Displays a list of the latest accounts.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **search_params** (dict): Search params for your request.
  > Example {"category_id":19} will return only VPN accounts

**Example:**

```python
data = api.market.list.new()
print(data)
```

```python
{"items": [item1, item2, item3, ...], "totalItems": 158625, "totalItemsPrice": null, "perPage": 40, "page": 1, "cacheTTL": 1695567089, "lastModified": 1695567059, "searchUrl": "/?locale=en", "stickyItems": [], "isIsolatedMarket": true, "isIsolatedMarketAlt": false, "system_info": {"visitor_id": 2410024, "time": 1695567059}}
```

### From url

*Displays a list of the latest accounts from your market url with search params.*

**Parameters:**

- **url** (str): Your market search url.
  > It can be https://lzt.market/search_params or https://api.lzt.market/search_params

**Example:**

```python
data = api.market.list.from_url(url="https://lzt.market/steam/cs-go-prime?origin[]=fishing&eg=1")
print(data)
```

```python
{'items': [item1, item2, item3, ...], 'totalItems': 29, 'totalItemsPrice': None, 'perPage': 40, 'page': 1, 'cacheTTL': 1695566864, 'lastModified': 1695566812, 'searchUrl': '/steam/cs-go-prime?origin%5B%5D=fishing&eg=1&locale=en', 'stickyItems': [], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695566811}}
```

### Owned

*Displays a list of owned accounts.*

*It's copy of*

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
{'items': [], 'totalItems': 0, 'totalItemsPrice': 0, 'perPage': 40, 'page': 1, 'userItemStates': {'stickied': {'item_state': 'stickied', 'item_count': 0, 'title': 'Highlighted'}, 'discount_request': {'item_state': 'active', 'item_count': 0, 'title': 'Discount requests'}, 'active': {'item_state': 'active', 'item_count': 0, 'title': 'Active'}, 'paid': {'item_state': 'paid', 'item_count': 0, 'title': 'Sold'}, 'closed': {'item_state': 'closed', 'item_count': 0, 'title': 'Closed'}, 'deleted': {'item_count': 1, 'item_state': 'deleted', 'title': 'Deleted'}, 'awaiting': {'item_state': 'awaiting', 'item_count': 0, 'title': 'Required action'}}, 'cacheTTL': 1695564784, 'lastModified': 1695564784, 'searchUrl': '/user/2410024/items?user_id=2410024&locale=en', 'stickyItems': [], 'user': {'user_id': 2410024, 'username': 'AS7RID', 'display_style_group_id': 22, 'avatar_date': 1693752388, 'is_banned': 0, 'uniq_username_css': ''}, 'periodLabel': '', 'periodLabelPhrase': '', 'filterDatesDefault': True, 'startDate': '2017-09-05T00:00:00+00:00', 'endDate': '2023-09-24T23:59:59+00:00', 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695564784}}
```
### Viewed

*Displays a list of viewed accounts.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **search_params** (dict): Search params for your request. 
  > Example {"category_id":19} will return only VPN accounts

**Example:**

```python
data = api.market.list.viewed()
print(data)
```

```python
{'items': [item1,item2,item3], 'totalItems': 149, 'totalItemsPrice': None, 'perPage': 40, 'page': 1, 'cacheTTL': 1695564896, 'lastModified': 1695564896, 'searchUrl': '/viewed?locale=en', 'stickyItems': [], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695564896}}
```

### Favorite

*Displays a list of favorite accounts.*

**Parameters:**

- **page** (int): The number of the page to display results from
- **search_params** (dict): Search params for your request.
  > Example {"category_id":19} will return only VPN accounts

**Example:**
```python
data = api.market.list.favorite()
print(data)
```

```python
{'items': [], 'totalItems': 0, 'totalItemsPrice': None, 'perPage': 40, 'page': 1, 'searchUrl': '/fave?locale=en', 'stickyItems': [], 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695564985}}

```

### Purchased

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
{'items': [item1, item2, item3, ...], 'totalItems': 75, 'totalItemsPrice': None, 'perPage': 40, 'page': 1, 'cacheTTL': 1695565203, 'lastModified': 1695565203, 'searchUrl': '/user/2410024/orders?locale=en', 'stickyItems': [], 'periodLabel': '', 'periodLabelPhrase': '', 'filterDatesDefault': True, 'startDate': '2017-09-05T00:00:00+00:00', 'endDate': '2023-09-24T23:59:59+00:00', 'user': {'user_id': 2410024, 'username': 'AS7RID', 'is_banned': 0, 'display_style_group_id': 22, 'uniq_username_css': '', 'avatar_date': 1693752388, 'balance': 500, 'hold': 0}, 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695565203}}
```

# Purchasing

*Methods for item purchasing*

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
{'status': 'ok', 'item': {'account': 'string'}, 'system_info': {'visitor_id': 2410024, 'time': 1695565203}}
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
{'status': 'ok', 'item': {'account': 'string'}, 'system_info': {'visitor_id': 2410024, 'time': 1695565203}}
```

### Confirm

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
{'status': 'ok', 'item': {'account': 'string'}, 'system_info': {'visitor_id': 2410024, 'time': 1695565203}
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
{'status': 'ok', 'item': {'title': 'Acc vk', 'price': 10, 'item_origin': 'autoreg', 'proxy_id': 0, 'extended_guarantee': 0, 'email_type': '', 'allow_ask_discount': 1, 'category_id': 2, 'description': '', 'description_en': '', 'title_en': 'Acc vk', 'item_domain': '', 'published_date': 1695571938, 'item_state': 'awaiting', 'update_stat_date': 0, 'refreshed_date': 1695571938, 'view_count': 0, 'is_sticky': 0, 'nsb': -1, 'is_reserved': 0, 'active_auction': 0, 'item_id': 74736369, 'reserve': {'reserve_user_id': 0, 'reserve_date': 0}, 'description_html': '', 'description_html_en': '', 'seller': {'user_id': 2410024}}, 'isIsolatedMarket': True, 'isIsolatedMarketAlt': False, 'system_info': {'visitor_id': 2410024, 'time': 1695571938}}
```

### Check

*Adds account on the market.*

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

### bump

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

### Email

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

### Guard

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

### Mafile

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

### Temp mail password

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

### Telegram confirmation code

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

### Telegram reset authorizations

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

*Displays info about your profile.*

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

# Batch

*Execute multiple API requests at once.(10 max)*

**Parameters:**

- **request_body** (list[dict]):

**Example:**

```python
jobs = [
    api.create_batch_job(job_name="Example1", method="POST", url="https://api.lzt.market/proxy",params={"proxy_row": "192.168.1.1:5000:login:password"}),
    api.create_batch_job(job_name="Example2", method="GET", url="https://api.lzt.market/proxy")
]
data = api.market.batch(request_body=jobs)
print(data)
```

```python
{'jobs': {'Example1': {'_job_result': 'message', '_job_message': 'Changes Saved'}, 'Example2': {'_job_result': 'ok', 'proxies': {'188900': {'proxy_id': 188900, 'user_id': 2410024, 'proxy_ip': '192.168.1.1', 'proxy_port': 5000, 'proxy_user': 'login', 'proxy_pass': 'password', 'proxyString': '192.168.1.1:5000@login:password'}}}}, 'system_info': {'visitor_id': 2410024, 'time': 1695587080}}
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

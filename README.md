<div align="center">
  <a href="https://zelenka.guru/threads/5523020/">
    <img src="https://i.imgur.com/Vm2tOZh.png" alt="LOLZTEAM API Library" width="80%"/>
  </a>
  <br>
  <a href="https://pypi.org/project/LOLZTEAM">
    <img src="https://img.shields.io/github/last-commit/AS7RIDENIED/LOLZTEAM?style=for-the-badge&color=2bad72" alt="GitHub last commit"> <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/AS7RIDENIED/LOLZTEAM?style=for-the-badge&color=2bad72">
    <br>
    <img src="https://img.shields.io/pypi/dm/LOLZTEAM?style=for-the-badge&color=2bad72" alt="PyPI Downloads"> <img src="https://img.shields.io/pypi/v/LOLZTEAM?style=for-the-badge&color=2bad72" alt="Package version">
  </a>
</div>

## 🚀 Installation

Install the package using pip:

```shell
pip install LOLZTEAM
```

Also you can download the package from [here](https://github.com/AS7RIDENIED/LOLZTEAM/releases/latest) and install it manually.

`pip install LOLZTEAM-<version>.tar.gz` or `pip install LOLZTEAM-<version>.whl`

## 💻 Usage

Import the required modules and initialize the API clients:

```python
from LOLZTEAM.Client import Forum, Market, Antipublic
from LOLZTEAM.Client.Base import Constants
import asyncio

token = "your_token"

forum = Forum(token=token)
market = Market(token=token)
antipublic = Antipublic(token="Antipublic_key")

# API Client Parameters

# - **token** (str): Your token.
# - **language** (str["ru", "en"]): Language of the API responses.
# - **delay_min** (float): Minimal delay between requests.
# - **proxy** (str): Proxy string.
#   > protocol://ip:port or protocol://login:password@ip:port (socks5://login:password@192.168.1.1:8080 or http://login:password@192.168.1.1:8080)
# - **timeout** (float): Request timeout.


# All following examples also work for Market & Antipublic clients

forum.settings.logger.enable()                                        # 📝 Start logging
# Forum & Market client will log into {user_id}.{Client_name}.log file
# Antipublic client will log into Antipublic.log file
forum.settings.delay.enable()                                         # 🕒 Enable auto delay (Auto delay is enabled by default for Market & Forum but not for Antipublic)

response = forum.users.get(user_id=2410024)                           # ⚡ Sync request
job = forum.users.get.job(user_id=2410024)                            # 📋 Job creation (Always SYNC)
response = forum.request("GET", "/users/2410024")                     # ⚡ Custom request (You can use full url or just path)
job = forum.request.job("GET", "/users/2410024")                      # 📋 Job creation for custom request

async def async_example():
    response = await forum.users.get(user_id=2410024)                 # ⚡ Async request
    job = forum.users.get.job(user_id=2410024)                        # 📋 Job creation (Always SYNC)
    response = await forum.request("GET", "/users/2410024")           # ⚡ Custom async request
    job = forum.request.job("GET", "/users/2410024")                  # 📋 Job creation for custom request

asyncio.run(async_example())

# You should just add ".job" between function name and parentheses to create a job.
# You can't create a job for methods that are uploading files (like avatar/background) and ofc not for client.batch(...) method.
# P.s Your IDE probably may not show that ".job" function exists but it does, trust me.

forum.settings.token = "token"                                        # 🔑 Change token
forum.settings.language = "en"                                        # 🌍 Change language (Antipublic client doesn't support language changing)
forum.settings.proxy = "http://login:password@192.168.1.1:8080"       # 🌐 Change proxy
forum.settings.delay.min = 3                                          # 🕒 Set minimal delay (E.g. your minimal delay is 3 seconds, but if a method you want to use has a 
                                                                      #     delay of 0.5 seconds, your script will sleep for 3 seconds instead of 0.5 seconds)
forum.settings.delay.disable()                                        # 🕒 Disable auto delay
forum.settings.logger.disable()                                       # 📝 Stop logging

# You can view all changeable settings in LOLZTEAM/Client/Base/Core.py file
```

## 📚 Documentation

### Package Documentation:

[![Forum API Client](https://img.shields.io/badge/Forum_API_Client-2bad72?style=for-the-badge)](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/Documentation/Forum.md)
[![Market API Client](https://img.shields.io/badge/Market_API_Client-2bad72?style=for-the-badge)](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/Documentation/Market.md)
[![Antipublic API Client](https://img.shields.io/badge/Antipublic_API_Client-2bad72?style=for-the-badge)](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/Documentation/Antipublic.md)

### Official API Documentation:

[![Forum API](https://img.shields.io/badge/Forum_API-2bad72?style=for-the-badge)](https://docs.api.zelenka.guru/?forum)
[![Market API](https://img.shields.io/badge/Market_API-2bad72?style=for-the-badge)](https://docs.api.zelenka.guru/?market)
[![Antipublic API](https://img.shields.io/badge/Antipublic_API-2bad72?style=for-the-badge)](https://antipublic.one/docs/)
<font size=6 style="margin: auto"> <center>

[Forum docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Forum.md) - [Market Docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Market.md)

</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

* [Info](#info)
  * [Lines Count](#lines-count)
  * [Lines Count Plain](#lines-count-plain)
  * [Version](#version)
* [Account](#account)
  * [License](#license)
  * [Queries](#queries)
* [Check](#check)
* [Search](#search)
* [Email Passwords](#email-passwords)


</details>

# Quickstart

You need to create class instance to use library

```python
from LOLZTEAM import AutoUpdate
from LOLZTEAM import Constants
from LOLZTEAM.API import Antipublic
from LOLZTEAM.Tweaks import SendAsAsync, CreateJob

token = "your_token"

antipublic = Antipublic(token=token)
```

**Parameters:**

- **token** (str): Your token.
  > You can get it [there](https://zelenka.guru/account/antipublic) or in antipublic app
- **proxy_type** (str): Your proxy type.
- **proxy** (str): Proxy string.
  > ip:port or login:password@ip:port
- **reset_custom_variables** (bool): Reset custom variables.
- **timeout** (int): Request timeout.

# Info

## Lines Count

GET https://antipublic.one/api/v2/countLines

Get count of rows in the AntiPublic db

:return: httpx Response object


## Lines Count Plain

GET https://antipublic.one/api/v2/countLinesPlain

Get count of rows in the AntiPublic db (raw format)

:return: str


## Version

GET https://antipublic.one/api/v2/version

Get current antipublic version, change log and download url

:return: json {'filename': str, 'version': str, 'changeLog': str, 'url': str}


# Account

## License

GET https://antipublic.one/api/v2/checkAccess

Checks your license

Token required

:return: httpx Response object


## Queries

GET https://antipublic.one/api/v2/availableQueries

Get your available queries

Token required

:return: httpx Response object


# Check

POST https://antipublic.one/api/v2/checkLines

Check your lines.

Token required
:param lines: Lines for check, email:password or login:password
:param insert: Upload private rows to AntiPublic db

:return: httpx Response object


# Search

POST https://antipublic.one/api/v2/search

Search lines by email/password/domain.

:param search_by: Search type. Can be email/password/domain
    (For password and domain search you need Antipublic Plus subscription)
:param query: Search query.
:param direction: Search direction. Can be start/strict/end

:return: httpx Response object


# Email Passwords

POST https://antipublic.one/api/v2/emailPasswords

Get passwords for login's/email's

Token required

:param emails: List of emails or logins for search.
:param limit: Result limit (per email).

:return: httpx Response object



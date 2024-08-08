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

*Get count of rows in the AntiPublic db*

**Example:**

```python
response = antipublic.info.lines_count()
print(response.json())
```


## Lines Count Plain

GET https://antipublic.one/api/v2/countLinesPlain

*Get count of rows in the AntiPublic db (raw format)*

**Example:**

```python
response = antipublic.info.lines_count_plain()
print(response.text)
```


## Version

GET https://antipublic.one/api/v2/version

*Get current antipublic version, change log and download url*

**Example:**

```python
response = antipublic.info.version()
print(response.json())
```


# Account

## License

GET https://antipublic.one/api/v2/checkAccess

*Checks your license*

Token required

**Example:**

```python
response = antipublic.account.license()
print(response.json())
```


## Queries

GET https://antipublic.one/api/v2/availableQueries

*Get your available queries*

**Example:**

```python
response = antipublic.account.queries()
print(response.json())
```


# Check

POST https://antipublic.one/api/v2/checkLines

*Check your lines.*

**Parameters:**

- **lines** (list): Lines for check, email:password or login:password
- **insert** (bool): Upload private rows to AntiPublic db

**Example:**

```python
response = antipublic.check(lines=["email:password", "login:password"])
print(response.json())
```


# Search

POST https://antipublic.one/api/v2/search

*Search lines by email/password/domain.*

**Parameters:**

- **search_by** (INSERT_HERE): Search type.
    > For password and domain search you need Antipublic Plus subscription
- **query** (INSERT_HERE): Search query.
- **direction** (INSERT_HERE): Search direction.

**Example:**

```python
response = antipublic.search(search_by="email", query="email7357@example.com")
print(response.json())
```


# Email Passwords

POST https://antipublic.one/api/v2/emailPasswords

*Get passwords for login's/email's*

**Parameters:**

- **emails** (list): List of emails or logins for search.
- **limit** (int): Result limit (per email).

**Example:**

```python
response = antipublic.email_passwords(emails=["email7357@example.com", "email7358@example.com"], limit=1)
print(response.json())
```



<font size=6 style="margin: auto"> <center>

[Forum docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/Documentation/Forum.md) - [Market Docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/Documentation/Market.md)

</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

* [Info](#info)
  * [Lines count](#lines-count)
  * [Lines count plain](#lines-count-plain)
  * [Version](#version)
* [Account info](#account-info)
  * [Access](#access)
  * [Queries](#queries)
* [Check](#check)
* [Search](#search)

</details>

# Quickstart

You need to create class instance to use library

```python
from LOLZTEAM import AutoUpdate
from LOLZTEAM import Constants
from LOLZTEAM.API import Antipublic
from LOLZTEAM.Tweaks import SendAsAsync

token = "your_token"

antipublic = Antipublic(token=token)
```

**Parameters:**

- **token** (str): Your token.

  > You can get in there -&gt; https://zelenka.guru/account/antipublic or in antipublic app

- **proxy_type** (str): Your proxy type.

  > You can use Types to set your proxy type
  >
  > ```python
  > from LOLZTEAM import Constants
  > 
  > Constants.Proxy.socks5  # "socks5"
  > Constants.Proxy.socks4  # "socks4"
  > Constants.Proxy.https   # "https"
  > Constants.Proxy.http    # "http"
  > 
  > antipublic = AntipublicApi(token="Your_token", proxy_type=Constants.Proxy.socks5)
  > ```

- proxy (str): Proxy string.

  > ip:port or login:password@ip:port

# Info

*A category that contains methods that return information about Antipublic*

*For this category token is **unrequired***

### Lines count

*Get count of rows in the AntiPublic db*

*[Official documentation reference](https://antipublic.readme.io/reference/antipubliccountlines)*

**Example:**

```python
response = antipublic.info.lines_count()
print(response.json())
```

```python
{'count': 10438655969}
```

### Lines count plain

*Get count of rows in the AntiPublic db (raw format)*

*[Official documentation reference](https://antipublic.readme.io/reference/antipubliccountlinesplain)*

**Example:**

```python
response = antipublic.info.lines_count_plain()
print(response.json())
```

```python
10438655969
```

### Version

*Get current antipublic version, change log and download url*

*[Official documentation reference](https://antipublic.readme.io/reference/antipublicversion)*

**Example:**

```python
response = antipublic.info.version()
print(response.json())
```
```python
{'filename': 'AntiPublic.exe', 'version': '1.0.18', 'changeLog': 'New feature for window title, provide custom password count input for per email/login', 'url': 'https://antipublic.one/dl/AntiPublic.zip'}
```

# Account info

*A category that contains methods that return information about account*

### Access

*Checks your license*

*[Official documentation reference](https://antipublic.readme.io/reference/antipublicchecklicense)*

```python
response = antipublic.account_info.access()
print(response.json())
```

```python
{'success': True, 'plus': False, 'trial': False, 'plus_expires': '0', 'trial_expires': '0'}
```

### Queries

*Get your available queries*

*[Official documentation reference](https://antipublic.readme.io/reference/antipublicavailablequeries)*

```python
response = antipublic.account_info.queries()
print(response.json())
```

```python
{'success': True, 'emailSearch': 1000, 'passwordSearch': 0}
```

# Data processing

*Methods for data processing*

### Check lines

*Check your lines for private*

*[Official documentation reference](https://antipublic.readme.io/reference/antipublicchecklines)*

**Parameters:**

- **lines** (list\[str\]): Lines for check
  > email:password or login:password
- **insert** (bool): Upload private rows to AntiPublic db

```python
lines = ["admin@zelenka.guru:Lanskoy228",
         "truea911fan@a911.com:Animeshka228"]
response = antipublic.check(lines=lines,insert=False)
print(response.json())

#  Or 

with open("Base.txt","r") as f:
    lines = f.readlines()
response = antipublic.check(lines=lines,insert=False)
print(response.json())
```

```python
{'success': True, 'result': [{'is_private': True, 'line': 'admin@zelenka.guru:Lanskoy228'}, {'is_private': True, 'line': 'truea911fan@a911.com:Animeshka228'}]}
```

### Search

*Get passwords for login's/email's*

*[Official documentation reference 1](https://antipublic.readme.io/reference/antipublicemailsearch)*
*[Official documentation reference 2](https://antipublic.one/api/v2/emailPasswords)*

**Parameters:**

- **login** (str): Email or login for search.
- **logins** (list[str]): Emails or logins for search.
  >  You need Antupublic Plus subscription to use this param
- **limit** (int): Result limit (per email).

```python
response = antipublic.search(login="example")
print(response.json())

# or

response = antipublic.search(logins=["example@gmail.com", "example1@gmail.com"], limit=1)
print(response.json())
```

```python
{"success":True,"availableQueries":0,"resultCount":1,"results":["example@gmail.com:password"]}
```
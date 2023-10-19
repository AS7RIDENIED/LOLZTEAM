<font size=6 style="margin: auto"> <center>

[Forum docs](https://github.com/AS7RIDENIED/Lolzteam_Python_Api/blob/main/Documentation/Forum.md) - [Market Docs](https://github.com/AS7RIDENIED/Lolzteam_Python_Api/blob/main/Documentation/Market.md)

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
* [Data processing](#data-processing)
  * [Check lines](#check-lines)
  * [Get passwords](#get-passwords)
  * [Get passwords plus](#get-passwords-plus)

</details>

# Quickstart

You need to create class instance to use library

```python
from LolzteamApi import AntipublicApi
antipublic = AntipublicApi(token="Your_token")
```

**Parameters:**

- **token** (str): Your token.

  > You can get in there -&gt; https://zelenka.guru/account/antipublic or in antipublic app

- **proxy_type** (str): Your proxy type.

  > You can use Types to set your proxy type
  >
  > ```python
  > from LolzteamApi import AntipublicApi, Types
  > 
  > Types.Proxy.socks5  # "socks5"
  > Types.Proxy.socks4  # "socks4"
  > Types.Proxy.https   # "https"
  > Types.Proxy.http    # "http"
  > 
  > antipublic = AntipublicApi(token="Your_token", proxy_type=Types.Proxy.socks5)
  > ```

- proxy (str): Proxy string.

  > ip:port or login:password@ip:port

# Info

*A category that contains methods that return information about Antipublic*

*For this category token is **unrequired***

### Lines count

*Get count of rows in the AntiPublic db*

**Example:**

```python
data = antipublic.info.lines_count()
print(data)
```

```python
{'count': 10438655969}
```

### Lines count plain

*Get count of rows in the AntiPublic db (raw format)*

**Example:**

```python
data = antipublic.info.lines_count_plain()
print(data)
```

```python
10438655969
```

### Version

*Get current antipublic version, change log and download url*

**Example:**

```python
data = antipublic.info.version()
print(data)
```
```python
{'filename': 'AntiPublic.exe', 'version': '1.0.18', 'changeLog': 'New feature for window title, provide custom password count input for per email/login', 'url': 'https://antipublic.one/dl/AntiPublic.zip'}
```

# Account info

*A category that contains methods that return information about account*

### Access

*Checks your license*

```python
data = antipublic.account_info.access()
print(data)
```

```python
{'success': True, 'plus': False, 'trial': False, 'plus_expires': '0', 'trial_expires': '0'}
```

### Queries

*Get your available queries*

```python
data = antipublic.account_info.queries()
print(data)
```

```python
{'success': True, 'emailSearch': 1000, 'passwordSearch': 0}
```

# Data processing

*Methods for data processing*

### Check lines

*Check your lines for private*

**Parameters:**

- **lines** (list\[str\]): Lines for check
  > email:password or login:password
- **insert** (bool): Upload private rows to AntiPublic db

```python
lines = ["admin@zelenka.guru:Lanskoy228",
         "truea911fan@a911.com:Animeshka228"]
data = antipublic.check_lines(lines=lines,insert=False)
print(data)

#  Or 

with open("Base.txt","r") as f:
    lines = f.readlines()
data = antipublic.check_lines(lines=lines,insert=False)
print(data)
```

```python
{'success': True, 'result': [{'is_private': True, 'line': 'admin@zelenka.guru:Lanskoy228'}, {'is_private': True, 'line': 'truea911fan@a911.com:Animeshka228'}]}
```

### Get passwords

*Get passwords for login/email*

**Parameters:**

- **login** (str): Email or login for search.

```python
data = antipublic.get_passwords(login="pisyapopa11")
print(data)
```

```python
{"success":True,"availableQueries":0,"resultCount":1,"results":["example@gmail.com:password"]}
```

### Get passwords plus

*Get passwords for logins/emails. AntiPublic Plus subscription required.*

**Parameters:**

- **logins** (list\[str\]): Email or login for search.
- **limit** (int): Result limit (per email)

```python
logins = ["pisyapopa11","pisyapopa95"]
data = antipublic.get_passwords_plus(logins=logins,limit=1)
print(data)
```

```python
{'success': True, 'availableQueries': 0, 'resultCount': 2, 'results': ['pisyapopa11@ya.ru:1234567890pflybwf', 'pisyapopa95@mail.ru:qwe12345']}
```

# Send async

*Send request as async*

**Parameters:**

- **func** (function): Target function.
- ****kwargs** (any): Target function parameters.

**Example:**

```python
response = await antipublic.send_as_async(antipublic.get_passwords, login="grishalanskoy228")
print(response)
```

```python
{"success":True,"availableQueries":0,"resultCount":1,"results":["example@gmail.com:password"]}
```
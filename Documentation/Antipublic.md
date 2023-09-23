# Quickstart

You need to create class instance to use library

```
from LolzteamApi import AntipublicApi
antipublic = AntipublicApi(token="Your_token")
```

**Parameters:**

- **token** (str): Your token.

  > You can get in there -&gt; https://zelenka.guru/account/antipublic or in antipublic app

- **proxy_type** (str): Your proxy type.

  > You can use Types to set your proxy type
  >
  > ```
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

```
data = antipublic.info.lines_count()
print(data)
```

```
{'count': 10438655969}
```

### Lines count plain

*Get count of rows in the AntiPublic db (raw format)*

```
data = antipublic.info.lines_count_plain()
print(data)
```

```
10438655969
```

### Version

*Get current antipublic version, change log and download url*

```
data = antipublic.info.version()
print(data)
```

# Account info

*A category that contains methods that return information about account*

### Access

*Checks your license*

```
data = antipublic.account_info.access()
print(data)
```

```
{'filename': 'AntiPublic.exe', 'version': '1.0.18', 'changeLog': 'New feature for window title, provide custom password count input for per email/login', 'url': 'https://antipublic.one/dl/AntiPublic.zip'}
```

### Queries

*Get your available queries*

```
data = antipublic.account_info.queries()
print(data)
```

```
{'success': True, 'emailSearch': 1000, 'passwordSearch': 0}
```

# Data processing

*Methods for data processing*

### Check lines

*Check your lines for private*

**Parameters:**

- **lines** (list\[str\]): Lines for check, email:password or login:password
- **insert** (bool): Upload private rows to AntiPublic db

```
lines = ["admin@zelenka.guru:Lanskoy228",
         "truea911fan@a911.com:Animeshka228"]
data = antipublic.check_lines(lines=lines,insert=False)
print(data)

///////////////////////////////////////////////////////

with open("Base.txt","r") as f:
    lines = f.readlines()
data = antipublic.check_lines(lines=lines,insert=False)
print(data)
```

```
{'success': True, 'result': [{'is_private': True, 'line': 'admin@zelenka.guru:Lanskoy228'}, {'is_private': True, 'line': 'truea911fan@a911.com:Animeshka228'}]}
```

### Get passwords

*Get passwords for login/email*

**Parameters:**

- **login** (str): Email or login for search.

```
data = antipublic.get_passwords(login="pisyapopa11")
print(data)
```

```
{'success': True, 'availableQueries': 999, 'resultCount': 2, 'results': ['pisyapopa11@ya.ru:1234567890pflybwf', 'pisyapopa11@yandex.ru:1234567890pflybwf']}
```

### Get passwords plus

*Get passwords for logins/emails. AntiPublic Plus subscription required.*

**Parameters:**

- **logins** (list\[str\]): Email or login for search.
- **limit** (int): Result limit (per email)

```
logins = ["pisyapopa11","pisyapopa95"]
data = antipublic.get_passwords_plus(logins=logins,limit=1)
print(data)
```

```
{'success': True, 'availableQueries': 0, 'resultCount': 1, 'results': ['pisyapopa11@ya.ru:1234567890pflybwf', 'pisyapopa95@mail.ru:qwe12345']}
```
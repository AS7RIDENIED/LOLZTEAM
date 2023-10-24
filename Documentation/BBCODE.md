<details>

<summary><font size="4">Method tree</font></summary>

* [Quickstart](#quickstart)
* [Bold](#bold)
* [Italic](#italic)
* [Underline](#underline)
* [Strike through](#strike-through)
* [Color](#color)
  * [Custom](#custom)
  * [Black](#black)
  * [White](#white)
  * [Red](#red)
  * [Green](#green)
  * [Blue](#blue)
  * [Yellow](#yellow)
  * [Purple](#purple)
  * [Cyan](#cyan)
  * [Magenta](#magenta)
* [Size](#size)
* [URL](#url)
* [Email](#email)
* [User](#user)
* [Image](#image)
* [Media](#media)
* [List](#list)
* [Alignment](#alignment)
  * [Center](#center)
  * [Left](#left)
  * [Right](#right)
* [Quote](#quote)
* [Spoiler](#spoiler)
* [Code](#code)
* [Plain](#plain)
* [Api](#api)
* [Hide](#hide)
  * [Club](#club)
  * [Days](#days)
  * [Sympathies](#sympathies)
  * [To users](#to-users)
  * [From users](#from-users)
* [Source code](#source-code)
* [Visitor](#visitor)

</details>

# Quickstart

You need to import BBCODE to use it

```python
from LolzteamApi import BBCODE
```

# Bold

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.bold(text="Sample text")
print(text)
```

```python
[b]Sample text[/b]
```

# Italic

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.italic(text="Sample text")
print(text)
```

```python
[i]Sample text[/i]
```

# Underline

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.underline(text="Sample text")
print(text)
```

```python
[u]Sample text[/u]
```

# Strike through

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.strike_through(text="Sample text")
print(text)
```

```python
[s]Sample text[/s]
```

# Color

## Custom

**Parameters:**

- **text** (str): Your text.
- **hex_color** (str): Your hex color.

**Example:**

```python
text = BBCODE.Color.custom(text="Sample text",hex_color="#f13838")
print(text)
```

```python
[color=#f13838]Sample text[/color]
```

## Black

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.black(text="Sample text")
print(text)
```

```python
[color=black]Sample text[/color]
```

## White

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.white(text="Sample text")
print(text)
```

```python
[color=white]Sample text[/color]
```

## Red

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.red(text="Sample text")
print(text)
```

```python
[color=red]Sample text[/color]
```

## Green

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.green(text="Sample text")
print(text)
```

```python
[color=green]Sample text[/color]
```

## Blue

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.blue(text="Sample text")
print(text)
```

```python
[color=blue]Sample text[/color]
```

## Yellow

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.yellow(text="Sample text")
print(text)
```

```python
[color=yellow]Sample text[/color]
```

## Purple

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.purple(text="Sample text")
print(text)
```

```python
[color=purple]Sample text[/color]
```

## Cyan

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.cyan(text="Sample text")
print(text)
```

```python
[color=cyan]Sample text[/color]
```

## Magenta

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Color.magenta(text="Sample text")
print(text)
```

```python
[color=magenta]Sample text[/color]
```

# Size

**Parameters:**

- **text** (str): Your text.
- **size** (int): Your size.

**Example:**

```python
text = BBCODE.text_size(text="Sample text", size=5)
print(text)
```

```python
[size=5]Sample text[/size]
```

# URL

**Parameters:**

- **text** (str): Your text.
- **url** (str): Your url.

**Example:**

```python
text = BBCODE.url(text="Sample text", url="https://zelenka.guru")
print(text)
```

```python
[url=https://zelenka.guru]Sample text[/url]
```

# Email

**Parameters:**

- **text** (str): Your text.
- **url** (str): Your url.

**Example:**

```python
text = BBCODE.email(text="Sample text", email="admin@zelenka.guru")
print(text)
```

```python
[email=admin@zelenka.guru]Sample text[/email]
```

# User

**Parameters:**

- **user_id** (str): User id.

**Example:**

```python
text = BBCODE.user(user_id=2410024)
print(text)
```

```python
[user=2410024]2410024[/user]
```

# Image

**Parameters:**

- **image_url** (str): Image url.

**Example:**

```python
text = BBCODE.image(image_url="https://zelenka.guru/styles/brivium/rezinc/xenforo/avatars/avatar_s.png")
print(text)
```

```python
[img]https://zelenka.guru/styles/brivium/rezinc/xenforo/avatars/avatar_s.png[/img]
```

# Media

**Parameters:**

- **media_url** (str): Media url.

**Example:**

```python
text = BBCODE.media(media_url="https://nztcdn.com/files/c23a20eb-81da-4dd5-ab44-caa11dfde900.mp4", site="cdn")
print(text)
```

```python
[media=cdn]https://nztcdn.com/files/c23a20eb-81da-4dd5-ab44-caa11dfde900.mp4[/media]
```

# List

**Parameters:**

- **text** (str): Your text.
- **ordered** (bool): Make ordered list or not.

**Example:**

```python
text = BBCODE.list(text="Sample\nText", ordered=True)
print(text)
```

```python
[LIST=1]
[*]Sample
[*]Text
[/LIST]
```

# Alignment

## Center

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Alignment.center(text="Sample Text")
print(text)
```

```python
[center]Sample Text[/center]
```

## Left

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Alignment.left(text="Sample Text")
print(text)
```

```python
[left]Sample Text[/left]
```

## Right

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Alignment.right(text="Sample Text")
print(text)
```

```python
[right]Sample Text[/right]
```

# Quote

**Parameters:**

- **text** (str): Your text.
- **author** (str): Author nickname.

**Example:**

```python
text = BBCODE.quote(text="Nice library, awesome methods", author="AS7RID")
print(text)
```

```python
[quote=AS7RID]Nice library, awesome methods[/quote]
```

# Spoiler

**Parameters:**

- **text** (str): Your text.
- **spoiler_title** (str): Spoiler title.

**Example:**

```python
text = BBCODE.spoiler(text="Sample Text", spoiler_title="Sample spoiler name")
print(text)
```

```python
[spoiler=Sample spoiler name]Sample Text[/spoiler]
```

# Code

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.code(text="print('Hello World')")
print(text)
```

```python
[code]print('Hello World')[/code]
```

# Plain

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.plain(text=f"""{BBCODE.bold(text=f"Sample {BBCODE.underline(text='not')} bold text")}""")
print(text)
```

```python
[plain][b]Sample [u]not[/u] bold text[/b][/plain]
```

# Api

**Parameters:**

- **url** (str): Your url.
- **option** (str): Api option.

**Example:**

```python
text = BBCODE.api(url="https://antipublic.one/api/v2/countLines", option="count")
print(text)
```

```python
[api=count]https://antipublic.one/api/v2/countLines[/api]
```

# Hide

## Club

**Parameters:**

- **text** (str): Your text.

**Example:**

```python
text = BBCODE.Hide.club(text="Sample text")
print(text)
```

```python
[club]Sample text[/club]
```

## Days

**Parameters:**

- **text** (str): Your text.
- **days** (int): Days count to view hide.

**Example:**

```python
text = BBCODE.Hide.days(text="Sample text", days=30)
print(text)
```

```python
[days=30]Sample text[/days]
```

## Sympathies

**Parameters:**

- **text** (str): Your text.
- **sympathies** (int): Sympathies count to view hide.

**Example:**

```python
text = BBCODE.Hide.sympathies(text="Sample text", sympathies=200)
print(text)
```

```python
[likes=200]Sample text[/likes]
```

## To users

**Parameters:**

- **text** (str): Your text.
- **user_ids** (list[int]): List with user ids.

**Example:**

```python
text = BBCODE.Hide.to_users(text="Sample text", user_ids=[1, 3, 2410024])
print(text)
```

```python
[userids=1,3,2410024]Sample text[/userids]
```

## From users

**Parameters:**

- **text** (str): Your text.
- **user_ids** (list[int]): List with user ids.

**Example:**

```python
text = BBCODE.Hide.from_users(text="Sample text", user_ids=[1, 3, 2410024])
print(text)
```

```python
[exceptids=1,3,2410024]Sample text[/exceptids]
```

# Source code

**Parameters:**

- **text** (str): Your text.
- **code_language** (str): Code language.
- **inline** (bool): Inline code.

**Example:**

```python
text = BBCODE.source_code(text='print("Hello World")', code_language="python")
print(text)
```

```python
[src="python"]print("Hello World")[/src]
```

# Visitor

**Example:**

```python
text = BBCODE.visitor()
print(text)
```

```python
[visitor][/visitor]
```
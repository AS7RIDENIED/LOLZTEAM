<a href="https://zelenka.guru/threads/5523020/">
<img src="https://i.imgur.com/Vm2tOZh.png"/>
</a>

## Installation

*You can install the library using pip:*

```commandline
pip install LOLZTEAM
```

## Usage

*Import the `LOLZTEAM` modules and create an instance of the `Forum`, `Market` or `Antipublic` class to start using the API:*

```python
from LOLZTEAM import AutoUpdate, Constants, Utils
from LOLZTEAM.API import Forum, Market, Antipublic
from LOLZTEAM.Tweaks import DelaySync, SendAsAsync, CreateJob

token = "your_token"

market = Market(token=token, language="en")
forum = Forum(token=token, language="en")
antipublic = Antipublic(token="Antipublic_key")

DelaySync(apis=[market,forum])
```

## Documentation

### [Forum](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Forum.md) - [Market](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Market.md) - [Antipublic](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Antipublic.md)
### [Utility](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Utils.md) - [DelaySync](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/DelaySync.md) - [BBCODE](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/BBCODE.md)

## Official Lolzteam documentation

### [Forum](https://docs.api.zelenka.guru/?forum) [Market](https://docs.api.zelenka.guru/?market) [Antipublic](https://antipublic.one/docs/?antipublic)

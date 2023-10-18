<details><summary><font size="4">Method tree</font></summary>

* [Quick start](#quickstart)
* [Delay Synchronizer](#delay-synchronizer)
  * [Add](#add-api-to-delaysynchronizer)
  * [Remove](#remove-api-from-delaysynchronizer)
  * [Remove all](#remove-all-apis-from-delaysynchronizer)

</details>

# Quickstart

**Parameters:**

- **apis** (list[LolzteamApi]): List with your api instances

```
from LolzteamApi import LolzteamApi, DelaySynchronizer  #      <-----
api_1 = LolzteamApi(token="token_1", language="en")
api_2 = LolzteamApi(token="token_2", language="ru")
apis = [api_1, api_2]

DelaySynchronizer(apis=apis)  #                                 <-----

for api in apis:
    print(api.forum.users.get(user_id=2410024))
```

```python
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}, 'system_info': {'visitor_id': 0, 'time': 0}}
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Delay synchronizer

*Synchronizes delay between different accounts to prevent ban or 429 http error*

**Parameters:**

- **apis** (list[LolzteamApi]): List with your api instances

**Example:**

```python
from LolzteamApi import DelaySynchronizer
synchronizer = DelaySynchronizer()
```

### Add api to DelaySynchronizer

*Adding api to the delay syncing list*

**Parameters:**

- **api** (LolzteamApi/list/dict): LolzteamApi instance/list/dict

**Example:**

```python
api_1 = LolzteamApi(token="token_1")
api_2 = LolzteamApi(token="token_2")

synchronizer.add(api_1)
synchronizer.add(api_2)
# or
synchronizer.add([api_1,api_2])
# or
synchonizer.add({"AS7RID_api":api_1, "a911_api":api_2})
```

# Remove api from DelaySynchronizer

*Removing api from the delay syncing list*

**Parameters:**

- **api** (LolzteamApi/list/dict): LolzteamApi instance/list/dict

**Example:**

```python
api_1 = LolzteamApi(token="token_1")
api_2 = LolzteamApi(token="token_2")

synchronizer.remove(api_1)
synchronizer.remove(api_2)
# or
synchronizer.remove([api_1,api_2])
# or
synchonizer.remove({"AS7RID_api":api_1, "a911_api":api_2})
```

### Remove all api's from DelaySynchronizer

*Removing all api's from the delay syncing list*

**Example:**

```python
api_1 = LolzteamApi(token="token_1")
api_2 = LolzteamApi(token="token_2")

synchronizer.clear()
```
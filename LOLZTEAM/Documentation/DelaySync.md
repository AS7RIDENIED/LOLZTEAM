<details><summary><font size="4">Method tree</font></summary>

* [Quick start](#quickstart)
* [Delay Synchronizer](#delay-synchronizer)
  * [Add](#add-api-to-DelaySync)
  * [Remove](#remove-api-from-DelaySync)
  * [Remove all](#remove-all-apis-from-DelaySync)

</details>

# Quickstart

**Parameters:**

- **apis** (list[Forum or Market]): List with your api instances

```
from LOLZTEAM import AutoUpdate
from LOLZTEAM import Constants
from LOLZTEAM.API import Forum, Market, Antipublic
from LOLZTEAM.Tweaks import DelaySync  #                <-----
forum_1 = Forum(token="token_1", language="en")
forum_2 = Forum(token="token_2", language="ru")
apis = [forum_1, forum_2]

DelaySync(apis=apis)  #                                 <-----

for forum in apis:
    print(forum.users.get(user_id=2410024))
```

```python
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}, 'system_info': {'visitor_id': 0, 'time': 0}}
{'user': {'user_id': 0, 'username': 'string', 'user_message_count': 0, 'user_register_date': 0, 'user_like_count': 0, 'short_link': 'string', 'user_title': 'string', 'user_is_valid': True, 'user_is_verified': True, 'user_is_followed': True, 'user_last_seen_date': 0, 'links': {'permalink': 'string', 'detail': 'string', 'avatar': 'string', 'avatar_big': 'string', 'avatar_small': 'string', 'followers': 'string', 'followings': 'string', 'ignore': 'string', 'timeline': 'string'}, 'permissions': {'edit': True, 'follow': True, 'ignore': True, 'profile_post': True}, 'user_is_ignored': True, 'user_is_visitor': True, 'user_group_id': 0, 'custom_fields': {'discord': 'string', 'jabber': 'string', 'lztAwardUserTrophy': 'string', 'lztCuratorNodeTitle': 'string', 'lztCuratorNodeTitleEn': 'string', 'lztInnovation20Link': 'string', 'lztInnovation30Link': 'string', 'lztInnovationLink': 'string', 'lztSympathyIncreasing': 'string', 'lztSympathyZeroing': 'string', 'qiwi': 'string', 'scamURL': 'string', 'steam': 'string', 'telegram': 'string', 'vk': 'string'}}, 'system_info': {'visitor_id': 0, 'time': 0}}
```

# Delay synchronizer

*Synchronizes delay between different accounts to prevent ban or 429 http error*

**Parameters:**

- **apis** (list[Forum or Market]): List with your api instances

**Example:**

```python
from LOLZTEAM.Tweaks import DelaySync
synchronizer = DelaySync()
```

### Add api to DelaySync

*Adding api to the delay syncing list*

**Parameters:**

- **api** (Forum/Market/list/dict): Forum/Market/list/dict

**Example:**

```python
forum_1 = Forum(token="token_1")
forum_2 = Forum(token="token_2")

synchronizer.add(forum_1)
synchronizer.add(forum_2)
# or
synchronizer.add([forum_1,forum_2])
# or
synchonizer.add({"AS7RID_api":forum_1, "a911_api":forum_2})
```

# Remove api from DelaySync

*Removing api from the delay syncing list*

**Parameters:**

- **api** (Forum/Market/list/dict): Forum/Market/list/dict

**Example:**

```python
synchronizer.remove(forum_1)
synchronizer.remove(forum_2)
# or
synchronizer.remove([forum_1, forum_2])
# or
synchonizer.remove({"AS7RID_api":forum_1, "a911_api":forum_2})
```

### Remove all api's from DelaySync

*Removing all api's from the delay syncing list*

**Example:**

```python
synchronizer.clear()
```
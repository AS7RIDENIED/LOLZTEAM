from LolzteamApi import LolzteamApi

token = input('Enter your token:\n')                       # You need token with scopes read,post to run that example
api = LolzteamApi(token=token)

#  Creating thread
thread_data = api.forum.threads.create(forum_id=876, thread_title="Api library example", post_body="sample text",
                                       thread_tags="Tag1,Tag2,Tag3")
print(thread_data["thread"]["links"]["permalink"])
thread_id = thread_data["thread"]["thread_id"]             # Save the ID to create a post here later

#  Getting user data
user_data = api.forum.users.get(user_id=2410024)
print(user_data["user"]["username"])                       # Printing username of user 2410024

#  Creating post in thread we created before
post_data = api.forum.posts.create(thread_id=thread_id, post_body="sample text but post")
print(post_data["post"]["post_id"])                        # Printing post_id of created post

#  Batch example
#  job 1 - We get our profile data
#  job 2 - We get list of ignored users by ourselves
#  job 3 - We get list of our profile followers.
data = [
    {
        "id": "1",
        "uri": "https://api.zelenka.guru/users/me",
        "method": "GET",
        "params": {
        }
    },
    {
        "id": "2",
        "uri": "https://api.zelenka.guru/users/ignored?total=1",
        "method": "GET",
        "params": {
        }
    },
    {
        "id": "3",
        "uri": "https://api.zelenka.guru/users/me/followers",
        "method": "POST",
        "params": {
        }
    },
]
jobs_data = api.forum.batch(request_body=data)
print(jobs_data['jobs']['1']['user']['user_like_count'])   # Number of user sympathies
print(jobs_data['jobs']['2']['users_total'])               # The number of users you ignore
print(jobs_data['jobs']['3'])                              # Try to follow ourselves. ( We will get an error because we can't follow yourself )

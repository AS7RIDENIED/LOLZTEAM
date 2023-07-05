import Lolz_lib, time

token = input('Enter your token:\n')
api = Lolz_lib.lolzteam_api(token=token)
post_data = api.create_post(thread_id=5501317, post_body='Этот пост я отправил с помощью либы на 2к мусорных строк')
print(post_data["post"]["post_id"])

time.sleep(4.5) # Кд между запросами 3 секунды, а кд между возможностью писать сообщения в районе 4-5 секунд. Я недоволен

post_comment_data = api.create_post_comment(post_id=post_data["post"]["post_id"],
                                            comment_body='Этот коммент к посту я отправил с помощью либы на 2к мусорных строк \n[CLUB]Ну а это хайд[/CLUB]')
print(post_comment_data)
data = [
    {
        "id": "1",
        "uri": "https://api.zelenka.guru/users/2410024",
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
        "uri": "https://api.zelenka.guru/users/2410024/followers",
        "method": "POST",
        "params": {
        }
    },
]
jobs_data = api.batch(request_body=data)
print(jobs_data['jobs']['1']['user']['username'])
print(jobs_data['jobs']['2']['users_total'])
print(jobs_data['jobs']['3'])

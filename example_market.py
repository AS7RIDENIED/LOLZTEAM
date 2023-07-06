from LolzteamApi import LolzteamApi
token = input('Enter your token:\n')                       # You need token with scope market to run that example
api = LolzteamApi(token=token)


profile_data = api.market.profile.get()                    # Getting our market profile data
print(profile_data["user"]["active_items_count"])          # Printing count of your active items on market

viewed_accs_data = api.market.profile.viewed()             # Getting our last viewed items
print(viewed_accs_data["totalItems"])                      # Printing total count of items you have viewed

new_items_data = api.market.list.new()                     # Getting the newest account on market
print(new_items_data["items"][0]["title"])                 # Printing title of the newest acc

#  Batch example
#  job 1 - We get our profile data
#  job 2 - We get list of accounts we marked as favorite
#  job 3 - We get our proxies
data = [
    {
        "id": "1",
        "uri": "https://api.lzt.market/me",
        "method": "GET",
        "params": {
        }
    },
    {
        "id": "2",
        "uri": "https://api.lzt.market/fave",
        "method": "GET",
        "params": {
        }
    },
    {
        "id": "3",
        "uri": "https://api.lzt.market/proxy",
        "method": "GET",
        "params": {
        }
    }
]
jobs_data = api.market.batch(request_body=data)
print(jobs_data['jobs']['1']["user"]["sold_items_count"])  # Number of sold accounts
print(jobs_data['jobs']['2']["totalItems"])                # The number of accounts you marked as favorite
print(jobs_data['jobs']['3']["proxies"])                   # Array of proxies you  currently have

from LolzteamApi import LolzteamApi

api = LolzteamApi(token='your_token')

# Money contest by time
api.forum.threads.contests.money.create_by_time(thread_title='Test contest', post_body='Test contest',
                                                prize_data_money=0,
                                                count_winners=1, length_value=1, length_option='hour',
                                                require_like_count=1, require_total_like_count=1,
                                                secret_answer="Your_secret_answer")
# Money contest by count
api.forum.threads.contests.money.create_by_count(thread_title='Test contest', post_body='Test contest',
                                                 prize_data_money=0,
                                                 count_winners=1, needed_members=500,
                                                 require_like_count=1, require_total_like_count=1,
                                                 secret_answer="Your_secret_answer")
# Upgrade contest by time
api.forum.threads.contests.upgrade.create_by_time(thread_title='Test contest', post_body='Test contest',
                                                  prize_data_upgrade=14,
                                                  count_winners=1, length_value=1, length_option='hour',
                                                  require_like_count=1, require_total_like_count=1,
                                                  secret_answer="Your_secret_answer")
# Upgrade contest by count
api.forum.threads.contests.upgrade.create_by_count(thread_title='Test contest', post_body='Test contest',
                                                   prize_data_upgrade=14,
                                                   count_winners=1, needed_members=500,
                                                   require_like_count=1, require_total_like_count=1,
                                                   secret_answer="Your_secret_answer")

class Proxy:
    socks5 = "SOCKS5"
    socks4 = "SOCKS4"
    http = "HTTP"
    https = "HTTPS"


class Market:
    class Operation_types:
        income = "income"
        cost = "cost"
        refilled_balance = "refilled_balance"
        withdrawal_balance = "withdrawal_balance"
        paid_item = "paid_item"
        sold_item = "sold_item"
        money_transfer = "money_transfer"
        receiving_money = "receiving_money"
        internal_purchase = "internal_purchase"
        claim_hold = "claim_hold"

    class Hold_Options:
        hour = "hour"
        day = "day"
        week = "week"
        month = "month"
        year = "year"

    class Currency:
        cny = "cny"
        usd = "usd"
        rub = "rub"
        eur = "eur"
        uah = "uah"
        kzt = "kzt"
        byn = "byn"
        gbp = "gbp"

    class Item_origin:
        brute = "brute"
        stealer = "stealer"
        fishing = "fishing"
        autoreg = "autoreg"
        personal = "personal"
        resale = "resale"
        retrieve = "retrieve"

    class Guarantee:
        half_day = -1
        day = 0
        three_days = 1

    class Item_status:
        active = "active"
        paid = "paid"
        deleted = "deleted"
        awaiting = "awaiting"

    class Order:
        price_to_up = "price_to_up"
        price_to_down = "price_to_down"
        date_to_down = "pdate_to_down"
        date_to_up = "pdate_to_up"
        date_to_down_upload = "pdate_to_down_upload"
        date_to_up_upload = "pdate_to_up_upload"

    class App_Ids:
        CSGO = 730
        PUBG = 578080
        Steam = 753
        Dota = 570
        TF2 = 440
        Rust = 252490
        Unturned = 304930
        KF2 = 232090
        DST = 322330  # Don't Starve Together


class Forum:
    class Contests:
        class Length:
            minutes = "minutes"
            hours = "hours"
            days = "days"

        class Upgrade_prizes:
            supreme = 1
            legend = 6
            antipublic = 12
            uniq = 14
            photo_leaks = 17
            auto_participation = 19

    class Order:
        default = 'natural'
        oldest = "thread_create_date"
        newest = "thread_create_date_reverse"
        newest_bumped = "thread_update_date"
        oldest_bumped = "thread_update_date_reverse"
        min_views = "thread_view_count"
        max_views = "thread_view_count_reverse"
        min_posts = "thread_post_count"
        max_posts = "thread_post_count"

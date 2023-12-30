class Proxy:
    socks5 = "SOCKS5"
    socks4 = "SOCKS4"
    http = "HTTP"
    https = "HTTPS"


class Market:
    class Categories:
        steam = "steam"
        fortnite = "fortnite"
        vk = "vkontakte"
        genshin = "genshin-impact"
        valorant = "valorant"
        lol = "league-of-legends"
        telegram = "telegram"
        diamondrp = "diamondrp"
        supercell = "supercell"
        origin = "origin"
        wot = "world-of-tanks"  # World of Tanks
        wot_blitz = "wot-blitz"
        epicgames = "epicgames"
        eft = "escape-from-tarkov"
        twitter = "twitter"  # Not released yet
        socialclub = "socialclub"
        uplay = "uplay"
        war_thunder = "war-thunder"
        discord = "discord"
        tiktok = "tiktok"
        instagram = "instagram"
        battlenet = "battlenet"
        vpn = "vpn"
        streaming_media = "cinema"
        spotify = "spotify"
        warface = "warface"
        youtube = "youtube"
        minecraft = "minecraft"

    class Categories_ID:
        steam = 1
        fortnite = 9
        vk = 2
        genshin = 17
        valorant = 13
        lol = 29
        telegram = 24
        diamondrp = 6
        supercell = 15
        origin = 3
        wot = 14
        wot_blitz = 16
        epicgames = 12
        eft = 18
        twitter = 21
        socialclub = 7
        uplay = 5
        war_thunder = 27
        discord = 22
        tiktok = 20
        instagram = 10
        battlenet = 11
        vpn = 19
        streaming_media = 23
        spotify = 26
        warface = 4
        youtube = 25
        minecraft = 28

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
        bid = "bid"

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
        dummy = "dummy"  # Only for steam (Пустышки)

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
        auction_expiration = "exp_auctions"

    class App_Ids:
        CS2 = 730
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
        default = "natural"
        oldest = "thread_create_date"
        newest = "thread_create_date_reverse"
        newest_bumped = "thread_update_date"
        oldest_bumped = "thread_update_date_reverse"
        min_views = "thread_view_count"
        max_views = "thread_view_count_reverse"
        min_posts = "thread_post_count"
        max_posts = "thread_post_count_reverse"
        min_likes = "first_post_likes"
        max_likes = "first_post_likes_reverse"

    class PostOrder:
        default = "natural"
        default_reverse = "natural_reverse"
        max_likes = "post_likes"
        min_likes = "post_likes_reverse"

    class ReplyGroups:
        staff = 0  # КФ + кураторы
        everyone = 2  # Все
        local = 21  # Местный и выше
        resident = 22  # Постоялец и выше
        expert = 23  # Эксперт и выше
        guru = 60  # Гуру и выше
        ai = 61  # ИИ и выше

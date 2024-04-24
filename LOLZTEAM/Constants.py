class Proxy:
    socks5 = "SOCKS5"
    socks4 = "SOCKS4"
    http = "HTTP"
    https = "HTTPS"


class Market:
    class Category:
        steam = "steam"
        fortnite = "fortnite"
        mihoyo = "mihoyo"
        valorant = "valorant"
        lol = "league-of-legends"
        telegram = "telegram"
        supercell = "supercell"
        origin = "origin"
        wot = "world-of-tanks"
        wot_blitz = "wot-blitz"
        epicgames = "epicgames"
        eft = "escape-from-tarkov"
        socialclub = "socialclub"
        uplay = "uplay"
        war_thunder = "war-thunder"
        discord = "discord"
        tiktok = "tiktok"
        instagram = "instagram"
        battlenet = "battlenet"
        vpn = "vpn"
        cinema = "cinema"
        spotify = "spotify"
        warface = "warface"

    class CategoryId:
        steam = 1
        fortnite = 9
        mihoyo = 17
        valorant = 13
        lol = 29
        telegram = 24
        supercell = 15
        origin = 3
        wot = 14
        wot_blitz = 16
        epicgames = 12
        eft = 18
        socialclub = 7
        uplay = 5
        war_thunder = 27
        discord = 22
        tiktok = 20
        instagram = 10
        battlenet = 11
        vpn = 19
        cinema = 23
        spotify = 26
        warface = 4
        gift = 30

    class OperationTypes:
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

    class HoldPeriod:
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

    class ItemOrigin:
        brute = "brute"
        stealer = "stealer"
        fishing = "fishing"
        autoreg = "autoreg"
        personal = "personal"
        resale = "resale"
        dummy = "dummy"  # Only for steam (Пустышки)

    class Guarantee:
        half_day = -1
        day = 0
        three_days = 1

    class ItemStatus:
        active = "active"
        paid = "paid"
        deleted = "deleted"
        awaiting = "awaiting"

    class ItemOrder:
        cheap = "price_to_up"
        expensive = "price_to_down"
        newest = "pdate_to_down"
        oldest = "pdate_to_up"
        newest_upload = "pdate_to_down_upload"
        oldest_upload = "pdate_to_up_upload"
        auction_expiration = "exp_auctions"

    class AppID:
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

        class UpgradePrize:
            supreme = 1
            legend = 6
            antipublic = 12
            uniq = 14
            photo_leaks = 17
            auto_participation = 19

    class ThreadOrder:
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
        ai = 351  # ИИ и выше

    class Arbitrage:
        class TransferType:
            safe = "safe"
            not_safe = "notsafe"

        class PayClaim:
            now = "now"
            later = "later"

        class Currency:
            cny = "cny"
            usd = "usd"
            rub = "rub"
            eur = "eur"
            uah = "uah"
            kzt = "kzt"
            byn = "byn"
            gbp = "gbp"

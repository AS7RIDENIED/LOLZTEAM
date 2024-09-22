from typing import Literal


class Proxy:
    socks5 = "SOCKS5"
    socks4 = "SOCKS4"
    http = "HTTP"
    https = "HTTPS"


class Market:
    class Category:
        _Literal = Literal["steam", "fortnite", "mihoyo", "riot", "telegram", "supercell", "origin", "world-of-tanks", "wot-blitz", "epicgames", "gifts", "escape-from-tarkov", "socialclub", "uplay", "war-thunder", "discord", "tiktok", "instagram", "battlenet", "vpn", "cinema", "roblox", "spotify", "warface", "minecraft"]
        steam = "steam"
        fortnite = "fortnite"
        mihoyo = "mihoyo"
        riot = "riot"
        telegram = "telegram"
        supercell = "supercell"
        origin = "origin"
        wot = "world-of-tanks"
        wot_blitz = "wot-blitz"
        epicgames = "epicgames"
        gifts = "gifts"
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
        roblox = "roblox"
        spotify = "spotify"
        warface = "warface"
        minecraft = "minecraft"

    class CategoryId:
        _Literal = Literal[1, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 26, 27, 28, 30, 31]
        steam = 1
        fortnite = 9
        mihoyo = 17
        riot = 13
        telegram = 24
        supercell = 15
        origin = 3
        wot = 14
        wot_blitz = 16
        epicgames = 12
        gifts = 30
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
        roblox = 31
        spotify = 26
        warface = 4
        minecraft = 28

    class OperationTypes:
        _Literal = Literal["income", "cost", "refilled_balance", "withdrawal_balance", "paid_item", "sold_item", "money_transfer", "receiving_money", "internal_purchase", "claim_hold", "bid"]
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
        _Literal = Literal["hour", "day", "week", "month", "year"]
        hour = "hour"
        day = "day"
        week = "week"
        month = "month"
        year = "year"

    class Currency:
        _Literal = Literal["cny", "usd", "rub", "eur", "uah", "kzt", "byn", "gbp"]
        cny = "cny"
        usd = "usd"
        rub = "rub"
        eur = "eur"
        uah = "uah"
        kzt = "kzt"
        byn = "byn"
        gbp = "gbp"

    class ItemOrigin:
        _Literal = Literal["brute", "stealer", "fishing", "autoreg", "personal", "resale", "dummy"]
        brute = "brute"
        stealer = "stealer"
        fishing = "fishing"
        autoreg = "autoreg"
        personal = "personal"
        resale = "resale"
        dummy = "dummy"      # Only for steam (Пустышки)

    class Guarantee:
        _Literal = Literal[-1, 0, 1]
        half_day = -1
        day = 0
        three_days = 1

    class ItemStatus:
        _Literal = Literal["active", "paid", "deleted", "awaiting", "closed", "discount_request", "stickied", "pre_active"]
        active = "active"
        paid = "paid"
        deleted = "deleted"
        awaiting = "awaiting"
        closed = "closed"
        discount_request = "discount_request"
        stickied = "stickied"
        pre_active = "pre_active"

    class ItemOrder:
        _Literal = Literal["price_to_up", "price_to_down", "pdate_to_down", "pdate_to_up", "pdate_to_down_upload", "pdate_to_up_upload", "exp_auctions", "ddate_to_down", "ddate_to_up"]
        cheap = "price_to_up"
        expensive = "price_to_down"
        newest = "pdate_to_down"
        oldest = "pdate_to_up"
        newest_upload = "pdate_to_down_upload"
        oldest_upload = "pdate_to_up_upload"
        auction_expiration = "exp_auctions"
        newest_deleted = "ddate_to_down",
        oldest_deleted = "ddate_to_up"

    class AppID:
        _Literal = Literal[730, 578080, 753, 570, 440, 252490, 304930, 232090, 322330]
        CS2 = 730
        PUBG = 578080
        Steam = 753
        Dota = 570
        TF2 = 440
        Rust = 252490
        Unturned = 304930
        KF2 = 232090
        DST = 322330


class Forum:
    class Contests:
        class Length:
            _Literal = Literal["minutes", "hours", "days"]
            minutes = "minutes"
            hours = "hours"
            days = "days"

        class UpgradePrize:
            _Literal = Literal[1, 6, 12, 14, 17, 19]
            supreme = 1
            legend = 6
            antipublic = 12
            uniq = 14
            photo_leaks = 17
            auto_participation = 19

    class ThreadOrder:
        _Literal = Literal["natural", "natural_reverse", "thread_create_date", "thread_create_date_reverse", "thread_update_date", "thread_update_date_reverse", "thread_view_count", "thread_view_count_reverse", "thread_post_count", "thread_post_count_reverse", "first_post_likes", "first_post_likes_reverse"]
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
        _Literal = Literal["natural", "natural_reverse", "post_likes", "post_likes_reverse"]
        default = "natural"
        default_reverse = "natural_reverse"
        max_likes = "post_likes"
        min_likes = "post_likes_reverse"

    class ReplyGroups:
        _Literal = Literal[0, 2, 21, 22, 23, 60, 351]
        staff = 0      # КФ + кураторы
        everyone = 2   # Все
        local = 21     # Местный и выше
        resident = 22  # Постоялец и выше
        expert = 23    # Эксперт и выше
        guru = 60      # Гуру и выше
        ai = 351       # ИИ и выше

    class Arbitrage:
        class TransferType:
            _Literal = Literal["safe", "notsafe"]
            safe = "safe"
            not_safe = "notsafe"

        class Currency:
            cny = "cny"
            usd = "usd"
            rub = "rub"
            eur = "eur"
            uah = "uah"
            kzt = "kzt"
            byn = "byn"
            gbp = "gbp"


class Antipublic:
    class SearchBy:
        _Literal = Literal["email", "password", "domain"]
        email = "email"
        password = "password"
        domain = "domain"

    class SearchDirection:
        _Literal = Literal["start", "strict", "end"]
        start = "start"
        strict = "strict"
        end = "end"

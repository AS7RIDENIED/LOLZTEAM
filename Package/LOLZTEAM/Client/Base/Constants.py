from typing import Literal


class Market:
    class Category:
        _Literal = Literal["steam", "fortnite", "mihoyo", "riot", "telegram", "supercell", "origin", "world-of-tanks", "wot-blitz", "epicgames", "gifts", "escape-from-tarkov", "socialclub", "uplay", "war-thunder", "discord", "tiktok", "instagram", "battlenet", "vpn", "roblox", "warface", "minecraft"]
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
        chatgpt = "chatgpt"
        vpn = "vpn"
        roblox = "roblox"
        warface = "warface"
        minecraft = "minecraft"

    class CategoryID:
        _Literal = Literal["1", "3", "4", "5", "6", "7", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "22", "24", "27", "28", "30", "31"]
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
        chatgpt = 6
        vpn = 19
        roblox = 31
        warface = 4
        minecraft = 28

    class OperationTypes:
        _Literal = Literal["income", "cost", "paid_item", "sold_item", "withdrawal_balance", "refilled_balance", "internal_purchase", "money_transfer", "claim_hold", "insurance_deposit", "paid_mail", "contest"]
        income = "income"
        cost = "cost"
        paid_item = "paid_item"
        sold_item = "sold_item"
        withdrawal_balance = "withdrawal_balance"
        refilled_balance = "refilled_balance"
        internal_purchase = "internal_purchase"
        money_transfer = "money_transfer"
        claim_hold = "claim_hold"
        insurance_deposit = "insurance_deposit"
        paid_mail = "paid_mail"
        contest = "contest"

    class HoldPeriod:
        _Literal = Literal["hour", "day", "week", "month"]
        hour = "hour"
        day = "day"
        week = "week"
        month = "month"
        # year = "year"  # Max period is month mhm

    class Currency:
        _Literal = Literal["rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try", "jpy", "brl"]
        ruble = "rub"
        hryvnia = "uah"
        tenge = "kzt"
        ruble_byn = "byn"
        dollar = "usd"
        euro = "eur"
        pound = "gbp"
        yuan = "cny"
        lira = "try"
        yen = "jpy"
        real = "brl"

    class ItemOrigin:
        _Literal = Literal["brute", "stealer", "phishing", "autoreg", "personal", "resale", "dummy", "self_registration"]
        brute = "brute"
        stealer = "stealer"
        phishing = "phishing"
        autoreg = "autoreg"
        personal = "personal"
        resale = "resale"
        dummy = "dummy"
        self_reg = "self_registration"

    class Guarantee:
        _Literal = Literal["-1", "0", "1"]
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
        _Literal = Literal["price_to_up", "price_to_down", "pdate_to_down", "pdate_to_up", "pdate_to_down_upload", "pdate_to_up_upload", "ddate_to_down", "ddate_to_up", "edate_to_down", "edate_to_up"]
        cheap = "price_to_up"
        expensive = "price_to_down"
        newest = "pdate_to_down"
        oldest = "pdate_to_up"
        newest_upload = "pdate_to_down_upload"
        oldest_upload = "pdate_to_up_upload"
        newest_deleted = "ddate_to_down",
        oldest_deleted = "ddate_to_up"
        newest_edited = "edate_to_down",
        oldest_edited = "edate_to_up"

    class Extra:
        _Literal = Literal["proxy", "close_item", "region", "service", "system", "confirmationCode", "cookies", "login_without_cookies", "cookie_login", "mfa_file", "dota2_mmr", "ea_games", "uplay_games", "the_quarry", "warframe", "ark", "ark_ascended", "genshin_currency", "honkai_currency", "zenless_currency", "telegramClient", "telegramJson", "checkChannels", "checkSpam", "checkHypixelBan"]
        proxy = "proxy"
        close_item = "close_item"
        region = "region"
        service = "service"
        system = "system"
        confirmationCode = "confirmationCode"
        cookies = "cookies"
        login_without_cookies = "login_without_cookies"
        cookie_login = "cookie_login"
        mfa_file = "mfa_file"
        dota2_mmr = "dota2_mmr"
        ea_games = "ea_games"
        uplay_games = "uplay_games"
        the_quarry = "the_quarry"
        warframe = "warframe"
        ark = "ark"
        ark_ascended = "ark_ascended"
        genshin_currency = "genshin_currency"
        honkai_currency = "honkai_currency"
        zenless_currency = "zenless_currency"
        telegramClient = "telegramClient"
        telegramJson = "telegramJson"
        checkChannels = "checkChannels"
        checkSpam = "checkSpam"
        checkHypixelBan = "checkHypixelBan"

    class AppID:
        _Literal = Literal["730", "578080", "753", "570", "440", "252490", "304930", "232090", "322330"]
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
            _Literal = Literal["1", "6", "12", "14", "17", "19"]
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
        oldest_bumped = "thread_update_date_reverse"
        newest = "thread_create_date_reverse"
        newest_bumped = "thread_update_date"
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
        _Literal = Literal["0", "2", "21", "22", "23", "60", "351"]
        staff = 0      # КФ + кураторы
        everyone = 2   # Все
        local = 21     # Местный и выше
        resident = 22  # Постоялец и выше
        expert = 23    # Эксперт и выше
        guru = 60      # Гуру и выше
        ai = 351       # ИИ и выше

    class Arbitrage:
        class TransferType:
            _Literal = Literal["safe", "notsafe", "guarantor"]
            safe = "safe"
            not_safe = "notsafe"
            guarantor = "guarantor"

    class User:
        class Fields:
            class Trophies:
                _Literal = Literal["moder_1_year", "moder_2_year", "moder_3_year", "moder_4_year", "moder_5_year", "curator_1_year", "curator_2_years", "curator_3_years", "curator_4_year", "editor_1_year", "editor_2_years", "editor_3_years", "designer_1_year", "designer_2_year", "telegram_1_year", "telegram_2_years", "telegram_3_years", "respectable_user", "trophy_sheriff", "truth_seller", "helper", "designer", "developer", "bug_hunter", "leader_of_community", "tournament_organizer", "innovator", "innovator2", "innovator3", "donater", "sponsor", "tournament_sponsor", "telegram_sponsor", "sponsor_10_year", "new_year_sponsor", "charity", "mamont", "mamont2022", "mamont2023", "mamonth_24", "valorant_member", "valorant_finalist", "valorant_winner", "csgo_winner_2021", "csgo_member_2021", "csgo_finalist_2022", "cs2_member", "cs2_finalist",
                                   "cs2_winner", "dota2_winner_2022", "dota2_finalist_2022", "dota2_member_2022", "members_brawl_stars", "winner_brawl_stars", "apex_member_2023", "apex_finalist_2023", "apex_winner_2023", "rust_member", "rust_winner", "fallguys_winner", "fallguys_member", "roblox_member", "roblox_finalist", "roblox_winner", "rainbow_six_siege_winner", "rainbow_six_siege_member", "warface_member", "warface_finalist", "warface_winner", "monopoly_member", "monopoly_finalist", "monopoly_winner", "clash_royale_member", "clash_royale_finalist", "clash_royale_winner", "pubg_member", "pubg_finalist", "pubg_winner", "minecraft_member", "minecraft_finalist", "minecraft_winner", "winner_logos_show", "member_finalist_show", "member_logos_show", "lzt_speedrunner", "poker_participant", "poker_winner", "pixel_battle_member", "ivent_lolzteam", "notpixel"]
                # Staff
                moderator_1_year = "moder_1_year"
                moderator_2_year = "moder_2_year"
                moderator_3_year = "moder_3_year"
                moderator_4_year = "moder_4_year"
                moderator_5_year = "moder_5_year"

                curator_1_year = "curator_1_year"
                curator_2_years = "curator_2_years"
                curator_3_years = "curator_3_years"
                curator_4_year = "curator_4_year"

                editor_1_year = "editor_1_year"
                editor_2_years = "editor_2_years"
                editor_3_years = "editor_3_years"

                designer_1_year = "designer_1_year"
                designer_2_year = "designer_2_year"

                telegram_1_year = "telegram_1_year"
                telegram_2_years = "telegram_2_years"
                telegram_3_years = "telegram_3_years"

                # Status trophies
                respectable_user = "respectable_user"
                trophy_sheriff = "trophy_sheriff"
                truth_seller = "truth_seller"
                helper = "helper"
                designer = "designer"
                developer = "developer"
                bug_hunter = "bug_hunter"
                leader_of_community = "leader_of_community"
                tournament_organizer = "tournament_organizer"

                # Innovation trophies
                innovator = "innovator"
                innovator2 = "innovator2"
                innovator3 = "innovator3"

                # Donation trophies
                donater = "donater"
                sponsor = "sponsor"
                tournament_sponsor = "tournament_sponsor"
                telegram_sponsor = "telegram_sponsor"
                sponsor_10_year = "sponsor_10_year"
                new_year_sponsor = "new_year_sponsor"
                charity = "charity"

                # Mammoth
                mammoth = "mamont"
                mammoth2022 = "mamont2022"
                mammoth2023 = "mamont2023"
                mammoth2024 = "mamonth_24"

                # <- Game tournament trophies ->
                # Valorant
                valorant_member = "valorant_member"
                valorant_finalist = "valorant_finalist"
                valorant_winner = "valorant_winner"
                # CS
                csgo_winner_2021 = "csgo_winner_2021"
                csgo_member_2021 = "csgo_member_2021"
                csgo_finalist_2022 = "csgo_finalist_2022"
                cs2_member = "cs2_member"
                cs2_finalist = "cs2_finalist"
                cs2_winner = "cs2_winner"
                # Dota 2
                dota2_winner_2022 = "dota2_winner_2022"
                dota2_finalist_2022 = "dota2_finalist_2022"
                dota2_member_2022 = "dota2_member_2022"
                # Brawl Stars
                members_brawl_stars = "members_brawl_stars"
                winner_brawl_stars = "winner_brawl_stars"
                # Apex Legends
                apex_member_2023 = "apex_member_2023"
                apex_finalist_2023 = "apex_finalist_2023"
                apex_winner_2023 = "apex_winner_2023"
                # Rust
                rust_member = "rust_member"
                rust_winner = "rust_winner"
                # Fall Guys
                fallguys_winner = "fallguys_winner"
                fallguys_member = "fallguys_member"
                # Roblox
                roblox_member = "roblox_member"
                roblox_finalist = "roblox_finalist"
                roblox_winner = "roblox_winner"
                # Rainbow Six Siege
                rainbow_six_siege_winner = "rainbow_six_siege_winner"
                rainbow_six_siege_member = "rainbow_six_siege_member"
                # Warface
                warface_member = "warface_member"
                warface_finalist = "warface_finalist"
                warface_winner = "warface_winner"
                # Monopoly
                monopoly_member = "monopoly_member"
                monopoly_finalist = "monopoly_finalist"
                monopoly_winner = "monopoly_winner"
                # Clash Royale
                clash_royale_member = "clash_royale_member"
                clash_royale_finalist = "clash_royale_finalist"
                clash_royale_winner = "clash_royale_winner"
                # PUBG
                pubg_member = "pubg_member"
                pubg_finalist = "pubg_finalist"
                pubg_winner = "pubg_winner"
                # Minecraft
                minecraft_member = "minecraft_member"
                minecraft_finalist = "minecraft_finalist"
                minecraft_winner = "minecraft_winner"

                # Other event trophies
                winner_logos_show = "winner_logos_show"
                member_finalist_show = "member_finalist_show"
                member_logos_show = "member_logos_show"
                lzt_speedrunner = "lzt_speedrunner"
                poker_participant = "poker_participant"
                poker_winner = "poker_winner"
                pixel_battle_member = "pixel_battle_member"
                ivent_lolzteam = "ivent_lolzteam"
                notpixel = "notpixel"
            _Literal = ["homepage", "location", "occupation", "_4", "scamURL", "banReason", "maecenasValue", "lztDeposit", "telegram", "vk", "discord", "steam", "jabber", "github", "lztInnovationLink", "lztInnovation20Link", "lztInnovation30Link"]
            homepage = "homepage"
            location = "location"
            occupation = "occupation"
            interests = "_4"
            scam_url = "scamURL"
            ban_reason = "banReason"

            maecenas_value = "maecenasValue"
            deposit = "lztDeposit"

            telegram = "telegram"
            vk = "vk"
            discord = "discord"
            steam = "steam"
            jabber = "jabber"
            github = "github"

            likes_increasing = "lztLikesIncreasing"
            likes_zeroing = "lztLikesZeroing"
            sympathies_increasing = "lztSympathyIncreasing"
            sympathies_zeroing = "lztSympathyZeroing"

            innovation1 = "lztInnovationLink"
            innovation2 = "lztInnovation20Link"
            innovation3 = "lztInnovation30Link"

        class GroupID:
            _Literal = Literal["2", "21", "22", "23", "60", "351", "65", "11", "26", "8", "265"]
            novice = 2             # Новокек
            local = 21             # Местный
            resident = 22          # Постоялец
            expert = 23            # Эксперт
            guru = 60              # Гуру
            ai = 351               # Искусственный интеллект

            market_privilege = 65  # Привилении на маркете
            forum_seller = 11      # Продавец на форуме
            legend = 26            # Легенда
            supreme = 8            # Суприм
            uniq = 265             # Уник

        class FollowOrder:
            _Literal = Literal["natural", "natural_reverse", "follow_date", "follow_date_reverse"]
            default = "natural"
            newest = "follow_date"
            oldest = "follow_date_reverse"

    class ChatRoomIDs:
        _Literal = Literal["1", "2", "3", "4", "13"]
        general_ru = 1             # [Russian] General chat
        general_en = 2             # [English] General hat
        market_ru = 3              # [Russian] Market chat
        market_en = 4              # [English] Market chat
        no_whiners = 13            # No whiners chat


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

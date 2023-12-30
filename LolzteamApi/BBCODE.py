class BBCODE:
    class Color:
        @staticmethod
        def black(text: str):
            return f"[color=black]{text}[/color]"

        @staticmethod
        def white(text: str):
            return f"[color=white]{text}[/color]"

        @staticmethod
        def red(text: str):
            return f"[color=red]{text}[/color]"

        @staticmethod
        def green(text: str):
            return f"[color=green]{text}[/color]"

        @staticmethod
        def blue(text: str):
            return f"[color=blue]{text}[/color]"

        @staticmethod
        def yellow(text: str):
            return f"[color=yellow]{text}[/color]"

        @staticmethod
        def purple(text: str):
            return f"[color=purple]{text}[/color]"

        @staticmethod
        def cyan(text: str):
            return f"[color=cyan]{text}[/color]"

        @staticmethod
        def magenta(text: str):
            return f"[color=magenta]{text}[/color]"

        @staticmethod
        def custom(text: str, hex_color: str):
            return f"[color={hex_color}]{text}[/color]"

    class Alignment:
        @staticmethod
        def left(text: str):
            return f"[left]{text}[/left]"

        @staticmethod
        def center(text: str):
            return f"[center]{text}[/center]"

        @staticmethod
        def right(text: str):
            return f"[right]{text}[/right]"

    class Hide:
        @staticmethod
        def club(text: str):
            return f"[club]{text}[/club]"

        @staticmethod
        def days(text: str, days: int):
            return f"[days={days}]{text}[/days]"

        @staticmethod
        def sympathies(text: str, sympathies: int):
            return f"[likes={sympathies}]{text}[/likes]"

        @staticmethod
        def from_users(text: str, user_ids: list):
            user_ids = list(map(str, user_ids))
            return f"[exceptids={','.join(user_ids)}]{text}[/exceptids]"

        @staticmethod
        def to_users(text: str, user_ids: list):
            user_ids = list(map(str, user_ids))
            return f"[userids={','.join(user_ids)}]{text}[/userids]"

    @staticmethod
    def list(text: str, ordered: bool = False):
        if ordered:
            ordered = "=1"
        else:
            ordered = ""
        formated = [f'[*]{line}\n' for line in text.split('\n')]
        return f"[LIST{ordered}]\n{''.join(formated)}[/LIST]"

    @staticmethod
    def text_size(text: str, size: int):
        return f"[size={size}]{text}[/size]"

    @staticmethod
    def bold(text: str):
        return f"[b]{text}[/b]"

    @staticmethod
    def italic(text: str):
        return f"[i]{text}[/i]"

    @staticmethod
    def strike_through(text: str):
        return f"[s]{text}[/s]"

    @staticmethod
    def underline(text: str):
        return f"[u]{text}[/u]"

    @staticmethod
    def code(text: str):
        return f"[code]{text}[/code]"

    @staticmethod
    def source_code(text: str, code_language: str = None, inline: bool = False):
        if code_language:
            if inline:
                return f"""[srci="{code_language}"]{text}[/srci]"""
            return f"""[src="{code_language}"]{text}[/src]"""
        else:
            if inline:
                return f"[srci]{text}[/srci]"
            return f"[src]{text}[/src]"

    @staticmethod
    def image(image_url: str):
        return f"[img]{image_url}[/img]"

    @staticmethod
    def media(media_url: str, site: str = None):
        if site:
            return f"[media={site}]{media_url}[/media]"
        else:
            return f"[media]{media_url}[/media]"

    @staticmethod
    def url(url: str, text: str = None):
        if text:
            return f"[url={url}]{text}[/url]"
        else:
            return f"[url]{url}[/url]"

    @staticmethod
    def email(email: str, text: str = None):
        if text:
            return f"[email={email}]{text}[/email]"
        else:
            return f"[email]{email}[/email]"

    @staticmethod
    def user(user_id: int or str):
        return f"[user={user_id}]{user_id}[/user]"

    @staticmethod
    def quote(text: str, author: str = None):
        if author:
            return f"[quote={author}]{text}[/quote]"
        else:
            return f"[quote]{text}[/quote]"

    @staticmethod
    def spoiler(text: str, spoiler_title: str = None):
        if spoiler_title:
            return f"[spoiler={spoiler_title}]{text}[/spoiler]"
        else:
            return f"[spoiler]{text}[/spoiler]"

    @staticmethod
    def visitor():
        return f"[visitor][/visitor]"

    @staticmethod
    def plain(text: str):
        return f"[plain]{text}[/plain]"

    @staticmethod
    def api(url: str, option: str = None):
        if option:
            return f"[api={option}]{url}[/api]"
        else:
            return f"[api]{url}[/api]"
    @staticmethod
    def custom(bbcode:str,text:str="",value:str=None):
        if value:
            return f"[{bbcode}={value}]{text}[/{bbcode}]"
        else:
            return f"[{bbcode}]{text}[/{bbcode}]"

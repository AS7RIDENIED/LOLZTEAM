from multiprocessing import Value, Lock
from httpx import ConnectError
import functools
import logging
import inspect
import asyncio
import ctypes
import base64
import types
import json
import time
import re

from . import Exceptions

logging.basicConfig(format="\033[93mWARNING:%(message)s\033[0m", level=logging.WARNING)


class _MainTweaks:
    @staticmethod
    def market_variable_fix(variable):
        if variable is None:
            variable = "nomatter"
        elif variable is True:
            variable = "yes"
        elif variable is False:
            variable = "no"
        return variable

    def _auto_delay(self):
        """
        Sleep for time difference between the last call and current call if it's less than 3 seconds
        """
        from .API import Antipublic

        if type(self) is not Antipublic:
            if self.bypass_429:
                if self._delay_synchronizer:
                    time_diff = time.time() - self._auto_delay_time.value
                    if (
                        time_diff < 3.0
                    ):  # if difference between current and last call > 3 seconds we will sleep the rest of the time
                        if self.debug:
                            print(f"Sleeping for {3-time_diff} seconds")
                        time.sleep(3.003 - time_diff)
                else:
                    time_diff = time.time() - self._auto_delay_time
                    if (
                        time_diff < 3.0
                    ):  # if difference between current and last call > 3 seconds we will sleep the rest of the time
                        if self.debug:
                            print(f"Sleeping for {3-time_diff} seconds")
                        time.sleep(3.003 - time_diff)

    async def _auto_delay_async(self):
        """
        Sleep for time difference between the last call and current call if it's less than 3 seconds
        """
        from .API import Antipublic

        if type(self) is not Antipublic:
            if self.bypass_429:
                if self._delay_synchronizer:
                    time_diff = time.time() - self._auto_delay_time.value
                    if (
                        time_diff < 3.0
                    ):  # if difference between current and last call > 3 seconds we will sleep the rest of the time
                        if self.debug:
                            print(f"Sleeping for {3-time_diff} seconds")
                        await asyncio.sleep(3.003 - time_diff)
                else:
                    time_diff = time.time() - self._auto_delay_time
                    if (
                        time_diff < 3.0
                    ):  # if difference between current and last call > 3 seconds we will sleep the rest of the time
                        if self.debug:
                            print(f"Sleeping for {3-time_diff} seconds")
                        await asyncio.sleep(3.003 - time_diff)

    def setup_jwt(self, token, user_id=None):
        if "." in self._token:
            decoded_payload = json.loads(
                base64.b64decode(
                    token.split(".")[1] + "=="
                    if "==" not in token.split(".")[1]
                    else token.split(".")[1]
                ).decode("utf-8")
            )
            if self.debug:
                print(decoded_payload)
            self.user_id = decoded_payload.get("sub", "me")
            scopes = decoded_payload.get(
                "scope", "basic read post conversate market"
            ).split(" ")
            self._scopes = scopes
        else:
            self._scopes = "basic read post conversate market".split(" ")
            self.user_id = user_id
        if self.debug:
            print(f"User ID: {self.user_id}\nScopes: {self._scopes}")

    def _CheckScopes(scopes: list = None):

        def _wrapper(func):

            def _wrapper_costyl(func_self, *args, **kwargs):
                main_self = func_self
                if hasattr(main_self, "__self__"):
                    main_self = main_self.__self__
                if hasattr(main_self, "_api"):
                    main_self = main_self._api
                path = str(func.__qualname__).replace("<class '", "").replace("'>", "")
                for bad_path, cute_path in {
                    "__Profile": "profile",
                    "__Payments": "payments",
                    "__Category": "category",
                    "__List": "list",
                    "__Publishing": "publishing",
                    "__Purchasing": "purchasing",
                    "__Managing": "managing",
                    "__Proxy": "proxy",
                    "__Steam": "steam",
                    "__Fortnite": "fortnite",
                    "__MiHoYo": "mihoyo",
                    "__Valorant": "valorant",
                    "__LeagueOfLegends": "lol",
                    "__Telegram": "telegram",
                    "__Supercell": "supercell",
                    "__Origin": "origin",
                    "__WorldOfTanks": "wot",
                    "__WorldOfTanksBlitz": "wot_blitz",
                    "__EpicGames": "epicgames",
                    "__EscapeFromTarkov": "eft",
                    "__SocialClub": "socialclub",
                    "__Uplay": "uplay",
                    "__WarThunder": "war_thunder",
                    "__Discord": "discord",
                    "__TikTok": "tiktok",
                    "__Instagram": "instagram",
                    "__BattleNet": "battlenet",
                    "__VPN": "vpn",
                    "__Cinema": "cinema",
                    "__Spotify": "spotify",
                    "__Warface": "warface",
                    "__Tag": "tag",
                    "__Auction": "auction",
                    "__Categories": "categories",
                    "__Forums": "forums",
                    "__Pages": "pages",
                    "__Threads": "threads",
                    "__Posts": "posts",
                    "__Tags": "tags",
                    "__Users": "users",
                    "__Profile_posts": "profile_posts",
                    "__Conversations": "conversations",
                    "__Notifications": "notifications",
                    "__Search": "search",
                    "__Oauth": "oauth",
                    "__Posts_comments": "comments",
                    "__Contests": "contests",
                    "__Arbitrage": "arbitrage",
                    "__Money": "money",
                    "__Upgrade": "upgrade",
                    "__Avatar": "avatar",
                    "__Profile_posts_comments": "comments",
                    "__Conversations_messages": "messages",
                }.items():
                    if bad_path in path:
                        path = path.replace(bad_path, cute_path)
                for scope in scopes:
                    scope_parsed = scope.split("?")
                    joined = ", ".join(scope_parsed)
                    if len(scope_parsed) > 1:
                        if not any(
                            _scope in main_self._scopes for _scope in scope_parsed
                        ):
                            logging.warn(
                                msg=f'{Exceptions.MISSING_SCOPE.__name__}: One of [{joined}] scope is required to use "{path}" but not provided in your token.\nYou should recreate token with at least one of these scopes.',
                                stack_info=False,
                            )
                    elif scope_parsed[0] not in main_self._scopes:
                        logging.warn(
                            msg=f'{Exceptions.MISSING_SCOPE.__name__}: "{joined}" scope is required to use "{path}" but not provided in your token.\nYou should recreate token with "{joined}" scope.',
                            stack_info=False,
                        )
                return func(func_self, *args, **kwargs)

            return _wrapper_costyl

        return _wrapper

    def _RetryWrapper(func):
        def _wrapper(*args, **kwargs):
            tries = 0
            self = kwargs["self"]
            if self._delay_synchronizer:
                self._lock.acquire()
            while tries < 30:
                tries += 1
                try:
                    response = func(*args, **kwargs)
                    if self._delay_synchronizer:
                        self._delay_synchronizer._synchronize(time.time())
                        self._lock.release()  # Unlocking to prevent softlock
                    else:
                        self._auto_delay_time = time.time()
                    return response
                except ConnectError as e:
                    if tries == 30:
                        raise e
                    time.sleep(0.05)
                    continue
        return _wrapper


class DelaySync:
    def __init__(self, apis: list = []):
        self.apis = [i for i in apis]
        self.lock = Lock()
        for api in self.apis:
            api._add_delay_synchronizer(self)
            api._auto_delay_time = Value(ctypes.c_longdouble, time.time())
            api._lock = self.lock

    def _synchronize(self, auto_delay_new):
        for api in self.apis:
            api._auto_delay_time.value = auto_delay_new

    def add(self, api):
        if self.apis:
            sync_time = self.apis[0]._auto_delay_time.value
        else:
            sync_time = time.time()
        if type(api) is list:
            for api_ in api:
                self.apis.append(api_)
                api_._add_delay_synchronizer(self)
                api._auto_delay_time = Value(ctypes.c_longdouble, sync_time)
                api._lock = self.lock
        elif type(api) is dict:
            for key, value in api.items():
                self.apis.append(value)
                value._add_delay_synchronizer(self)
                value._auto_delay_time = Value(ctypes.c_longdouble, sync_time)
                value._lock = self.lock
        else:
            self.apis.append(api)
            api._add_delay_synchronizer(self)
            api._auto_delay_time = Value(ctypes.c_longdouble, sync_time)
            api._lock = self.lock

    def remove(self, api):
        if type(api) is list:
            for api_ in api:
                self.apis.remove(api_)
                api_._remove_delay_synchronizer(self)
        elif type(api) is dict:
            for key, value in api.items():
                self.apis.remove(value)
                value._remove_delay_synchronizer(self)
        else:
            self.apis.remove(api)
            api._remove_delay_synchronizer()

    def clear(self):
        apis_td = []
        for api in self.apis:
            apis_td.append(api)
        for api in apis_td:
            self.remove(api)

    def __del__(
        self,
    ):  # Удаляем линки на синхронайзеры из объектов Forum/Market при удалении
        self.clear()


def CreateJob(func, job_name, **cur_kwargs):
    self = functools.partial(func).func.__self__
    if "scope" in functools.partial(func).func.__code__.co_varnames:
        func = next(
            (
                c
                for c in (c.cell_contents for c in func.__closure__)
                if isinstance(c, types.FunctionType)
            ),
            None,
        )
    else:
        func = functools.partial(func).func
    if hasattr(self, "_api"):
        self = self._api
    arguments = func.__code__.co_varnames
    CREATE_JOB = True
    loc = locals()
    for arg in arguments:
        if arg != "self":
            exec(f"{arg} = None", loc)
        if arg == "kwargs":
            exec("kwargs = {}", loc)
    user_id = None  # Костыль для Tweak 1
    for arg, value in cur_kwargs.items():
        if "kwargs" not in arguments and arg not in arguments:
            raise Exceptions.INVALID_ARG(
                f'Function "{func.__name__}" don\'t have "{arg}" parameter'
            )
        else:
            if arg not in arguments:
                loc["kwargs"][arg] = value
            else:
                loc[arg] = value
    func_code = str(inspect.getsource(func)).replace(" -> httpx.Response", "")
    func_code = func_code.split("):\n", 1)[1]
    lines = func_code.split("\n")
    indent = lines[0].split('"""')[0]
    for line in lines:
        if " def " in line:
            lines.remove(line)
    lines = [line.replace(indent, "", 1) for line in lines]
    return_code = "\n".join(lines).split('"""')[2].split("return ")[-1]
    func_code = "\n".join(lines).split('"""')[2].split("return ")[0]
    exec(func_code, globals(), loc)
    path = loc.get("path")
    params = loc.get("params", {})
    data = loc.get("data", {})
    params.update(data)
    method = [
        eval(i.replace("method=", "").strip())
        for i in return_code.split(",")
        if "method=" in i
    ][0]
    url = self.base_url + path
    params["locale"] = self._locale
    job = {"id": str(job_name), "uri": url, "method": method, "params": params}
    return job


async def SendAsAsync(func, **cur_kwargs):
    """
    Send async request

    :param func: Target function
    :param kwargs: Target function parameters

    :return: httpx Response object
    """
    self = functools.partial(func).func.__self__
    if "scope" in functools.partial(func).func.__code__.co_varnames:
        func = next(
            (
                c
                for c in (c.cell_contents for c in func.__closure__)
                if isinstance(c, types.FunctionType)
            ),
            None,
        )
    else:
        func = functools.partial(func).func
    if hasattr(self, "_api"):
        self = self._api
    arguments = func.__code__.co_varnames
    SEND_AS_ASYNC = True
    loc = locals()
    for arg in arguments:
        if arg != "self":
            exec(f"{arg} = None", loc)
        if arg == "kwargs":
            exec("kwargs = {}", loc)
    user_id = None  # Костыль для Tweak 1
    for arg, value in cur_kwargs.items():
        if "kwargs" not in arguments and arg not in arguments:
            raise Exceptions.INVALID_ARG(
                f'Function "{func.__name__}" don\'t have "{arg}" parameter'
            )
        else:
            if arg not in arguments:
                loc["kwargs"][arg] = value
            else:
                loc[arg] = value

    # Не придумал пока лучшего испольнения чека скопов для асинк запросов
    if True:
        pre_def = inspect.getsource(func).split("def")[0]
        pattern = r"\[.*?\]"
        result = re.findall(pattern, pre_def)
        scopes = None
        if result:
            scopes = eval(result[0])
        if scopes:
            path = str(func.__qualname__).replace("<class '", "").replace("'>", "")
            for bad_path, cute_path in {
                "__Profile": "profile",
                "__Payments": "payments",
                "__Category": "category",
                "__List": "list",
                "__Publishing": "publishing",
                "__Purchasing": "purchasing",
                "__Managing": "managing",
                "__Proxy": "proxy",
                "__Steam": "steam",
                "__Fortnite": "fortnite",
                "__MiHoYo": "mihoyo",
                "__Valorant": "valorant",
                "__LeagueOfLegends": "lol",
                "__Telegram": "telegram",
                "__Supercell": "supercell",
                "__Origin": "origin",
                "__WorldOfTanks": "wot",
                "__WorldOfTanksBlitz": "wot_blitz",
                "__EpicGames": "epicgames",
                "__EscapeFromTarkov": "eft",
                "__SocialClub": "socialclub",
                "__Uplay": "uplay",
                "__WarThunder": "war_thunder",
                "__Discord": "discord",
                "__TikTok": "tiktok",
                "__Instagram": "instagram",
                "__BattleNet": "battlenet",
                "__VPN": "vpn",
                "__Cinema": "cinema",
                "__Spotify": "spotify",
                "__Warface": "warface",
                "__Tag": "tag",
                "__Auction": "auction",
                "__Categories": "categories",
                "__Forums": "forums",
                "__Pages": "pages",
                "__Threads": "threads",
                "__Posts": "posts",
                "__Tags": "tags",
                "__Users": "users",
                "__Profile_posts": "profile_posts",
                "__Conversations": "conversations",
                "__Notifications": "notifications",
                "__Search": "search",
                "__Oauth": "oauth",
                "__Posts_comments": "comments",
                "__Contests": "contests",
                "__Arbitrage": "arbitrage",
                "__Money": "money",
                "__Upgrade": "upgrade",
                "__Avatar": "avatar",
                "__Profile_posts_comments": "comments",
                "__Conversations_messages": "messages",
            }.items():
                if bad_path in path:
                    path = path.replace(bad_path, cute_path)
            for scope in scopes:
                scope_parsed = scope.split("?")
                joined = ", ".join(scope_parsed)
                if len(scope_parsed) > 1:
                    if not any(_scope in self._scopes for _scope in scope_parsed):
                        logging.warn(
                            msg=f'{Exceptions.MISSING_SCOPE.__name__}: One of [{joined}] scope is required to use "{path}" but not provided in your token.\nYou should recreate token with at least one of these scopes.',
                            stack_info=False,
                        )
                    elif scope_parsed[0] not in self._scopes:
                        logging.warn(
                            msg=f'{Exceptions.MISSING_SCOPE.__name__}: "{joined}" scope is required to use "{path}" but not provided in your token.\nYou should recreate token with "{joined}" scope.',
                            stack_info=False,
                        )

    func_code = str(inspect.getsource(func)).replace(" -> httpx.Response", "")
    func_code = func_code.split("):\n", 1)[1]
    lines = func_code.split("\n")
    indent = lines[0].split('"""')[0]
    for line in lines:
        if " def " in line:
            lines.remove(line)
    lines = [line.replace(indent, "", 1) for line in lines]
    return_code = "\n".join(lines).split('"""')[2].split("return ")[-1]
    func_code = "\n".join(lines).split('"""')[2].split("return ")[0]
    exec(func_code, globals(), loc)
    path = loc.get("path")
    params = loc.get("params", {})
    data = loc.get("data", {})
    if type(data) is dict:
        params.update(data)
    method = [
        eval(i.replace("method=", "").strip())
        for i in return_code.split(",")
        if "method=" in i
    ][0]
    params["locale"] = self._locale
    from .API import _send_async_request

    return await _send_async_request(
        self=self, method=method, path=path, params=params, data=data
    )

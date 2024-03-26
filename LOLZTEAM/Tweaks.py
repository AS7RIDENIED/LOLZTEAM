from multiprocessing import Value, Lock
import functools
import inspect
import asyncio
import ctypes
import time

from . import Exceptions


class _MainTweaks:
    @staticmethod
    def market_variable_fix(var):
        if var is None:
            var = "nomatter"
        elif var is True:
            var = "yes"
        elif var is False:
            var = "no"
        return var

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
                        time.sleep(3.003 - time_diff)
                else:
                    time_diff = time.time() - self._auto_delay_time
                    if (
                        time_diff < 3.0
                    ):  # if difference between current and last call > 3 seconds we will sleep the rest of the time
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
                        await asyncio.sleep(3.003 - time_diff)
                else:
                    time_diff = time.time() - self._auto_delay_time
                    if (
                        time_diff < 3.0
                    ):  # if difference between current and last call > 3 seconds we will sleep the rest of the time
                        await asyncio.sleep(3.003 - time_diff)


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
    func = functools.partial(func)
    self = func.func.__self__
    if hasattr(self, "_api"):
        self = self._api
    func = func.func
    arguments = func.__code__.co_varnames
    batch_mode = True
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
    func_code = str(inspect.getsource(func)).replace(" -> Response", "")
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

    :return: Response object (Even if you use SendAsAsync function)
    """
    func = functools.partial(func)
    self = func.func.__self__
    if hasattr(self, "_api"):
        self = self._api
    func = func.func

    im_async = True
    arguments = func.__code__.co_varnames
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
    func_code = str(inspect.getsource(func)).replace(" -> Response", "")
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

"""
Some useful wrappers
"""

from concurrent.futures import ThreadPoolExecutor
from typing import Callable, TypeVar
from functools import wraps
import curl_cffi
import asyncio
import random


T = TypeVar('T', bound=Callable)


def RETRY(count: int = 10):
    """
    Retry wrapper
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for _ in range(count):
                try:
                    resp = await func(*args, **kwargs)
                    if 500 <= resp.status_code < 600:
                        continue
                    return resp
                except (curl_cffi.exceptions.RequestException):
                    # TODO: Add error logging here somehow -> e.__class__.__name__
                    await asyncio.sleep(0.5)
                    continue
            return await func(*args, **kwargs)
        return wrapper
    return decorator


def UNIVERSAL(batchable=False) -> curl_cffi.Response:
    """
    Universal wrapper to run async function in sync context and create batch jobs
    """
    def decorator(func: T) -> T:
        class UniversalWrapper:
            def __init__(self, func, batchable=False):
                self.func = func
                self.batchable = batchable

            def __get__(self, instance, owner):
                if instance is None:
                    return self.func
                from .Core import _NONE

                class RequestCapture:
                    """
                    Request capture
                    """

                    def __init__(self):
                        self.captured = None

                    async def __call__(self, method: str, endpoint: str, **kwargs):
                        self.captured = {
                            "method": method,
                            "endpoint": endpoint,
                            **kwargs
                        }
                        return None

                def job(*args, **kwargs) -> dict:
                    """
                    Returns job for batch request
                    """
                    capture = RequestCapture()
                    job_id = str(kwargs.pop("job_id", random.randint(1000000, 9999999)))
                    if hasattr(instance, "core"):
                        head_instance = instance.core
                    else:
                        head_instance = instance

                    original_request = head_instance.request
                    head_instance.request = capture

                    def _worker():
                        async def method_wrapper(*args, **kwargs):
                            return await self.func(instance, *args, **kwargs)
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        try:
                            return loop.run_until_complete(method_wrapper(*args, **kwargs))
                        finally:
                            loop.close()

                    try:
                        with ThreadPoolExecutor() as executor:
                            executor.submit(_worker).result()
                        captured = capture.captured

                        params = _NONE.TrimNONE(captured.get("params", {}))
                        params.update(_NONE.TrimNONE(captured.get("data", {})))
                        params.update(_NONE.TrimNONE(captured.get("json", {})))

                        return {
                            "id": job_id,
                            "method": captured["method"],
                            "uri": captured["endpoint"],
                            "params": params,
                        }
                    finally:
                        head_instance.request = original_request

                def job_on_request(method: str, endpoint: str, **kwargs) -> dict:
                    """
                    Returns job for batch request
                    """
                    params = _NONE.TrimNONE(kwargs.get("params", {}))
                    params.update(_NONE.TrimNONE(kwargs.get("data", {})))
                    params.update(_NONE.TrimNONE(kwargs.get("json", {})))
                    return {
                        "id": str(kwargs.pop("job_id", random.randint(1, 1000000))),
                        "method": method,
                        "uri": endpoint,
                        "params": params,
                    }

                def null_job(*args, **kwargs):
                    #  Preventing errors when the function is not batchable
                    return None

                def wrapper(*args, **kwargs):
                    try:
                        asyncio.get_running_loop()
                        return self.func(instance, *args, **kwargs)
                    except RuntimeError:
                        return asyncio.run(self.func(instance, *args, **kwargs))

                if self.batchable:
                    if self.func.__qualname__ == "APIClient.request":
                        setattr(wrapper, "job", job_on_request)
                    else:
                        setattr(wrapper, "job", job)
                else:
                    setattr(wrapper, "job", null_job)

                return wrapper

        return UniversalWrapper(func, batchable=batchable)

    return decorator

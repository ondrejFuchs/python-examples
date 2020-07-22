import asyncio
import logging
from concurrent.futures import Future

import time
from threading import RLock
from typing import Awaitable


def apply_in_executor(func, *args, on_complete=None, on_error=None, **kwargs) -> Future:

    from concurrent.futures import ThreadPoolExecutor
    
    futures = None
    executor = ThreadPoolExecutor(max_workers=2)

    # Multiple args
    if args:
        futures = executor.submit(func, args)
    # Without args    
    else:
        futures = executor.submit(func)

    if on_complete is not None or on_error is not None:
        try:
            result = futures.result()
            if args:
                on_complete(*args)
        except:
            if on_error:
                on_error("error")
                
    return futures


logger = logging.getLogger(__name__)
_loop = None
_lock = RLock()


def get_loop():
    global _lock, _loop
    with _lock:
        if _loop is None:
            logger.info(f"creating a new event loop")
            _loop = asyncio.new_event_loop()
            apply_in_executor(_loop.run_forever)
            time.sleep(0.1)
        return _loop


def kill_loop():
    with _lock:
        loop = get_loop()
        loop.call_soon_threadsafe(loop.stop)
        for attempt in range(3):
            if not loop.is_running():
                break
            else:
                time.sleep(0.1)
        else:
            raise Exception(f"failed to stop loop")
        loop.close()
        global _loop
        _loop = None


def run_coroutine(coroutine: Awaitable) -> Future:
    loop = get_loop()
    futures = None
    futures = asyncio.run_coroutine_threadsafe(coroutine, loop)
    return futures
    

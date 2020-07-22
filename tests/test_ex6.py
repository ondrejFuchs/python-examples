from concurrent.futures import Future

import pytest
import time

from ex6.pool_async import apply_in_executor, run_coroutine


def one_sec_wait(arg):
    time.sleep(1)
    return arg


def error():
    time.sleep(1)
    raise Exception("error")


def test_apply_in_executor_on_complete():
    complete_flag = Future()

    def set_complete_flag(result):
        nonlocal complete_flag
        complete_flag.set_result(result)

    apply_in_executor(one_sec_wait, 2, on_complete=set_complete_flag)
    assert complete_flag.result(timeout=2) == 2


def test_apply_in_executor_on_error():
    complete_flag = Future()

    def set_complete_flag(result):
        nonlocal complete_flag
        complete_flag.set_result(result)

    apply_in_executor(error, on_error=set_complete_flag)
    error_result = complete_flag.result(timeout=2)
    assert str(error_result) == "error"

async def coroutine(arg):
    return arg


@pytest.fixture()
def with_loop():
    """call get_loop() before test and kill_loop() after the test"""
    from ex6.pool_async import get_loop, kill_loop
    get_loop()
    yield
    kill_loop()


def test_run_coroutine(with_loop):
    f = run_coroutine(coroutine(2))
    result = f.result(timeout=1)
    assert result == 2




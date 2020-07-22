"""
1. Write a decorator "count_calls" that counts the number of calls to any function.
It should be possible to retrieve the count.

Test your decorator by writing a test in tests/test_decorators.py.

2. Write a decorator "memorize" that memories the result and test your decorator by using the add function below and retrieving the count
"""


def count_calls(f):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return f(*args, **kwargs)
    wrapper.calls = 0
    return wrapper  # We return wrapper function instead of f to modify behavioral of original func


def memorize(f):
    def wrapper(*args, **kwargs):
        out = f(*args, **kwargs)
        wrapper.mem[f.calls] = out  
        return wrapper.mem[f.calls]
    wrapper.mem = {}
    return wrapper


@memorize
@count_calls
def add(a, b):
    return a + b

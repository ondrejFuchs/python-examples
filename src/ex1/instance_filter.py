from typing import TypeVar, Any, Type, Iterable

T = TypeVar("T")


def filter_on(it: Iterable[Any], t: Type[T]) -> Iterable[T]:
    out = []
    for i in it:
        if isinstance(i, str):
            out.append(i)
    return out

from ex5.never_attr_error import NeverAttributeError
from ex5.subclasses import Base, A, B


def test_subclass_list():
    assert Base.subclasses == [A, B]


def test_never_attr_error():
    instance = NeverAttributeError()
    assert instance.a == NeverAttributeError.UNKNOWN
    assert instance.b == NeverAttributeError.UNKNOWN
    instance.c = "lol"
    assert instance.c == "lol"

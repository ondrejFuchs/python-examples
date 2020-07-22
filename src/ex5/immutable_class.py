class ImmtableError(Exception):
    pass


class Immutable:
    """
    >>> instance1 = Immutable(a=3)
    >>> instance1.a
    3
    >>> instance1.a = 4
    Traceback (most recent call last):
    ...
    immutable_class.ImmtableError
    >>> instance2 = Immutable()
    >>> instance2.a = 3
    Traceback (most recent call last):
    ...
    immutable_class.ImmtableError
    """
    
    __slots__ = ("a")
    def __init__(self, a=None):
        super(Immutable, self).__setattr__("a", a)
    
    def __setattr__(self, name, value):
        raise ImmtableError()
        
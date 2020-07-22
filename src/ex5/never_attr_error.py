from typing import ClassVar


class NeverAttributeError:
    """
    Should return 'unknown' whenever the attribute does not exist
    """

    UNKNOWN: ClassVar[str] = "unknown"
    
    def __getattr__(self, item):
        return "unknown"

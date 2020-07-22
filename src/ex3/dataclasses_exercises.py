from dataclasses import dataclass, field

from pathlib import Path


@dataclass
class IsDuplicateChecker:
    """
    >>> checker = IsDuplicateChecker(maxsize=10)
    >>> checker(1)
    False
    >>> checker(1)
    True
    >>> checker(2)
    False
    >>> all(checker(check) is False for check in range(3,13))
    True
    >>> checker(1)
    False
    """

    maxsize: int
    elems:  set = field(default_factory=lambda: [])
    
    def __call__(self, val): 
        if val not in self.elems:
            self.elems.append(val) 
            return False
        else:
            self.elems.remove(val) 
            return True


DIR = Path(__file__).parent

@dataclass
class EnsureInitExist:
    """
    >>> EnsureInitExist(DIR)
    EnsureInitExist('ex3/__init__.py')
    >>> EnsureInitExist(DIR.parent)
    Traceback (most recent call last):
    ...
    AssertionError: Init is missing!
    """

    dir_path: Path = field(repr=False)
    
    def validate(self):
        ret = True
        file_to_check = "__init__.py"
        final_path = self.dir_path.absolute() / file_to_check
        if not final_path.is_file():
            ret = False
        else:
            second_level = self.dir_path.absolute().parent
            parent_name = str(self.dir_path.absolute().relative_to(second_level))
            self.dir_path = str("{}/{}".format(parent_name, file_to_check))    
        return ret
    
    def __post_init__(self):
        # Change relative path of DIR variable to absolute 
        global DIR
        DIR = DIR.absolute()
        # Control if file __init__.py exist
        if not self.validate():
            raise AssertionError('Init is missing!')
    
    def __repr__(self):
         return f'EnsureInitExist({self.dir_path!r})'


import traceback
import os

class OsEnv:
    os_var = None
    # Descriptors
    def __init__(self, default, typ=str):
        self.val = default
        self.def_name = None
        # To get name of instance in class
        if self.def_name == None:
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            self.def_name = text[:text.find('=')].strip()
        os.environ[self.def_name] = ""

    def __get__(self, instance, owner):
        # To manage changes with os.env
        if os.environ.get(self.def_name):
            if os.environ[self.def_name] != self.os_var:
                self.val = os.environ[self.def_name]
                self.os_var = os.environ[self.def_name]
                return self.val
            else:
                os.environ[self.def_name] = self.val
                self.os_var = self.val
                return int(self.val)
        else:
            return self.val

    def __set__(self, instance, value):
        self.val = value
        os.environ[self.def_name] = value
        self.os_var = value


class Settings:
    var1 = OsEnv("default")
    var2 = OsEnv(2, int)

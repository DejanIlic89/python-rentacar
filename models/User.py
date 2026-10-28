# public    = self.name
# protected = self._name
# private   = self.__name
from models.Db import Db

class User(Db):

    def __init__(self):
        super().__init__()

    def set_age(self, age):
        if age < 18:
            raise ValueError("Age must be greater than or equal to 18")
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 3:
            raise ValueError("User name must be at least 3 characters long")
        self.__name = name

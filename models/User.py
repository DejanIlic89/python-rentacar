# public    = self.name
# protected = self._name
# private   = self.__name
from models.Db import Db


class User(Db):

    def __init__(self):
        super().__init__()
        self.__name = None
        self.__age = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Age must be greater than or equal to 18")
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise ValueError("User name must be at least 3 characters long")
        self.__name = name

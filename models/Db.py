import pymysql


class Db:

    def __init__(self):
        self.__connection = pymysql.connect(
            host="localhost",
            user="root",
            password="admin",
            database="oop_2",
            ssl_disabled=True
        )

    def _get_connection(self):
        return self.__connection

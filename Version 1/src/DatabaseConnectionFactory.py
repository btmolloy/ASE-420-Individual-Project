import sqlite3

class DatabaseConnectionFactory:
    _instance = None

    def __new__(cls, db_name='tasks.db'):
        if cls._instance is None:
            cls._instance = super(DatabaseConnectionFactory, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect(db_name)
# CODE SMELL BELOW CURSOR WAS C
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        return self.cursor

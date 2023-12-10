# Singleton Pattern for Database Connection
import sqlite3

class DatabaseConnectionFactory:
    # Class variable to hold the single instance of the class
    _instance = None

    def __new__(cls, db_name='tasks.db'):
        # If there is no existing instance, create one
        if cls._instance is None:
            cls._instance = super(DatabaseConnectionFactory, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect(db_name)
            cls._instance.cursor = cls._instance.conn.cursor()
        # Return the single instance
        return cls._instance

    def get_connection(self):
        # Return the database connection
        return self.conn

    def get_cursor(self):
        # Return the database cursor
        return self.cursor

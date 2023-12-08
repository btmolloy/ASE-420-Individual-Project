# test_database_connection_factory.py

import sqlite3
import pytest
from src.DatabaseConnectionFactory import DatabaseConnectionFactory  

@pytest.fixture
def temp_database_factory():
    # Create a temporary instance of DatabaseConnectionFactory for testing
    factory = DatabaseConnectionFactory(db_name=':memory:')
    yield factory
    factory.conn.close()

def test_singleton_behavior(temp_database_factory):
    # Test if DatabaseConnectionFactory is a singleton
    factory1 = temp_database_factory
    factory2 = DatabaseConnectionFactory(db_name=':memory:')

    assert factory1 is factory2  # Both instances should be the same (singleton)

def test_get_connection(temp_database_factory):
    # Test if get_connection method returns a connection
    factory = temp_database_factory
    conn = factory.get_connection()

    assert isinstance(conn, sqlite3.Connection)

def test_get_cursor(temp_database_factory):
    # Test if get_cursor method returns a cursor
    factory = temp_database_factory
    cursor = factory.get_cursor()

    assert isinstance(cursor, sqlite3.Cursor)

import sqlite3
import pytest
from unittest.mock import patch
from src.DatabaseConnectionFactory import DatabaseConnectionFactory

# Test that the singleton pattern is working
def test_singleton_pattern():
    instance1 = DatabaseConnectionFactory()
    instance2 = DatabaseConnectionFactory()

    # Both instances should be the same
    assert instance1 is instance2

# Test that the connection and cursor are correctly created
# test_database_connection_factory.py

from src.DatabaseConnectionFactory import DatabaseConnectionFactory

def test_connection_and_cursor():
    # Create an instance of DatabaseConnectionFactory
    instance = DatabaseConnectionFactory()

    # Check that get_connection and get_cursor return values
    assert instance.get_connection() is not None
    assert instance.get_cursor() is not None

def test_custom_database_name():
    custom_db_name = 'custom_tasks.db'

    # Create an instance of DatabaseConnectionFactory with a custom database name
    instance = DatabaseConnectionFactory(db_name=custom_db_name)

    # Check that get_connection and get_cursor return values
    assert instance.get_connection() is not None
    assert instance.get_cursor() is not None

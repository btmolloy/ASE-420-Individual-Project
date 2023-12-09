# test_task_record_repository.py

import sqlite3
import tempfile
import pytest
from src.TaskRecordRepository import TaskRecordRepository  
from src.TaskRecord import TaskRecord

@pytest.fixture
def temp_database():
    # Create a temporary SQLite database for testing
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    yield conn, cursor
    conn.close()

def test_create_table(temp_database):
    # Test if create_table method creates the 'tasks' table
    conn, cursor = temp_database
    repository = TaskRecordRepository(conn, cursor)

    # Check if the 'tasks' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks';")
    result = cursor.fetchone()
    assert result is not None

def test_insert_task_record(temp_database):
    # Test if insert_task_record method inserts a task record into the 'tasks' table
    conn, cursor = temp_database
    repository = TaskRecordRepository(conn, cursor)

    # Create a task record and insert it
    task_record = TaskRecord("2023-12-08", "10:00 AM", "11:00 AM", "Task 1", "Tag 1")
    repository.insert_task_record(task_record)

    # Retrieve the inserted task record
    cursor.execute("SELECT * FROM tasks WHERE task_name = 'Task 1';")
    result = cursor.fetchone()
    assert result is not None
    assert result[4] == "Task 1"  # Check if the task name matches

def test_search_tasks(temp_database):
    # Test if search_tasks method retrieves the correct task records
    conn, cursor = temp_database
    repository = TaskRecordRepository(conn, cursor)

    # Insert task records for testing
    task_records = [
        TaskRecord("2023-12-08", "10:00 AM", "11:00 AM", "Task 1", "Tag 1"),
        TaskRecord("2023-12-09", "12:00 PM", "01:00 PM", "Task 2", "Tag 2"),
        TaskRecord("2023-12-10", "02:00 PM", "03:00 PM", "Task 3", "Tag 3"),
    ]

    for task_record in task_records:
        repository.insert_task_record(task_record)

    # Search for tasks with a specific tag
    result = repository.search_tasks("task_tag", "Tag 2")

    # Check if the correct task record is retrieved
    assert len(result) == 1
    assert result[0][4] == "Task 2"  # Check if the task name matches

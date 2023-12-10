import unittest
from unittest.mock import MagicMock
from src.TaskRecordRepository import TaskRecordRepository
from src.TaskRecord import TaskRecord

class TestTaskRecordRepository(unittest.TestCase):
    def setUp(self):
        # Create a mock connection and cursor
        self.mock_connection = MagicMock()
        self.mock_cursor = self.mock_connection.cursor.return_value

        # Create a TaskRecordRepository with the mock connection and cursor
        self.repository = TaskRecordRepository(self.mock_connection, self.mock_cursor)

    def test_create_table(self):
        # Ensure that create_table method is executed and commits changes
        self.repository.create_table()
        self.mock_connection.commit.assert_called()
        self.assertEqual(self.mock_connection.commit.call_count, 2)

    def test_insert_task_record(self):
        # Create a sample TaskRecord for testing
        task_record = TaskRecord('2023-01-01', '09:00 AM', '05:00 PM', 'Task Name', 'Task Tag', '08:00')

        # Ensure that insert_task_record method is executed and commits changes
        self.repository.insert_task_record(task_record)
        self.mock_connection.commit.assert_called()
        self.assertEqual(self.mock_connection.commit.call_count, 2)


    def test_search_tasks(self):
        # Ensure that search_tasks method is executed
        self.repository.search_tasks('date_of_task', '2023-01-01')
        self.mock_cursor.execute.assert_called()
        self.assertEqual(self.mock_cursor.execute.call_count, 2)

    def test_get_activities_in_date_range(self):
        # Ensure that get_activities_in_date_range method is executed
        self.repository.get_activities_in_date_range('2023-01-01', '2023-01-02')
        self.mock_cursor.execute.assert_called()
        self.assertEqual(self.mock_cursor.execute.call_count, 2)

    def test_get_priority_activities(self):
        # Ensure that get_priority_activities method is executed
        self.repository.get_priority_activities()
        self.mock_cursor.execute.assert_called()
        self.assertEqual(self.mock_cursor.execute.call_count, 2)

if __name__ == '__main__':
    unittest.main()

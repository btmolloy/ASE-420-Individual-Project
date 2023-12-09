from io import StringIO
from unittest.mock import patch, MagicMock, Mock
import pytest
from src.TaskManager import TaskManager

@pytest.fixture
def task_manager():
    with patch('src.DatabaseConnectionFactory.DatabaseConnectionFactory.get_connection'):
        with patch('src.DatabaseConnectionFactory.DatabaseConnectionFactory.get_cursor'):
            with patch('src.TaskRecordRepository.TaskRecordRepository.insert_task_record'):
                yield TaskManager()

def test_record_time_successful_insert(task_manager: TaskManager):
    # Mocking user input
    with patch('builtins.input', side_effect=["2023-12-08", "12:00 PM", "01:00 PM", "Sample Task", "Work"]):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Run the test
            task_manager.record_time()

            # Check the output
            output = mock_stdout.getvalue().strip()
            assert "Data successfully inserted into the database." in output

def test_search_tasks_successful_search(task_manager):
    # Mocking user input
    with patch('builtins.input', side_effect=["1", "2023-12-08", "12:00 PM", "01:00 PM", "Sample Task", "Work"]):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Mocking the search_tasks method to return a predefined result
            with patch('src.TaskRecordRepository.TaskRecordRepository.search_tasks', return_value=['Sample Task']):
                # Run the test
                task_manager.search_tasks()

            # Check the output
            output = mock_stdout.getvalue().strip()
            assert "Search Results:" in output, f"Actual output: {output}"
            if "Search Results:" in output:
                search_results_part = output.split("Search Results:")[1].strip()
                assert "Sample Task" in search_results_part, f"Actual output: {search_results_part}"
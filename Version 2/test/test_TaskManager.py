import datetime
from unittest.mock import MagicMock, patch
from src.TaskManager import TaskManager

def test_record_time(capsys):
    # Create a mock TaskRepository
    mock_repository = MagicMock()

    # Set user input for the test
    user_inputs = [
        '2023-01-01',   # Date
        '09:00 AM',     # Start time
        '05:00 PM',     # End time
        'Task Name',    # Task name
        'Task Tag'      # Task tag
    ]

    # Redirect standard input to provide user inputs
    with patch('builtins.input', side_effect=user_inputs):
        # Create an instance of TaskManager with the mock repository
        task_manager_instance = TaskManager()
        task_manager_instance.task_repository = mock_repository

        # Call the record_time method
        task_manager_instance.record_time()

    # Assert that the mock repository's insert_task_record method was called
    mock_repository.insert_task_record.assert_called()

def test_search_tasks(capsys):
    # Create a mock TaskRepository
    mock_repository = MagicMock()

    # Set user input for the test
    user_inputs = [
        '1',           # Choose Date_of_Task as the search criterion
        '2023-01-01'   # Enter the search value
    ]

    # Redirect standard input to provide user inputs
    with patch('builtins.input', side_effect=user_inputs):
        # Create an instance of TaskManager with the mock repository
        task_manager_instance = TaskManager()
        task_manager_instance.task_repository = mock_repository

        # Call the search_tasks method
        task_manager_instance.search_tasks()

    # Assert that the mock repository's search_tasks method was called
    mock_repository.search_tasks.assert_called()

def test_view_priorities(capsys):
    # Create a mock TaskRepository with priority activities
    mock_repository = MagicMock()
    mock_repository.get_priority_activities.return_value = [
        "Tag 1 | 02:30",
        "Tag 2 | 01:45"
    ]

    # Create an instance of TaskManager with the mock repository
    task_manager_instance = TaskManager()
    task_manager_instance.task_repository = mock_repository

    # Call the view_priorities method
    task_manager_instance.view_priorities()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the output contains the expected priority activities
    assert "Priority Activities:" in captured.out
    assert "Tag 1 | 02:30" in captured.out
    assert "Tag 2 | 01:45" in captured.out

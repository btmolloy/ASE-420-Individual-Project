from unittest.mock import MagicMock, patch
from src.SearchTask import SearchTask

def test_search_tasks_with_results(capsys):
    # Create a mock task repository with search results
    mock_repository = MagicMock()
    mock_repository.search_tasks.return_value = [
        "1 | 2023-01-01 | 09:00 AM | 05:00 PM | Task 1 | Tag 1 | 08:00",
        "2 | 2023-01-02 | 10:00 AM | 02:00 PM | Task 2 | Tag 2 | 04:00"
    ]

    # Set user input for the test
    user_inputs = [
        '1',            # Choose Date_of_Task as the search criterion
        '2023-01-01'    # Enter the search value
    ]

    # Redirect standard input to provide user inputs
    with patch('builtins.input', side_effect=user_inputs):
        # Create an instance of SearchTask with the mock repository
        search_task_instance = SearchTask(mock_repository)

        # Call the search_tasks method
        search_task_instance.search_tasks()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the output contains the expected search results
    assert "Search Results:" in captured.out
    assert "Task 1" in captured.out
    assert "Task 2" in captured.out

def test_search_tasks_no_results(capsys):
    # Create a mock task repository with no search results
    mock_repository = MagicMock()
    mock_repository.search_tasks.return_value = []

    # Set user input for the test
    user_inputs = [
        '1',            # Choose Date_of_Task as the search criterion
        '2023-01-01'    # Enter the search value
    ]

    # Redirect standard input to provide user inputs
    with patch('builtins.input', side_effect=user_inputs):
        # Create an instance of SearchTask with the mock repository
        search_task_instance = SearchTask(mock_repository)

        # Call the search_tasks method
        search_task_instance.search_tasks()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the output contains the expected message
    assert "No results found for the search criteria." in captured.out

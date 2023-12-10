from unittest.mock import MagicMock, patch
from src.ReportGenerator import ReportGenerator

def test_ReportGenerator_with_activities(capsys):
    # Create a mock task repository with activities
    mock_repository = MagicMock()
    mock_repository.get_activities_in_date_range.return_value = [
        "1 | 2023-01-01 | 09:00 AM | 05:00 PM | Task 1 | Tag 1 | 08:00",
        "2 | 2023-01-02 | 10:00 AM | 02:00 PM | Task 2 | Tag 2 | 04:00"
    ]

    # Set user input for the test
    user_inputs = [
        '2023-01-01',  # Start date
        '2023-01-02'   # End date
    ]

    # Redirect standard input to provide user inputs
    with patch('builtins.input', side_effect=user_inputs):
        # Create an instance of ReportGenerator with the mock repository
        report_generator_instance = ReportGenerator()

        # Call the ReportGenerator method
        report_generator_instance.ReportGenerator(mock_repository)

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the output contains the expected report
    assert "Report:" in captured.out
    assert "Task 1" in captured.out
    assert "Task 2" in captured.out

def test_ReportGenerator_no_activities(capsys):
    # Create a mock task repository with no activities
    mock_repository = MagicMock()
    mock_repository.get_activities_in_date_range.return_value = []

    # Set user input for the test
    user_inputs = [
        '2023-01-01',  # Start date
        '2023-01-02'   # End date
    ]

    # Redirect standard input to provide user inputs
    with patch('builtins.input', side_effect=user_inputs):
        # Create an instance of ReportGenerator with the mock repository
        report_generator_instance = ReportGenerator()

        # Call the ReportGenerator method
        report_generator_instance.ReportGenerator(mock_repository)

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the output contains the expected message
    assert "No activities found for the specified date range." in captured.out

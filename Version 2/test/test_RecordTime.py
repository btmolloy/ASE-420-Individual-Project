# test_record_time.py

import pytest
from src.RecordTime import RecordTime
from unittest.mock import MagicMock, patch
from io import StringIO
import datetime

def test_record_time_valid_input():
    # Create a mock task repository
    mock_repository = MagicMock()

    # Set user input for the test
    user_inputs = [
        '2023-12-01',  # Valid date
        '09:00 AM',    # Valid start time
        '05:00 PM',    # Valid end time
        'Task Name',   # Task name
        'Task Tag'     # Task tag
    ]

    # Redirect standard input to provide user inputs
    with patch('builtins.input', side_effect=user_inputs):
        # Create an instance of RecordTime with the mock repository
        record_time_instance = RecordTime(mock_repository)

        # Call the record_time method
        record_time_instance.record_time()

    # Validate that the mock repository's insert_task_record method was called
    mock_repository.insert_task_record.assert_called_once()

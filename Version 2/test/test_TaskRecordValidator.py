# test_task_record_validator.py

from src.TaskRecordValidator import TaskRecordValidator 

def test_verify_date_valid():
    # Test a valid date format
    valid_date = "2023-12-08"
    assert TaskRecordValidator.verify_date(valid_date) is True

def test_verify_date_invalid():
    # Test an invalid date format
    invalid_date = "2023/12/08"
    assert TaskRecordValidator.verify_date(invalid_date) is False

def test_verify_time_valid():
    # Test a valid time format
    valid_time = "10:00 AM"
    assert TaskRecordValidator.verify_time(valid_time) is True

def test_verify_time_invalid():
    # Test an invalid time format
    invalid_time = "25:00 PM"
    assert TaskRecordValidator.verify_time(invalid_time) is False

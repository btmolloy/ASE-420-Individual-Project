# test_date_validation_strategy.py

from src.DateValidationStrategy import DateValidationStrategy

def test_valid_date():
    # Create an instance of DateValidationStrategy
    date_validator = DateValidationStrategy()

    # Test a valid date string
    valid_date_str = '2023-12-01'
    assert date_validator.validate(valid_date_str) is True

def test_invalid_date():
    # Create an instance of DateValidationStrategy
    date_validator = DateValidationStrategy()

    # Test an invalid date string
    invalid_date_str = '2023-13-01'  # Month 13 is invalid
    assert date_validator.validate(invalid_date_str) is False

from src.TimeValidationStrategy import TimeValidationStrategy

def test_time_validation_strategy_valid_time():
    # Arrange
    time_validator = TimeValidationStrategy()
    valid_time_str = "12:30 PM"

    # Act
    result = time_validator.validate(valid_time_str)

    # Assert
    assert result is True

def test_time_validation_strategy_invalid_time():
    # Arrange
    time_validator = TimeValidationStrategy()
    invalid_time_str = "25:00 PM"

    # Act
    result = time_validator.validate(invalid_time_str)

    # Assert
    assert result is False

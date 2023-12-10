import pytest
from unittest.mock import MagicMock
from src.TaskRecordValidator import TaskRecordValidator
from src.ValidationStrategy import ValidationStrategy

class MockValidationStrategy(ValidationStrategy):
    def validate(self, value):
        # Mock implementation for testing
        return True

def test_task_record_validator():
    # Arrange
    mock_strategy = MockValidationStrategy()
    task_record_validator = TaskRecordValidator(mock_strategy)

    # Act
    result = task_record_validator.validate("some_value")

    # Assert
    assert result is True 
import unittest
from src.ValidationStrategy import ValidationStrategy
from src.TimeValidationStrategy import TimeValidationStrategy

def test_validation_strategy():
    # Arrange
    strategy = ValidationStrategy()

    # Act
    result = strategy.validate("some_value")

    # Assert
    assert result is None
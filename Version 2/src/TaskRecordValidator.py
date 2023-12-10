from src.ValidationStrategy import ValidationStrategy

# Strategy Pattern for Validation
class TaskRecordValidator(ValidationStrategy):
    def __init__(self, validation_strategy):
        # Set the validation strategy
        self.validation_strategy = validation_strategy

    def validate(self, value):
        # Delegate validation to the assigned strategy
        return self.validation_strategy.validate(value)

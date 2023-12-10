# Strategy Pattern for Validation
class TaskRecordValidator:
    def __init__(self, validation_strategy):
        self.validation_strategy = validation_strategy

    def validate(self, value):
        return self.validation_strategy.validate(value)
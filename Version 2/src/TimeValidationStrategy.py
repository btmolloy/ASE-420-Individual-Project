from src.ValidationStrategy import ValidationStrategy
import datetime

class TimeValidationStrategy(ValidationStrategy):
    def validate(self, time_str):
        try:
            datetime.datetime.strptime(time_str, '%I:%M %p')
            return True
        except ValueError:
            return False
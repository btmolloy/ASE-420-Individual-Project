from src.ValidationStrategy import ValidationStrategy
import datetime

class TimeValidationStrategy(ValidationStrategy):
    def validate(self, time_str):
        # Attempt to parse the time string using the specified format
        try:
            datetime.datetime.strptime(time_str, '%I:%M %p')
            return True
        except ValueError:
            # Return False if an exception is raised (invalid time string)
            return False

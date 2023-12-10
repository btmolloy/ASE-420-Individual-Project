from src.ValidationStrategy import ValidationStrategy
import datetime

class DateValidationStrategy(ValidationStrategy):
    def validate(self, date_str):
        try:
            # Attempt to parse the date string using the specified format
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            # Return False if an exception is raised (invalid date string)
            return False

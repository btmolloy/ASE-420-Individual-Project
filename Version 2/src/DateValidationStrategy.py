from src.ValidationStrategy import ValidationStrategy
import datetime

class DateValidationStrategy(ValidationStrategy):
    def validate(self, date_str):
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
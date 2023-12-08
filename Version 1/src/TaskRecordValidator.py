from datetime import datetime

class TaskRecordValidator:
    @staticmethod
    def verify_date(date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def verify_time(time):
        try:
            datetime.strptime(time, '%I:%M %p')
            return True
        except ValueError:
            return False

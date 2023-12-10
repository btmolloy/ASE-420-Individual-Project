from src.TaskRecord import TaskRecord
import datetime
from src.TimeValidationStrategy import TimeValidationStrategy
from src.TaskRecordValidator import TaskRecordValidator
from src.DateValidationStrategy import DateValidationStrategy

class RecordTime:

    def __init__(self, task_repository):
        self.validator = TaskRecordValidator(DateValidationStrategy())
        self.task_repository = task_repository

    def record_time(self):
        date_of_task = self.get_valid_input("Enter date (YYYY-MM-DD or today): ", self.validator.validate)
        self.start_time_of_task = self.get_valid_input("Enter start time (HH:MM AM/PM): ", TimeValidationStrategy().validate)
        self.end_time_of_task = self.get_valid_input("Enter end time (HH:MM AM/PM): ", TimeValidationStrategy().validate)
        task_name = input("Enter task name: ")
        task_tag = input("Enter task tag: ")

        task_record = TaskRecord(date_of_task, self.start_time_of_task, self.end_time_of_task, task_name, task_tag, self.calculate_time_input())
        self.task_repository.insert_task_record(task_record)
        print("Data successfully inserted into the database.")
    
    def get_valid_input(self, prompt, validation_strategy):
        while True:
            user_input = input(prompt)
            if user_input.lower() == 'today':
                return datetime.datetime.now().strftime('%Y-%m-%d')
            elif validation_strategy(user_input):
                return user_input
            else:
                print(f"Invalid input. {prompt}")

    def calculate_time_input(self):
        # Calculate duration
        start_time = datetime.datetime.strptime(self.start_time_of_task, '%I:%M %p')
        end_time = datetime.datetime.strptime(self.end_time_of_task, '%I:%M %p')
        duration_seconds = (end_time - start_time).seconds
        duration_hours = duration_seconds // 3600
        duration_minutes = (duration_seconds % 3600) // 60

        # Format the duration as HH:MM
        return "{:02}:{:02}".format(duration_hours, duration_minutes)

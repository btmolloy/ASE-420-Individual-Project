import datetime
from src.DatabaseConnectionFactory import DatabaseConnectionFactory
from src.TaskRecordRepositoryFactory import TaskRecordRepositoryFactory
from src.TimeValidationStrategy import TimeValidationStrategy
from src.TaskRecordValidator import TaskRecordValidator
from src.DateValidationStrategy import DateValidationStrategy
from src.TaskRecord import TaskRecord
from src.ReportGenerator import ReportGenerator


class TaskManager:
    def __init__(self):
        self.db_factory = DatabaseConnectionFactory()
        self.task_repository_factory = TaskRecordRepositoryFactory()
        self.task_repository = self.task_repository_factory.create_repository(
            self.db_factory.get_connection(), self.db_factory.get_cursor()
        )
        self.validator = TaskRecordValidator(DateValidationStrategy())

    def record_time(self):
        date_of_task = self.get_valid_input("Enter date (YYYY-MM-DD or today): ", self.validator.validate)
        start_time_of_task = self.get_valid_input("Enter start time (HH:MM AM/PM): ", TimeValidationStrategy().validate)
        end_time_of_task = self.get_valid_input("Enter end time (HH:MM AM/PM): ", TimeValidationStrategy().validate)
        task_name = input("Enter task name: ")
        task_tag = input("Enter task tag: ")

        task_record = TaskRecord(date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag)
        self.task_repository.insert_task_record(task_record)
        print("Data successfully inserted into the database.")

    def search_tasks(self):
        query_options = {
            "1": "date_of_task",
            "2": "start_time_of_task",
            "3": "end_time_of_task",
            "4": "task_name",
            "5": "task_tag",
            "6": "start_time_of_task AND end_time_of_task"
        }

        print("\nSearch options:")
        for key, value in query_options.items():
            print(f"{key}. {value.replace('_', ' ')}")

        choice = input("Enter your choice: ")
        if choice not in query_options:
            print("Invalid choice. Please enter a number between 1 and 6.")
            return

        search_value = input(f"Enter the {query_options[choice].replace('_', ' ')} you want to search for: ")
        results = self.task_repository.search_tasks(query_options[choice], search_value)

        if results:
            print("Search Results:")
            for result in results:
                print(result)
        else:
            print("No results found for the search criteria.")

    def generate_report(self):
        report_generator = ReportGenerator()
        report_generator.generate_report(self.task_repository)

    def exit(self):
        self.db_factory.conn.close()
        print("\n  _____                 _ _                _ \n / ____|               | | |              | |\n| |  __  ___   ___   __| | |__  _   _  ___| |\n| | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ |\n| |__| | (_) | (_) | (_| | |_) | |_| |  __/_|\n \_____|\___/ \___/ \__,_|_.__/ \__, |\___(_)\n                                 __/ |       \n                                |___/        ")
        exit()

    def get_valid_input(self, prompt, validation_strategy):
        while True:
            user_input = input(prompt)
            if user_input.lower() == 'today':
                return datetime.datetime.now().strftime('%Y-%m-%d')
            elif validation_strategy(user_input):
                return user_input
            else:
                print(f"Invalid input. {prompt}")

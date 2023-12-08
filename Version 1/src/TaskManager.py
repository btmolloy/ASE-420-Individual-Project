from src.DatabaseConnectionFactory import DatabaseConnectionFactory
from src.TaskRecordValidator import TaskRecordValidator
from src.TaskRecord import TaskRecord
from src.TaskRecordRepository import TaskRecordRepository

class TaskManager:
    def __init__(self):
        self.db_factory = DatabaseConnectionFactory()
        self.conn = self.db_factory.get_connection()
# CODE SMELL BELOW IT WAS SELF.C
        self.cursor = self.db_factory.get_cursor()
        self.task_repository = TaskRecordRepository(self.conn, self.cursor)
        self.validator = TaskRecordValidator()

    def record_time(self):
        date_of_task = input("Enter date (YYYY-MM-DD or today): ")
        while not (self.validator.verify_date(date_of_task) or date_of_task.lower() == 'today'):
            print("Invalid date format. Please use the format YYYY-MM-DD or 'today'.")
            date_of_task = input("Enter date (YYYY-MM-DD or today): ")

        start_time_of_task = input("Enter start time (HH:MM AM/PM): ")
        while not self.validator.verify_time(start_time_of_task):
            print("Invalid time format. Please use the format HH:MM AM/PM.")
            start_time_of_task = input("Enter start time (HH:MM AM/PM): ")

        end_time_of_task = input("Enter end time (HH:MM AM/PM): ")
        while not self.validator.verify_time(end_time_of_task):
            print("Invalid time format. Please use the format HH:MM AM/PM.")
            end_time_of_task = input("Enter end time (HH:MM AM/PM): ")

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

        print("Search options:")
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

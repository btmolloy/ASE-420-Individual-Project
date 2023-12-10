import datetime
from src.DatabaseConnectionFactory import DatabaseConnectionFactory
from src.TaskRecordRepositoryFactory import TaskRecordRepositoryFactory
from src.ReportGenerator import ReportGenerator
from src.SearchTask import SearchTask
from src.RecordTime import RecordTime

class TaskManager:
    def __init__(self):
        # Initialize the TaskManager with database and repository connections, and report generator
        self.db_factory = DatabaseConnectionFactory()
        self.task_repository_factory = TaskRecordRepositoryFactory()
        self.task_repository = self.task_repository_factory.create_repository(
            self.db_factory.get_connection(), self.db_factory.get_cursor()
        )
        self.report_generator = ReportGenerator()

    def record_time(self):
        # Initialize and execute the RecordTime action
        record_action = RecordTime(self.task_repository)
        record_action.record_time()

    def search_tasks(self):
        # Initialize and execute the SearchTask action
        search_action = SearchTask(self.task_repository)
        search_action.search_tasks()

    def generate_report(self):
        # Execute the ReportGenerator action
        self.report_generator.ReportGenerator(self.task_repository)

    def view_priorities(self):
        # Retrieve and display priority activities from the repository
        priority_activities = self.task_repository.get_priority_activities()
        if priority_activities:
            print("Priority Activities:\n====================\n|  TAG  | DURATION |\n====================")
            for activity in priority_activities:
                print(activity)
        else:
            print("No priority activities found.")

    def exit(self):
        # Close the database connection and exit the application
        self.db_factory.conn.close()
        print("\n  _____                 _ _                _ \n / ____|               | | |              | |\n| |  __  ___   ___   __| | |__  _   _  ___| |\n| | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ |\n| |__| | (_) | (_) | (_| | |_) | |_| |  __/_|\n \_____|\___/ \___/ \__,_|_.__/ \__, |\___(_)\n                                 __/ |       \n                                |___/        ")
        exit(0)

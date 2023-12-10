from src.ReportObserver import ReportObserver

class ReportGenerator:
    def generate_report(self, task_repository):
        observer = ReportObserver()
        task_repository.attach(observer)

        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        task_repository.notify(start_date, end_date)
        task_repository.detach(observer)
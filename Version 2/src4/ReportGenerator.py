class ReportGenerator:
    def generate_report(self, task_repository):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        activities = task_repository.get_activities_in_date_range(start_date, end_date)

        if activities:
            print("Report:")
            for activity in activities:
                print(activity)
        else:
            print("No activities found for the specified date range.")

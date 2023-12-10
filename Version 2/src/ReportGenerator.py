class ReportGenerator:
    def generate_report(self, task_repository):
        # Get user input for start and end dates
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        # Retrieve activities within the specified date range from the task repository
        activities = task_repository.get_activities_in_date_range(start_date, end_date)

        # Display the report if activities are found, otherwise, print a message
        if activities:
            print("Report:\n=======================================================================\n| ID |  DATE  | START TIME | END TIME |   NAME   |  TAG  |  DURATION  |\n=======================================================================")
            for activity in activities:
                print(activity)
        else:
            print("No activities found for the specified date range.")

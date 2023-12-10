class SearchTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository
        self.query_options = {
            "1": "date_of_task",
            "2": "start_time_of_task",
            "3": "end_time_of_task",
            "4": "task_name",
            "5": "task_tag",
        }

    def search_tasks(self):
        print("\nSearch options:")
        for key, value in self.query_options.items():
            print(f"{key}. {value.replace('_', ' ')}")

        choice = input("Enter your choice: ")
        if choice not in self.query_options:
            print("Invalid choice. Please enter a number between 1 and 5.")
            return

        search_value = input(f"Enter the {self.query_options[choice].replace('_', ' ')} you want to search for: ")
        results = self.task_repository.search_tasks(self.query_options[choice], search_value)

        if results:
            print("Search Results:\n=======================================================================\n| ID |  DATE  | START TIME | END TIME |   NAME   |  TAG  |  DURATION  |\n=======================================================================")
            for result in results:
                print(result)
        else:
            print("No results found for the search criteria.")

class SearchTask:
    def __init__(self, task_repository):
        # Initialize with the task repository and query options
        self.task_repository = task_repository
        self.query_options = {
            "1": "Date_of_Task",
            "2": "Start_Time_of_Task",
            "3": "End_Time_of_Task",
            "4": "Task_Name",
            "5": "Task_Tag",
        }

    def search_tasks(self):
        # Display search options to the user
        print("\nSearch options:")
        for key, value in self.query_options.items():
            print(f"{key}. {value.replace('_', ' ')}")

        # Prompt the user to choose a search criterion
        choice = input("Enter your choice: ")
        if choice not in self.query_options:
            print("Invalid choice. Please enter a number between 1 and 5.")
            return

        # Prompt the user to enter the search value
        search_value = input(f"Enter the {self.query_options[choice].replace('_', ' ')} you want to search for: ")
        
        # Retrieve and display the search results
        results = self.task_repository.search_tasks(self.query_options[choice], search_value)
        if results:
            print("Search Results:\n=======================================================================\n| ID |  DATE  | START TIME | END TIME |   NAME   |  TAG  |  DURATION  |\n=======================================================================")
            for result in results:
                print(result)
        else:
            print("No results found for the search criteria.")

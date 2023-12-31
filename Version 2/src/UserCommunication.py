from src.TaskManager import TaskManager

class UserCommunication:
    def __init__(self):
        self.user_choice = None
        self.task_manager = TaskManager()
        self.inputOptions = None

    def applicationLoop(self):
        while True:
            self.printOptions()
            self.user_choice = input("Enter your choice: ")
            self.validateInput()
            selected_option = self.inputOptions.get(self.choice)
            if selected_option:
                selected_option()

    def printOptions(self):
        print("\nChoose one of the following actions.")
        print("1. Record time")
        print("2. Search tasks")
        print("3. Generate report")
        print("4. View Priorities ")
        print("5. Exit")

    def validateInput(self):
        # Validate user input and set the choice attribute
        if self.user_choice in ["1", "2", "3", "4", "5"]:
            self.choice = self.user_choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            self.choice = None

        # Define dictionary mapping user choices to corresponding methods
        self.inputOptions = {
            "1": self.task_manager.record_time,
            "2": self.task_manager.search_tasks,
            "3": self.task_manager.generate_report,
            "4": self.task_manager.view_priorities,
            "5": self.task_manager.exit
        }

from src.TaskManager import TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\nChoose one of the following actions.")
        print("1. Record time")
        print("2. Search tasks")
        print("3. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            task_manager.record_time()
        elif user_choice == "2":
            task_manager.search_tasks()
        elif user_choice == "3":
            task_manager.db_factory.conn.close()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()

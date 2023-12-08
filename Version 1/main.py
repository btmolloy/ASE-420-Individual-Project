import sqlite3
from datetime import datetime

class TimeManagementApp:
    def __init__(self, db_name='tasks.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_of_task DATE,
                start_time_of_task TIME,
                end_time_of_task TIME,
                task_name TEXT,
                task_tag TEXT
            )
        ''')
        self.conn.commit()

    def verify_date(self, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def verify_time(self, time):
        try:
            datetime.strptime(time, '%I:%M %p')
            return True
        except ValueError:
            return False

    def record_time(self):
        date_of_task = input("Enter date (YYYY-MM-DD or today): ")
        while not (self.verify_date(date_of_task) or date_of_task.lower() == 'today'):
            print("Invalid date format. Please use the format YYYY-MM-DD or 'today'.")
            date_of_task = input("Enter date (YYYY-MM-DD or today): ")

        start_time_of_task = input("Enter start time (HH:MM AM/PM): ")
        while not self.verify_time(start_time_of_task):
            print("Invalid time format. Please use the format HH:MM AM/PM.")
            start_time_of_task = input("Enter start time (HH:MM AM/PM): ")

        end_time_of_task = input("Enter end time (HH:MM AM/PM): ")
        while not self.verify_time(end_time_of_task):
            print("Invalid time format. Please use the format HH:MM AM/PM.")
            end_time_of_task = input("Enter end time (HH:MM AM/PM): ")

        task_name = input("Enter task name: ")
        task_tag = input("Enter task tag: ")

        self.c.execute('''
            INSERT INTO tasks (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag)
            VALUES (?, ?, ?, ?, ?)
        ''', (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag))

        self.conn.commit()
        print("Data successfully inserted into the database.")

    def search_tasks(self):
        print("Search options:")
        print("1. Date")
        print("2. Start Time")
        print("3. End Time")
        print("4. Task Name")
        print("5. Task Tag")
        print("6. Time Range (Start Time to End Time)")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_date = input("Enter the date you want to search for (YYYY-MM-DD): ")
            while not self.verify_date(search_date):
                print("Invalid date format. Please use the format YYYY-MM-DD.")
                search_date = input("Enter the date you want to search for (YYYY-MM-DD): ")

            cursor = self.c.execute('''
                SELECT * FROM tasks WHERE date_of_task = ?
            ''', (search_date,))
        elif choice == "2":
            search_start_time = input("Enter the start time you want to search for (HH:MM AM/PM): ")
            while not self.verify_time(search_start_time):
                print("Invalid time format. Please use the format HH:MM AM/PM.")
                search_start_time = input("Enter the start time you want to search for (HH:MM AM/PM): ")

            cursor = self.c.execute('''
                SELECT * FROM tasks WHERE start_time_of_task = ?
            ''', (search_start_time,))
        elif choice == "3":
            search_end_time = input("Enter the end time you want to search for (HH:MM AM/PM): ")
            while not self.verify_time(search_end_time):
                print("Invalid time format. Please use the format HH:MM AM/PM.")
                search_end_time = input("Enter the end time you want to search for (HH:MM AM/PM): ")

            cursor = self.c.execute('''
                SELECT * FROM tasks WHERE end_time_of_task = ?
            ''', (search_end_time,))
        elif choice == "4":
            search_task_name = input("Enter the task name you want to search for: ")

            cursor = self.c.execute('''
                SELECT * FROM tasks WHERE task_name = ?
            ''', (search_task_name,))
        elif choice == "5":
            search_task_tag = input("Enter the task tag you want to search for: ")

            cursor = self.c.execute('''
                SELECT * FROM tasks WHERE task_tag = ?
            ''', (search_task_tag,))
        elif choice == "6":
            search_start_time = input("Enter the start time you want to search for (HH:MM AM/PM): ")
            while not self.verify_time(search_start_time):
                print("Invalid time format. Please use the format HH:MM AM/PM.")
                search_start_time = input("Enter the start time you want to search for (HH:MM AM/PM): ")

            search_end_time = input("Enter the end time you want to search for (HH:MM AM/PM): ")
            while not self.verify_time(search_end_time):
                print("Invalid time format. Please use the format HH:MM AM/PM.")
                search_end_time = input("Enter the end time you want to search for (HH:MM AM/PM): ")

            cursor = self.c.execute('''
                SELECT * FROM tasks WHERE start_time_of_task = ? AND end_time_of_task = ?
            ''', (search_start_time, search_end_time))
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            return

        # Fetch and print the search results
        search_results = cursor.fetchall()

        if search_results:
            print("Search Results:")
            for result in search_results:
                print(result)
        else:
            print("No results found for the search criteria.")

    def close_connection(self):
        self.conn.close()

# Example usage with user inputs:
app = TimeManagementApp()

while True:
    print("\nChoose one of the following actions.")
    print("1. Record time")
    print("2. Search tasks")
    print("3. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        app.record_time()
    elif user_choice == "2":
        app.search_tasks()
    elif user_choice == "3":
        app.close_connection()
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

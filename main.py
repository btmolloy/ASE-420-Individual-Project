import sqlite3
from datetime import datetime

class TimeUsageManager:
    def __init__(self, db_name='time_usage.db'):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        # Establish a connection and create a table if it doesn't exist
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS time_usage (
                id INTEGER PRIMARY KEY,
                date TEXT,
                start_time TEXT,
                end_time TEXT,
                task TEXT,
                tag TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def record_time(self, date, start_time, end_time, task, tag):
        # Record time usage into the database
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO time_usage (date, start_time, end_time, task, tag)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, start_time, end_time, task, tag))
        conn.commit()
        conn.close()

    def query_time(self, query):
        # Query time usage based on provided criteria
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM time_usage WHERE date = ? OR task = ? OR tag = ?', (query, query, query))
        rows = cursor.fetchall()
        conn.close()
        return rows

if __name__ == "__main__":
    # Initialize the TimeUsageManager
    time_manager = TimeUsageManager()

    # Continuous loop to listen for user input
    while True:
        user_input = input("Enter a command or 'quit' to exit: ").strip().lower()

        # Check if user wants to exit the program
        if user_input == 'quit':
            print("Exiting the program...")
            break

        parts = user_input.split()

        # Record time if command is 'record' and input format is correct
        if parts[0] == 'record' and len(parts) == 6:
            date, start_time, end_time, task, tag = parts[1], parts[2], parts[3], parts[4], parts[5]
            time_manager.record_time(date, start_time, end_time, task, tag)
            print('Time usage recorded successfully!')

        # Query time usage if command is 'query' and input format is correct
        elif parts[0] == 'query' and len(parts) == 2:
            query = parts[1]
            result = time_manager.query_time(query)
            if result:
                print('Time usage:')
                for row in result:
                    print(row)
            else:
                print('No records found for the query.')

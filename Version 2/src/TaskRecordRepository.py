import datetime

class TaskRecordRepository:
    def __init__(self, connection, cursor):
        # Initialize TaskRecordRepository with database connection and cursor
        self.conn = connection
        self.cursor = cursor
        # Create the tasks table if it doesn't exist
        self.create_table()

    def create_table(self):
        # Create the tasks table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_of_task DATE,
                start_time_of_task TIME,
                end_time_of_task TIME,
                task_name TEXT,
                task_tag TEXT,
                duration INTEGER  
            )
        ''')
        # Commit changes to the database
        self.conn.commit()

    def insert_task_record(self, task_record):
        # Insert a task record into the tasks table
        self.cursor.execute('''
            INSERT INTO tasks (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag, duration)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (task_record.date_of_task, task_record.start_time_of_task,
              task_record.end_time_of_task, task_record.task_name, task_record.task_tag, task_record.duration))
        # Commit changes to the database
        self.conn.commit()

    def search_tasks(self, query, value):
        # Search for tasks based on a specific query and value
        self.cursor.execute(f'''
            SELECT * FROM tasks WHERE {query} = ?
        ''', (value,))
        return self.cursor.fetchall()

    def get_activities_in_date_range(self, start_date, end_date):
        # Get tasks within a specified date range
        self.cursor.execute('''
            SELECT * FROM tasks WHERE date_of_task BETWEEN ? AND ?
        ''', (start_date, end_date))
        return self.cursor.fetchall()
    
    def get_priority_activities(self):
        # Get priority activities and their total durations
        self.cursor.execute('''
            SELECT task_tag, 
                   COALESCE(SUM(
                       CAST(SUBSTR(duration, 1, 2) AS INTEGER) * 3600 + 
                       CAST(SUBSTR(duration, 4, 2) AS INTEGER) * 60
                   ), 0) AS total_duration
            FROM tasks
            GROUP BY task_tag
            ORDER BY total_duration DESC
        ''')

        results = self.cursor.fetchall()
        formatted_results = []

        for tag, total_duration_seconds in results:
            # Convert total duration to a formatted HH:MM string
            total_duration_timedelta = datetime.timedelta(seconds=total_duration_seconds)
            formatted_duration = "{:02}:{:02}".format(total_duration_timedelta.days * 24 + total_duration_timedelta.seconds // 3600, (total_duration_timedelta.seconds % 3600) // 60)

            formatted_results.append((tag, formatted_duration))

        return formatted_results

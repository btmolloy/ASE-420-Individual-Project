from src.Observable import Observable

class TaskRecordRepository(Observable):
    def __init__(self, connection, cursor):
        super().__init__()
        self.conn = connection
        self.cursor = cursor
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
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

    def insert_task_record(self, task_record):
        self.cursor.execute('''
            INSERT INTO tasks (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag)
            VALUES (?, ?, ?, ?, ?)
        ''', (task_record.date_of_task, task_record.start_time_of_task,
              task_record.end_time_of_task, task_record.task_name, task_record.task_tag))
        self.conn.commit()
        self.notify_observers()

    def search_tasks(self, query, value):
        self.cursor.execute(f'''
            SELECT * FROM tasks WHERE {query} = ?
        ''', (value,))
        return self.cursor.fetchall()

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.get_activities_in_date_range("0001-01-01", "9999-12-31"))

    def get_activities_in_date_range(self, start_date, end_date):
        self.cursor.execute('''
            SELECT * FROM tasks WHERE date_of_task BETWEEN ? AND ?
        ''', (start_date, end_date))
        return self.cursor.fetchall()

    def get_priority_activities(self):
        self.cursor.execute('''
            SELECT task_name, SUM((julianday(end_time_of_task) - julianday(start_time_of_task)) * 24 * 60) as total_minutes
            FROM tasks
            GROUP BY task_name
            ORDER BY total_minutes DESC
            LIMIT 5
        ''')
        return self.cursor.fetchall()
    
    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)
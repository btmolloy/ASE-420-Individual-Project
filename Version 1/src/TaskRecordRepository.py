class TaskRecordRepository:
    def __init__(self, connection, cursor):
        self.conn = connection
        self.c = cursor
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

    def insert_task_record(self, task_record):
        self.c.execute('''
            INSERT INTO tasks (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag)
            VALUES (?, ?, ?, ?, ?)
        ''', (task_record.date_of_task, task_record.start_time_of_task,
              task_record.end_time_of_task, task_record.task_name, task_record.task_tag))
        self.conn.commit()

    def search_tasks(self, query, value):
        self.c.execute(f'''
            SELECT * FROM tasks WHERE {query} = ?
        ''', (value,))
        return self.c.fetchall()

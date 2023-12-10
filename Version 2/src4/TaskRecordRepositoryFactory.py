from src.TaskRecordRepository import TaskRecordRepository

# Factory Pattern for Task Record Repository
class TaskRecordRepositoryFactory:
    def create_repository(self, connection, cursor):
        return TaskRecordRepository(connection, cursor)
from src.TaskRecordRepository import TaskRecordRepository

# Factory Pattern for Task Record Repository
class TaskRecordRepositoryFactory:
    def create_repository(self, connection, cursor):
        # Create and return an instance of TaskRecordRepository
        return TaskRecordRepository(connection, cursor)

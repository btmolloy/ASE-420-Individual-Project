import pytest
from unittest.mock import MagicMock
from src.TaskRecordRepositoryFactory import TaskRecordRepositoryFactory
from src.TaskRecordRepository import TaskRecordRepository

@pytest.fixture
def connection():
    # You can provide a mock or MagicMock for the connection
    return MagicMock()

@pytest.fixture
def cursor():
    # You can provide a mock or MagicMock for the cursor
    return MagicMock()

def test_create_repository_returns_instance(connection, cursor):
    # Arrange
    factory = TaskRecordRepositoryFactory()

    # Act
    repository = factory.create_repository(connection, cursor)

    # Assert
    assert isinstance(repository, TaskRecordRepository)

if __name__ == "__main__":
    pytest.main()

# test_task_record.py

from src.TaskRecord import TaskRecord  

def test_task_record_initialization():
    # Test data
    date_of_task = "2023-12-08"
    start_time_of_task = "10:00 AM"
    end_time_of_task = "12:00 PM"
    task_name = "Test Task"
    task_tag = "Work"

    # Create a TaskRecord instance
    task_record = TaskRecord(date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag)

    # Check if attributes are set correctly
    assert task_record.date_of_task == date_of_task
    assert task_record.start_time_of_task == start_time_of_task
    assert task_record.end_time_of_task == end_time_of_task
    assert task_record.task_name == task_name
    assert task_record.task_tag == task_tag


import unittest
from src.TaskRecord import TaskRecord

class TestTaskRecord(unittest.TestCase):
    def test_task_record_initialization(self):
        # Define sample values
        date_of_task = '2023-01-01'
        start_time_of_task = '09:00 AM'
        end_time_of_task = '05:00 PM'
        task_name = 'Sample Task'
        task_tag = 'Tag1'
        duration = '08:00'

        # Create an instance of TaskRecord
        task_record = TaskRecord(date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag, duration)

        # Assert that the attributes are initialized correctly
        self.assertEqual(task_record.date_of_task, date_of_task)
        self.assertEqual(task_record.start_time_of_task, start_time_of_task)
        self.assertEqual(task_record.end_time_of_task, end_time_of_task)
        self.assertEqual(task_record.task_name, task_name)
        self.assertEqual(task_record.task_tag, task_tag)
        self.assertEqual(task_record.duration, duration)

if __name__ == '__main__':
    unittest.main()

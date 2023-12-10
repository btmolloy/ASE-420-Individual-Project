import unittest
from unittest.mock import patch, call
from src.UserCommunication import UserCommunication

class TestUserCommunication(unittest.TestCase):
    def test_validate_input_valid_choice(self):
        user_communication = UserCommunication()
        user_communication.user_choice = "1"
        user_communication.validateInput()
        self.assertEqual(user_communication.choice, user_communication.user_choice)

    def test_validate_input_invalid_choice(self):
        user_communication = UserCommunication()
        user_communication.user_choice = "6"
        with patch("builtins.input", return_value=user_communication.user_choice):
            user_communication.validateInput()
        self.assertIsNone(user_communication.choice)

    def test_print_options(self):
        user_communication = UserCommunication()
        with patch("builtins.print") as mock_print:
            user_communication.printOptions()
            expected_calls = [
                call("\nChoose one of the following actions."),
                call("1. Record time"),
                call("2. Search tasks"),
                call("3. Generate report"),
                call("4. View Priorities "),
                call("5. Exit"),
            ]
            mock_print.assert_has_calls(expected_calls, any_order=False)

 
    def test_application_loop_exit(self):
        # Arrange
        user_communication = UserCommunication()
        user_communication.user_choice = "5"  # Exit option

        # Act
        with patch("builtins.input", side_effect=[user_communication.user_choice]), \
                patch("src.TaskManager.TaskManager.exit", side_effect=SystemExit(0)):
            try:
                user_communication.applicationLoop()
            except (SystemExit, KeyboardInterrupt) as e:
                assert str(e) == "0"  # SystemExit code for a successful exit

        # Assert
        assert user_communication.choice == user_communication.user_choice

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
import io
from src.calculator.main import main


class TestMain(unittest.TestCase):

    @patch("builtins.input", return_value="5+3")
    def test_main_valid_expression(self, mock_input):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            main()
            self.assertEqual(fake_stdout.getvalue().strip(), "Result: 8")

    @patch("builtins.input", return_value="10-2*3")
    def test_main_valid_expression_order_of_operations(self, mock_input):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            main()
            self.assertEqual(fake_stdout.getvalue().strip(), "Result: 4")

    @patch("builtins.input", return_value="1+*2")
    def test_main_invalid_expression(self, mock_input):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            main()
            self.assertTrue(
                "Error: Invalid characters in expression"
                in fake_stdout.getvalue().strip()
            )

    @patch("builtins.input", return_value="5/0")
    def test_main_division_by_zero(self, mock_input):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            main()
            self.assertEqual(fake_stdout.getvalue().strip(), "Error: Division by zero")

    @patch("builtins.input", return_value="")
    def test_main_empty_expression(self, mock_input):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            main()
            self.assertEqual(fake_stdout.getvalue().strip(), "Error: Empty expression")


if __name__ == "__main__":
    unittest.main()


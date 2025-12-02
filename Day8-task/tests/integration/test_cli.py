import unittest
import subprocess
import sys


class TestCliIntegration(unittest.TestCase):

    def run_cli_command(self, expression):
        process = subprocess.run(
            [sys.executable, "src/calculator/main.py"],
            input=expression,  # Pass the expression as stdin
            capture_output=True,
            text=True,  # Decode stdout/stderr as text
            check=False,  # Do not raise an exception for non-zero exit codes
        )
        return process.stdout.strip(), process.stderr.strip(), process.returncode

    def test_valid_addition(self):
        stdout, stderr, returncode = self.run_cli_command("5+3")
        self.assertEqual(stdout, "Result: 8.0")
        self.assertEqual(stderr, "")
        self.assertEqual(returncode, 0)

    def test_valid_subtraction(self):
        stdout, stderr, returncode = self.run_cli_command("10-2")
        self.assertEqual(stdout, "Result: 8.0")
        self.assertEqual(stderr, "")
        self.assertEqual(returncode, 0)

    def test_valid_multiplication(self):
        stdout, stderr, returncode = self.run_cli_command("7*6")
        self.assertEqual(stdout, "Result: 42.0")
        self.assertEqual(stderr, "")
        self.assertEqual(returncode, 0)

    def test_valid_division(self):
        stdout, stderr, returncode = self.run_cli_command("12/4")
        self.assertEqual(stdout, "Result: 3.0")
        self.assertEqual(stderr, "")
        self.assertEqual(returncode, 0)

    def test_valid_order_of_operations(self):
        stdout, stderr, returncode = self.run_cli_command("10-2*3")
        self.assertEqual(stdout, "Result: 4.0")
        self.assertEqual(stderr, "")
        self.assertEqual(returncode, 0)

    def test_valid_parentheses(self):
        stdout, stderr, returncode = self.run_cli_command("(1+2)*3")
        self.assertEqual(stdout, "Result: 9.0")
        self.assertEqual(stderr, "")
        self.assertEqual(returncode, 0)

    def test_division_by_zero(self):
        stdout, stderr, returncode = self.run_cli_command("5/0")
        self.assertEqual(stdout, "Error: Division by zero")
        self.assertEqual(stderr, "")
        self.assertNotEqual(returncode, 0)  # Expect a non-zero exit code for errors

    def test_invalid_expression_characters(self):
        stdout, stderr, returncode = self.run_cli_command("1$2")
        self.assertTrue("Error: Invalid characters in expression" in stdout)
        self.assertEqual(stderr, "")
        self.assertNotEqual(returncode, 0)

    def test_invalid_expression_mismatched_parentheses(self):
        stdout, stderr, returncode = self.run_cli_command("(1+2")
        self.assertTrue("Error: Mismatched parentheses" in stdout)
        self.assertEqual(stderr, "")
        self.assertNotEqual(returncode, 0)

    def test_empty_expression(self):
        stdout, stderr, returncode = self.run_cli_command("")
        self.assertTrue("Error: Empty expression" in stdout)
        self.assertEqual(stderr, "")
        self.assertNotEqual(returncode, 0)


if __name__ == "__main__":
    unittest.main()

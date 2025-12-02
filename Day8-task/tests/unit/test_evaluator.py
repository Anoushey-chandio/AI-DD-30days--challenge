import unittest
from src.calculator.evaluator import evaluate_postfix, EvaluatorError


class TestEvaluator(unittest.TestCase):

    def test_evaluate_valid_postfix_expressions(self):
        self.assertEqual(evaluate_postfix(["1", "2", "+"]), 3.0)
        self.assertEqual(evaluate_postfix(["1", "2", "3", "*", "+"]), 7.0)
        self.assertEqual(evaluate_postfix(["10", "2", "2", "/", "-"]), 9.0)
        self.assertEqual(evaluate_postfix(["5", "3", "-", "2", "*", "4", "/"]), 1.0)

    def test_evaluate_division_by_zero(self):
        with self.assertRaises(EvaluatorError) as cm:
            evaluate_postfix(["5", "0", "/"])
        self.assertEqual(str(cm.exception), "Division by zero")

    def test_evaluate_invalid_expression_not_enough_operands(self):
        with self.assertRaises(EvaluatorError) as cm:
            evaluate_postfix(["+", "1", "2"])
        self.assertEqual(
            str(cm.exception), "Invalid expression: not enough operands for operator"
        )

        with self.assertRaises(EvaluatorError) as cm:
            evaluate_postfix(["1", "+"])
        self.assertEqual(
            str(cm.exception), "Invalid expression: not enough operands for operator"
        )

    def test_evaluate_invalid_expression_too_many_operands(self):
        with self.assertRaises(EvaluatorError) as cm:
            evaluate_postfix(["1", "2", "3", "+"])
        self.assertEqual(str(cm.exception), "Invalid expression")

    def test_evaluate_unknown_token(self):
        with self.assertRaises(EvaluatorError) as cm:
            evaluate_postfix(["1", "2", "$"])
        self.assertEqual(str(cm.exception), "Unknown token: $")


if __name__ == "__main__":
    unittest.main()

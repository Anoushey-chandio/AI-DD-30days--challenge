import unittest
from src.calculator.parser import parse, ParserError, tokenize


class TestParser(unittest.TestCase):

    def test_tokenize_valid_expression(self):
        self.assertEqual(
            tokenize("1+2-3*4/5"), ["1", "+", "2", "-", "3", "*", "4", "/", "5"]
        )
        self.assertEqual(tokenize("(1+2)*3"), ["(", "1", "+", "2", ")", "*", "3"])

    def test_tokenize_invalid_characters(self):
        with self.assertRaises(ParserError):
            tokenize("1$2")
        with self.assertRaises(ParserError):
            tokenize("1_2")

    def test_parse_valid_expressions(self):
        self.assertEqual(parse("1+2"), ["1", "2", "+"])
        self.assertEqual(parse("1+2*3"), ["1", "2", "3", "*", "+"])
        self.assertEqual(parse("(1+2)*3"), ["1", "2", "+", "3", "*"])
        self.assertEqual(parse("10-2/2"), ["10", "2", "2", "/", "-"])
        self.assertEqual(parse(" (1 + 2) * 3 "), ["1", "2", "+", "3", "*"])

    def test_parse_empty_expression(self):
        with self.assertRaises(ParserError) as cm:
            parse("")
        self.assertEqual(str(cm.exception), "Empty expression")

    def test_parse_mismatched_parentheses(self):
        with self.assertRaises(ParserError) as cm:
            parse("(1+2")
        self.assertEqual(str(cm.exception), "Mismatched parentheses")

        with self.assertRaises(ParserError) as cm:
            parse("1+2)")
        self.assertEqual(str(cm.exception), "Mismatched parentheses")

    def test_parse_invalid_tokens(self):
        # This case is primarily handled by tokenize, but ensure parse also fails if somehow an invalid token got through
        with self.assertRaises(ParserError):
            parse("1 2")


if __name__ == "__main__":
    unittest.main()

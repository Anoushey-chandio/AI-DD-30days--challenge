"""
main.py
---------

This module provides the command-line interface for the Basic Calculator.
It takes an arithmetic expression as input, parses it, evaluates it, and prints the result.
"""
import sys
from src.calculator.parser import parse, ParserError
from src.calculator.evaluator import evaluate_postfix, EvaluatorError

def main():
    """
    Main function to run the calculator CLI.
    Prompts the user for an expression, evaluates it, and prints the result or an error.
    """
    try:
        expression = input("Enter expression: ")
        if not expression.strip():  # Handle empty or whitespace-only input
            raise ParserError("Empty expression")

        postfix_expression = parse(expression)
        result = evaluate_postfix(postfix_expression)

        # ✅ Integer check: if result is whole number, print without .0
        if isinstance(result, (float, int)) and float(result).is_integer():
            print(f"Result: {int(result)}")
        else:
            print(f"Result: {result}")

    except (ParserError, EvaluatorError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

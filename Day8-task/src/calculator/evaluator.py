"""
evaluator.py
------------

This module provides a function for evaluating arithmetic expressions in postfix (Reverse Polish Notation).
"""


class EvaluatorError(Exception):
    """Custom exception for evaluator-related errors."""

    pass


def evaluate_postfix(postfix_expression):
    """
    Evaluates an arithmetic expression given in postfix (Reverse Polish Notation).

    Args:
        postfix_expression (list): A list of tokens in postfix notation.

    Returns:
        float: The numerical result of the evaluated expression.

    Raises:
        EvaluatorError: For invalid expressions (e.g., not enough operands,
                        too many operands) or division by zero.
    """
    stack = []

    for token in postfix_expression:
        if token.isdigit():
            # If the token is a number, push it to the stack
            stack.append(float(token))
        elif token in "+-*/":
            # If the token is an operator, pop two operands, perform the operation,
            # and push the result back onto the stack.
            if len(stack) < 2:
                raise EvaluatorError(
                    "Invalid expression: not enough operands for operator"
                )
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                if operand2 == 0:
                    raise EvaluatorError("Division by zero")
                stack.append(operand1 / operand2)
        else:
            # Should not happen if parser works correctly, but as a safeguard
            raise EvaluatorError(f"Unknown token: {token}")

    if len(stack) != 1:
        # If there's not exactly one element left, the expression was invalid
        raise EvaluatorError("Invalid expression")

    return stack.pop()

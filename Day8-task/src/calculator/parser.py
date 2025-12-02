"""
parser.py
---------

This module provides functions for tokenizing and parsing arithmetic expressions.
It converts infix expressions into postfix (Reverse Polish Notation) using the Shunting-yard algorithm.
"""

import re


class ParserError(Exception):
    """Custom exception for parser-related errors."""

    pass


def tokenize(expression):
    """
    Tokenizes a given arithmetic expression string into a list of tokens.

    Valid tokens include numbers (integers), operators (+, -, *, /),
    and parentheses.

    Args:
        expression (str): The input arithmetic expression string.

    Returns:
        list: A list of tokens (strings).

    Raises:
        ParserError: If the expression contains invalid characters.
    """
    # Use regular expression to find all numbers, operators, and parentheses
    tokens = re.findall(r"\d+|\+|\-|\*|\/|\(|\)", expression)
    # Validate that all found tokens are indeed valid
    if not all(re.fullmatch(r"\d+|\+|\-|\*|\/|\(|\)", token) for token in tokens):
        raise ParserError("Invalid characters in expression")
    return tokens


def parse(expression):
    """
    Parses an arithmetic expression from infix notation to postfix (Reverse Polish Notation).

    This function uses the Shunting-yard algorithm. It handles basic arithmetic
    operators (+, -, *, /) and parentheses, respecting standard operator precedence.

    Args:
        expression (str): The infix arithmetic expression string.

    Returns:
        list: A list of tokens in postfix notation.

    Raises:
        ParserError: For empty expressions, invalid tokens, or mismatched parentheses.
    """
    tokens = tokenize(expression)
    if not tokens:
        raise ParserError("Empty expression")

    output_queue = []
    operator_stack = []
    # Define operator precedence
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    for token in tokens:
        if re.fullmatch(r"\d+", token):
            # If the token is a number, add it to the output queue
            output_queue.append(token)
        elif token in "+-*/":
            # If the token is an operator, pop operators from the stack
            # to the output queue based on precedence
            while (
                operator_stack
                and operator_stack[-1] != "("
                and precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)
            ):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            # If it's a left parenthesis, push it to the operator stack
            operator_stack.append(token)
        elif token == ")":
            # If it's a right parenthesis, pop operators until a left parenthesis is found
            while operator_stack and operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())
            if not operator_stack:
                raise ParserError("Mismatched parentheses")
            operator_stack.pop()  # Pop the '(' from the stack
        else:
            # Should ideally be caught by tokenize, but as a safeguard
            raise ParserError(f"Unknown token: {token}")

    # Pop any remaining operators from the stack to the output queue
    while operator_stack:
        if operator_stack[-1] == "(":
            raise ParserError("Mismatched parentheses")  # Mismatched parentheses
        output_queue.append(operator_stack.pop())

    if not output_queue:
        raise ParserError("Empty expression after parsing")

    return output_queue

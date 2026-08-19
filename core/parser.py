"""Tokenize and evaluate calculator expressions using Decimal arithmetic."""

from decimal import Decimal, InvalidOperation

from .exceptions import CalculatorError, DivisionByZeroError, InvalidExpressionError


class ExpressionParser:
    """Evaluate basic arithmetic expressions with standard operator precedence."""

    OPERATORS = {
        "+": (1, lambda left, right: left + right),
        "-": (1, lambda left, right: left - right),
        "*": (2, lambda left, right: left * right),
        "/": (2, lambda left, right: left / right),
        "%": (2, lambda left, right: left % right),
    }

    def evaluate(self, expression: str) -> Decimal:
        """Return the Decimal result for a valid non-empty expression."""
        if not expression:
            raise InvalidExpressionError("Enter an expression first.")

        try:
            return self._compute(self._tokenize(expression))
        except CalculatorError:
            raise
        except (IndexError, InvalidOperation, ValueError) as error:
            raise InvalidExpressionError("Invalid expression.") from error

    def _tokenize(self, expression: str) -> list[Decimal | str]:
        tokens: list[Decimal | str] = []
        index = 0
        expecting_number = True

        while index < len(expression):
            if expecting_number:
                sign = Decimal("-1") if expression[index] == "-" else Decimal("1")
                if expression[index] == "-":
                    index += 1

                number_start = index
                decimal_points = 0
                while index < len(expression) and (
                    expression[index].isdigit() or expression[index] == "."
                ):
                    if expression[index] == ".":
                        decimal_points += 1
                    index += 1

                number = expression[number_start:index]
                if not number or number == "." or decimal_points > 1:
                    raise InvalidExpressionError("Invalid expression.")

                tokens.append(sign * Decimal(number))
                expecting_number = False
                continue

            operator = expression[index]
            if operator not in self.OPERATORS:
                raise InvalidExpressionError("Invalid expression.")

            tokens.append(operator)
            index += 1
            expecting_number = True

        if expecting_number:
            raise InvalidExpressionError("Invalid expression.")

        return tokens

    def _compute(self, tokens: list[Decimal | str]) -> Decimal:
        """Evaluate multiplication-level operators before addition-level operators."""
        working_tokens = tokens[:]
        index = 0

        while index < len(working_tokens):
            token = working_tokens[index]
            if token in ("*", "/", "%"):
                operator = str(token)
                left = working_tokens[index - 1]
                right = working_tokens[index + 1]

                if not isinstance(left, Decimal) or not isinstance(right, Decimal):
                    raise InvalidExpressionError("Invalid expression.")

                if operator in ("/", "%") and right == Decimal("0"):
                    raise DivisionByZeroError("Cannot divide by zero.")

                result = self.OPERATORS[operator][1](left, right)
                working_tokens[index - 1:index + 2] = [result]
                index = 0
                continue

            index += 1

        result = working_tokens[0]
        if not isinstance(result, Decimal):
            raise InvalidExpressionError("Invalid expression.")

        index = 1
        while index < len(working_tokens):
            operator = working_tokens[index]
            next_number = working_tokens[index + 1]
            if not isinstance(operator, str) or not isinstance(next_number, Decimal):
                raise InvalidExpressionError("Invalid expression.")

            result = self.OPERATORS[operator][1](result, next_number)
            index += 2

        return result

from .exceptions import InvalidExpressionError, DivisionByZeroError, CalculatorError

"""Define expression parser (Expression evaluations)"""
class ExpressionParser:

    '''Define calculator operators'''
    OPERATORS = {
        "+": (1, lambda a, b: a + b),
        "-": (1, lambda a, b: a - b),
        "*": (2, lambda a, b: a * b),
        "/": (2, lambda a, b: a / b),
        "%": (2, lambda a, b: a % b),
    }

    '''Evaluate the expression'''
    def evaluate(self, expression: str) -> float:

        if not expression:
            return ""

        try:
            tokens = self._tokenize(expression)
            return self._compute(tokens)

        except CalculatorError:
            raise

        except Exception:
            raise InvalidExpressionError("Invalid expression.")

    # Tokenize the expression
    def _tokenize(self, expression: str):
        number = ""
        tokens = []

        for char in expression:
            if char.isdigit() or char == ".":
                number += char

            elif char in self.OPERATORS:
                if number:
                    tokens.append(float(number))
                    number = ""
                tokens.append(char)

            else:
                raise InvalidExpressionError("Invalid expression.")

        if number:
            tokens.append(float(number))

        return tokens

    # Compute the expression
    def _compute(self, tokens):

        # Handle *, /, %
        i = 0
        while i < len(tokens):

            if tokens[i] in ("*", "/", "%"):
                op = tokens[i]
                left = tokens[i - 1]
                right = tokens[i + 1]

                if op == "/" and right == 0:
                    raise DivisionByZeroError("Cannot divide by zero.")

                result = self.OPERATORS[op][1](left, right)

                tokens[i - 1:i + 2] = [result]

                i = 0
                continue

            i += 1

        # Handle + and -
        result = tokens[0]
        i = 1

        while i < len(tokens):
            op = tokens[i]
            next_num = tokens[i + 1]

            result = self.OPERATORS[op][1](result, next_num)

            i += 2

        return result
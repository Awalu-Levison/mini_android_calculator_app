"""Stateful calculator input handling independent of the Kivy UI."""

from decimal import Decimal, InvalidOperation

from .exceptions import CalculatorError, ExpressionTooLongError, InvalidExpressionError
from .parser import ExpressionParser


class CalculatorEngine:
    """Manage calculator input, expression state, display state, and evaluation."""

    BACKSPACE = "\u232B"
    CLEAR = "C"
    EQUALS = "="
    PERCENT = "%"
    SIGN_TOGGLE = "+/-"
    DIGITS = "0123456789"
    OPERATORS = "+-*/"
    MAX_EXPRESSION_LENGTH = 100

    def __init__(self, max_expression_length: int | None = None):
        self.max_expression_length = (
            max_expression_length or self.MAX_EXPRESSION_LENGTH
        )
        self.expression = ""
        self.display = "0"
        self.last_error: str | None = None
        self.just_evaluated = False
        self.parser = ExpressionParser()

    def press(self, value: str) -> str:
        """Process a keypad value and return the display text for the UI."""
        if value == self.CLEAR:
            self.clear()
        elif value == self.BACKSPACE:
            self.backspace()
        elif value == self.EQUALS:
            self.evaluate()
        elif value == self.SIGN_TOGGLE:
            self.toggle_sign()
        elif value == self.PERCENT:
            self.percentage()
        elif value in self.DIGITS:
            self.append_digit(value)
        elif value == ".":
            self.append_decimal()
        elif value in self.OPERATORS:
            self.append_operator(value)
        else:
            self._set_error(InvalidExpressionError("Unsupported calculator input."))

        return self.display

    def append(self, value: str) -> str:
        """Backward-compatible alias for keypad input processing."""
        return self.press(value)

    def clear(self) -> None:
        self.expression = ""
        self.display = "0"
        self.last_error = None
        self.just_evaluated = False

    def backspace(self) -> None:
        if self.expression:
            self.expression = self.expression[:-1]
        self._show_expression()

    def append_digit(self, value: str) -> None:
        if self.just_evaluated:
            self.clear()
        self._append_to_expression(value)

    def append_decimal(self) -> None:
        if self.just_evaluated:
            self.clear()

        current_number = self._current_number()
        if "." in current_number:
            self._set_error(InvalidExpressionError("A number can contain only one decimal point."))
            return

        if current_number == "-":
            self._append_to_expression("0.")
        elif current_number:
            self._append_to_expression(".")
        else:
            self._append_to_expression("0.")

    def append_operator(self, operator: str) -> None:
        if not self.expression:
            if operator == "-":
                self._append_to_expression(operator)
            else:
                self._set_error(InvalidExpressionError("Enter a number before an operator."))
            return

        if self.expression[-1] in self.OPERATORS:
            self._set_error(InvalidExpressionError("Enter a number before another operator."))
            return

        self._append_to_expression(operator)

    def toggle_sign(self) -> None:
        """Toggle the sign of the current number, including after an operator."""
        if not self.expression:
            self._append_to_expression("-")
            return

        number_start = self._current_number_start()
        if number_start < len(self.expression):
            if self.expression[number_start] == "-":
                self.expression = (
                    self.expression[:number_start]
                    + self.expression[number_start + 1:]
                )
            elif self._has_space_for(1):
                self.expression = (
                    self.expression[:number_start]
                    + "-"
                    + self.expression[number_start:]
                )
            else:
                return
            self._show_expression()
            return

        if self.expression.endswith("-") and self._is_unary_minus(len(self.expression) - 1):
            self.expression = self.expression[:-1]
            self._show_expression()
        else:
            self._append_to_expression("-")

    def percentage(self) -> None:
        """Replace the current number with that number divided by one hundred."""
        number_start = self._current_number_start()
        number = self.expression[number_start:]
        if not number or number == "-":
            self._set_error(InvalidExpressionError("Enter a number before applying percentage."))
            return

        # Evaluate percentage value on valid number
        try:
            percentage_value = Decimal(number) / Decimal("100")
        except InvalidOperation as error:
            self._set_error(InvalidExpressionError("Invalid expression."))
            return

        replacement = self.format_decimal(percentage_value)
        updated_expression = self.expression[:number_start] + replacement
        if len(updated_expression) > self.max_expression_length:
            self._set_error(
                ExpressionTooLongError(
                    f"Expression is limited to {self.max_expression_length} characters."
                )
            )
            return

        self.expression = updated_expression
        self._show_expression()

    def evaluate(self) -> str:
        if not self.expression:
            self.display = "0"
            return self.display

        try:
            result = self.parser.evaluate(self.expression)
        except CalculatorError as error:
            self._set_error(error)
            return self.display

        self.expression = self.format_decimal(result)
        self.display = self.expression
        self.last_error = None
        self.just_evaluated = True
        return self.display

    @staticmethod
    def format_decimal(value: Decimal) -> str:
        """Format Decimal output without exponent notation or redundant zeros."""
        formatted = format(value, "f")
        if "." in formatted:
            formatted = formatted.rstrip("0").rstrip(".")
        return "0" if formatted in ("", "-0") else formatted

    def _append_to_expression(self, value: str) -> bool:
        if not self._has_space_for(len(value)):
            return False
        self.expression += value
        self._show_expression()
        return True

    def _has_space_for(self, character_count: int) -> bool:
        if len(self.expression) + character_count <= self.max_expression_length:
            return True
        self._set_error(
            ExpressionTooLongError(
                f"Expression is limited to {self.max_expression_length} characters."
            )
        )
        return False

    def _show_expression(self) -> None:
        self.display = self.expression or "0"
        self.last_error = None
        self.just_evaluated = False

    def _set_error(self, error: CalculatorError) -> None:
        self.last_error = str(error)
        self.display = self.last_error
        self.just_evaluated = False

    def _current_number_start(self) -> int:
        index = len(self.expression)
        while index > 0 and (
            self.expression[index - 1].isdigit() or self.expression[index - 1] == "."
        ):
            index -= 1

        sign_index = index - 1
        if sign_index >= 0 and self._is_unary_minus(sign_index):
            return sign_index

        return index

    def _current_number(self) -> str:
        return self.expression[self._current_number_start():]

    def _is_unary_minus(self, index: int) -> bool:
        return self.expression[index] == "-" and (
            index == 0 or self.expression[index - 1] in self.OPERATORS
        )

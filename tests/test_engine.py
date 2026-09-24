"""Regression tests for calculator input and arithmetic behavior."""

import unittest

from core.engine import CalculatorEngine
from core.exceptions import DivisionByZeroError
from core.parser import ExpressionParser


class TestCalculatorEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CalculatorEngine()

    def enter(self, *keys):
        for key in keys:
            self.engine.press(key)

    def test_addition_formats_whole_number_without_decimal_tail(self):
        self.enter("2", "+", "3", "=")
        self.assertEqual(self.engine.display, "5")
        self.assertEqual(self.engine.expression, "5")

    def test_precedence_and_left_associative_division(self):
        self.enter("2", "+", "3", "*", "4", "=")
        self.assertEqual(self.engine.display, "14")
        self.enter("8", "/", "4", "/", "2", "=")
        self.assertEqual(self.engine.display, "1")

    def test_negative_numbers_and_negative_result(self):
        self.enter("2", "+/-", "*", "5", "=")
        self.assertEqual(self.engine.display, "-10")
        self.engine.clear()
        self.enter("5", "*", "2", "+/-", "=")
        self.assertEqual(self.engine.display, "-10")

    def test_unary_minus_after_operator_and_leading_decimal(self):
        self.enter("5", "*", "+/-", ".", "5", "=")
        self.assertEqual(self.engine.display, "-2.5")

    def test_second_decimal_is_rejected_without_mutating_expression(self):
        self.enter("1", ".", "2", ".")
        self.assertEqual(self.engine.expression, "1.2")
        self.assertIsNotNone(self.engine.last_error)
        self.engine.press("3")
        self.assertEqual(self.engine.expression, "1.23")

    def test_trailing_operator_is_reported_and_recoverable(self):
        self.enter("2", "+", "=")
        self.assertEqual(self.engine.display, "Invalid expression.")
        self.enter("3", "=")
        self.assertEqual(self.engine.display, "5")

    def test_division_by_zero(self):
        self.enter("5", "/", "0", "=")
        self.assertEqual(self.engine.display, "Cannot divide by zero.")

    def test_parser_rejects_modulo_by_zero(self):
        with self.assertRaises(DivisionByZeroError):
            ExpressionParser().evaluate("5%0")

    def test_percentage_converts_only_current_number(self):
        self.enter("2", "+", "5", "0", "%", "=")
        self.assertEqual(self.engine.display, "2.5")

    def test_backspace_after_evaluation_keeps_edited_value(self):
        self.enter("1", "2", "3", "=")
        self.engine.press(CalculatorEngine.BACKSPACE)
        self.enter("4", "=")
        self.assertEqual(self.engine.display, "124")

    def test_digit_after_evaluation_starts_new_expression(self):
        self.enter("2", "+", "3", "=", "7", "=")
        self.assertEqual(self.engine.display, "7")

    def test_operator_after_evaluation_continues_from_result(self):
        self.enter("2", "+", "3", "=", "+", "4", "=")
        self.assertEqual(self.engine.display, "9")

    def test_empty_clear_and_backspace_are_consistent(self):
        self.engine.press(CalculatorEngine.BACKSPACE)
        self.assertEqual(self.engine.display, "0")
        self.engine.press("C")
        self.assertEqual(self.engine.display, "0")

    def test_length_limit_and_positive_configuration(self):
        with self.assertRaises(ValueError):
            CalculatorEngine(max_expression_length=0)
        engine = CalculatorEngine(max_expression_length=2)
        engine.press("1")
        engine.press("2")
        engine.press("3")
        self.assertEqual(engine.expression, "12")
        self.assertIsNotNone(engine.last_error)

    def test_large_result_is_reported_without_uncaught_decimal_error(self):
        self.engine.expression = "9" * 50 + "*" + "9" * 50
        self.engine.press("=")
        self.assertTrue(self.engine.display)
        self.assertIsNotNone(self.engine.last_error)


if __name__ == "__main__":
    unittest.main()

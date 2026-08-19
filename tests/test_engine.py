"""Unit tests goes here"""
import unittest
from core.engine import CalculatorEngine


class TestCalculatorEngine(unittest.TestCase):

    def setUp(self):
        self.engine = CalculatorEngine()

    def test_addition(self):
        self.engine.append("2")
        self.engine.append("+")
        self.engine.append("3")
        self.assertEqual(self.engine.evaluate(), "5.0")

    def test_division_by_zero(self):
        self.engine.append("5")
        self.engine.append("/")
        self.engine.append("0")

        result = self.engine.evaluate()
        
        self.assertEqual(result, "Cannot divide by zero.")

    def test_backspace(self):
        self.engine.append("1")
        self.engine.append("2")
        self.engine.append("3")

        self.engine.backspace()

        self.assertEqual(self.engine.expression, "12")

    def test_multiplication_with_negative_first_number(self):
        self.engine.append("2")
        self.engine.toggle_sign()
        self.engine.append("*")
        self.engine.append("5")

        self.assertEqual(self.engine.evaluate(), "-10.0")

    def test_multiplication_with_negative_second_number(self):
        self.engine.append("5")
        self.engine.append("*")
        self.engine.append("2")
        self.engine.toggle_sign()

        self.assertEqual(self.engine.evaluate(), "-10.0")



if __name__ == "__main__":
    unittest.main()

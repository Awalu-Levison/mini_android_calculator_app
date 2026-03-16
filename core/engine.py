from .parser import ExpressionParser
from .exceptions import CalculatorError, InvalidExpressionError


class CalculatorEngine:
    
    def __init__(self):
        self.expression = ""
        self.parser = ExpressionParser()

    def append(self, value: str):
        self.expression += value

    # Clear the display
    def clear(self):
        self.expression = ""
    
    # Handle backspace functionality
    def backspace(self):
        if self.expression:
            self.expression = self.expression[:-1]
    
    # Handle percentage calculations
    def percentage(self):
        if not self.expression:
            return
        
        # Prevent double % entry
        if self.expression.endswith("%"):
            return

        # Get current num
        number = ""
        for char in reversed(self.expression):
            if char in "+-*/%":
                break
            number = char + number

        if not number:
                return
        try:
            percentage_num = float(number) / 100
        except ValueError:
            return
        
        self.expression = self.expression[:-len(number)] + str(percentage_num)


    # Evaluation entry
    def evaluate(self) -> str:
        if not self.expression:
            return
            # raise InvalidExpressionError("Expression is empty.")
        
        try:
            result = self.parser.evaluate(self.expression)
            self.expression = str(result)
            return self.expression
        
        except CalculatorError as e:
            self.expression = ""
            return str(e)
        
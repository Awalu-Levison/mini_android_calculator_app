class CalculatorError(Exception):
    """Base calculator exception."""
    pass

class InvalidExpressionError(CalculatorError):
    """Raised when expression is invalid."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when dividing by zero."""
    pass
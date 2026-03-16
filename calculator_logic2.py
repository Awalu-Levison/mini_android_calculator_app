# Calculator Logic

class CalculatorEngine:
    OPERATORS = {"+", "-", "*", "/", "%"}

    '''Initialise the calculator engine'''
    def _init_(self):
        self.expression = ""

    """append value to existing expression"""
    def append(self, value: str) -> None:
        self.expression += value

    '''Handle decimals'''
    def handle_decimal(self) -> None:
        current_number = self.get_current_number()
        if "." in current_number:
            return
        
        if not current_number:
            self.expression += "0."
        else:
            self.expression += "."
    
    """Get current number being entered"""
    def get_current_number(self) -> str:
        number = []

        for char in reversed(self.expression):
            if char in self.OPERATORS:
                break
            number.append(char)
        return "".join(reversed(number))
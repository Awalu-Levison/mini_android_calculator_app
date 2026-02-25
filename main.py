from kivy.app import App
from kivy.lang import Builder
from calculator_logic import CalculatorEngine


"""The main Calculator component
Controls App components and user interface"""
class MinimalCalcApp(App):

    """A method that creates and returns
    the app’s user interface"""
    def build(self):
        self.engine = CalculatorEngine()
        self.expression = ""
        return Builder.load_file("calculator.kv")

    """Define button functionalities & display"""
    def on_button(self, value):
        """Prevent multiple decimals in a single number: eg 5..3"""
        if value == ".":
            number_parts = self.expression.split()
            last_number_part = number_parts[-1] if number_parts else ""

            """get last number part"""
            number = ""
            for char in reversed(self.expression):
                if char in "+-*/%":
                    break
                number = char + number

                """Check extra . in number"""
                if "." in number:
                    return # Ignore extra decimal point
                
                """return 0 if not a number"""
                if not number:
                    self.expression += "0"
                else:
                    self.expression += "."
            else:
                self.expression += value
                
            self.root.ids.display.text = self.expression



    """Define the clear button functionality"""
    def clear(self):
        self.expression = ""
        self.root.ids.display.text = "0"

    """Define the delete button functionality"""
    def delete(self):
        self.expression = self.expression[:-1]
        if self.expression == "":
            self.root.ids.display.text = "0"
        else:
            self.root.ids.display.text = self.expression


    """Define the calculation function"""
    def calculate(self):
        if not self.expression:
            return
        result = self.engine.evaluate(self.expression)

        self.root.ids.display.text = result

        """Handle error or empty expression cases """
        if result == "Error":
            self.expression = ""
        else:
            self.expression = result 

        # result = self.engine.evaluate(self.expression)
        # self.root.ids.display.text = result
        # self.expression = result


if __name__ == "__main__":
    MinimalCalcApp().run()

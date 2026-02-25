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
        self.expression += value
        self.root.ids.display.text = self.expression

    """Define the clear button functionality"""
    def clear(self):
        self.expression = ""
        self.root.ids.display.text = "0"

    """Define the calculation function"""
    def calculate(self):
        result = self.engine.evaluate(self.expression)
        self.root.ids.display.text = result
        self.expression = result


if __name__ == "__main__":
    MinimalCalcApp().run()

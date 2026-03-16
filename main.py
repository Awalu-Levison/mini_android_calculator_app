from kivy.app import App
from kivy.lang import Builder
from core.engine import CalculatorEngine

class CalculatorApp(App):

    def build(self):
        self.engine = CalculatorEngine()
        return Builder.load_file("ui_components/calculator.kv")

    # Button handler based on the value of the button pressed
    def on_button(self, value):

        if value == "=":
            result = self.engine.evaluate()
            self.root.ids.display.text = str(result)

        elif value == "C":
            self.engine.clear()
            self.root.ids.display.text = ""

        elif  value == "⌫":
            self.engine.backspace()
            self.root.ids.display.text = self.engine.expression

        elif value == "%":
            self.engine.percentage()
            self.root.ids.display.text = self.engine.expression
        

        else:
            self.engine.append(value)
            self.root.ids.display.text = self.engine.expression 
    

    
    # Handle percentage calculations
    def percentage(self):
        current = self.root.ids.display.text

        if current != "" and current != "0":

            try:
                percentage_value = float(current) / 100
                self.engine.expression = str(percentage_value)
                self.root.ids.display.text = str(percentage_value)
            except ValueError:
                self.root.ids.display.text = "Error"

                         
if __name__ == "__main__":
    CalculatorApp().run()
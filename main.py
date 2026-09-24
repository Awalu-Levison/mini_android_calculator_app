"""Kivy application entry point for the mini calculator."""

from pathlib import Path

from kivy.app import App  # pyright: ignore[reportMissingImports]
from kivy.lang import Builder  # pyright: ignore[reportMissingImports]

from core.engine import CalculatorEngine


class CalculatorApp(App):
    """Connect keypad events to the calculator engine and display."""

    def build(self):
        self.engine = CalculatorEngine()
        layout_path = Path(__file__).parent / "ui_components" / "calculator.kv"
        self.root_widget = Builder.load_file(str(layout_path))
        return self.root_widget

    def on_button(self, value: str) -> None:
        self.engine.press(value)
        if self.root_widget is not None:
            self.root_widget.ids.display.text = self.engine.display
            self.root_widget.ids.expression.text = self.engine.expression


if __name__ == "__main__":
    CalculatorApp().run()

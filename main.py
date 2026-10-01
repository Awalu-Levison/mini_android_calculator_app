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
        self.refresh_view()
        return self.root_widget

    def on_button(self, value: str) -> None:
        self.engine.press(value)
        self.refresh_view()

    def on_history(self) -> None:
        """Toggle the temporary recent-calculations panel."""
        if self.root_widget is not None:
            panel = self.root_widget.ids.history_panel
            panel.opacity = 0 if panel.opacity else 1
            panel.disabled = not panel.disabled
            self.refresh_view()

    def refresh_view(self) -> None:
        if self.root_widget is None:
            return
        ids = self.root_widget.ids
        ids.display.text = self.engine.display
        ids.expression.text = self.engine.expression
        ids.history.text = "\n".join(
            f"{expression} = {result}"
            for expression, result in self.engine.history
        ) or "No recent calculations"
        ids.clear_button.text = "C" if self.engine.expression else "AC"


if __name__ == "__main__":
    CalculatorApp().run()

# Mini Kivy Calculator

## Overview

Mini Kivy Calculator is a lightweight calculator application written in Python with a Kivy user interface. It currently runs as a local Kivy application. The calculation engine and expression parser are separate from the UI so that calculation behavior can be tested independently.

Android packaging is planned, but this repository does not yet contain an Android build configuration or a Play Store-ready package.

## Current Features

- Dark, touch-friendly calculator interface with a two-line display and rounded buttons.
- Digit entry, decimal point, addition, subtraction, multiplication, division, clear, backspace, percentage, sign toggle, and equals controls.
- Expression evaluation with standard precedence: multiplication and division are evaluated before addition and subtraction.
- Negative-number support, including expressions such as `-2*5` and `5*-2`.
- Percentage conversion for the number currently being entered.
- Division-by-zero and invalid-expression messages instead of unhandled application errors.
- Offline calculation: no network connection or external service is required.
- Python unit tests for core engine behavior.

## Project Structure

| Location | Purpose |
| --- | --- |
| `main.py` | Kivy application entry point and button-event handling. |
| `ui_components/calculator.kv` | Kivy layout, display, keypad, and button styles. |
| `core/engine.py` | Calculator state and actions such as clear, backspace, percentage, sign toggle, and evaluation. |
| `core/parser.py` | Expression tokenization and arithmetic evaluation. |
| `core/exceptions.py` | Calculator-specific exception types. |
| `tests/test_engine.py` | Unit tests for the calculation engine. |

## Requirements

- Python 3.11 or later is recommended.
- Kivy 2.3.1 (installed from `requirements.txt`).

## Run Locally

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Start the app:

```powershell
python main.py
```

## Run Tests

```powershell
python -m unittest discover -s tests -v
```

## Current Limitations

- The app is not packaged for Android yet.
- Calculation history, memory registers, scientific functions, localization, and export/share features are not implemented.
- The percent key performs percentage conversion; it is not exposed as a modulo key in the UI.

## Planned Next Steps

- Improve input validation, decimal formatting, and error recovery.
- Make the UI more responsive across small, large, portrait, and landscape screens.
- Add Android packaging configuration and test release builds on supported device versions and CPU architectures.

## License

This project is distributed under the [MIT License](LICENSE).

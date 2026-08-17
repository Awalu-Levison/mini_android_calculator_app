# Project Summary: Mini Calculator

## Overview

This project is a lightweight calculator application built with Python and Kivy. `main.py` starts the Kivy app, loads the keypad interface from `ui_components/calculator.kv`, and delegates calculation state and evaluation to the Python calculator engine in `core/`.

The codebase currently implements a basic four-function calculator with decimal values, percentage conversion, deletion, error handling, and unit tests for key engine behavior.

## Implemented Features

### Calculator interface

- A dark, touch-friendly Kivy interface with rounded buttons and a highlighted orange style for operators.
- A two-line display area: one line is intended to show the expression and the main line shows the current input or result.
- A four-column keypad containing digits `0` to `9`, decimal point, clear, backspace, percentage, division, multiplication, subtraction, addition, and equals controls.
- Clear (`C`) resets the stored expression and restores the display to `0`.
- The Backspace button removes the most recently entered character.

### Arithmetic engine

- An expression-based calculation engine (`CalculatorEngine`) that stores the user's current expression.
- Floating-point evaluation of addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and modulo (`%`) operations.
- Standard operator precedence: multiplication, division, and modulo are evaluated before addition and subtraction; operations at the same precedence are processed left to right.
- Results replace the current expression, allowing a result to be used in the next calculation.
- Division by zero is detected and shown as `Cannot divide by zero.` rather than raising an unhandled error.
- Invalid characters or malformed expressions are converted into a user-facing `Invalid expression.` message.

### Number-entry helpers

- Percentage converts the current number being entered to its value divided by 100. For example, entering `50` and pressing `%` changes the expression to `0.5`.
- The `calculator_logic2.py` module contains an additional, currently unused helper for decimal input. It prevents a second decimal point in the current number and inserts `0.` when a decimal begins a number.

### Testing

- A `unittest` suite verifies addition, backspace, and division-by-zero behavior.
- The suite currently contains three tests, all of which pass when run with `python -m unittest discover -s tests -v`.

## Project Structure

| Location | Responsibility |
| --- | --- |
| `main.py` | Kivy application entry point and button-event handling. |
| `ui_components/calculator.kv` | Layout, button styling, display, and keypad definitions. |
| `core/engine.py` | Expression state, clear/backspace/percentage actions, and evaluation entry point. |
| `core/parser.py` | Tokenization and arithmetic evaluation with operator precedence. |
| `core/exceptions.py` | Calculator-specific error types. |
| `tests/test_engine.py` | Unit tests for the calculation engine. |
| `calculator_logic2.py` | Separate, unfinished or experimental decimal-entry helper; not used by the running app. |

## Current Scope and Gaps

- The visible `+/-` button is not yet implemented in the event handler; pressing it appends `+/-`, which is not a valid expression.
- The decimal button is connected directly to normal character appending. The duplicate-decimal protection in `calculator_logic2.py` is not integrated into the active engine.
- Although the parser supports modulo, the keypad's `%` button performs percentage conversion, so the UI does not currently expose a direct modulo operation.
- Parentheses, scientific functions, memory registers, calculation history, localization, and history export are not implemented.
- The code currently provides a Kivy app only. Android packaging and the Jetpack Compose/Kotlin-Python bridge described in the README are not present in the project files.
- The README also mentions history, memory, responsive orientation handling, and automatic light/dark theming, but these are not implemented in the current source.

## Dependencies and Runtime

Kivy is the UI framework used by the application. The repository includes a local Python virtual environment with Kivy installed; however, `requirements.txt` is currently empty, so dependencies are not yet documented for a fresh installation.

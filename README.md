# Mini Kivy Calculator

A small offline calculator built with Python and Kivy. The interface is described in Kivy Language (KV), while calculation input and arithmetic live in a standalone engine under `core/`. This separation keeps keypad presentation independent from calculator rules and lets the engine be tested without launching the graphical app.

## Current status

The calculator currently runs as a local Kivy application. It has not yet been packaged or verified as an Android release. The project does not include Buildozer/python-for-android configuration, app signing setup, or a Play Store release package.

## Features

- Four standard arithmetic operations with multiplication and division precedence.
- Decimal input, unary sign toggle, and percentage conversion of the currently entered number (divide that operand by 100).
- Clear/all-clear, backspace, and equals controls. The clear key shows `AC` for an empty expression and `C` when there is an active expression; both clear the active calculation.
- Live result preview for complete valid expressions. An incomplete expression has no preview; pressing equals on an invalid expression shows an error.
- Negative operands, including leading negatives and negatives after an operator (for example, `-2*5` and `5*-2`).
- A recent-history panel showing up to ten successful calculations for the current app session. History is in memory and is cleared when the app process restarts.
- Dark Kivy interface with a five-row keypad, adaptive keypad row height, and canvas-drawn history and backspace icons.
- Decimal-based arithmetic, bounded expression/result length, and user-facing input and division-by-zero errors.

The parser also supports `%` as remainder, but the keypad's `%` action is percentage conversion; remainder is not directly exposed as a separate key. Parentheses, scientific functions, memory keys, persistent history, and restoring a history row are not implemented.

## How the code is organized

| File | Responsibility |
| --- | --- |
| `main.py` | Starts Kivy, creates the engine, handles button actions, and copies engine state into the UI. |
| `ui_components/calculator.kv` | Defines the display, keypad, layout sizing, button styles, and vector icons. |
| `core/engine.py` | Owns the expression and display state, keypad behavior, preview, history, and evaluation flow. |
| `core/parser.py` | Tokenizes expressions and evaluates them with Decimal arithmetic and operator precedence. |
| `core/exceptions.py` | Defines calculator-specific errors shown by the engine. |
| `tests/test_engine.py` | Checks calculator behavior without requiring a running Kivy window. |
| `requirements.txt` | Pins the Kivy dependency used by this project. |

### Calculation flow

1. The KV keypad calls `CalculatorApp.on_button()` with a digit, operator, or action name.
2. `on_button()` forwards the input to `CalculatorEngine.press()` and refreshes the visible labels.
3. The engine updates the expression. For edits, it asks `ExpressionParser` for a preview; equals evaluates and stores successful results in session history.
4. The parser converts the expression to Decimal operands and operators, then computes multiplication/division/remainder before addition/subtraction.
5. `refresh_view()` updates the expression line, result display, history text, and clear-key label from engine state.

The code contains docstrings for the application, engine, parser, and test helper functions. Comments in the implementation explain non-obvious input rules. Contributions and focused improvement suggestions are welcome.

## Requirements

- Python 3.11 or later is recommended.
- Kivy 2.3.1, pinned in `requirements.txt`.

## Run locally

Create and activate a virtual environment, install the dependency, and start the app:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

## Run the tests

```powershell
python -m unittest discover -s tests -v
```

These tests exercise the calculation engine, not Android packaging or the rendered interface. A Kivy installation and device/emulator check are needed to verify UI rendering.

## Before an Android release

- Add and document an Android build configuration and choose the minimum Android API level and CPU architectures to support.
- Build and test on the minimum supported Android version and a current Android version, including portrait, landscape, and small screens.
- Verify icon rendering, display scaling, touch targets, app startup, and back navigation on device/emulator.
- Configure release signing and inspect the final APK or app bundle before distribution.
- Prepare store listing, privacy disclosures, and a support channel appropriate to the release.

## Technology and community

The app is written in Python and uses Kivy for its graphical interface. It is maintained by Global Solutions Technology, an emerging technology company in Malawi focused on technology solutions for businesses and individuals.

For improvements, advice, or general inquiries, contact **Awalu Levison** (software engineer focused on frontend development) at [levisonawalu251@gmail.com](mailto:levisonawalu251@gmail.com). Community contributions and suggestions are welcome; please include the behavior you observed, steps to reproduce it, and the Android/device details when reporting a UI issue.

## License

This project is distributed under the [MIT License](LICENSE).

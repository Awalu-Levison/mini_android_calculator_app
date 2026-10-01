# Project Summary: Mini Kivy Calculator

## Overview

Mini Kivy Calculator is an offline Kivy application with a Python calculation engine. The Kivy Language (KV) file describes the screen and keypad; `core/engine.py` manages user input and calculator state; `core/parser.py` evaluates arithmetic expressions using `Decimal`. Calculation data is local to the running process.

## Implemented functionality

- Standard addition, subtraction, multiplication, and division with normal operator precedence.
- Decimal entry, sign toggle, percentage conversion of the current operand, clear, backspace, and equals.
- Negative values at the start of an expression and after a binary operator.
- Live preview for complete valid expressions; an incomplete expression leaves the preview blank.
- Error messages for invalid input, division by zero, too-long input, and unsupported keypad actions.
- Up to 100 characters in an expression and a ten-item, most-recent-first history of successful equals operations.
- History is session-only. Clearing the active expression does not erase history; restarting the app does.
- A dark interface with a two-line expression/result display, five rows of four keypad controls, adaptive row sizing, and canvas-drawn history/backspace icons.
- The clear key label switches between `AC` and `C` according to whether the expression is empty.

The percent keypad control converts the number currently being entered to that number divided by 100. Although the parser recognizes `%` as a remainder operator, the UI does not expose remainder separately. Parentheses, scientific operations, memory functions, persistent history, and selecting history entries are not implemented. Arithmetic follows expression evaluation and operator precedence; it is not a step-by-step commercial calculator model.

## Architecture and calculation flow

- `main.py` creates one `CalculatorEngine`, loads the KV file, forwards keypad presses to the engine, toggles history visibility, and refreshes labels from engine state.
- `ui_components/calculator.kv` defines the responsive vertical layout, keypad actions, and canvas vector strokes used for history and backspace icons.
- `core/engine.py` handles keypad dispatch and state changes. It requests previews for edits, evaluates on equals, formats Decimal results, applies the expression limit, and keeps a bounded session history.
- `core/parser.py` tokenizes signed decimal operands and operators. It evaluates multiplication, division, and remainder first, then addition and subtraction from left to right.
- `core/exceptions.py` defines the base calculator error and specialized invalid-expression, division-by-zero, and expression-length errors.
- `tests/test_engine.py` exercises engine and parser behavior independently of Kivy rendering.

All functions in the application, engine, parser, and engine test helper have docstrings describing their role. Inline comments call out operator replacement and unary-minus handling where the behavior is less obvious.

## Verification and limitations

- Run engine tests with `python -m unittest discover -s tests -v`.
- Python syntax can be checked with `python -m py_compile main.py core/engine.py core/parser.py`.
- The tests do not verify KV parsing, visual appearance, touch targets, Android packaging, or behavior on physical devices. Verify those with Kivy installed and by running builds on representative Android devices/emulators.
- No Android build configuration, signing setup, or distributable APK/AAB is currently included.
- The display scales its result text to fit the available width. Very long values may appear in smaller type to keep all digits visible.

## Project files

| Path | Purpose |
| --- | --- |
| `main.py` | Kivy app entry point and UI/engine adapter. |
| `ui_components/calculator.kv` | Layout, button styles, actions, and vector icons. |
| `core/engine.py` | Key input, expression state, previews, formatting, errors, and history. |
| `core/parser.py` | Expression tokenization and Decimal arithmetic. |
| `core/exceptions.py` | Calculator-specific exceptions. |
| `tests/test_engine.py` | Engine regression tests. |
| `requirements.txt` | Kivy dependency pin. |
| `README.md` | Setup, current features, architecture overview, and contributor guidance. |

## Suggested contribution areas

- Verify and improve display/keypad behavior on small screens, landscape layouts, and varied Android font scales.
- Add Android packaging, minimum/target API decisions, architecture coverage, signed release builds, and device testing.
- Improve parser test coverage and define desired behavior for repeated equals, remainder, overflow, and percentage semantics.
- Consider selectable history entries and optional persistent history if those fit the product goals.
- Review accessibility, localization, and store-release requirements before public distribution.

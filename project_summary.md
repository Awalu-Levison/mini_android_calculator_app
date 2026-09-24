# Project Summary: Mini Kivy Calculator

## Overview

This is a small Kivy calculator application. `main.py` loads the interface from
`ui_components/calculator.kv` and forwards keypad events to the UI-independent
engine in `core/`. Arithmetic uses Python's `Decimal` type.

## Current Features

- Four-function expressions with multiplication and division precedence, plus
  modulo in the parser.
- Decimal and negative-number entry, sign toggle, percentage conversion,
  backspace, clear, and equals.
- User-facing errors for malformed expressions, division by zero, unsupported
  inputs, and expression/result length limits.
- A dark four-column Kivy keypad with separate expression and result displays.
- Regression tests for parser behavior, entry state, error recovery, and limits.

## Recent Fixes

- Unified all button handling through `CalculatorEngine.press`; the Kivy view now
  refreshes both labels from engine state after each key.
- Corrected the backspace key glyph encoding and made it match the engine key.
- Routed clear through the same handler as every other key.
- Kept a result editable after backspace, while a digit after evaluation starts
  a fresh calculation and an operator continues from the result.
- Rejected invalid repeated decimals without changing the expression; the next
  valid key recovers the display and continues the expression.
- Allowed unary minus after a binary operator and added leading-zero behavior
  for decimal entry.
- Enforced positive expression-length configuration and handled oversized
  formatted results as calculator errors.
- Expanded Decimal exception handling so arithmetic failures are translated to
  calculator errors rather than escaping into the UI.
- Updated result formatting to omit redundant `.0` tails; tests now assert that
  consistent display format.

## Project Structure

| Location | Purpose |
| --- | --- |
| `main.py` | Kivy app entry point and thin keypad/display adapter. |
| `ui_components/calculator.kv` | Layout, display labels, keypad, and button styles. |
| `core/engine.py` | Input state, display state, actions, and error handling. |
| `core/parser.py` | Tokenization and Decimal arithmetic with precedence. |
| `core/exceptions.py` | Calculator-specific exception types. |
| `tests/test_engine.py` | Engine and regression tests. |
| `requirements.txt` | Kivy dependency pin. |

## Current Scope

The parser supports `+`, `-`, `*`, `/`, and modulo, while the keypad's `%` key
converts the current number to one hundredth of its value. Parentheses,
scientific functions, history, memory, localization, and Android packaging are
not implemented. `calculator_logic2.py` is an unused legacy helper and should
not be treated as the active engine; the application uses `core/engine.py`.

## Verification Progress

The existing tests had stale expectations for `.0` formatting and lacked
coverage of key state transitions. The suite has been expanded to cover those
cases along with decimal validation, error recovery, precedence, percentages,
and expression limits. The current verification run is recorded in the change
handoff; rerun with:

```powershell
python -m unittest discover -s tests -v
```

The Kivy dependency is pinned in `requirements.txt` as `Kivy==2.3.1`.

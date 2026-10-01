# Project Summary: Mini Kivy Calculator

## Overview

Mini Kivy Calculator is an offline Kivy app with a Decimal-based arithmetic engine
in `core/`. The expression and result display, keypad behavior, and recent history
are managed locally in memory for the lifetime of the running app.

## Implemented

- iPhone-inspired dark calculator layout with circular utility, number, and orange
  operator keys, large right-aligned result, and a compact expression line.
- Standard four-function operations, decimal entry, sign toggle, percent conversion,
  clear/all-clear, delete/backspace, and equals.
- Live result preview for complete valid expressions; blank preview for incomplete
  expressions. Evaluation errors remain visible after equals is pressed.
- Repeated binary operator entry replaces the pending operator, while unary minus
  remains available for negative operands.
- Most recent 10 completed calculations appear in a history panel. History uses a
  bounded deque in memory and is not written to disk, so a new app process starts
  with empty history.
- Decimal arithmetic with operator precedence, input/result length limits, and
  user-facing malformed-expression and divide-by-zero handling.

## Standard Mode Scope

The standard-mode keypad provides four arithmetic operations, percentage, sign,
decimal, clear/delete, and equals. The compact history control is an app feature.
This is an iPhone-inspired Kivy layout, not a pixel-identical Apple implementation.
The current input model uses expression evaluation with precedence rather than
Apple's exact step-by-step interaction semantics. Modulo is parser-supported but
not presented as a separate keypad operation. Scientific mode, unit conversion,
parentheses, and memory register controls are not part of iPhone standard mode and
are not implemented.

## Security, Performance, and Memory Review

- The app evaluates expressions through a custom tokenizer and Decimal arithmetic;
  it does not use `eval`, execute user-provided code, access the network, or persist
  calculation history.
- Input length remains bounded at 100 characters. History holds at most 10 pairs,
  so session memory use stays bounded.
- Live preview reparses the bounded expression after edits. This is small, local
  work and needs no background thread or external service.
- Kivy's startup logger reported a permission error writing under the user profile
  during layout verification; the KV layout still loaded successfully. This is an
  environment logging-path issue, not a calculator evaluation failure.

## Verification

- `python -m unittest discover -s tests -v`: 19 tests pass, covering arithmetic,
  error handling, previews, operator replacement, history limit, and session reset.
- Kivy 2.3.1 loaded `ui_components/calculator.kv` successfully; expected widget IDs
  were present.
- The GUI was not interactively exercised across Android devices or screen sizes.

## Project Structure

| Location | Purpose |
| --- | --- |
| `main.py` | Kivy app entry point and UI/engine adapter. |
| `ui_components/calculator.kv` | iPhone-inspired calculator layout and controls. |
| `core/engine.py` | Input state, live preview, evaluation, and session history. |
| `core/parser.py` | Tokenization and Decimal arithmetic. |
| `core/exceptions.py` | Calculator error types. |
| `tests/test_engine.py` | Engine behavior and regression tests. |
| `requirements.txt` | Kivy dependency pin. |

## Known Limitations and Follow-up

- No Android packaging or device release configuration exists yet.
- UI layout needs visual verification on portrait/landscape and small Android
  screens; the current keypad uses fixed minimum row dimensions.
- A runtime history panel shows recent expressions and results but does not let a
  user tap a row to restore it.
- The repository's `calculator_logic2.py` was already deleted in the working tree
  when this task began; the active app uses `core/engine.py`.

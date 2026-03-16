# Mini Android Calculator App (Python Backend)

## Overview
Mini Android Calculator App is a lightweight utility that mirrors a classic handheld calculator while taking advantage of a Python-driven logic layer. The user interface is Android-native, while every arithmetic operation is validated and computed through a concise Python core to guarantee consistent, testable results.

## Key Features
- **Responsive Keypad Layout**: Mimics familiar calculator ergonomics, supports both portrait and landscape orientations, and offers immediate tactile feedback for rapid calculations.
- **Real-Time Expression Parsing**: Validates each input as it is entered, preventing malformed expressions and highlighting errors before evaluation.
- **Core Arithmetic Suite**: Provides addition, subtraction, multiplication, and division with floating-point precision, including graceful handling of divide-by-zero scenarios.
- **Operation History Tape**: Captures recent calculations in a scrollable log so users can double-check previous results or reuse expressions.
- **Memory Registers (M+, M-, MR, MC)**: Enables quick storage and retrieval of interim values, enhancing multi-step computations without re-entering numbers.
- **Theme-Aware UI**: Adapts to system-wide light and dark themes while preserving contrast ratios for accessibility compliance.
- **Offline-First Architecture**: Requires no network connectivity; all computations occur locally, ensuring speed and data privacy.

## Architecture
1. **Android UI Layer**: Built with Jetpack Compose (or XML layouts) for input capture, keypad rendering, and dynamic display updates.
2. **Kotlin-Python Bridge**: Uses a lightweight interoperability layer (e.g., Chaquopy) to call Python functions directly from the Android client.
3. **Python Logic Module**: Houses the arithmetic engine, expression parser, and test suite to guarantee deterministic results across devices.

## Getting Started
1. Clone the repository and open it in Android Studio.
2. Ensure the Python bridge dependency (Chaquopy or equivalent) is configured in `build.gradle`.
3. Sync the project, run on an emulator or physical device, and interact with the calculator UI.

## Testing
- **Unit Tests (Python)**: Validate arithmetic operations, edge cases, and expression parsing.
- **UI Tests (Android)**: Cover keypad responsiveness, display updates, and history tape rendering under different orientations.

## Roadmap
- Add scientific functions (trigonometry, logarithms, factorials).
- Include localization for additional languages.
- Provide export/share for calculation history.

## License
Distributed under the MIT License. See `LICENSE` for details.

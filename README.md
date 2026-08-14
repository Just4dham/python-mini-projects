# Python Mini Projects 🐍

A collection of interactive command-line interface (CLI) applications built using pure Python. This repository showcases basic to intermediate programming concepts like conditional logic, `while` loops, input validation, string manipulation, functions, and JSON file handling.

---

## 🛠️ Projects Included

| File | Description | Key Features |
| :--- | :--- | :--- |
| `number_guessing_game.py` | Guess a random number between 1 and 100 with attempt limits. | Saves personal best records to `highscore.json` using JSON file I/O. |
| `rock_paper_scissors.py` | Classic game played against the computer. | Keeps running score state until the player exits. |
| `cli_calculator.py` | Command-line math calculator. | Error handling for zero division and invalid numerical inputs. |
| `try.py` | Interactive decision maker that picks a random option from a custom list. | Input sanitation (`.strip().lower()`), auto-capitalization (`capwords`), and crash protection. |
| `currency_converter.py` | Instant exchange rate calculator (e.g., USD to SAR). | Handles `float` conversions, arithmetic math, and clean formatted outputs. |

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Clone or download this repository.
3. Run any file directly from your terminal:

```bash
python number_guessing_game.py
python rock_paper_scissors.py
python cli_calculator.py
python try.py
python currency_converter.py

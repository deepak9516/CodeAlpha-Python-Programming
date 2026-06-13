## 🎮 Hangman Game (Python Command-Line Tool)

A complete, interactive command-line implementation of the classic **Hangman Game** written in Python. The program automatically selects a random secret word from a predefined catalog, masks it, and challenges the player to guess it letter-by-letter within a fixed number of attempts.

---

### 📋 Table of Contents
1. [Features](#-features)
2. [Project Architecture](#%EF%B8%8F-project-architecture)
3. [Prerequisites & Installation](#-prerequisites--installation)
4. [How to Run](#-how-to-run)
5. [Game Rules & Logic](#-game-rules--logic)
6. [Included Vocabulary](#-included-vocabulary)
7. [Current Code Limitations](#-current-code-limitations)

---

### 🚀 Features

* **Automated Word Selection:** Leverages Python's `random.choice` to pick a new word every session.
* **Dynamic Masking:** Displays real-time game progress using underscores (`_`) that instantly reveal correctly guessed characters.
* **Strict Attempt Tracking:** Limits the user to exactly 6 wrong/unique guesses before triggering a Game Over sequence.
* **Case Insensitivity:** Automatically normalizes all keyboard inputs to lowercase using `.lower()` to prevent case mismatch bugs.

---

### 🛠️ Project Architecture

The application is completely self-contained in a single executable script:
* `hangman.py` (Main application logic containing game loops and text rendering)

---

### 🧰 Prerequisites & Installation

#### System Requirements
* **Python 3.x** or higher must be installed on your machine.
* No third-party external libraries (`pip install`) are required.

#### Setup Instructions
1. Download or clone this repository to your local drive.
2. Open your System Terminal, Command Prompt, or VS Code Terminal.
3. Navigate to the folder containing your script:
   ```bash
   cd path/to/your/hangman-folder
   ```

---

### 💻 How to Run

Execute the script directly using the Python interpreter from your terminal terminal:
```bash
python hangman.py
```
*(Note: If you use Linux or macOS, you might need to type `python3 hangman.py` instead).*

---

### 🎮 Game Rules & Logic

1. **Initialization:** The game boots up, prints a welcome banner, and selects a secret word.
2. **The Loop:** At every turn, the system outputs the masked word state (e.g., `Word: _ _ _ _ _ _`).
3. **The Guess:** You are prompted to type a single character:
   * **Correct Guess:** The system appends it to the history list and updates the hidden word tracking.
   * **Wrong Guess:** The system docks 1 life point and prints out your total remaining attempts.
4. **End Game Conditions:**
   * **Victory:** If the revealed text matches the secret word, you receive a congratulations message and the program terminates.
   * **Defeat:** If the total remaining attempts hit `0`, the game ends and reveals what the secret word actually was.

---

### 📜 Included Vocabulary

The game randomly shuffles through the following built-in string array:
* `python` | `cpp` | `java` | `html` | `coding` | `hello` | `deepak` | `namaste`

---

### ⚠️ Current Code Limitations (Known Edge Cases)
* **Duplicate Penalty Bug:** In this initial codebase version, if you enter a previously guessed wrong letter again, the program jumps straight into the `else` block, penalizing your remaining lives again.
* **Non-Alphabet Inputs:** The code currently accepts numbers, symbols, or multi-letter words without throwing an explicit validation warning.
*

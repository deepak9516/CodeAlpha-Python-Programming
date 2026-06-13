# CodeAlpha Python Programming Projects

This repository contains 4 Python projects completed as part of my CodeAlpha internship.

---

## 🎮 Hangman Game (Python Command-Line Tool)

A complete, interactive command-line implementation of the classic **Hangman Game** written in Python. The program automatically selects a random secret word from a predefined catalog, masks it, and challenges the player to guess it letter-by-letter within a fixed number of attempts.

---

### 📋 Table of Contents
1. [Features](##-features)
2. [Project Architecture](##%EF%B8%8F-project-architecture)
3. [Prerequisites & Installation](##-prerequisites--installation)
4. [How to Run](##-how-to-run)
5. [Game Rules & Logic](##-game-rules--logic)
6. [Included Vocabulary](##-included-vocabulary)
7. [Current Code Limitations](##-current-code-limitations)

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

## 📈 Stock Portfolio Tracker (Python & CSV Data Persistence)

An end-to-end, terminal-based **Stock Portfolio Tracker** utility. This console application manages mocked equity transactions, checks real-time inventory lists, calculates dynamic transaction valuations, and automatically exports your finalized asset positions into a persistent, universally readable **CSV spreadsheet**.

---

### 📋 Table of Contents
1. [Core Features](##-core-features)
2. [File Directory Layout](##%EF%B8%8F-file-directory-layout)
3. [Prerequisites & Environment Setup](##-prerequisites--environment-setup)
4. [Step-by-Step Execution Guide](##-step-by-step-execution-guide)
5. [Data Architecture & CSV Mapping](##-data-architecture--csv-mapping)
6. [Detailed Code Workflow](##-detailed-code-workflow)
7. [Technical Safeguards](##-technical-safeguards)

---

### 🚀 Core Features

* **Ticker Inventory Verification:** Checks user queries against an active dictionary database to reject non-existent stock symbols.
* **Aggregation Management:** Automatically bundles purchases of identical stock tickers together, scaling up your overall share count values.
* **Mathematical Ledger Tracking:** Multiplies live stock quantities by unit price to update total capital layout indicators.
* **Case Normalization:** Converts user text requests into capital letters (`.upper()`), accepting inputs like `aapl` or `Aapl` flawlessly.
* **Persistent CSV Exporting:** Drops file header keys and records raw transactions to an external database file using `csv.DictWriter` upon session termination.

---

### 🛠️ File Directory Layout

Upon executing your program, the project will generate the following file tree structures inside your root directory:
```text
├── portfolio_tracker.py     # Main executable engine containing terminal UI and functions
└── my_portfolio.csv         # Automatically generated data storage spreadsheet (Appears after exiting)
```

---

### 🧰 Prerequisites & Environment Setup

#### System Configuration
* Fully optimized for **Python 3.6** up to any modern current release.
* Utilizes core native modules (`csv`). Requires absolutely **zero external dependencies**.

#### Directory Navigation
Open your local shell application and change the destination working directory to where your python file sits:
```bash
cd path/to/your/portfolio-folder
```

---

### 💻 Step-by-Step Execution Guide

To boot up the user interactive wizard, launch this command from your command prompt terminal:
```bash
python portfolio_tracker.py
```

#### Supported Active Stocks Tickers & Unit Pricing Map:
* **AAPL:** $180 | **TSLA:** $250 | **GOOGL:** $140 | **MSFT:** $320 | **AMZN:** $130

---

### 📊 Data Architecture & CSV Mapping

When you exit the application loop by typing anything other than `yes`, the application instantly creates or overrides `my_portfolio.csv` with a standard UTF-8 encoded matrix block.

#### CSV Layout Format:
```csv
stock,quantity
AAPL,15
MSFT,4
```

---

### ⚙️ Detailed Code Workflow

1. **Display Menu:** The app logs down what tickers are valid to purchase.
2. **Ticker Validation:** You input a ticker name. A logical validation function (`check_stocks`) runs a confirmation process. If invalid, the loop skips back to the top.
3. **Quantity Input:** The application requests a numerical index payload indicating total shares bought.
4. **Math Matrix Processing:** Computes total transaction costs and appends the asset count directly onto a localized dictionary structure (`portfolio`).
5. **Session Continuation Check:** Prompts if you would like to continue shopping or export metrics.
6. **Data Output:** Iterates over storage blocks to print summaries, logs overall investment totals, and streams parameters straight into the CSV file container.

---

### ⚠️ Technical Safeguards & Edge Cases
* **Crash Risk on Quantity:** If a user types a float (e.g., `1.5`) or regular string symbols (e.g., `ten shares`), the application will throw a terminal runtime `ValueError` exception and close unexpectedly.
* **Overwrite Warning:** Running the script a second time will wipe out old data entries within `my_portfolio.csv` and write fresh metrics from scratch.
*

### 📧 Automated Email Extractor (Python Text Automation)

A high-utility, regex-powered **Automated Email Extractor** script built with Python. This tool automatically parses through raw, unstructured text files, identifies all valid email addresses using Pattern Matching, and exports them into a clean, line-separated text file.

---

### 📋 Table of Contents
1. [Core Features](##-core-features)
2. [File Directory Structure](##%EF%B8%8F-file-directory-structure)
3. [Prerequisites & Requirements](##-prerequisites--requirements)
4. [Step-by-Step Execution Guide](##-step-by-step-execution-guide)
5. [How the Regex Pattern Works](##-how-the-regex-pattern-works)
6. [Data Workflow & Output Format](##-data-workflow--output-format)
7. [Technical Safeguards & Edge Cases](##-technical-safeguards--edge-cases)

---

### 🚀 Core Features

* **Advanced Pattern Matching:** Uses Python's native `re` (Regular Expression) module to scan complex text blobs.
* **Automated File Handling:** Utilizes safe contextual file handling (`with open`) to automatically read and write files without memory leaks.
* **Clean Data Segregation:** Isolates mixed text data and pipes pure email strings into a structured repository file.
* **Real-time Metrics:** Displays a live console log detailing successful executions and the absolute count of target emails recovered.

---

### 🛠️ File Directory Structure

For this script to execute successfully, your directory layout must match this structure:
```text
├── email_extractor.py                                 # Your python script containing this code
└── Task 3 (Task Automation with Python Scripts)/       # Subfolder
    └── input.txt                                      # Source file containing mixed text and emails
```
*Note: Once you run the script, a new file named `email.txt` will automatically appear in your main root directory.*

---

### 🧰 Prerequisites & Requirements

#### System Configuration
* **Python 3.x** or higher installed on your machine.
* Uses the standard internal **`re`** library. Requires **zero external dependencies** (`pip install`).

#### Directory Navigation
Open your local shell or terminal and change the directory to your workspace path:
```bash
cd path/to/your/automation-folder
```

---

### 💻 Step-by-Step Execution Guide

1. Make sure you have placed your source text inside the subfolder file: `Task 3 (Task Automation with Python Scripts)/input.txt`.
2. Launch the automation script from your command prompt terminal:
   ```bash
   python email_extractor.py
   ```
3. Check the console layout for confirmation and open the newly generated `email.txt` file to view results.

---

### 🔬 How the Regex Pattern Works

The core extraction engine relies on this powerful Regular Expression formula:
`[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`

* **`[a-zA-Z0-9._%+-]+`** : Matches the username part before the `@` symbol (allows letters, numbers, dots, underscores, percentages, plusses, and hyphens).
* **`@`** : Looks for the mandatory literal `@` separator symbol.
* **`[a-zA-Z0-9.-]+`** : Matches the domain name provider (e.g., `gmail`, `yahoo`, `company-name`).
* **`\.[a-zA-Z]{2,}`** : Matches the literal dot `.` followed by top-level domains like `.com`, `.org`, `.in` (must be at least 2 or more alphabetic characters long).

---

### 📊 Data Workflow & Output Format

#### Sample Input (`input.txt`):
```text
Hello team, please contact support at admin@example.com or reach out to john.doe@company.org for sales queries.
```

#### Generated Output (`email.txt`):
```text
admin@example.com
john.doe@company.org
```

---

### ⚠️ Technical Safeguards & Edge Cases
* **File Missing Error:** If the `input.txt` file is missing or if the subfolder name has a typing error, Python will throw a fatal `FileNotFoundError` crash.
* **Duplicate Emails:** If the exact same email appears multiple times inside the raw source text, the current engine will capture and log all duplicates inside `email.txt`.
* **Overwrite Rule:** Every new execution clears old data rows inside `email.txt` and starts logging from scratch.
*
### 🤖 Smart Rule-Based Chatbot & Quiz System (Python)

An interactive, terminal-based **Rule-Based Chatbot** built using Python. This application acts as an educational assistant that can answer technical questions about Artificial Intelligence (AI), Machine Learning (ML), and Computer Networks (CN). Additionally, it features an integrated **Technical Quiz Module** that dynamically tests users and tracks their live performance scores.

---

### 📋 Table of Contents
1. [Core Features](#-core-features)
2. [Project Architecture](#%EF%B8%8F-project-architecture)
3. [Prerequisites & System Setup](#-prerequisites--system-setup)
4. [How to Run](#-how-to-run)
5. [How to Interact & Play](#-how-to-interact--play)
6. [Supported Knowledge Base & Quiz Mapping](#-supported-knowledge-base--quiz-mapping)
7. [Current Code Limitations](#-current-code-limitations)

---

### 🚀 Core Features

* **Intent & Keyword Matching:** Parses user statements to find predefined keywords (e.g., matching "tell me about ai" with the "ai" definition key).
* **Interactive Programming Quiz:** Features 6 distinct technical questions covering core Python, ML, and data libraries.
* **Live Score Ledger:** Tracks student progress globally, incrementing points dynamically for accurate answers.
* **Smart Fallbacks:** Normalizes human input automatically using `.lower()` to process responses accurately regardless of capitalization styles.
* **Clean Session Termination:** Gracefully exits the terminal runtime environment when the user types the specific string keyword `bye`.

---

### 🛠️ Project Architecture

The complete system logic runs out of a single executable flat file:
* `chatbot.py` (Contains the main runtime loop, knowledge base dictionaries, response matchers, and quiz engines)

---

### 🧰 Prerequisites & System Setup

#### Requirements
* **Python 3.x** or higher installed on your operating system.
* Purely relies on native Python data structures (`dictionaries`, `lists`, `functions`). Requires **zero external library installations** (`pip`).

#### Directory Navigation
Fire up your terminal tool or command window and route your path inside your script directory:
```bash
cd path/to/your/chatbot-folder
```

---

### 💻 How to Run

Execute the engine straight out of your terminal using this command:
```bash
python chatbot.py
```

---

### 🎮 How to Interact & Play

#### 💬 Mode 1: General Q&A Chat
When the bot launches, you can ask questions. It reads your input sentence, checks for keywords, and delivers the answer directly.
* *Example Input:* "what is machine learning?"
* *Bot Response:* "machine learning means a computer learn pattern from data..."

#### 🧠 Mode 2: Tech Quiz Mode
Trigger a specialized question instantly by typing any number key from `1` to `6`.
1. The bot prints out the chosen problem statement.
2. The user types their guess into the sub-prompt.
3. The engine performs validations and outputs feedback (`✅ Correct ans` or `❌ Wrong ans`), modifying the live scores.

---

### 📊 Supported Knowledge Base & Quiz Mapping

#### 📚 Chatbot Definitions Library
* **AI / Artificial Intelligence:** Human-like machine thinking technology.
* **ML / Machine Learning:** Finding data patterns to make predictions without explicit hardcoding.
* **CN / Computer Network:** Systems of interconnected devices passing bidirectional data streams.

#### 📝 Core Quiz Keys:
* `1` ➔ Outputs of `print(type(5))` (`<class 'int'>`)
* `2` ➔ Loop running until conditions become false (`while loop`)
* `3` ➔ Function definition keywords (`def`)
* `4` ➔ Meaning of the ML abbreviation (`machine learning`)
* `5` ➔ Most widely deployed AI language (`python`)
* `6` ➔ Core numerical computing framework (`numpy`)

---

### ⚠️ Current Code Limitations (Known Edge Cases)

* **Broken Fallback Logic:** In the initial code block, the variable tracking flag `found` is hardcoded to `True` right inside the loop. As a result, if a user types random characters (e.g., "xyz"), the bot will skip the `if not found:` block and print nothing instead of showing the "sorry, I did not understand" error string message.
* **Exact Matching for Quiz Answers:** The answer engine checks for exact string matches. For example, if the answer is `while loop` and the user types just `while`, the script evaluates it as incorrect.
*
---
---

## 🛠️ Skills Learned
* **Python Programming:** Working with basic syntax, data structures, and terminal interfaces.
* **File Handling:** Reading and writing text/CSV files safely using contextual handlers.
* **Regex (re module):** Implementing complex string pattern matching for automation.
* **Loops and Conditions:** Managing game states, menus, and data validation matrices.
* **Basic Automation:** Building scripts to speed up manual digital tasks.

---

## 👨‍💻 Author
* **Deepak Kushwaha** -

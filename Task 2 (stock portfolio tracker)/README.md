## 📈 Stock Portfolio Tracker (Python & CSV Data Persistence)

An end-to-end, terminal-based **Stock Portfolio Tracker** utility. This console application manages mocked equity transactions, checks real-time inventory lists, calculates dynamic transaction valuations, and automatically exports your finalized asset positions into a persistent, universally readable **CSV spreadsheet**.

---

### 📋 Table of Contents
1. [Core Features](#-core-features)
2. [File Directory Layout](#%EF%B8%8F-file-directory-layout)
3. [Prerequisites & Environment Setup](#-prerequisites--environment-setup)
4. [Step-by-Step Execution Guide](#-step-by-step-execution-guide)
5. [Data Architecture & CSV Mapping](#-data-architecture--csv-mapping)
6. [Detailed Code Workflow](#-detailed-code-workflow)
7. [Technical Safeguards](#-technical-safeguards)

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

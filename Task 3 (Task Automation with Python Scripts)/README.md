## 📧 Automated Email Extractor (Python Text Automation)

A high-utility, regex-powered **Automated Email Extractor** script built with Python. This tool automatically parses through raw, unstructured text files, identifies all valid email addresses using Pattern Matching, and exports them into a clean, line-separated text file.

---

### 📋 Table of Contents
1. [Core Features](#-core-features)
2. [File Directory Structure](#%EF%B8%8F-file-directory-structure)
3. [Prerequisites & Requirements](#-prerequisites--requirements)
4. [Step-by-Step Execution Guide](#-step-by-step-execution-guide)
5. [How the Regex Pattern Works](#-how-the-regex-pattern-works)
6. [Data Workflow & Output Format](#-data-workflow--output-format)
7. [Technical Safeguards & Edge Cases](#-technical-safeguards--edge-cases)

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

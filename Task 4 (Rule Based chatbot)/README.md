## 🤖 Smart Rule-Based Chatbot & Quiz System (Python)

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

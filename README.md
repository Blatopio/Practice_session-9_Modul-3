[README (1).md](https://github.com/user-attachments/files/26368031/README.1.md)
# 🤖 Tanya Aku — ELI10 Bot

A conversational AI chatbot that explains any concept in simple language understandable by a 10-year-old child. Built with LangChain and OpenAI.

---

## 📁 Project Structure

```
Tanya_aku_app/
├── main.py
├── chains/
│   └── explain_chains.py
├── prompts/
│   └── explain_prompt.py
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- OpenAI API Key

Install dependencies:

```bash
pip install langchain langchain-openai langchain-core python-dotenv
```

---

## 🔐 Environment Setup

Create a `.env` file in the root of `Tanya_aku_app/`:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
MODEL=gpt-4o-mini
MAX_TOKENS=1000
TIMEOUT=30
```

> ⚠️ Never share your `.env` file or commit it to GitHub. It is already listed in `.gitignore`.

---

## 🚀 How to Run

```bash
cd Tanya_aku_app
python main.py
```

---

## 💬 How It Works

1. The app starts and displays a welcome banner
2. You type any question or concept you want explained
3. The AI responds in simple, easy-to-understand language (like explaining to a 10-year-old)
4. Type `exit` or `quit` to close the app

---

## 🗂️ File Descriptions

| File | Description |
|------|-------------|
| `main.py` | Entry point — runs the chat loop and handles user input |
| `chains/explain_chains.py` | Sets up the LLM (ChatOpenAI) and chains it with the prompt |
| `prompts/explain_prompt.py` | Defines the PromptTemplate used to instruct the AI |
| `.env` | Stores secret config values like your API key (not committed to Git) |
| `.gitignore` | Tells Git which files to ignore (e.g. `.env`, `.venv`) |

---

## 🧠 Tech Stack

- [LangChain](https://www.langchain.com/) — LLM framework
- [OpenAI GPT-4o-mini](https://platform.openai.com/) — Language model
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management

---

## 👤 Author

Made by Alghi — Purwadhika Bootcamp, Module 3 Session 9

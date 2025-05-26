
# 🧠 AI-Powered Customer Support Agent

This project is an **LLM-driven AI agent** that acts as a **buddy to human customer support agents**, helping them:
- ✉️ Compose and send support emails
- 🧠 Retrieve and summarize similar past case tasks
- 🔍 Pull customer-specific case histories
- 🤖 Extract intent and variables from user prompts using OpenAI

---

## 🚀 How It Works

1. **Client sends a natural language request** (e.g., “Send an update email to John about case 442.”)
2. The **Support Agent uses an LLM** to classify intent + extract relevant fields
3. Based on the intent, it **routes the task to the correct utility function**
4. The response is returned as **structured JSON** (summary, email content, list of past cases, etc.)

---

## 🧱 Architecture Overview

- **Framework**: FastAPI
- **LLM**: OpenAI GPT-3.5
- **Email**: SendGrid API
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **Vector/RAG (optional)**: Add ChromaDB later for similar case retrieval

Upward Flow diagram : 

![Upward Flow diagram](<./Upward Flow.png>)

Complete Flow Diagram : 

![Complete Flow Diagram](<./Complete Flow.png>)



---

## 📁 Project Structure

```

support\_ai\_agent/
├── app/
│   ├── main.py               # FastAPI entry
│   ├── api/routes.py         # POST /support-agent
│   ├── agent/                # AI agent logic
│   │   ├── support\_agent.py
│   │   ├── function\_router.py
│   │   └── prompts/          # Prompt templates
│   ├── db/                   # SQLAlchemy models + session
│   ├── utilities/            # Logic: email, summarizer, case fetcher
│   ├── schema/models.py      # Pydantic request/response
│   ├── config.py             # API keys & DB URL
│   └── constants.py          # Enums/intents
├── requirements.txt
└── .env

````

---

## 🛠️ Setup Instructions

1. **Clone Repo**  
   ```bash
   git clone https://github.com/yourname/support-ai-agent.git
   cd support-ai-agent
````

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up `.env`**

   ```env
   OPENAI_API_KEY=sk-...
   SENDGRID_API_KEY=SG-...
   FROM_EMAIL=support@example.com
   DATABASE_URL=postgresql://user:pass@localhost:5432/support_db
   ```

4. **Run Server**

   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🧪 Example Request

```bash
curl -X POST http://localhost:8000/support-agent \
  -H "Content-Type: application/json" \
  -d '{"user_prompt": "Send an update email to John about ticket 442"}'
```

---

## 🧩 Extending

* Add a **RAG system** (ChromaDB or FAISS) in `fetch_similar_cases`
* Add **LangChain tools** for smarter tool-use
* Use **LangGraph or workflow agents** for multi-step decisions

---


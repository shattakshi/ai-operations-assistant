# AI Operations Assistant

A production-style multi-agent AI system that accepts natural language tasks, plans execution steps, calls real-world APIs, and returns structured results.

This project demonstrates agent-based reasoning, LLM orchestration, and tool execution in a modular architecture.

---

## 🚀 Features

- Multi-agent architecture (Planner, Executor, Verifier)
- LLM-powered reasoning using Groq (Llama)
- Integration with real third-party APIs:
  - GitHub API
  - OpenWeather API
- Structured JSON responses
- FastAPI backend with interactive Swagger UI
- Runnable locally with a single command

---

## 🧠 Architecture Overview

The system follows a production-style orchestration pattern:

User Task
↓
Planner Agent → Generates a step-by-step execution plan
↓
Executor Agent → Calls external APIs based on the plan
↓
Verifier Agent → Validates outputs and detects failures
↓
Structured Response


### Agents

**Planner Agent**
- Uses an LLM to interpret natural language tasks
- Selects appropriate tools
- Produces a structured execution plan

**Executor Agent**
- Iterates through plan steps
- Invokes GitHub and Weather APIs
- Collects tool outputs

**Verifier Agent**
- Checks execution results
- Detects tool failures
- Ensures response completeness

---

## 📂 Project Structure

ai_ops_assistant/
│
├── agents/
│ planner.py
│ executor.py
│ verifier.py
│
├── tools/
│ github_tool.py
│ weather_tool.py
│
├── llm/
│ llm_config.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd ai_ops_assistant
2️⃣ Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate
(Mac/Linux)

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure environment variables
Create a .env file using .env.example.

GROQ_API_KEY=your_key_here
WEATHER_API_KEY=your_key_here
5️⃣ Run the application
uvicorn main:app --reload
✅ Access Swagger UI
Open:

http://127.0.0.1:8000/docs
From here you can test the assistant interactively.

🧪 Example Prompts
Try these tasks:

Example 1

Find the top 3 AI repositories on GitHub and tell me the weather in Delhi.
Example 2

Get trending machine learning repositories and check the weather in Bangalore.
Example 3

Search for Python repositories and provide the current weather in Mumbai.
Example 4

Find popular data science repositories and tell me the weather in New York.
Example 5

Get top deep learning GitHub projects and the weather in London.
🔌 Integrated APIs
✅ GitHub API
Repository search

Star metrics

Descriptions

✅ OpenWeather API
Real-time weather data

Temperature

Humidity

Conditions

⚠️ Known Limitations / Tradeoffs
Planner relies on LLM JSON formatting.

No retry mechanism for failed API calls (can be added for production).

Sequential tool execution (parallelization is a future improvement).

No response caching.

🔮 Future Improvements
Retry logic for API failures

Parallel tool execution

Response caching

Cost tracking per request

Streaming responses

🎯 Design Philosophy
This project implements a modular multi-agent orchestration pattern commonly used in modern AI systems.

The focus was on:

Clear agent separation

Tool-driven execution

Structured outputs

Production-style backend design

✅ One-Command Run
uvicorn main:app --reload
Author
Shatakshi Tiwari


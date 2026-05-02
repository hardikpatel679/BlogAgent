# 🤖 BlogAgent

> An AI-powered blog generation system built with **LangGraph**, **LangChain**, **Groq LLM**, and **FastAPI** — capable of autonomously researching, drafting, and returning structured blog content via a REST API.

---

## 📌 Overview

BlogAgent is an agentic AI application that accepts a blog topic through an HTTP endpoint and autonomously generates a complete blog post using a multi-step LangGraph agent pipeline. The agent leverages **Groq's ultra-fast LLM inference** and LangChain's ecosystem to plan, write, and refine content — all orchestrated as a stateful graph.

This project demonstrates practical experience with:

- **Agentic AI workflows** using LangGraph's stateful graph abstraction
- **LLM integration** via LangChain and Groq (`langchain-groq`)
- **Production API design** with FastAPI and async request handling
- **Clean modular architecture** separating LLM config, graph logic, and API concerns
- **Observability** via LangSmith tracing

---

## 🏗️ Architecture

```
BlogAgent/
├── api.py                  # FastAPI app — REST endpoint & orchestration entry point
├── main.py                 # CLI entry point
├── src/
│   ├── llm/
│   │   └── groqllm.py      # Groq LLM factory — wraps langchain-groq initialization
│   └── graph/
│       └── agent_graph.py  # LangGraph agent graph — defines nodes, edges, and state
├── pyproject.toml          # Project metadata & pinned dependencies (uv)
├── requirement.txt         # pip-compatible dependency list
└── request.json            # Sample API request payload
```

### Request Flow

```
POST /blogs  →  FastAPI  →  Groq_LLM.get_llm()  →  Agent_Graph.build_blog_graph()
                                                          │
                                                    LangGraph Graph
                                                    (compile + invoke)
                                                          │
                                                    ← Structured blog state returned
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI + Uvicorn |
| LLM Provider | Groq (`llama3` / configurable) |
| LLM Orchestration | LangChain, LangChain-Core, LangChain-Community |
| Agent Framework | LangGraph (stateful graph execution) |
| Observability | LangSmith |
| Package Manager | `uv` (with `pyproject.toml`) |
| Python Version | 3.14+ |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- A [Groq API key](https://console.groq.com/) — free tier available
- A [LangSmith API key](https://smith.langchain.com/) (optional, for tracing)

### Installation

```bash
# Clone the repository
git clone https://github.com/hardikpatel679/BlogAgent.git
cd BlogAgent

# Install dependencies using uv (recommended)
pip install uv
uv sync

# Or install via pip
pip install -r requirement.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here   # optional — enables LangSmith tracing
```

### Running the API

```bash
# Start the FastAPI server
python api.py
```

The server will start at `http://0.0.0.0:8000` with hot-reload enabled.

---

## 📡 API Reference

### `POST /blogs`

Generate a complete blog post on the given topic.

**Request Body**

```json
{
  "topic": "The future of AI agents in mobile development"
}
```

**Response**

```json
{
  "status": "success",
  "blog_details": {
    "topic": "The future of AI agents in mobile development",
    "title": "...",
    "content": "...",
    ...
  }
}
```

**Error Response**

```json
{
  "status": "error",
  "message": "Missing or invalid JSON body"
}
```

---

## 🔍 Key Design Decisions

**LangGraph for agent orchestration** — Rather than a simple chain, the agent is modelled as a stateful graph. This allows conditional branching, multi-step reasoning (research → outline → draft → refine), and clean state propagation across nodes without manually threading context.

**Groq as the LLM backend** — Groq's hardware-accelerated inference delivers significantly lower latency than standard cloud LLM endpoints, making it well-suited for agentic loops where multiple LLM calls occur in sequence.

**Separation of concerns** — LLM instantiation (`src/llm/`), graph construction (`src/graph/`), and API routing (`api.py`) are kept in separate layers, making the system easy to extend — e.g. swapping Groq for OpenAI or adding new graph nodes requires changes in exactly one place.

**LangSmith tracing** — The `LANGSMITH_API_KEY` environment variable is wired up at startup, enabling full trace visibility into each graph execution for debugging and evaluation.

---

## 📦 Dependencies

```toml
fastapi>=0.136.1
langchain>=1.2.17
langchain-community>=0.4.1
langchain-core>=1.3.2
langchain-groq>=1.1.2
langgraph>=1.1.10
langgraph-cli[inmem]>=0.4.24
uvicorn>=0.46.0
watchdog>=6.0.0
```

---

## 🗺️ Roadmap

- [ ] Add streaming response support (`StreamingResponse`)
- [ ] Expose graph visualization endpoint using LangGraph's built-in tooling
- [ ] Add tone/length/audience parameters to the blog request
- [ ] Integrate web search tool node for grounded, fact-checked content
- [ ] Dockerize for one-command deployment
- [ ] Add LangSmith evaluation dataset for output quality benchmarking

---

## 👤 Author

**Hardik Patel** — Senior Android Engineer with 12+ years of production experience, exploring AI agent systems and LLM-powered backend development.

- GitHub: [@hardikpatel679](https://github.com/hardikpatel679)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

# Day 2 Live — AI Agents for DevOps

The code we build in the Day 2 live session, kept deliberately small.

Day 1 turned DevOps functions into an API. Day 2 turns functions into tools an
AI agent can call. The agent has just two tools:

1. Read a log file and count INFO / WARNING / ERROR lines.
2. List the Docker containers running on this machine (using `subprocess`).

The rule that keeps it reliable: the tool does the work, the LLM writes the
story. The log function is plain Python and unit-tested without any LLM; the
agent only decides which tool to call and summarizes the result.

## Files

- `devops_tools.py` — the two functions: `count_log_levels` and `list_containers`.
- `agent.py` — wraps them as tools and builds the agent with `create_agent`.
- `test_tools.py` — tests for the log function (no Ollama, no Docker needed).
- `app.log` — sample log (INFO=10, WARNING=2, ERROR=3).

## Prerequisites

[Ollama](https://ollama.com) running with a model pulled:

```bash
ollama serve
ollama pull llama3.2
curl http://localhost:11434/api/tags
```

Docker is only needed for the container tool. Without it, that tool returns a
friendly "Docker is not installed" message instead of crashing.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run it

```bash
python -m pytest .     # the log function (no Ollama needed)
python agent.py        # the agent - it decides which tools to call
```

`llama3.2` calls tools reliably but its summaries can be generic. For sharper
output, pull a stronger model and set `OLLAMA_MODEL`:

```bash
OLLAMA_MODEL=qwen3-coder:30b python agent.py
```

## Practice

1. Ask the agent only about logs, then only about Docker — watch which tool it picks.
2. Add a third tool (e.g. return the last N lines of a log) and try it.
3. Change `list_containers` to also show stopped containers (`docker ps -a`).
4. Bonus: expose the agent behind a FastAPI `/ask` endpoint (reuse Day 1's pattern).

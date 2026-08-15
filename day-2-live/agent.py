# A tiny local DevOps agent with two tools: read logs, and list Docker containers.
#   python agent.py
# Set OLLAMA_MODEL to switch models (default llama3.2).

import os
from pathlib import Path

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from devops_tools import LEVELS, count_log_levels, list_containers, read_log_file

APP_LOG = str(Path(__file__).parent / "app.log")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")

SYSTEM_PROMPT = (
    "You are a DevOps assistant. Use analyze_logs for exact log counts and "
    "list_docker_containers to see what is running - never guess. "
    "Report the facts, then give a short plain-English summary. "
    "Suggest actions only, never run them."
)


@tool
def analyze_logs(path: str) -> str:
    """Count INFO, WARNING and ERROR lines in a log file."""
    counts = count_log_levels(read_log_file(path))
    return ", ".join(f"{level}={counts[level]}" for level in LEVELS)


@tool
def list_docker_containers() -> str:
    """List the Docker containers currently running on this machine."""
    return list_containers()


TOOLS = [analyze_logs, list_docker_containers]


def make_model():
    return ChatOllama(model=MODEL, base_url="http://localhost:11434", temperature=0)


def main():
    print(f"Model: {MODEL}")
    agent = create_agent(make_model(), tools=TOOLS, system_prompt=SYSTEM_PROMPT)

    question = (
        f"Check the log file at {APP_LOG}, then tell me which Docker containers are "
        "running. Summarize how things look."
    )
    result = agent.invoke(
        {"messages": [HumanMessage(content=question)]},
        {"recursion_limit": 10},
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()

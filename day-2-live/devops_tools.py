# Two plain DevOps functions. The log one has no LLM and no Docker, so it's easy to test.

import subprocess
from collections import Counter
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")


def read_log_file(path):
    return Path(path).read_text(encoding="utf-8")


def count_log_levels(text):
    counts = Counter()
    for line in text.splitlines():
        tokens = set(line.split())
        for level in LEVELS:
            if level in tokens:
                counts[level] += 1
    return {level: counts.get(level, 0) for level in LEVELS}


def list_containers():
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}} | {{.Status}} | {{.Image}}"],
            capture_output=True,
            text=True,
            timeout=10,
        )
    except FileNotFoundError:
        return "Docker is not installed or not on PATH."

    if result.returncode != 0:
        return f"docker error: {result.stderr.strip()}"

    output = result.stdout.strip()
    return output if output else "No running containers."

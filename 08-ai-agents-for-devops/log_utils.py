# Plain functions for counting log levels. No LLM here, so it's easy to test.

from collections import Counter
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")


def count_log_levels(text):
    """Count INFO/WARNING/ERROR lines. Matches whole words so "no errors" in a
    message doesn't get counted as an ERROR."""
    counts = Counter()
    for line in text.splitlines():
        tokens = set(line.split())
        for level in LEVELS:
            if level in tokens:
                counts[level] += 1
    return {level: counts.get(level, 0) for level in LEVELS}


def read_log_file(path):
    return Path(path).read_text(encoding="utf-8")

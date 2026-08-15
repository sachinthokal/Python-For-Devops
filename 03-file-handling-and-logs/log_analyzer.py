# Read a log, count levels, write a summary. Plain functions, no classes.

import json
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")
LOG_FILE = Path(__file__).parent / "app.log"


def read_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Log file not found: {path}")
        return []


def count_levels(lines):
    counts = {level: 0 for level in LEVELS}
    for line in lines:
        tokens = set(line.split())
        for level in LEVELS:
            if level in tokens:
                counts[level] += 1
    return counts


def write_summary(counts, stem="log_summary"):
    here = Path(__file__).parent
    with open(here / f"{stem}.txt", "w", encoding="utf-8") as f:
        for level in LEVELS:
            f.write(f"{level}: {counts[level]}\n")
    with open(here / f"{stem}.json", "w", encoding="utf-8") as f:
        json.dump(counts, f, indent=2)


def main():
    lines = read_lines(LOG_FILE)
    if not lines:
        print("No logs to analyze.")
        return

    counts = count_levels(lines)

    print("Log Analysis Summary")
    print("--------------------")
    for level in LEVELS:
        print(f"{level:7}: {counts[level]}")

    write_summary(counts)
    print("Wrote log_summary.txt and log_summary.json")


if __name__ == "__main__":
    main()

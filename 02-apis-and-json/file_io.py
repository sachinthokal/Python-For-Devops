# Reading and writing files, including JSON.

import json
from pathlib import Path

DEMO_TXT = Path(__file__).parent / "demo.txt"
DEMO_JSON = Path(__file__).parent / "demo.json"


def write_text():
    with open(DEMO_TXT, "w", encoding="utf-8") as f:
        f.write("Hello Dosto, kya haal chaal\n")
        f.write("This file was written by Python.\n")


def read_text():
    with open(DEMO_TXT, "r", encoding="utf-8") as f:
        print("--- demo.txt ---")
        print(f.read())


def write_json():
    data = {"tool": "python", "purpose": "devops", "clouds": ["aws", "azure"]}
    with open(DEMO_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def read_json():
    with open(DEMO_JSON, "r", encoding="utf-8") as f:
        print("--- demo.json ---")
        print(json.load(f))


if __name__ == "__main__":
    write_text()
    read_text()
    write_json()
    read_json()

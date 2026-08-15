# Checks your environment is ready for the course.  Run: python check_setup.py

import importlib.util
import json
import sys
import urllib.request

# (pip name, import name) for every package the course uses
PACKAGES = [
    ("psutil", "psutil"),
    ("requests", "requests"),
    ("boto3", "boto3"),
    ("fastapi", "fastapi"),
    ("uvicorn", "uvicorn"),
    ("langchain", "langchain"),
    ("langchain-core", "langchain_core"),
    ("langchain-ollama", "langchain_ollama"),
    ("langgraph", "langgraph"),
    ("pytest", "pytest"),
]


def check_python():
    v = sys.version_info
    ok = v >= (3, 10)
    mark = "ok" if ok else "!!"
    print(f"[{mark}] Python {v.major}.{v.minor}  (need 3.10+)")
    return ok


def check_packages():
    missing = []
    for pip_name, module in PACKAGES:
        found = importlib.util.find_spec(module) is not None
        print(f"[{'ok' if found else '!!'}] {pip_name}")
        if not found:
            missing.append(pip_name)
    return missing


def check_ollama():
    # Only needed for module 08, so this is a soft check — never fails the script.
    try:
        with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=2) as r:
            models = [m.get("name", "") for m in json.load(r).get("models", [])]
    except Exception:
        print("[..] Ollama not reachable (only needed for module 08)  ->  run: ollama serve")
        return
    print(f"[ok] Ollama is running ({len(models)} model(s))")
    if any(m.startswith("llama3.2") for m in models):
        print("[ok] llama3.2 is pulled")
    else:
        print("[..] llama3.2 not pulled  ->  run: ollama pull llama3.2")


def main():
    print("Checking your environment...\n")
    py_ok = check_python()
    print()
    missing = check_packages()
    print()
    check_ollama()
    print()

    if not py_ok:
        print("Your Python is too old — install 3.10 or newer.")
    if missing:
        print("Missing packages:", ", ".join(missing))
        print("Install them with:  pip install -r requirements.txt")

    if py_ok and not missing:
        print("All set. You're ready for the course.")
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()

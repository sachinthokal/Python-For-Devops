from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")
DEFAULT_LOG = Path(__file__).parent / "app.log"


def analyze_logs(log_path=None):
    path = Path(log_path) if log_path else DEFAULT_LOG
    counts = {level: 0 for level in LEVELS}
    for line in path.read_text(encoding="utf-8").splitlines():
        tokens = set(line.split())
        for level in LEVELS:
            if level in tokens:
                counts[level] += 1
    return {"log_file": str(path), "counts": counts}


if __name__ == "__main__":
    print(analyze_logs())

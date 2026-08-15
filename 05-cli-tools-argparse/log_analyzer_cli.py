# Log analyzer as a proper CLI tool with argparse.
#   python log_analyzer_cli.py --file app.log
#   python log_analyzer_cli.py --file app.log --out summary.json --level ERROR

import argparse
import json
import sys
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")


def count_levels(lines):
    counts = {level: 0 for level in LEVELS}
    for line in lines:
        tokens = set(line.split())
        for level in LEVELS:
            if level in tokens:
                counts[level] += 1
    return counts


def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze a log file and count INFO / WARNING / ERROR lines.",
    )
    parser.add_argument("--file", required=True, help="path to the log file")
    parser.add_argument("--out", help="write the summary to this JSON file")
    parser.add_argument(
        "--level",
        choices=LEVELS,
        help="show the count for only this level",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    log_path = Path(args.file)
    if not log_path.is_file():
        print(f"Error: log file not found: {args.file}", file=sys.stderr)
        sys.exit(2)   # non-zero exit tells the shell / CI it failed

    counts = count_levels(log_path.read_text(encoding="utf-8").splitlines())

    if args.level:
        print(f"{args.level}: {counts[args.level]}")
    else:
        for level in LEVELS:
            print(f"{level:7}: {counts[level]}")

    if args.out:
        Path(args.out).write_text(json.dumps(counts, indent=2), encoding="utf-8")
        print(f"Wrote summary to {args.out}")


if __name__ == "__main__":
    main()

# Building CLI Tools with argparse

`kubectl`, `terraform`, `aws`, `helm` — a lot of the DevOps world runs on CLIs.
This module turns the log analyzer into a real command-line tool using Python's
built-in [`argparse`](https://docs.python.org/3/library/argparse.html).

## Files

- `app.log` — sample log
- `log_analyzer_cli.py` — the CLI tool

```bash
python log_analyzer_cli.py --file app.log
python log_analyzer_cli.py --file app.log --out summary.json
python log_analyzer_cli.py --file app.log --level ERROR
python log_analyzer_cli.py --help
```

If the file is missing it prints a friendly error and exits with code 2:

```
$ python log_analyzer_cli.py --file nope.log
Error: log file not found: nope.log
```

## Practice

Build the CLI yourself:

1. Required `--file` argument.
2. Optional `--out` (output JSON path) and `--level` (INFO/WARNING/ERROR).
3. If `--file` doesn't exist, print an error and `sys.exit(2)`.
4. Count the levels and print the summary (or just `--level` if given).
5. If `--out` is set, write the counts as JSON.

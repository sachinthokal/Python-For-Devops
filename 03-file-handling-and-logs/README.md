# File Handling & Log Analysis

Logs are usually the first place you look when something breaks. This module
covers reading a log file and turning it into a summary — count the
`INFO` / `WARNING` / `ERROR` lines, print them, and write the result to `.txt`
and `.json`.

Pure standard library, no dependencies.

## Files

- `app.log` — sample log
- `log_analyzer.py` — reads the log, counts levels, writes a summary

```bash
python log_analyzer.py
```

Expected counts for the bundled log: `INFO=10, WARNING=2, ERROR=3`.

We match a level when the word appears as a token on the line (the word `ERROR`),
not as any substring, so a message like `no errors found` isn't miscounted.

## Practice

Write your own log analyzer:

1. Read `app.log` line by line.
2. Count how many lines contain `INFO`, `WARNING`, and `ERROR`.
3. Print a summary and write it to `log_summary.json`.
4. Bonus: handle the file being missing (`FileNotFoundError`) without crashing.

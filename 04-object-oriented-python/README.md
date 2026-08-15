# Object-Oriented Python for DevOps

Automation scripts grow into tools, and tools need structure. This module
refactors the log analyzer into a class — the way a lot of internal DevOps tools
are built. Same behaviour as
[03-file-handling-and-logs](../03-file-handling-and-logs), now with state in
`__init__` and behaviour in methods. Light, practical OOP — no inheritance or
abstract classes.

## Files

- `app.log` — sample log
- `log_analyzer_oop.py` — the `LogAnalyzer` class

```bash
python log_analyzer_oop.py
```

Expected: `INFO=10, WARNING=2, ERROR=3` for the bundled log.

## Practice

Build the `LogAnalyzer` class yourself:

1. In `__init__`, store the log file path and set up a `counts` dict.
2. `read_logs()` returns the file's lines (handle a missing file).
3. `analyze()` counts `INFO` / `WARNING` / `ERROR` — check `LEVEL in tokens`.
4. Create an object and print the summary.
5. Bonus: add a `write_summary()` method that dumps `counts` to JSON.

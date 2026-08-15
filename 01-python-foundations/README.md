# Python Foundations for DevOps

The Python fundamentals you actually need for automation — variables, data
types, conditionals, loops, and functions — used to build a real DevOps script:
a system health checker that reads CPU, memory, and disk usage and compares them
against thresholds.

## What you'll learn

- Variables, data types, operators, and type casting
- `if / elif / else`, `for` and `while` loops
- Writing functions
- Reading live system metrics with [`psutil`](https://pypi.org/project/psutil/)
- Basic `try / except` error handling

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Files

- `variables.py` — variables, data types, operators
- `control_flow.py` — if/else and loops
- `functions.py` — functions
- `system_health.py` — the main one: CPU/memory/disk health report

```bash
python variables.py
python system_health.py
```

`system_health.py` prints something like:

```
=== System Health Report ===
CPU    : 12.4%  -> Healthy
Memory : 63.1%  -> Healthy
Disk   : 78.0%  -> WARNING (above 75%)
Overall: NEEDS ATTENTION
```

## Practice

Write your own `system_health.py` from scratch:

1. Ask the user for a CPU threshold with `input()` and cast it to a number.
2. Read current CPU usage with `psutil.cpu_percent(interval=1)`.
3. Print whether the CPU is healthy or over the threshold.
4. Bonus: also check memory (`psutil.virtual_memory().percent`) and disk
   (`psutil.disk_usage("/").percent`).
5. Bonus: wrap the input in `try / except ValueError` so bad input doesn't crash it.

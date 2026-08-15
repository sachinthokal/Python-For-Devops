# Working with APIs & JSON

Clouds, Kubernetes, monitoring and CI/CD all speak HTTP and JSON, so calling
APIs is a big part of DevOps automation. This module covers how to call them and
handle their data in Python with the [`requests`](https://docs.python-requests.org/)
library.

## What you'll learn

- Call a public API with `requests.get()` and parse JSON with `.json()`
- Work with `list`, `dict`, and `set`
- Read and write files, including JSON
- Keep API keys out of source code using environment variables

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Files

- `collections_demo.py` — list / dict / set basics
- `call_api.py` — fetch and filter a JSONPlaceholder todo
- `jokes_api.py` — switch between two endpoints at runtime
- `file_io.py` — read/write text and JSON files
- `stock_market_api.py` — a real API using a key from an env var

```bash
python collections_demo.py
python call_api.py

# stock_market_api needs a free Alpha Vantage key
export ALPHAVANTAGE_API_KEY="your_key_here"
python stock_market_api.py
```

Never hardcode API keys in source — `stock_market_api.py` reads the key from
`ALPHAVANTAGE_API_KEY`. Get a free key at
https://www.alphavantage.co/support/#api-key

## Practice

Fetch a GitHub user and save it to JSON:

1. Call `https://api.github.com/users/<username>`.
2. Print `name`, `public_repos`, `followers`, `location`.
3. Save the full response to `github_user.json` with `json.dump(..., indent=2)`.
4. Bonus: handle a non-existent user (GitHub returns 404) with
   `response.raise_for_status()` inside a `try / except`.

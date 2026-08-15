# Day 1 Live — AWS Boto3 + FastAPI

The code we build in the Day 1 live session. One idea runs through all of it:

You write plain Python functions that do DevOps work, and those same functions
get a second front door — an HTTP API — without changing the logic.

## Files

- `aws_functions.py` — boto3 helpers (`list_buckets`, `s3_summary`, `ec2_summary`,
  `find_public_buckets`) plus a `main()` that prints a report and writes
  `aws_report.json`. With no AWS credentials it returns labelled demo data, so it
  runs on any laptop.
- `metrics.py` — `get_system_metrics()` using psutil.
- `logs.py` — `analyze_logs()` counting INFO / WARNING / ERROR in a log file.
- `hello_api.py` — the smallest FastAPI app, to learn the basics.
- `api.py` — the DevOps Utilities API. It imports the functions above and exposes
  them as endpoints. This is the "second front door".
- `app.log` — sample log (INFO=10, WARNING=2, ERROR=3).
- `Dockerfile` — ship the API as a container.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The `/aws/*` endpoints and the report work without an AWS account — with no
credentials they return labelled demo data (look for `"demo": true`). Configure
credentials when you want real results:

```bash
aws configure   # or export AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_DEFAULT_REGION
```

## First front door: functions and a report

```bash
python aws_functions.py     # prints an S3 + EC2 report, writes aws_report.json
python metrics.py           # CPU / memory / disk
python logs.py              # log-level counts
```

Everything here reads from AWS only. Nothing is created, modified, or deleted.

## Second front door: the same functions over HTTP

Warm up with the tiny app:

```bash
uvicorn hello_api:app --reload
# open http://127.0.0.1:8000/docs
```

Then the utilities API:

```bash
uvicorn api:app --reload
```

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/metrics
curl "http://127.0.0.1:8000/metrics?cpu_threshold=50"
curl http://127.0.0.1:8000/logs
curl http://127.0.0.1:8000/aws/s3              # buckets, new vs old
curl http://127.0.0.1:8000/aws/ec2             # instances + state
curl http://127.0.0.1:8000/aws/public-buckets  # security check: which buckets are public
```

The `/aws/*` endpoints return demo data when no credentials are set, so they
respond even without an AWS account.

Interactive docs: http://127.0.0.1:8000/docs

## Docker

```bash
docker build -t devops-utilities-api .
docker run -p 8000:8000 devops-utilities-api
curl http://127.0.0.1:8000/health
```

## Practice

1. Add a `/version` endpoint returning `{"version": "1.0.0"}`.
2. Add `/logs/errors` returning only the ERROR count (reuse `analyze_logs`).
3. Add a `/aws/buckets` endpoint returning just bucket names (reuse `list_buckets`).
4. Bonus: build the Docker image and hit `/health`.

This flat layout keeps the live session simple. A larger project would split the
logic into `services/` and the HTTP layer into `routers/` — see
`07-apis-with-fastapi/devops-utilities-api/`.

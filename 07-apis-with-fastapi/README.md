# Building DevOps APIs with FastAPI

Teams often trigger automation, health checks, and reporting through APIs. This
module turns your Python logic into a real HTTP service with
[FastAPI](https://fastapi.tiangolo.com/).

Start with a one-file "hello" API, then study a full Internal DevOps Utilities
API that exposes system metrics, log analysis, and AWS info — with routers,
services, auto-generated docs, and a Dockerfile.

## What you'll learn

- Build an API with FastAPI and run it with `uvicorn`
- The request/response flow and JSON responses
- Organize a real app into `routers/` (HTTP) and `services/` (logic)
- Reuse the log-analyzer and metrics logic from earlier modules
- Explore the auto-generated Swagger docs at `/docs`

## Files

- `hello_api.py` — the smallest possible FastAPI app
- `devops-utilities-api/` — the full app (routers, services, Dockerfile)

## Quick start

```bash
pip install fastapi uvicorn psutil boto3
uvicorn hello_api:app --reload
# open http://127.0.0.1:8000/docs
```

## The full app

```bash
cd devops-utilities-api
pip install -r requirements.txt
python main.py           # uvicorn on http://0.0.0.0:8000
```

```bash
curl http://127.0.0.1:8000/           # hello
curl http://127.0.0.1:8000/health     # {"status":"ok"}
curl http://127.0.0.1:8000/metrics    # CPU/mem/disk
curl http://127.0.0.1:8000/logs       # analyze bundled app.log
curl http://127.0.0.1:8000/aws/s3     # needs AWS creds
```

Interactive docs: http://127.0.0.1:8000/docs

## Practice

Extend the utilities API (work in `devops-utilities-api/`):

1. Add a `/version` endpoint returning `{"version": "1.2.0"}`.
2. Add `/logs/errors` returning only the ERROR count (reuse `services/logs_service.py`).
3. Add a `cpu_threshold` query param to `/metrics` (e.g. `/metrics?cpu_threshold=50`).
4. Bonus: build the Docker image and hit `/health`.

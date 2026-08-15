# The same functions from aws_functions / metrics / logs, now exposed over HTTP.
# Run: uvicorn api:app --reload  then open /docs

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from fastapi import FastAPI, HTTPException

from aws_functions import ec2_summary, find_public_buckets, s3_summary
from logs import analyze_logs
from metrics import get_system_metrics

app = FastAPI(title="DevOps Utilities API", version="1.0.0")


@app.get("/")
def hello():
    return {"message": "Day 1 DevOps Utilities API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics(cpu_threshold: int = 85):
    return get_system_metrics(cpu_threshold)


@app.get("/logs")
def logs():
    return analyze_logs()


@app.get("/aws/s3")
def aws_s3():
    try:
        return s3_summary(boto3.Session())
    except (BotoCoreError, ClientError) as exc:
        raise HTTPException(status_code=502, detail=f"AWS error: {exc}")


@app.get("/aws/ec2")
def aws_ec2():
    try:
        return {"instances": ec2_summary(boto3.Session())}
    except (BotoCoreError, ClientError) as exc:
        raise HTTPException(status_code=502, detail=f"AWS error: {exc}")


@app.get("/aws/public-buckets")
def aws_public_buckets():
    try:
        return find_public_buckets(boto3.Session())
    except (BotoCoreError, ClientError) as exc:
        raise HTTPException(status_code=502, detail=f"AWS error: {exc}")

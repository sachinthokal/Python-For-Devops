# AWS Automation with Python (Boto3 + IaC)

AWS is managed with APIs, not clicks. This module shows how Python automates the
cloud with Boto3 (read-only here), plus an intro to Infrastructure as Code with
AWS CDK.

The scripts only read from AWS (list S3 buckets, list EC2 instances). Nothing is
created, modified, or deleted unless you choose to run the optional create
helpers.

## Prerequisites

AWS credentials configured locally:

```bash
aws configure   # or set AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_DEFAULT_REGION
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Files

- `s3_utilities.py` — `AWSUtils` class: list buckets, optional create/upload
- `aws_resource_report.py` — list S3 + EC2 and write `aws_report.json`
- `cdk_demo/` — an Infrastructure-as-Code example: a CDK stack with one S3 bucket

```bash
python aws_resource_report.py
python s3_utilities.py
```

These call real AWS APIs and need valid credentials — without them you'll get a
`NoCredentialsError` / `ClientError`, which is expected.

## Boto3 vs Infrastructure as Code

Boto3 is great for reading state, reporting, and one-off automation. For
creating/updating/deleting infrastructure, prefer IaC tools (Terraform,
CloudFormation, CDK) — they track state and are repeatable. See `cdk_demo/`.

## Practice

Write an AWS resource report:

1. Create a `boto3.Session()` and an S3 client, and list all bucket names.
2. List EC2 instances (instance id + state).
3. Print the report and save it to `aws_report.json`.
4. Bonus: wrap the calls in `try / except (BotoCoreError, ClientError)` so
   missing credentials print a friendly message instead of a traceback.

Read-only only — don't create or delete resources.

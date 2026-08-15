# Read-only AWS report (S3 + EC2) saved as JSON.

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError

OUTPUT = Path(__file__).parent / "aws_report.json"


def s3_summary(session):
    """Summarize S3 buckets, splitting them into new vs. older than 90 days."""
    s3 = session.client("s3")
    buckets = s3.list_buckets().get("Buckets", [])
    cutoff = datetime.now(timezone.utc) - timedelta(days=90)

    new_buckets, old_buckets = [], []
    for bucket in buckets:
        target = old_buckets if bucket["CreationDate"] < cutoff else new_buckets
        target.append(bucket["Name"])

    return {
        "total": len(buckets),
        "new_buckets": new_buckets,
        "old_buckets": old_buckets,
    }


def ec2_summary(session):
    """Return each EC2 instance's id and state."""
    ec2 = session.client("ec2")
    reservations = ec2.describe_instances().get("Reservations", [])
    instances = []
    for reservation in reservations:
        for inst in reservation.get("Instances", []):
            instances.append(
                {"id": inst["InstanceId"], "state": inst["State"]["Name"]}
            )
    return instances


def main():
    session = boto3.Session()
    try:
        report = {
            "s3": s3_summary(session),
            "ec2": ec2_summary(session),
        }
    except (BotoCoreError, ClientError) as exc:
        print("AWS call failed (check your credentials/region):", exc)
        return

    print(json.dumps(report, indent=2))
    OUTPUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nWrote {OUTPUT.name}")


if __name__ == "__main__":
    main()

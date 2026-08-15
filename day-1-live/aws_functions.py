# Read-only AWS helpers. Each returns a plain dict/list so any caller can reuse them.
# No AWS credentials? Every function falls back to labelled demo data so you can still run it.

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError

OUTPUT = Path(__file__).parent / "aws_report.json"

PUBLIC_ACL_URIS = (
    "http://acs.amazonaws.com/groups/global/AllUsers",
    "http://acs.amazonaws.com/groups/global/AuthenticatedUsers",
)


def has_credentials(session):
    return session.get_credentials() is not None


def list_buckets(session):
    if not has_credentials(session):
        return ["demo-app-logs", "demo-artifacts", "demo-legacy-backups"]
    s3 = session.client("s3")
    return [bucket["Name"] for bucket in s3.list_buckets().get("Buckets", [])]


def s3_summary(session):
    if not has_credentials(session):
        return {
            "demo": True,
            "total": 3,
            "new_buckets": ["demo-app-logs", "demo-artifacts"],
            "old_buckets": ["demo-legacy-backups"],
        }

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
    if not has_credentials(session):
        return [
            {"id": "i-0demo1111", "state": "running"},
            {"id": "i-0demo2222", "state": "stopped"},
        ]

    ec2 = session.client("ec2")
    reservations = ec2.describe_instances().get("Reservations", [])
    instances = []
    for reservation in reservations:
        for inst in reservation.get("Instances", []):
            instances.append({"id": inst["InstanceId"], "state": inst["State"]["Name"]})
    return instances


def bucket_is_public(s3, name):
    acl = s3.get_bucket_acl(Bucket=name)
    for grant in acl.get("Grants", []):
        if grant.get("Grantee", {}).get("URI", "") in PUBLIC_ACL_URIS:
            return True
    try:
        status = s3.get_bucket_policy_status(Bucket=name)
        if status["PolicyStatus"]["IsPublic"]:
            return True
    except ClientError:
        pass
    return False


def find_public_buckets(session):
    if not has_credentials(session):
        return {"demo": True, "public_buckets": ["demo-public-website"], "count": 1}

    s3 = session.client("s3")
    public = []
    for bucket in s3.list_buckets().get("Buckets", []):
        name = bucket["Name"]
        try:
            if bucket_is_public(s3, name):
                public.append(name)
        except ClientError:
            continue
    return {"public_buckets": public, "count": len(public)}


def main():
    session = boto3.Session()
    if not has_credentials(session):
        print("No AWS credentials found — showing demo data. Run `aws configure` for real results.\n")

    try:
        report = {
            "buckets": list_buckets(session),
            "s3": s3_summary(session),
            "ec2": ec2_summary(session),
            "public_buckets": find_public_buckets(session),
        }
    except (BotoCoreError, ClientError) as exc:
        print("AWS call failed (check your credentials/region):", exc)
        return

    print(json.dumps(report, indent=2))
    OUTPUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nWrote {OUTPUT.name}")


if __name__ == "__main__":
    main()

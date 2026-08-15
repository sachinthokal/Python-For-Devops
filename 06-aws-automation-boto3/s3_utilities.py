# S3/EC2 helpers. The read operations are safe; create/upload only run when you call them.

import boto3
from botocore.exceptions import BotoCoreError, ClientError


class AWSUtils:
    def __init__(self, region=None):
        session = boto3.Session(region_name=region)
        self.s3 = session.client("s3")
        self.ec2 = session.client("ec2")

    def list_buckets(self):
        response = self.s3.list_buckets()
        return [bucket["Name"] for bucket in response.get("Buckets", [])]

    def list_regions(self):
        response = self.ec2.describe_regions()
        return [region["RegionName"] for region in response.get("Regions", [])]

    def create_bucket(self, bucket_name, region="us-west-2"):
        try:
            self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
            print(f"Bucket created: {bucket_name}")
        except ClientError as exc:
            print(f"Could not create bucket '{bucket_name}': {exc}")

    def upload_file(self, file_path, bucket, key):
        self.s3.upload_file(file_path, bucket, key)
        print(f"Uploaded {file_path} -> s3://{bucket}/{key}")


def main():
    try:
        aws = AWSUtils()
        print("S3 buckets:")
        for name in aws.list_buckets():
            print("  -", name)
    except (BotoCoreError, ClientError) as exc:
        print("AWS call failed (check your credentials/region):", exc)


if __name__ == "__main__":
    main()

# Minimal CDK app: declare one S3 bucket and let CDK synth the CloudFormation.
# Try:  cdk synth   (or  cdk deploy  to actually create it)

from aws_cdk import App, Stack
from aws_cdk import aws_s3 as s3
from constructs import Construct


class DemoStack(Stack):
    def __init__(self, scope, construct_id):
        super().__init__(scope, construct_id)

        s3.Bucket(
            self,
            "PythonForDevOpsDemoBucket",
            versioned=True,
        )


app = App()
DemoStack(app, "PythonForDevOpsDemoStack")
app.synth()

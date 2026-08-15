# CDK Demo — Infrastructure as Code (optional)

A tiny AWS CDK app that declares one S3 bucket. The point is to understand the
idea of Infrastructure as Code, not necessarily to deploy it.

## The IaC flow

```
Python (CDK code)  ->  cdk synth  ->  CloudFormation template  ->  AWS resources
```

You describe what you want (a versioned S3 bucket); CDK figures out how to
create it and tracks its state for you.

## Try it (optional)

```bash
npm install -g aws-cdk
pip install aws-cdk-lib constructs

cdk synth      # prints the generated CloudFormation — makes NO changes to AWS
cdk deploy     # optional: actually creates the bucket
cdk destroy    # clean up
```

## Boto3 vs CDK

- Boto3 is imperative ("do this API call"); CDK/Terraform/CloudFormation are
  declarative ("this should exist").
- Boto3 is best for reading state, reporting, and glue scripts; IaC is best for
  creating and managing infrastructure.
- Boto3 doesn't track state; IaC does.

Use Boto3 to observe and automate one-off tasks; use IaC to own your
infrastructure.

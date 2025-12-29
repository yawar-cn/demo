import json
import boto3
import os

s3 = boto3.client("s3")

BUCKET_NAME = os.environ.get("BUCKET_NAME")

def lambda_handler(event, context):
    file_content = "Hello from Lambda + S3 🚀"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key="hello.txt",
        Body=file_content
    )

    return {
        "statusCode": 200,
        "body": json.dumps("File uploaded to S3 successfully")
    }

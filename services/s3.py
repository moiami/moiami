from typing import Optional

import boto3
from botocore.exceptions import ClientError
from django.conf import settings


def get_client():
    return boto3.client(
        's3',
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )


def generate_presigned_url(file_key: str, expiration: int = 3600) -> Optional[str]:
    try:
        client = get_client()
        return client.generate_presigned_url('get_object',Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,'Key': file_key,},ExpiresIn=expiration)
    except ClientError:
        return None


def generate_presigned_post(
        file_key: str,
        content_type: str,
        expiration: int = 3600
) -> Optional[dict]:
    try:
        client = get_client()
        return client.generate_presigned_post(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME,
            Key=file_key,
            Fields={
                'Content-Type': content_type,
                'acl': settings.AWS_DEFAULT_ACL,
            },
            Conditions=[
                {'Content-Type': content_type},
                {'acl': settings.AWS_DEFAULT_ACL},
            ],
            ExpiresIn=expiration,
        )
    except ClientError:
        return None


def delete_file(file_key: str) -> bool:
    try:
        client = get_client()
        client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME,Key=file_key)
        return True
    except ClientError:
        return False

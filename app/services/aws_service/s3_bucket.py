import boto3
from ...core.config import settings
import botocore.exceptions as exe
import json

class S3Manager:
    def __init__(self):
        self.bucket_name = settings.aws_s3_bucket
        self.s3 = boto3.client(
            's3', 
            region_name=settings.aws_region, 
            aws_access_key_id=settings.aws_access_key, 
            aws_secret_access_key=settings.aws_secrect_key
        )

    async def create_bucket(self):
        try:
            # Check if the bucket already exists
            self.s3.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket '{self.bucket_name}' already exists.")
        except exe.ClientError as e:
            if e.response['Error']['Code'] == '404':
                print(f"Bucket '{self.bucket_name}' doesn't exist. Creating...")

                # Create the bucket without specifying an ACL
                self.s3.create_bucket(
                    Bucket=self.bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': settings.aws_region}
                )
                print(f"Bucket '{self.bucket_name}' created successfully.")

                # Define the bucket policy
                bucket_policy = {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": "*",
                            "Action": "s3:GetObject",
                            "Resource": f"arn:aws:s3:::{self.bucket_name}/*"
                        }
                    ]
                }

                # Convert the policy to a JSON string
                bucket_policy_str = json.dumps(bucket_policy)

                # Apply the bucket policy
                self.s3.put_bucket_policy(Bucket=self.bucket_name, Policy=bucket_policy_str)
                print(f"Bucket policy applied for {self.bucket_name}")

                # No need to block public access since it's already public
                print(f"Public access configured for objects in '{self.bucket_name}'.")
            else:
                print(f"Error creating bucket: {e}")

    async def upload_to_s3(self, file, s3_object_name):
        try:
            self.s3.put_object(Body=file, Bucket=self.bucket_name, Key=f"course/{s3_object_name}.png")
            print(f"File uploaded successfully to {self.bucket_name}/course/{s3_object_name}.png")
            return True
        except exe.NoCredentialsError:
            print("AWS credentials not available.")
            return False
        except Exception as e:
            print(f"Error uploading file: {e}")
            return False

# Usage:
# Create an instance of S3Manager and call create_bucket to create the bucket
s3_manager = S3Manager()
# await s3_manager.create_bucket()

# # Example: Upload a file to S3
# local_file_path = 'main.py'
# s3_object_name = 'amar.py'
# await s3_manager.upload_to_s3(local_file_path, s3_object_name)

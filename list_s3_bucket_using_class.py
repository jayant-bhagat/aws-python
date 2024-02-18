import boto3
import os

class S3Manager:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def create_bucket(self):
        try:
            response = self.s3.create_bucket(Bucket=self.bucket_name)
            print(f"Bucket '{self.bucket_name}' created successfully.")
            return response
        except Exception as e:
            print(f"Error creating bucket '{self.bucket_name}': {e}")
            return None

    def upload_file(self, local_file_path, s3_key):
        try:
            self.s3.upload_file(local_file_path, self.bucket_name, s3_key)
            print(f"File '{local_file_path}' uploaded to '{self.bucket_name}' with key '{s3_key}'.")
        except Exception as e:
            print(f"Error uploading file to S3: {e}")

    def list_objects(self):
        try:
            response = self.s3.list_objects_v2(Bucket=self.bucket_name)
            objects = response.get('Contents', [])
            if objects:
                print(f"Objects in bucket '{self.bucket_name}':")
                for obj in objects:
                    print(f"- {obj['Key']}")
            else:
                print(f"No objects found in bucket '{self.bucket_name}'.")
        except Exception as e:
            print(f"Error listing objects in bucket '{self.bucket_name}': {e}")

if __name__ == "__main__":
    bucket_names = ["bucket1", "bucket2", "bucket3"]  # Add your desired bucket names here

    for bucket_name in bucket_names:
        s3_manager = S3Manager(bucket_name)

        # Create bucket
        s3_manager.create_bucket()

        # Upload file to S3 (modify the file path and key as needed)
        local_file_path = "path/to/your/file.txt"
        s3_key = f"{bucket_name}_uploaded-file.txt"
        if os.path.exists(local_file_path):
            s3_manager.upload_file(local_file_path, s3_key)
        else:
            print(f"Local file '{local_file_path}' not found. Please provide a valid file path.")

        # List objects in the bucket
        s3_manager.list_objects()
        print()  # Add a newline for better output separation

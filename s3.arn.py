import boto3

def get_s3_bucket_arn(bucket_name):
   try:
      client =  boto3.client('s3')
      head = client.head_bucket(Bucket=bucket_name)
      print("bucket already exists")
      account_id = boto3.client('sts').get_caller_identity().get('Account')
      arn = f"arn:aws:s3::{account_id}:{bucket_name}"
      return arn
   except client.exceptions.NoSuchBucket:
      print("Bucket does not exist.")
      response = client.create_bucket(Bucket=bucket_name)
      print(response)
   except Exception  as e:
      print(e)

if __name__ == "__main__":
   bucket_name = "mydemo-jayant"
   arn = get_s3_bucket_arn(bucket_name)
   if arn:
      print(f"The ARN of the S3 bucket '{bucket_name}' is: {arn}")
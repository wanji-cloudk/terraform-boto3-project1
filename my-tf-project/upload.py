import boto3

s3 = boto3.client("s3")

s3.upload_file("hello.txt", "wanji-terraform-bucket-254", "hello.txt")
print("Uploaded!")

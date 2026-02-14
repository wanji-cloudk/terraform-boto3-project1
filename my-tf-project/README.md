## AWS S3 -Terraform + boto3
Create an S3 bucket with Terraform, then upload a file with Python
## Make sure you sign up at aws.amazon.com
aws configure credetials
  AWS Access Key ID:      - your key
  AWS Secret Access Key:  - your secret
  Default region name:    us-east-1
  Default output format:  - press Enter


## Files and what they do:
`main.tf` | Creates the S3 bucket on AWS 
`upload.py` | Uploads a file to the bucket 

## Setup 
1, Install dependancies:
```bash
pip install boto3
pip install awscli

2, configure AWS:
```bash
aws configure
3, install Terraform
Download from terraform.io/downloads

## Run
1, create the bucket
```bash
terraform init
terraform apply

2, Upload a file
```bash
echo "Hello from Wanji" > hello.text

3, Upload a file to s3 bucket
```bash
python upload.py

4, Destroy when done
```bash
terraform destory









## AWS S3 -Terraform + boto3
Create an S3 bucket with Terraform, then upload a file with Python
## Make sure you sign up at aws.amazon.com
aws configure credetials

  AWS Access Key ID:      - your key
  AWS Secret Access Key:  - your secret
  Default region name:    us-east-1
  Default output format:  - press Enter


## Files and what they do:
`main.tf` to Creates the S3 bucket on AWS 

`upload.py` to Uploads a file to the bucket 

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

#### Run Locally
clone the project

git clone [https://github.com/wanji-cloudk/boto3-aws-project1.git]

### Authers:
This project is developed by(https://www.github.com/wanji-cloudk)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

### Contributing:
You are always welcome to contribute to this project and kindly submit a pull requst to any improment you've made,Your input can help make the terraform-boto3 script even better for users.








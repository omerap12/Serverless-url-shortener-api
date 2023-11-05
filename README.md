
# Serverless URL Shortener API

This repository contains Terraform configurations and AWS Lambda functions to create a simple URL shortener API using AWS API Gateway, AWS Lambda, and DynamoDB. The API allows users to create short URLs and retrieve the original full URLs associated with the short URLs.
![READ](https://github.com/omerap12/Serverless-url-shortener-api/assets/61663422/22ae2c2f-b262-4f5e-b64d-c08eb26bf463)

## Terraform Configurations



The Terraform configurations in this repository create the following AWS resources:


* API Gateway: An API Gateway with HTTP protocol enabled. It has two routes:

1. GET /read: Retrieves the original full URL associated with a short URL.
2. POST /write: Creates a short URL associated with a full URL.

* AWS Lambda Functions:

1. read_lambda: Handles the GET /read route. It retrieves the full URL associated with a short URL from DynamoDB.
2. write_lambda: Handles the POST /write route. It stores the short URL and full 
* URL mapping in DynamoDB.
DynamoDB Table: A DynamoDB table named url-table to store the mappings between short URLs and full URLs.
## Prerequisites

Before applying the Terraform configurations, make sure you have the following:
* AWS account credentials configured.
* Terraform installed on your local machine.

## Deployment

1. Clone this repository:

```bash
  git clone https://github.com/omerap12/Serverless-url-shortener-api.git
  cd Serverless-url-shortener-api
```
2. Initialize Terraform and apply the configurations:
```bash
terraform init
terraform apply
```
3. After applying the Terraform configurations, the API Gateway endpoint URLs for read and write operations will be provided as outputs. You can find them in the Terraform output variables.
## Lambda Functions

### `read_lambda` Function

The read_lambda function handles the GET /read route. It takes a short URL as input, retrieves the corresponding full URL from DynamoDB, and returns the full URL in the response.

### `write_lambda` Function
The write_lambda function handles the POST /write route. It takes a JSON payload containing a short URL and a full URL, stores the mapping in DynamoDB, and returns a success message in the response.
## Cleanup

To destroy the resources created by Terraform, run:
```bash
terraform destroy
```

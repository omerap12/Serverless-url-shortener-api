# serverless-url-shortener-api

A fully Serverless URL shortener app (aws).<br>
There are two API endpoints.<br>
1. Adding a new URL to shortener and save it to dynamodb.<br>
2. Get from the shortened URL (query dynamodb) the original one.<br>

![image](https://user-images.githubusercontent.com/61663422/224678039-2a0f5542-2d4d-4672-8374-0a0c25f5a673.png)

- get_full_url - Code for the application's Lambda function get from short url a fully url (get from the database).
- post_short_url - Code for the application's Lambda function: add a new recodrd to the database short url: fully url.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name serverless-url-shortener-api
```

import json
import boto3
import os
import logging

# Initialize DynamoDB client and logger
dynamodb_client = boto3.client('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Extract the request body from the event
        body = event['body']
        
        # Log the received request body
        logger.info(body)
        
        # Parse the JSON body into a dictionary
        body = json.loads(body)
        
        # Retrieve 'short_url' and 'full_url' from the parsed JSON body
        short_url = body.get('short_url')
        full_url = body.get('full_url')

        # Check if 'short_url' or 'full_url' is missing in the request
        if not short_url or not full_url:
            raise ValueError("short_url and full_url are required.")
        
        # Retrieve the DynamoDB table name from environment variables
        table_name = os.environ.get('TABLE_NAME')
        
        # Check if TABLE_NAME environment variable is not set
        if not table_name:
            raise EnvironmentError("TABLE_NAME environment variable is not set.")
        
        # Put item into DynamoDB table with 'short_url' and 'full_url' attributes
        dynamodb_client.put_item(
            TableName=table_name,
            Item={'shortened_url': {'S': short_url}, 'url': {'S': full_url}}
        )
        
        # Log success message
        logger.info("Record added successfully.")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Record added"
            })
        }
    
    except ValueError as e:
        # Handle invalid input error
        logger.error(f"Invalid input: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": str(e)
            })
        }
    
    except Exception as e:
        # Handle other errors
        logger.error(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            })
        }

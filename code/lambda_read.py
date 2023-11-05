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

        # Retrieve the 'short_url' from the parsed JSON body
        short_url = body.get('short_url')
        
        # Check if 'short_url' is missing in the request
        if not short_url:
            raise ValueError("short_url is required.")
                
    except ValueError as e:
        # Handle invalid input error
        logger.error(f"Invalid input: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": str(e)
            })
        }
    
    try:
        # Retrieve the DynamoDB table name from environment variables
        table_name = os.environ.get('TABLE_NAME')
        
        # Check if TABLE_NAME environment variable is not set
        if not table_name:
            raise EnvironmentError("TABLE_NAME environment variable is not set.")
        
        # Query DynamoDB for the item with the provided 'short_url'
        response = dynamodb_client.get_item(TableName=table_name, Key={'shortened_url': {'S': short_url}})
        
        # Check if the item was not found in DynamoDB
        if 'Item' not in response:
            return {
                "statusCode": 404,
                "body": json.dumps({
                    "message": "Short URL not found"
                })
            }
        
        # Extract the 'full_url' from the DynamoDB response
        item = response['Item']
        full_url = item['url']['S']
    
    except Exception as e:
        # Handle database-related errors
        logger.error(f"DB Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal Server Error"
            })
        }

    # Return the 'full_url' in the response
    return {
        "statusCode": 200,
        "body": json.dumps({
            "full_url": full_url
        })
    }

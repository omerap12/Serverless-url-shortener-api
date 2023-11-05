import json
import boto3
import os
import logging

dynamodb_client = boto3.client('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        short_url = event.get('short_url')
        logger.info(f"Short url: {short_url}")
        
        if not short_url:
            raise ValueError("short_url is required.")
                
    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": str(e)
            })
        }
    
    try:
        table_name = os.environ.get('TABLE_NAME')
        if not table_name:
            raise EnvironmentError("TABLE_NAME environment variable is not set.")
        
        response = dynamodb_client.get_item(TableName= table_name, Key = {'shortened_url' : {'S': short_url}})
        if 'Item' not in response:
            return {
                "statusCode": 404,
                "body": json.dumps({
                    "message": "Short URL not found"
                })
            }
        item = response['Item']
        full_url = item['url']['S']
    
    except Exception as e:
        logger.error(f"DB Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal Server Error"
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "full_url": full_url
        })
    }

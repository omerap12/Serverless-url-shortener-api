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
        full_url = event.get('full_url')
        logger.info(f"Short url: {short_url}")
        logger.info(f"Full url: {full_url}")
        
        if not short_url or not full_url:
            raise ValueError("short_url and full_url are required.")
                
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
        
        dynamodb_client.put_item(
            TableName=table_name,
            Item={'shortened_url': {'S': short_url}, 'url': {'S': full_url}}
        )
    
    except Exception as e:
        logger.error(f"DB Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal Server Error"
            })
        }
    
    logger.info("Record added successfully.")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Record added"
        })
    }

import json
import boto3
import os
import logging

dynamodb_client = boto3.client('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        body = event['body']
        logger.info(body)
        body = json.loads(body)
        short_url = body.get('short_url')
        full_url = body.get('full_url')

        if not short_url or not full_url:
            raise ValueError("short_url and full_url are required.")
        
        table_name = os.environ.get('TABLE_NAME')
        if not table_name:
            raise EnvironmentError("TABLE_NAME environment variable is not set.")
        
        dynamodb_client.put_item(
            TableName=table_name,
            Item={'shortened_url': {'S': short_url}, 'url': {'S': full_url}}
        )
        
        logger.info("Record added successfully.")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Record added"
            })
        }
    
    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": str(e)
            })
        }
    
    except Exception as e:
        logger.error(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            })
        }

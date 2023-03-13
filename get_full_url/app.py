import json
import boto3

dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000') # connect to dynamo db


def lambda_handler(event, context):
    shortened_url = event['shortened_url']
    response = dynamodb.get_item(
        TableName='url-table',
        Key = {
            'shortened_url' : {'S':shortened_url}
        }
    )
    item = response['Item']['url']["S"]
    if item:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message" : item
            }),
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message" : "Not exist"
            }),
        }

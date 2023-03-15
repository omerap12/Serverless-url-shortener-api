import json
import boto3

dynamodb_client = boto3.client('dynamodb', endpoint_url='http://abp-sam-nestjs-dynamodb:8000') # connect to dynamo db

def lambda_handler(event, context):
    try:
        request_body = json.loads(event['body'])
        short_url = request_body['short_url']
        print(short_url)
        full_url = request_body['full_url']
        print(full_url)
    except Exception as e:
        print(e)
        return {
                    "statusCode": 502,
                    "body": json.dumps({
                    "message" : "Error! wrong parameters sent"
                    }),
                }
    # putting the item into the db
    try:
        dynamodb_client.put_item(TableName='url-table', Item={'shortened_url':{'S':short_url},'url':{'S':full_url}})
    except Exception as e:
        print(e)
        return {
                    "statusCode": 502,
                    "body": json.dumps({
                    "message" : "DB Error"
                    }),
                }
    return {
                    "statusCode": 200,
                    "body": json.dumps({
                    "message" : "Record added"
                    }),
                }
    

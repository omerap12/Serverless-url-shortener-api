import json
import boto3

dynamodb_client = boto3.client('dynamodb', endpoint_url='http://abp-sam-nestjs-dynamodb:8000') # connect to dynamo db

def lambda_handler(event, context):
    parameters_sent = json.loads(event['body'])
    url_requested = parameters_sent['shortened_url']

    # getting the item from the database
    response = dynamodb_client.get_item(
        TableName='url-table',
        Key = {
            'shortened_url' : {'S':url_requested}
        }
    )

    # check if the item is within the database
    try:
        item = response['Item']['url']['S']
    # id not return 404
    except Exception as e:
        return {
                "statusCode": 404,
                "body": json.dumps({
                    "message" : "Not found"
                }),
            }
    else:
        return {
                "statusCode": 200,
                "body": json.dumps({
                    "message" : response['Item']['url']['S']
                }),
            }
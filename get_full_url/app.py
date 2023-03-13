import json

def lambda_handler(event, context):
    short_url = event['short_url']
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message" : short_url
        }),
    }

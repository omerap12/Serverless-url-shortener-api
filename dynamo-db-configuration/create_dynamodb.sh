#!/bin/bash

function usage {
    echo "USAGE: $0 PORT_NUMBER"
    echo "Create and run the local dynamodb at port number."
}

PORT=$1
if [ -z $PORT ]; then 
    usage
    exit
fi
echo "Create dynamodb docker on port $PORT"
docker-compose -f docker-compose.yml up &

echo "Create user-table"
aws dynamodb create-table --cli-input-json file://create-table.json --endpoint-url http://localhost:$PORT
if [[ $? -ne 0 ]]; then
    echo "Error creating table"
    exit
fi

echo "Add dummy value to table"
aws dynamodb put-item --table-name url-table --item '{"shortened_url": {"S": "abc123"}, "url": {"S": "https://example.com"}}' --endpoint-url http://localhost:$PORT
if [[ $? -ne 0 ]]; then
    echo "Error put item in table"
    exit
fi

echo "Get the dummy value from the db"
aws dynamodb get-item --table-name url-table --key '{"shortened_url": {"S": "abc123"}}' --endpoint-url http://localhost:$PORT
if [[ $? -ne 0 ]]; then
    echo "Error get item from table table"
    exit
fi

sed -i "s/ENDPOINT_URL: http:\/\/abp-sam-nestjs-dynamodb:8000/ENDPOINT_URL: http:\/\/abp-sam-nestjs-dynamodb:$PATH/" template.yaml
echo "dynamodb is up and running!"
echo "run sam build && sam local start-api -t template.yaml --docker-network abp-sam-backend"
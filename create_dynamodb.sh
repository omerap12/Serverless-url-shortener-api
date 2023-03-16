#!/bin/bash
echo "Create dynamodb docker on port 8000"
docker-compose -f dynamo-db-configuration/docker-compose.yml up --force-recreate &

echo "Create user-table"

aws dynamodb create-table --cli-input-json file://dynamo-db-configuration/create-table.json --endpoint-url http://localhost:8000
if [[ $? -ne 0 ]]; then
    echo "Error creating table, might be because table already exist."
    echo "Continue"
fi

echo "Add dummy value to table"
aws dynamodb put-item --table-name url-table --item '{"shortened_url": {"S": "abc123"}, "url": {"S": "https://example.com"}}' --endpoint-url http://localhost:8000
if [[ $? -ne 0 ]]; then
    echo "Error put item in table"
    exit
fi

echo "Get the dummy value from the db"
aws dynamodb get-item --table-name url-table --key '{"shortened_url": {"S": "abc123"}}' --endpoint-url http://localhost:8000
if [[ $? -ne 0 ]]; then
    echo "Error get item from table table"
    exit
fi
echo "Dynamodb is up and running!"
echo "run sam build && sam local start-api -t template.yaml --docker-network abp-sam-backend"
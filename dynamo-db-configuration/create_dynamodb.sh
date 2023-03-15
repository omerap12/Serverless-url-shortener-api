#!/bin/bash

echo "Create dynamodb docker compose"
docker-compose -f docker-compose.yml up

echo "Create user-table"
aws dynamodb create-table --cli-input-json file://dynamo-db-configuration/create-table.json --endpoint-url http://localhost:8000

echo "Add dummy value to table"
aws dynamodb put-item --table-name url-table --item '{"shortened_url": {"S": "abc123"}, "url": {"S": "https://example.com"}}' --endpoint-url http://localhost:8000

echo "Get the dummy value from the db"

aws dynamodb get-item --table-name url-table --key '{"shortened_url": {"S": "abc123"}}' --endpoint-url http://localhost:8000

echo "dynamodb is up and running!"
echo "run sam build && sam local start-api -t template.yaml --docker-network abp-sam-backend"
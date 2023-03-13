echo "Run dynamo-db container locally at port 8000"

sudo docker run -p 8000:8000 amazon/dynamodb-local

echo "Create the url table"

aws dynamodb create-table --cli-input-json file://dynamo-db-configuration/create-table.json --endpoint-url http://localhost:8000

echo "Put dummy value at the db"

aws dynamodb put-item --table-name url-table --item '{"shortened_url": {"S": "abc123"}, "url": {"S": "https://example.com"}}' --endpoint-url http://localhost:8000

echo "Get the dummy value from the db"

aws dynamodb get-item --table-name url-table --key '{"shortened_url": {"S": "abc123"}}' --endpoint-url http://localhost:8000

# set sam to the same network as an API
# sam local start-api -t template.yaml --docker-network abp-sam-backend

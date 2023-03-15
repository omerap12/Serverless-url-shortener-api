# add to db:
curl -v -X POST http://127.0.0.1:3000/post_short_url -H 'Content-Type: application/json' -d '{"short_url":"omer","full_url":"https://omer.com"}'

# pull from db:
curl -v -X GET http://127.0.0.1:3000/get_full_url -H 'Content-Type: application/json' -d '{"shortened_url":"abc123"}'
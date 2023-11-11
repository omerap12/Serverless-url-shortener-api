output "dynamodb_table_name" {
  value = module.dynamodb_table.dynamodb_table_id
}
output "api_url_read" {
    value = "${module.api_gateway.apigatewayv2_api_api_endpoint}/read"
}
output "api_url_write" {
    value = "${module.api_gateway.apigatewayv2_api_api_endpoint}/write"
}
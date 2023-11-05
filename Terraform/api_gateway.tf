module "api_gateway" {
  source = "terraform-aws-modules/apigateway-v2/aws"

  name          = var.api_gateway_name
  description   = var.api_gateway_info
  protocol_type = "HTTP"
  cors_configuration = {
    allow_headers = ["content-type", "x-amz-date", "authorization", "x-api-key", "x-amz-security-token", "x-amz-user-agent"]
    allow_methods = ["*"]
    allow_origins = ["*"]
  }

  create_api_domain_name = false # to control creation of API Gateway Domain Name


  # Routes and integrations
  integrations = {

    "GET /read" = {
      lambda_arn             = module.read_lambda_function.lambda_function_arn
      payload_format_version = "2.0"
      authorization_type     = "NONE"
    }

    "POST /write" = {
      lambda_arn             = module.write_lambda_function.lambda_function_arn
      payload_format_version = "2.0"
      authorization_type     = "NONE"
    }
  }

  tags = {
    Name = var.api_gateway_name
  }
}

resource "aws_lambda_permission" "api_gateway_read_invoke" {
  action        = "lambda:InvokeFunction"
  function_name = module.read_lambda_function.lambda_function_arn
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${module.api_gateway.apigatewayv2_api_execution_arn}/*/*/read"
}

resource "aws_lambda_permission" "api_gateway_write_invoke" {
  action        = "lambda:InvokeFunction"
  function_name = module.write_lambda_function.lambda_function_arn
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${module.api_gateway.apigatewayv2_api_execution_arn}/*/*/write"
}


output "api-url-read" {
    value = "${module.api_gateway.apigatewayv2_api_api_endpoint}/read"
}
output "api-url-write" {
    value = "${module.api_gateway.apigatewayv2_api_api_endpoint}/write"
}
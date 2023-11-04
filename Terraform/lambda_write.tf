module "write_lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = var.write_lambda_function_name
  description   = var.write_lambda_function_description
  handler       = "lambda_write.lambda_handler"
  runtime       = "python3.8"
  create_role   = true

  source_path = "../code/lambda_write.py"

  environment_variables = {
    TABLE_NAME = module.dynamodb_table.dynamodb_table_id
  }
  tags = {
    Name = var.write_lambda_function_name
  }
  depends_on = [module.dynamodb_table]
}

resource "aws_iam_policy" "write_lambda_policy" {
  name        = var.write_lambda_function_name
  description = "Policy that allows lambda writing access to dynamodb"
  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBTableAccess",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:DescribeTable",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:UpdateItem"
            ],
            "Resource": module.dynamodb_table.dynamodb_table_arn
        },
    ]
})
  depends_on = [module.dynamodb_table]

}

resource "aws_iam_role_policy_attachment" "attach_lambda_role_write" {
  role       = module.write_lambda_function.lambda_role_name
  policy_arn = aws_iam_policy.write_lambda_policy.arn
  depends_on = [module.write_lambda_function]
}
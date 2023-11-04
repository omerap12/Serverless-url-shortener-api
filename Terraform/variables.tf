variable "write_lambda_function_name" {
    type = string
    description = "Name of writing function to dynamodb table"
    default = "url_writer_function"
}

variable "write_lambda_function_description" {
    type = string
    description = "Description of writing function to dynamodb table"
    default = "Function writes to dynamodb table"
}
###

variable "read_lambda_function_name" {
    type = string
    description = "Name of reading function from dynamodb table"
    default = "url_reader_function"
}

variable "read_lambda_function_description" {
    type = string
    description = "Description of reading function from dynamodb table"
    default = "Function reads from dynamodb table"
}


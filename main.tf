provider "aws" {
  access_key = "YOUR_ACCESS_KEY"
  secret_key = "YOUR_SECRET_KEY"
  region     = "YOUR_REGION"
}

# Criação do API Gateway
resource "aws_api_gateway_rest_api" "fraud_detection" {
  name = "fraud_detection"
}

# Criação do AWS Lambda
resource "aws_lambda_function" "fraud_detection_lambda" {
  filename         = "fraud_detection_lambda.zip"
  function_name    = "fraud_detection_lambda"
  role             = "arn:aws:iam::${var.account_id}:role/lambda-role"
  handler          = "lambda_handler"
  runtime          = "python3.8"
  source_code_hash = filebase64sha256("fraud_detection_lambda.zip")
}

# Criação do endpoint do modelo de detecção de fraudes usando o Amazon SageMaker
resource "aws_sagemaker_endpoint" "fraud_detection_endpoint" {
  name = "fraud_detection_endpoint"
  endpoint_config_name = "fraud_detection_endpoint_config"
}

# Criação da configuração do endpoint do modelo de detecção de fraudes usando o Amazon SageMaker
resource "aws_sagemaker_endpoint_configuration" "fraud_detection_endpoint_config" {
  name = "fraud_detection_endpoint_config"
  production_variants {
    variant_name = "fraud_detection_variant"
    initial_instance_count = 1
    instance_type = "ml.t2.medium"
    model_name = "fraud_detection_model"
  }
}

# Criação do Kinesis Data Firehose
resource "aws_kinesis_firehose_delivery_stream" "fraud_detection_firehose" {
  name        = "fraud_detection_firehose"
  destination = "s3"
  s3_configuration {
    role_arn           = "arn:aws:iam::${var.account_id}:role/kinesis-role"
    bucket_arn         = "arn:aws:s3:::fraud_detection_bucket"
    buffer_size        = 5
    buffer_interval    = 300
    compression_format = "GZIP"
  }
}

# Criação do Amazon S3 Bucket para as transações
resource "aws_s3_bucket" "fraud_detection_bucket" {
  bucket = "fraud_detection_bucket"
  acl    = "private"
}

# Criação do Amazon S3 Bucket para os modelos
resource "aws_s3_bucket" "fraud_detection_models_bucket" {
  bucket = "fraud_detection_models_bucket"
  acl    = "private"
}

# Criação do Amazon QuickSight
resource "aws_quicksight_user" "quicksight_user" {
  email               = "gabriel@europeos.com"
  identity_type       = "IAM"
  user_role           = "AUTHOR"
  session_name_prefix = "quicksight_session"
}
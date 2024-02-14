import json

def lambda_handler(event, context):
    # Your main handler logic here
    return {
        'statusCode': 200,
        'body': json.dumps('Hello sahil')
    }
{
#   "LambdaFunctionConfigurations": [
#     {
#       "LambdaFunctionArn": "arn:aws:lambda:region:account-id:function:your-lambda-function",
#       "Events": ["s3:ObjectCreated:*", "s3:ObjectUpdated:*"]
#     }
#   ]
# }

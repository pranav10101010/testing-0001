import json
def lambda_handler(event, context):
    # Your main handler logic here
    return {
        'statusCode': 200,
        'body': json.dumps('Hello bhai ke haal ')
    }

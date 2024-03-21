import random
import json

def lambda_handler(event, context):
    # Generate a random number
    random_number = random.randint(1, 100)

    # Create a response object
    response = {
        'statusCode': 200,
        'body': json.dumps({'random_number': random_number})
    }

    return response


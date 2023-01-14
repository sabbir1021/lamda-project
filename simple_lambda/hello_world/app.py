import json

def lambda_handler(event, context):
    print(event.get('first_name'))
    # body = json.loads(event)
    # name = body.get('first_name') + ' ' + body.get('first_name')
    return {
        "statusCode": 200,
        "body": json.dumps({
            "full_name": 'name',
        }),
    }

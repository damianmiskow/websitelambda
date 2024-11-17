import json

def lambda_handler(event, context):
    op = event.get('operator')
    num1 = int(event.get('num1', 0))
    num2 = int(event.get('num2', 0))
    result = None
    if op == "*":
        result = num1 * num2
    else:
        result = "INVALID"

    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }


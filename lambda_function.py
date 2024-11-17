import json

def lambda_handler(event, context):
    op = event.get('operator')
    num1 = int(event.get('num1', 0))
    num2 = int(event.get('num2', 0))

    if op == "*":
        result = num1 * num2
    

    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }


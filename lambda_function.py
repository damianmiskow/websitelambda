import json

def lambda_handler(event, context):
    num1 = int(event.get('num1', 0))
    num2 = int(event.get('num2', 0))
    num3 = int(event.get('num2', 0))
    result = num1 + num2 + num3
    

    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }


#test 123

print ("Hello world")
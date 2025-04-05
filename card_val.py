import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ccn')

def lambda_handler(event, context):
    card_num_str = str(event.get('card_num', 0))
    index = 1

    card_num_list = [int(digit) for digit in reversed(card_num_str)]

    multiplied_list = [(num * 2 if i % 2 != 0 else num) for i, num in enumerate(card_num_list)]
    adjusted_list = [num - 9 if num >= 10 else num for num in multiplied_list]
    
    total = sum(adjusted_list)
    is_valid = total % 10 == 0

    date_str = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    table.put_item(
        Item={
            'date': date_str,
            'ccn': card_num_str
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'is_valid': is_valid})
    }
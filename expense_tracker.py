import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'Addresses')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        address_id = str(uuid.uuid4())
        street = body.get('street', '')
        city = body.get('city', '')
        state = body.get('state', '')
        zip_code = body.get('zip', '')

        if not street or not city or not state or not zip_code:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required address fields'})
            }

        item = {
            'address_id': address_id,
            'street': street,
            'city': city,
            'state': state,
            'zip': zip_code
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Address added', 'address_id': address_id})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'LoginPage'

def lambda_handler(event, context):
    try:
        username = event.get('Username')
        password = event.get('Password')
        
        if not username or not password:
            return {
                'statusCode': 400,
                'body': json.dumps('Error: Username and Password are required.')
            }
        table = dynamodb.Table(table_name)
        
        table.put_item(
            Item={
                'username': username, 
                'Password': password
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f'User {username} added successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error adding user: {str(e)}')
        }

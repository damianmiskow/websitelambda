import json
from card_val import lambda_handler  

event = {
    'card_num': 374245455400126
}
context = {}  
response = lambda_handler(event, context)

print("Response:", response)
print("Body:", json.loads(response['body']))

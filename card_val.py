import json

def lambda_handler(event, context):
    card_num_str = str(event.get('card_num', 0))
    index = 1

    card_num_list = []
    for element in card_num_str:
        card_num_list.insert(0, int(element))

    multiplied_list = []
    for element in card_num_list:
        if index % 2 == 0:
            multiplied_list.append(element * 2)
        else:
            multiplied_list.append(element)
        index += 1

    over10_check = []
    for element in multiplied_list:
        if element >= 10:
            over10_check.append(element-9)
        else: 
            over10_check.append(element)

    total = 0
    for element in over10_check:
        total+= element
    if total % 10 == 0:
        return {
            'statusCode': 200,
            'body': json.dumps({'is_valid': True})
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'is_valid': False})
        }


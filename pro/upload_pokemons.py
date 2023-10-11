import boto3
import json

profile_name = 'juan'

table_name = 'pokemonpro'

with open('pokemon_pro_data_base.json', 'r') as json_file:
    data = json.load(json_file)


session = boto3.Session(profile_name=profile_name)
dynamodb = session.client('dynamodb')

batch_size = 25
data_batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

for batch in data_batches:
    batch_write_data = []
    for item in batch:
        for key, value in item.items():
            if isinstance(value, int):
                item[key] = int(value)
        batch_write_data.append({
            'PutRequest': {
                'Item': item
            }
        })

    try:
        print(batch_write_data)
        response = dynamodb.batch_write_item(
            RequestItems={
                table_name: batch_write_data
            }
        )
    except Exception as e:
        print(f"Error: {e}")

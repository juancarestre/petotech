###This is a python script to retrieve a pokemon from dynamodb table called pokemon, pokemon by id
import boto3

boto3.setup_default_session(profile_name='juan')
#Create the client
dynamodb = boto3.client('dynamodb')
#Retrieve the pokemon by id

pokemon_id = '1'
response = dynamodb.get_item(
    TableName='pokemon',
    Key={
        'id': {
            'S': pokemon_id
        }
    }
)
item = response['Item']
print(item)

print('dale like mi rey')
# a scan to get all the pokemons
response = dynamodb.scan(
    TableName='pokemon')
items = response['Items']
print(items)
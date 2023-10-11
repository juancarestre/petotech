import boto3
from utils import parse_results

profile_name = 'juan'

session = boto3.Session(profile_name=profile_name)

table_name = 'pokemonpro'

pk_value = 'alakazam'
sk_value = 'entrenador#'

dynamodb = session.client('dynamodb')

try:
    response = dynamodb.query(
        TableName=table_name,
        KeyConditionExpression='razaPokemon = :pk_value and begins_with(pk, :sk_value)',
        IndexName='razaPokemon-pk-index',
        ExpressionAttributeValues={
            ':pk_value': {'S': pk_value},
            ':sk_value': {'S': sk_value}
        }
    )

    items = response['Items']

    result = []

    result = parse_results(items, result)

    print(result)

except Exception as e:
    print(f"Error al realizar la consulta: {e}")

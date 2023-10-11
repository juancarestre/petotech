import boto3
from utils import parse_results

profile_name = 'juan'

session = boto3.Session(profile_name=profile_name)

table_name = 'pokemonpro'

pk_value = 'entrenador#69'
sk_value = 'team#entrenador#69'

dynamodb = session.client('dynamodb')

try:
    response = dynamodb.query(
        TableName=table_name,
        KeyConditionExpression='pk = :pk_value and sk = :sk_value',
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

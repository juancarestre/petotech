import boto3
from utils import parse_results

profile_name = 'juan'

session = boto3.Session(profile_name=profile_name)

table_name = 'pokemonpro'

pk_value = 'pokemon'
sk_value = 'rata'

dynamodb = session.client('dynamodb')

try:
    response = dynamodb.query(
        TableName=table_name,
        KeyConditionExpression='pk = :pk_value and lsi1 = :sk_value',
        IndexName='lsi1',
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

import boto3
import json

from utils import parse_results

profile_name = 'juan' #Cambia esto si no tienes profiles en tu configuracion de keys de aws

session = boto3.Session(profile_name=profile_name)

dynamodb = session.client('dynamodb')

table_name = 'pokemonpro'

paginator = dynamodb.get_paginator('scan')

try:
    result = []
    for page in paginator.paginate(TableName=table_name):
        items = page['Items']
        result = parse_results(items, result)

        print(result)


except Exception as e:
    print(f"Error al escanear la tabla: {e}")

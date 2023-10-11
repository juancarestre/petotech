import json
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from decimal import Decimal


def from_dynamodb_to_json(item):
    d = TypeDeserializer()
    return {k: d.deserialize(value=v) for k, v in item.items()}

def convert_decimal_to_int(value):
    if isinstance(value, Decimal):
        return int(value)
    return value

def parse_results(items, result):
    for item in items:
        item = from_dynamodb_to_json(item)

        for key, value in item.items():
            item[key] = convert_decimal_to_int(value)

        result += [item]

    result = json.dumps(result)

    return result
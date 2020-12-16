import json
from json import loads


def normalize(event, context):
    body_json = event["body"]
    body_decoded = loads(body_json)
    print(body_decoded)

    normalized = {current["name"]: current[[x for x in current.keys() if "val" in x.lower()][0]] for current in
                  body_decoded}

    response = {
        "statusCode": 200,
        "body": json.dumps(normalized)
    }

    return response

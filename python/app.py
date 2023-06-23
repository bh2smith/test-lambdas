import json
import os

from src.db_client import PgClient


import base64




def handler(event, context):
    """
    Strange issue where locally and when testing in 
    AWS Console posted `data = {'txHash': 'Hello2', 'solver': 'World2'}`
    results in `event = data`.
    However, when called via function lambda it results in 
    this big ridiculous and misleading JSON file with json content inside "body"
    `event = { "body": data, "other_stuff": {...} }` 
    """
    print("Received Event", json.dumps(event))
    
    # TODO - this is a hacky way of handling both event types.
    if "body" in event:
        encoded_string = event["body"]
        event = json.loads(base64.b64decode(encoded_string))
    print("Body", event)
    
    db = PgClient(os.environ.get("DATABASE_URL"))

    response = db.select_given_string(event["txHash"])
    print("Read from DB", response)

    return {"statusCode": 200, "body": json.dumps(event)}

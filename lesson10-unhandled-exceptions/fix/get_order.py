import json
import boto3
import os
import decimal
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    print(json.dumps(event))

    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                if o % 1 > 0:
                    return float(o)
                else:
                    return int(o)
            return super(DecimalEncoder, self).default(o)

    # FIX: input validation
    if "orderId" not in event:
        return {
            "status": "err",
            "msg": "invalid request"
        }

    if "user" not in event:
        return {
            "status": "err",
            "msg": "unauthorized"
        }

    orderId = event["orderId"]
    userId = event["user"]
    is_admin = str(event.get("isAdmin", False)).lower() == "true"

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["ORDERS_TABLE"])

    if is_admin:
        response = table.query(
            KeyConditionExpression=Key("orderId").eq(orderId)
        ).get("Items", [None])
    else:
        key = {"orderId": orderId, "userId": userId}
        response = [table.get_item(Key=key).get("Item")]

    res = (
        {"status": "ok", "order": response[0]}
        if response[0] is not None
        else {"status": "err", "msg": "could not find order"}
    )

    return json.loads(
        json.dumps(res, cls=DecimalEncoder)
        .replace("\\\"", "\"")
        .replace("\\n", "")
    )

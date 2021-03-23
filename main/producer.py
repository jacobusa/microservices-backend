import pika, json
import os

amqps = os.environ.get("AMQPS")

params = pika.URLParameters(amqps)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    print(method.values)
    print(body.values)
    print(properties.values)
    channel.basic_publish(
        exchange="", routing_key="admin", body=json.dumps(body), properties=properties
    )

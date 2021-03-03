import pika, json

import os

amqps = os.environ.get("AMQPS")

params = pika.URLParameters(amqps)
connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="main", body=json.dumps(body), properties=properties
    )

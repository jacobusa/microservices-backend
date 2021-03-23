import pika, json
import os

amqps = os.environ.get("AMQPS")

params = pika.URLParameters(amqps)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    if not connection or connection.is_closed:
        amqps = os.environ.get("AMQPS")
        params = pika.URLParameters(amqps)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
    properties = pika.BasicProperties(method)
    print(method)
    print(body)
    print(properties)
    channel.basic_publish(
        exchange="", routing_key="admin", body=json.dumps(body), properties=properties
    )

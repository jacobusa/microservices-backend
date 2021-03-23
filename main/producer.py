import pika, json
import os

amqps = os.environ.get("AMQPS")

params = pika.URLParameters(amqps)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    if not connection or connection.is_closed:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue="main")
        channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)
    properties = pika.BasicProperties(method)
    print(method)
    print(body)
    print(properties)
    channel.basic_publish(
        exchange="", routing_key="admin", body=json.dumps(body), properties=properties
    )

import pika, json
from main import Product, db
import os

amqps = os.environ.get("AMQPS")

params = pika.URLParameters(amqps)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    if not connection or connection.is_closed:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue="main")
        channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

    print("Recieved in main")
    data = json.loads(body)
    print(data)

    if properties.content_type == "product_created":
        product = Product(id=data["id"], title=data["title"], image=data["image"])
        db.session.add(product)
        db.session.commit()
        print("Product Created")
    elif properties.content_type == "product_updated":
        try:
            product = Product.query.get(data["id"])
            product.title = data["title"]
            product.image = data["image"]
            db.session.commit()
            print("Product Updated")
        except:
            abort(400, "No Product Exists")

    elif properties.content_type == "product_deleted":
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print("Product Deleted")
    else:
        print("No properties.content.type chosen")



channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
import requests, os, producer
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask import Flask, jsonify, abort
from dataclasses import dataclass

app = Flask(__name__)
database_uri = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config["DEBUG"] = os.environ.get("DEBUG")
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    # UniqueConstraint("user_id", "product_id", name="user_product_unique")


@app.route("/api/products")
def index():
    return jsonify(Product.query.all())


@app.route("/api/products/<int:id>/like", methods=["POST"])
def like(id):
    req = requests.get("http://admin-proxy/api/user")
    json = req.json()
    print('entering like with')
    print(req)
    print(json)

    try:
        productUser = ProductUser(user_id=json["id"], product_id=id)
        print('fetched productuser', productUser)
        db.session.add(productUser)
        print('added session')
        db.session.commit()
        print('committed')
        producer.publish("product_liked", id)
    except Exception as e:
        print("exception raised: ", e)
        abort(400, "You already liked this product")
    return jsonify([{"message": "success"}, {"mimetype": "application/json"}])


if __name__ == "__main__":
    # app.run(debug=True , host="0.0.0.0")
    # app.run(host="0.0.0.0")
    app.run()

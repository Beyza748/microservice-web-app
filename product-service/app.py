from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/products")
def products():
    data = requests.get("https://dummyjson.com/products?limit=5").json()
    return jsonify(data["products"])

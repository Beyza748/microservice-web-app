from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    products = requests.get("http://product-service:5001/products").json()
    holidays = requests.get("http://holiday-service:5002/holidays").json()
    return render_template("index.html", products=products, holidays=holidays)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

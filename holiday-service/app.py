from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/holidays")
def holidays():
    url = "https://date.nager.at/api/v3/PublicHolidays/2025/TR"
    return jsonify(requests.get(url).json()[:5])

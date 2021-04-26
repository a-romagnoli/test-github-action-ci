import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
app.config['TESTING'] = False

load_dotenv()


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/mongo')
def mongo():
    conn_mongo = MongoClient(f'mongodb://{os.getenv("MONGO_HOST")}:27017/')
    payload = []

    with conn_mongo:
        stocks = conn_mongo.unittest.stock.find()

        for stock in stocks:
            payload.append({
                'store_id': stock['store_id'],
                'material_id': stock['material_id'],
                'quantity': stock['quantity'],
                'stock_scenario': stock['stock_scenario']
            })
    conn_mongo.close()

    return jsonify(payload)


if __name__ == '__main__':
    app.run(host="localhost", debug=True)

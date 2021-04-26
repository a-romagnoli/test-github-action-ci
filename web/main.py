from flask import Flask, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.config['TESTING'] = False


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/query/mongo')
def mongo():
    conn_mongo = MongoClient('mongodb://mongo:27017/')
    result = ''

    with conn_mongo:
        stocks = conn_mongo.unittest.stock.find()

        for stock in stocks:
            result += f"<p>" \
                      f"STORE_ID={stock['store_id']}, " \
                      f"MATERIAL_ID={stock['material_id']}, " \
                      f"QUANTITY={stock['quantity']}, " \
                      f"STOCK_SCENARIO={stock['stock_scenario']}" \
                      f"</p>"
    conn_mongo.close()
    result += f"<p>" \
              f'<a href="{url_for("home")}">Return to Homepage</a>' \
              f"</p>"

    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0")

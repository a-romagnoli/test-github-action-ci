import os
import unittest

from pymongo import MongoClient

from web.main import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

        conn_mongo = MongoClient(f'mongodb://{os.getenv("MONGO_HOST")}:27017/')
        conn_mongo.unittest.stock.insert_one({
            "store_id": "foo",
            "material_id": "bar",
            "quantity": 666,
            "stock_scenario": "baz"
        })

    def test_get_home(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Hello, World!')

    def test_post_home(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)

    def test_get_mongo(self):
        response = self.app.get('/mongo')

        self.assertEqual(
            200,
            response.status_code
        )
        self.assertEqual(1, len(response.json))
        self.assertDictEqual(
            {
                "store_id": "foo",
                "material_id": "bar",
                "quantity": 666,
                "stock_scenario": "baz"
            },
            response.json[0]
        )

    def tearDown(self):
        conn_mongo = MongoClient(f'mongodb://{os.getenv("MONGO_HOST")}:27017/')
        conn_mongo.drop_database('unittest')


if __name__ == '__main__':
    unittest.main()

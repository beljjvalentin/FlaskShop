# the file name for unit testing must follow this convention: test_<something>
from pymongo.errors import ConnectionFailure
from database import db, products_collection
from app import flask_app
import unittest


# class to represent the test cases
# use functions (methods) to define the scenarios

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Setting up the test client
        self.app = flask_app.test_client()
        self.app.testing = True

    # Test 1: Route Test for /home (expecting 405 on POST)
    def test_home_route_method_not_allowed(self):
        # Sending a POST request to the /home route (Only GET is allowed)
        response = self.app.post('/home')
        # Asserting that the response status code is 405 (Method Not Allowed)
        self.assertEqual(response.status_code, 405)

    # Test 2: Database Read Operation - MongoDB connection and data fetch
    def test_mongodb_connection_and_products_route(self):
        # Check MongoDB connection
        try:
            # Using the 'ping' command to verify MongoDB connection
            # db.admin.command('ping') - this command produces an error
            products_collection.database.client.admin.command('ping')
        except ConnectionFailure:
            self.fail("MongoDB is not connected")

        # Verifying that products route returns data correctly
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        # Checking that the response includes 'products' data (non-empty if data exists)
        self.assertIn(b'products', response.data)

    # Test 3: Database Write Operation - Inserting a document and verifying if it exists
    def test_mongodb_write_operation(self):
        test_product = {
            "name": "Test Product",
            "tag": "test",
            "price": 99.99,
            "image_path": "/path/to/image"
        }

        # Inserting test document
        insert_result = products_collection.insert_one(test_product)
        self.assertIsNotNone(insert_result.inserted_id, "Document insertion failed")

        # Calling the database to verify the document was inserted
        fetched_product = products_collection.find_one({"_id": insert_result.inserted_id})
        self.assertIsNotNone(fetched_product, "Inserted document not found in the collection")
        self.assertEqual(fetched_product["name"], "Test Product")
        self.assertEqual(fetched_product["tag"], "test")
        self.assertEqual(fetched_product["price"], 99.99)
        self.assertEqual(fetched_product["image_path"], "/path/to/image")

        # Cleaning up database by deleting the test document
        products_collection.delete_one({"_id": insert_result.inserted_id})

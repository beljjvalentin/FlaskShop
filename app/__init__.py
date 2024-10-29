# To install flask, first run the following line in the terminal:
# pip install flask
import os

# To import the flask into the project use the following line:
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

flask_app = Flask(__name__)
flask_app.static_folder = 'static'

# MongoDB Atlas Connection
client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.flk7i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.get_database("shop_db")  # Replace "app" with your database name

products_collection = db.products  # Replace products with your collection name

from app import routes

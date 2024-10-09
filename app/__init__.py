# To install flask, first run the following line in the terminal:
# pip install flask

# To import the flask into the project use the following line:
from flask import Flask
from pymongo import MongoClient

flask_app = Flask(__name__)
flask_app.static_folder = 'static'

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://valentin:dLnI23EfvYpg3pua@cluster0.flk7i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.get_database("shop_db")  # Replace "app" with your database name

products_collection = db.products  # Replace products with your collection name

from app import routes
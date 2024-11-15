# db.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve MongoDB credentials
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

# Set up MongoDB client and database
client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.flk7i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.get_database("shop_db")  # Adjust with your database name

# Collection
products_collection = db.products  # Adjust with your collection name
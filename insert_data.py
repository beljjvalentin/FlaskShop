# pip install pymongo
from database import db, products_collection

# Example product objects
products = [
    {
        "name": "Product 1",
        "image": "/static/images/product1.jpg",
        "price": 29.99,
        "tag": "New"
    },
    {
        "name": "Product 2",
        "image": "/static/images/product2.jpg",
        "price": 49.99,
        "tag": "Discounted"
    },
    {
        "name": "Product 3",
        "image": "/static/images/product3.jpg",
        "price": 19.99,
        "tag": "Best Seller"
    }
]

black_friday_deals = {
        "name": "Product 4",
        "image": "/static/images/product4.jpg",
        "price": 9.99,
        "tag": "Black Friday Deals"
    }

products_collection.insert_many(black_friday_deals)  # allows you to add a list of dictionaries into the database
# products_collection.insert_one(black_friday_deals)  # allows you to add a single dictionary into the database

# To install flask, first run the following line in the terminal:
# pip install flask

# To import the flask into the project use the following line:
from flask import Flask


flask_app = Flask(__name__)
flask_app.static_folder = 'static'

from app import routes

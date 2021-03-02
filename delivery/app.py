from flask import Flask
from delivery.ext import site

def create_app():
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    site.init_app(app)
    return app

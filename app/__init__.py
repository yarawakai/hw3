from flask import Flask
from config import Config

myapp_obj = Flask(__name__)
myapp_obj.config['SECRET_KEY'] = 'ABC'

from app import routes

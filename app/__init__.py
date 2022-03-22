from flask import Flask

myobj = Flask(__name__)
myobj.config['SECRET_KEY'] = 'ABC'

from app import routes

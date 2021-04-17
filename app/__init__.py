# flask import
from flask import Flask

# first party imports
from config import Config

# initialize the application
app = Flask(__name__)

# config
app.config.from_object(Config)

from app import routes
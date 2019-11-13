from flask import Flask
from flask_cors import CORS

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
import config

handler = RotatingFileHandler('server.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
CORS(app, resources={r"/*": {"origins": "*","supports_credentials":"true"}})


# Middleware
# import api.middleware

import api.routes

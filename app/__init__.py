from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

file_handler = logging.FileHandler("log.txt")
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

from app import views, models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from harddrop import config

db = SQLAlchemy(app)

from harddrop import views

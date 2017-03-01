from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
import harddrop.config

db = SQLAlchemy(app)

import harddrop.views

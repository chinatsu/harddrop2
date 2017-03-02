from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy
import flask_login

app = Flask(__name__)

import harddrop.config

Bootstrap(app)

from .nav_elements import init_custom_nav_renderer, nav

nav.init_app(app)
init_custom_nav_renderer(app)

db = SQLAlchemy(app)

login = flask_login.LoginManager()
login.init_app(app)

import harddrop.views


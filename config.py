from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DevelopmentConfig.DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = DevelopmentConfig.SECRET_KEY
db = SQLAlchemy(app)

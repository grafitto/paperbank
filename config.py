from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import *
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ProductionConfig.DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "thisisthesecretkeypleasedonotread"
db = SQLAlchemy(app)

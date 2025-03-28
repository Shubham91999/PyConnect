# Importing required libraries
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initiationg flask app
app = Flask(__name__)
CORS(app) # Wrapping our app in CORS to prevent cross-origin request errors

# Configuring db with SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Creating a database instance
db = SQLAlchemy(app)



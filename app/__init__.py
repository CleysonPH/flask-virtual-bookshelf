from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


from app.core import routes
from app.book import routes
from app.book import models
from app.author import routes
from app.author import models

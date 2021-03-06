from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db
from . import config
from . import initial_insert

#Everything starts here, when you "flask run", the connection to the database is set up here

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    try:
        initial_insert.run_insert()
    except:
        pass
    flask_app.secret_key = config.SECRET_KEY
    return flask_app
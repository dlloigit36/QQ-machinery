import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# CREATE DATABASE
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def init_db(app, db_filename):
    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)
    db_path = os.path.join(app.instance_path, db_filename)
    # Connect to Database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", f'sqlite:///{db_path}')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
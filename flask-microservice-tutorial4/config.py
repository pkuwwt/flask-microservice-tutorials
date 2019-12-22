
import os
import connexion
from connexion.resolver import RestyResolver
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

basedir = os.path.abspath(os.path.dirname(__file__))

connexion_app = connexion.App(__name__, specification_dir='swagger/')
app = connexion_app.app
ma = Marshmallow(app)

connexion_app.add_api('my_app.yaml', resolver=RestyResolver('api'))


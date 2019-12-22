
import os
import connexion
from connexion.resolver import RestyResolver
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

DB_FILENAME = os.path.join(basedir, 'items.db')

connexion_app = connexion.App(__name__, specification_dir='swagger/')
app = connexion_app.app
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + DB_FILENAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

connexion_app.add_api('my_app.yaml', resolver=RestyResolver('api'))

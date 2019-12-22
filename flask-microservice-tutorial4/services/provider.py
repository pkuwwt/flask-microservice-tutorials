from flask_injector import inject
from injector import provider, Module, singleton
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from typing import Callable

from config import Base

class SqlalchemyProvider(Module):
    """
    A module bind to a SQLAlchemy instance
    """
    @inject
    def __init__(self, app:Flask, uri:str, init_db: Callable):
        self.app = app
        self.uri = uri
        self.init_db = init_db

    def configure(self, binder):
        # We configure the DB here, explicitly, as Flask-SQLAlchemy requires
        # the DB to be configured before request handlers are called.
        db = self.configure_db(self.app)
        binder.bind(SQLAlchemy, to=db, scope=singleton)

    def configure_db(self, app):
        print('configure db')
        app.config['SQLALCHEMY_ECHO'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = self.uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)
        Base.metadata.create_all(db.engine)
        if callable(self.init_db):
            self.init_db(db)
        return db

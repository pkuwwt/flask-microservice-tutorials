
from flask_injector import inject
from models.Item import Item, ItemSchema
from services.provider import SqlalchemyProvider
from flask_sqlalchemy import SQLAlchemy
from flask import request

@inject
def search(db: SQLAlchemy) -> list:
    items = db.session.query(Item).order_by(Item.name).all()
    item_schema = ItemSchema(many=True)
    return item_schema.dump(items)

@inject
def post(db: SQLAlchemy):
    name = request.json['name']
    item = Item.create(name, db)
    return ItemSchema.dump_data(item)


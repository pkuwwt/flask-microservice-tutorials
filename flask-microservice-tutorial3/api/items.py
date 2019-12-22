
from flask_injector import inject
from models.Item import Item, ItemSchema

def search() -> list:
    items = Item.query.order_by(Item.name).all()
    item_schema = ItemSchema(many=True)
    return item_schema.dump(items)

def post(item):
    item = Item.create(item['name'])
    return ItemSchema().dump(item)


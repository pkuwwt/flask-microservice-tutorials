
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime
from config import ma, Base

print('import Item')

class Item(Base):
    __tablename__ = 'items'
    item_id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def create(name:str, db: SQLAlchemy):
        item = Item(name=name)
        db.session.add(item)
        db.session.commit()
        return item


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item

    @staticmethod
    def dump_data(item: Item):
        return ItemSchema().dump(item)
    @staticmethod
    def load_data(data, db: SQLAlchemy):
        return ItemSchema().load(data, session=db.session)


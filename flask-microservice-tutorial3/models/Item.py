
from datetime import datetime
from config import db, ma

class Item(db.Model):
    __tablename__ = 'items'
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def create(name):
        item = Item(name=name)
        db.session.add(item)
        db.session.commit()
        return item


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item
        sqla_session = db.session  


import os
from config import db, DB_FILENAME
from models.Item import Item

# Data to initialize database with
items = [
    {'name': 'Doug'},
    {'name': 'Kent'},
    {'name': 'Bunny'}
]

def initDB():
    # Delete database file if it exists currently
    if os.path.exists(DB_FILENAME):
        os.remove(DB_FILENAME)
    
    # Create the database
    db.create_all()
    
    # Iterate over the PEOPLE structure and populate the database
    for item in items:
        i = Item(name=item['name'])
        db.session.add(i)
    
    db.session.commit()

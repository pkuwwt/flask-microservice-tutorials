
import os
from models.Item import Item
from flask_sqlalchemy import SQLAlchemy

# Data to initialize database with
items = [
    {'name': 'Doug'},
    {'name': 'Kent'},
    {'name': 'Bunny'}
]

sqlite_uri_header = 'sqlite:///'

# Delete database file if it exists currently
def delete_sqlite_file(uri: str):
    if uri == ':memory:':
        return
    if uri.startswith(sqlite_uri_header):
        filename = uri[len(sqlite_uri_header):]
        print(filename)
        if os.path.exists(filename):
            print('delete file ', filename)
            os.remove(filename)

def init_db(db:SQLAlchemy):
    # Create the database
    db.create_all()
    
    # Iterate over the PEOPLE structure and populate the database
    for item in items:
        i = Item(name=item['name'])
        db.session.add(i)
    
    db.session.commit()


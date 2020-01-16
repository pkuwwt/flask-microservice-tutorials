
from config import app
from flask_injector import FlaskInjector
from build_database import delete_sqlite_file, init_db
from services.provider import SqlalchemyProvider
from flask_injector import Injector

if __name__ == '__main__':
    uri = 'sqlite:///./items.db'
    delete_sqlite_file(uri)
    injector = Injector([SqlalchemyProvider(app, uri, init_db)])
    FlaskInjector(app=app, injector=injector)
    app.run(debug=True, host='0.0.0.0', port=5000)



from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from services.provider import ItemsProvider, BooksProvider
import connexion

def configure1(binder: Binder):
    binder.bind(
            ItemsProvider,
            ItemsProvider([{"name": "Test 1"}])
            )
def configure2(binder: Binder):
    binder.bind(
            BooksProvider,
            BooksProvider([{"name": "Book 1"}])
            )

if __name__ == '__main__':
    app = connexion.App(__name__, debug=True, port=9099, specification_dir='swagger/')
    app.add_api('my_app.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure1, configure2])
    app.run()


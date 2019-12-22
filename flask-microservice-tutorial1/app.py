
from connexion.resolver import RestyResolver
import connexion

if __name__ == '__main__':
    app = connexion.App(__name__, debug=True, port=9099, specification_dir='swagger/')
    app.add_api('my_app.yaml', resolver=RestyResolver('api'))
    app.run()



from config import app
from build_database import initDB

if __name__ == '__main__':
    initDB()
    app.run(debug=True, port=9099)


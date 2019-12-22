
from flask_injector import inject
from services.provider import BooksProvider 

@inject
def search(data_provider: BooksProvider) -> list:
    return data_provider.get()

from flask_injector import inject
from injector import provider, Module

class ItemsProvider(Module):
    @inject
    def __init__(self, items:list):
        self._items = items

    @provider
    def get(self, number_of_items: int=5) -> list:
        if not self._items:
            return []
        if number_of_items > len(self._items):
            number_of_items = len(self._items)

        return self._items[0:number_of_items]

class BooksProvider(Module):
    @inject
    def __init__(self, items:list):
        self._items = items

    @provider
    def get(self, number_of_items: int=5) -> list:
        if not self._items:
            return []
        if number_of_items > len(self._items):
            number_of_items = len(self._items)

        return self._items[0:number_of_items]


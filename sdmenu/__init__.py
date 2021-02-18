from sdmenu.classes import menu_item
from sdmenu.webworker import menu_cache
from typing import List


class menu:
    def __init__(self) -> 'menu':
        self.cache = menu_cache()

    def get(self, restaurant: str) -> List[menu_item]:
        '''Get a restaurant menu'''
        # TODO: Write this function
        pass

    def has(self, restaurant: str, item: str, time_of_day='Auto') -> bool:
        '''Whether or not the restaurant has the item at the moment'''
        # TODO: Write this function
        pass

    def find(self) -> List[menu_item]:
        '''Search for menu items'''
        # TODO: Write this function
        pass

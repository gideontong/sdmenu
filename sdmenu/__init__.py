from sdmenu.classes import menu_item
from sdmenu.webworker import menu_cache
from typing import List


class menu:
    def __init__(self) -> 'menu':
        self.cache = menu_cache()

    def get(self, restaurant: str) -> List[menu_item]:
        '''Get a restaurant menu'''
        pass

    def has(self, restaurant: str, item: str, time_of_day='Auto') -> bool:
        '''Whether or not the restaurant has the item at the moment'''
        pass

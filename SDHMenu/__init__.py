from SDHMenu.classes import menu_item
from SDHMenu.webworker import menu_cache
from typing import List


class menu:
    def __init__(self):
        self.cache = menu_cache()

    def get(self, restaurant: str) -> List[menu_item]:
        pass

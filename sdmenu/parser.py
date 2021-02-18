from bs4 import BeautifulSoup as Soup
from bs4.element import Tag
from requests.models import Response
from sdmenu.classes import menu_item
from typing import List

DEFAULT_PARSER = 'html.parser'
HOURS_ID = 'hoursContainer'
MENU_ID = 'menuContainer'


def parse_web_items_list(tag: Tag) -> List[menu_item]:
    '''Parse a <ul> subsection of the page'''
    # TODO: Write this function
    pass


class page_object:
    def __init__(self, name: str, time_of_day: str, hours: List[List[int]], menu_items: List[menu_item]) -> 'page_object':
        self.name = name
        self.time_of_day = time_of_day
        self.hours = hours
        self.menu_items = menu_items

    @classmethod
    def from_web_call(cls, dining_hall: str, time_of_day: str, page: Response) -> 'page_object':
        '''Create a page object directly from HTML'''
        soup = Soup(page.text, DEFAULT_PARSER)
        hours_soup = soup.find(id=HOURS_ID)
        menu = soup.find(id=MENU_ID)
        menu = [child for child in menu if type(child) is Tag]
        menu_items = list()
        for child in menu:
            menu_items.extend(parse_web_items_list(child))
        # TODO: Parse page
        hours = list()
        return cls(dining_hall, time_of_day, hours, menu_items)

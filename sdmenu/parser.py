from bs4 import BeautifulSoup as Soup
from bs4.element import Tag
from requests.models import Response
from sdmenu.classes import menu_item
from typing import List

DEFAULT_PARSER = 'html.parser'
HOURS_ID = 'hoursContainer'
MENU_ID = 'menuContainer'


def parse_one_item(tag: Tag) -> menu_item:
    '''Parse a <li> listing to a menu item'''
    name = str()
    price = float()
    link = str()
    nutrition = list()
    for item in tag.contents:
        if item.name == 'a':
            # TODO: name
            # TODO: price
            # TODO: link
            pass
        elif item.name == 'img':
            # TODO: nutritions
            pass
    return menu_item()


def parse_item_list(tag: Tag) -> List[menu_item]:
    '''Parse a <ul> subsection of the menu'''
    if 'id' in tag.attrs and 'nutrition' in tag['id']:
        return list()
    items = list()
    for item in tag.contents:
        if type(item) is Tag and item.name == 'li':
            items.append(parse_one_item(item))
    return items


def parse_web_items(tag: Tag) -> List[menu_item]:
    '''Parse the <div> menu'''
    items = list()
    for container in tag.contents:
        if type(container) is Tag:
            items.extend(parse_item_list(container))
    return items


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
            menu_items.extend(parse_web_items(child))
        # TODO: Parse page
        hours = list()
        return cls(dining_hall, time_of_day, hours, menu_items)

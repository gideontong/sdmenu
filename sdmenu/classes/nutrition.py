'''Hardcoded values for nutrition, since they don't change'''

GLOBAL_ITEMS = [
    {
        'name': 'Vegan',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/Vegan_40x40.png',
        'alt': 'Legend: Vegan Icon'
    },
    {
        'name': 'Vegetarian',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/Vegetarian_40x40.png',
        'alt': 'Legend: Vegetarian Icon'
    },
    {
        'name': 'Wellness',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/Wellness_40x40.png',
        'alt': 'Legend: Wellness Icon'
    },
    {
        'name': 'Dairy',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsDairy_40x40.png',
        'alt': 'Legend: ContainsDairy Icon'
    },
    {
        'name': 'Tree Nuts',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsTreeNuts_40x40.png',
        'alt': 'Legend: ContainsTreeNuts Icon'
    },
    {
        'name': 'Soy',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsSoy_40x40.png',
        'alt': 'Legend: ContainsSoy Icon'
    },
    {
        'name': 'Wheat',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsWheat_40x40.png',
        'alt': 'Legend: ContainsWheat Icon'
    },
    {
        'name': 'Fish',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsFish_40x40.png',
        'alt': 'Legend: ContainsFish Icon'
    },
    {
        'name': 'Shellfish',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsShellfish_40x40.png',
        'alt': 'Legend: ContainsShellfish Icon'
    },
    {
        'name': 'Peanuts',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsPeanuts_40x40.png',
        'alt': 'Legend: Contains Peanuts Icon'
    },
    {
        'name': 'Eggs',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsEggs_40x40.png',
        'alt': 'Legend: Contains Eggs Icon'
    },
    {
        'name': 'Gluten',
        'icon': 'https://hdh-web.ucsd.edu/images/Dining/allergenicons/ContainsGluten_40x40.png',
        'alt': 'Legend: Contains Gluten Icon'
    }
]


class nutrition_item:
    def __init__(self, name: str, icon: str, alt: str):
        self.name = name
        self.icon = icon
        self.alt = alt


nutrition_items = list()
nutrition_url_dict = dict()
for item_data in GLOBAL_ITEMS:
    item = nutrition_item(**item_data)
    nutrition_items.append(item)
    nutrition_url_dict[item.icon] = item


def find_nutrition_by_url(url: str) -> nutrition_item:
    '''Find nutrition by icon URL'''
    if url in nutrition_url_dict:
        return nutrition_url_dict[url]
    else:
        raise KeyError('Provided URL in parser was not valid as a nutrition icon!')
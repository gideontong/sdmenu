from typing import List

NUTRITION_POSITIONAL_ARGUMENTS = {
    'calories': int,
    'cholesterol': float,
    'fat_calories': int,
    'fat': float,
    'fiber': float,
    'ingredients': float,
    'protein': float,
    'saturated_fat': float,
    'serving_size': str,
    'sodium': float,
    'sugars': float,
    'total_carbohydrates': float,
    'trans_fat': float
}


class nutrition_data:
    def __init__(self, **kwargs) -> 'nutrition_data':
        '''Create nutrition data object

        Supported: calories, fat_calories, serving_size, fat, saturated_fat,
        trans_fat, cholesterol, sodium, total_carbohydrates, fiber, sugars,
        protein, ingredients
        '''
        for arg in kwargs:
            pass
        self.calories = kwargs['calories'] if 'calories' in kwargs else None
        self.fat_calories = kwargs['fat_calories'] if 'fat_calories'

    @classmethod
    def from_url(self, url: str) -> 'nutrition_data':
        '''Pass in a UCSD HDH nutrition URL for parsing'''
        pass


class menu_item:
    def __init__(self, name: str, price: float, nutrition: List[str], link: str) -> 'menu_item':
        self.name = name
        self.price = price
        self.nutrition = nutrition
        self.link = link
        self.data = None

    def get_nutrition_data(self) -> nutrition_data:
        '''Get nutrition data of a menu item'''
        if not self.data:
            self.data = nutrition_data.from_url(self.link)
        return self.data

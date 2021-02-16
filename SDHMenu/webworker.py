from datetime import datetime, timedelta
from typing import Tuple

ALLOWED_DINING_HALLS = {
    '64 Degrees',
    'Cafe Ventanas',
    'Canyon Vista',
    'Club Med',
    'Foodworx',
    'OceanView',
    'Pines',
    'Sixth College',
    'The Bistro'
}

ALLOWED_TIMES = {
    'Auto',
    'Breakfast',
    'Lunch',
    'Dinner'
}


def get_current_time() -> Tuple[int, int, int, int, int]:
    '''The current time of day and date

    Returns: Tuple - Year, month, day, day of week, current hour
    '''
    now = datetime.utcnow() + timedelta(hours=-8)
    return now.year, now.month, now.day, now.weekday(), now.hour


class menu_cache:
    def __init__(self):
        self.year, self.month, self.day, weekday, hour = get_current_time()

    def needs_update(self) -> bool:
        year, month, day, weekday, hour = get_current_time()
        if self.year != year or self.month != month or self.day != day:
            pass


def get_current_menu_time():
    pass


def get_menu_page(dining_hall: str, time_of_day: str):
    pass

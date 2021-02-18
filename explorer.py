file = open('test.html').read()
from bs4 import BeautifulSoup as BS
from bs4.element import Tag, NavigableString
soup = BS(file, 'html.parser')
hours_soup = soup.find(id='hoursContainer')

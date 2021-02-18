file = open('test.html').read()
from bs4 import BeautifulSoup as BS
from bs4.element import Tag, NavigableString
soup = BS(file, 'html.parser')
menu = soup.find(id='menuContainer')
print(type(menu))
for child in menu:
    if (type(child) == Tag):
        # TAGS ARE THE ONE WE WANT, we want to filter divs
        print('found tag')
    elif (type(child) == NavigableString):
        print('found string')
    else:
        print('degen', type(child))
    # print(type(child), type(child.string), str(child)[:15], str(child.string)[:15])
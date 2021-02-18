file = open('test.html').read()
from bs4 import BeautifulSoup as BS
from bs4.element import Tag, NavigableString
soup = BS(file, 'html.parser')
menu = soup.find(id='menuContainer')
print(type(menu))
'''
for child in menu:
    if (type(child) == Tag):
        # TAGS ARE THE ONE WE WANT, we want to filter divs
        print('found tag')
    elif (type(child) == NavigableString):
        print('found string')
    else:
        print('degen', type(child))
    # print(type(child), type(child.string), str(child)[:15], str(child.string)[:15])
'''
menu1 = [child for child in menu if type(child) is Tag]
print(len(menu1))
for child in menu1:
    children = [item for item in child.contents if type(item) is Tag]
    print(len(children))
    for item in children:
        print(type(item), item.name, item.attrs)
        item = [x for x in item.contents if type(x) is Tag]
        arr = item.pop(0)
        print(arr)
        for thing in item:
            print(type(thing), thing.name, thing.attrs)
            if thing.name == 'li':
                things = [x for x in thing.contents if type(x) is Tag]
                for i in things:
                    # print(type(i), i.name, i.attrs)
                    if i.name == 'a':
                        print(i['href'])
                        print(i.contents[0].strip())
                exit()
        exit()
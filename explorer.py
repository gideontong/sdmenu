file = open('test.html').read()
from bs4 import BeautifulSoup as BS
from bs4.element import Tag, NavigableString
soup = BS(file, 'html.parser')
hours_soup = soup.find(id='hoursContainer')
for x in hours_soup.div.ul.li.contents:
    if type(x) is Tag:
        s = x.contents[0].strip()
        r = s.split(' ')
        print(r[0], s[4:])
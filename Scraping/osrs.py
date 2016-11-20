import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://oldschool.runescape.com/slu?order=WMLPA').read()
soup = bs.BeautifulSoup(sauce,'lxml')

contents = []
for i in soup.find_all('tr', class_='server-list__row server-list__row--members'):
    print(i.text)
    content = i.text.strip('\n').split('\n')
    content.pop(1)
    contents.append(content)

print(contents)

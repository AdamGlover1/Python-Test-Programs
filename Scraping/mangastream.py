import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://mangastream.com/').read()
soup = bs.BeautifulSoup(sauce,'lxml')

contents = []
for i in soup.find_all('div', class_="featurebox-caption"):
    print(i.text)
    content = i.text.strip('\n').split('\n')
    contents.append(content)

print(contents)

#installin
import urllib.request

from bs4 import BeautifulSoup
from urllib import request

html_file = urllib.request.urlopen('https://in.seamsfriendly.com/?utm_source=google.com&utm_medium=organic')
content = html_file.read()
# print(content)

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify()) #aligns the content

# anchors = soup.findAll('a')
# # print(anchors)  ###<p> tags with  html tags

# for anchor in anchors:
#     print(anchor.text) # <p> tags with  html tags

# divs = soup.findAll('span', class_='ProductItem__Price Price Text--subdued')
# # print(div)
# for div in divs:
#     print(div.text)

titles = soup.findAll('div', class_ = 'Collapsible')
# print(titles)

for title in titles:
    print(title.text)
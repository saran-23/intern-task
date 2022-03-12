from bs4 import BeautifulSoup
import requests

html_text = requests.get('http://saran-23.github.io/Grocery-e-commerce').text
# print(html_text)

soup = BeautifulSoup(html_text,'lxml')
items = soup.findAll('div', class_ = 'module-product-caption')
for item in items:

    prod_name = item.find('a').text
    cart = item.find('button', class_='btn module-product-btn-cart animation rounded-3').text.strip()
    price = item.find('div', class_='module-product-price').text.strip().replace('$', '')
    link = item.a['href']
    print(link)
    if '122' in price:


        print(f"PRODUCT NAME: {prod_name}")
        print(f"PROUDCT PRICE: {price}")
        print(f"PROUDCT STATUS: {cart}\n")

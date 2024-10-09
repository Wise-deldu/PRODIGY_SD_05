import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.banggood.com/search/arduino-kits.html?from=nav')

sp = BeautifulSoup(webpage.content, 'html.parser')

# print(sp.text)

title = sp.find_all('a', 'title')
sellprice = sp.find_all('span', 'price')
origprice = sp.find_all('span', 'price-old')
ratings = sp.find_all('span', 'review')

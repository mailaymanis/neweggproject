import requests
import bs4
# from bs4 import BeautifulSoup
#page1
url = "https://www.newegg.com/p/pl?Submit=StoreIM&Depa=3"
result = requests.get(url)
print(result)

doc = bs4.BeautifulSoup(result.content, "html.parser")

price_current = doc.find_all('div', {'class': 'item-cell'})

for Item in price_current:
	print(Item.find('a',{'class':'item-title'}).text)
	print(Item.find('li', {'class': 'price-current'}).text)
	print('\n\n\n')

#page2
url = "https://www.newegg.com/p/pl?Submit=StoreIM&Depa=3&page=2"
result = requests.get(url)
print(result)

doc = bs4.BeautifulSoup(result.content, "html.parser")

price_current = doc.find_all('div', {'class': 'item-cell'})

for Item in price_current:
	print(Item.find('a',{'class':'item-title'}).text)
	print(Item.find('li', {'class': 'price-current'}).text)
	print('\n\n\n')



import requests
from bs4 import BeautifulSoup



URL = input("Copy and paste the url from the amazon product you want to check:  ")



headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").getText()
    price = soup.find(id="priceblock_ourprice").getText()
    converted_price = price[1:5]

    if (converted_price < '22.1'):
        print('The price is lower')



check_price()




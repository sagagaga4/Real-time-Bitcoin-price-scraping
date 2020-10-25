import bs4
import requests
from bs4 import BeautifulSoup

def parsePrice():
        page = requests.get("https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD")
        soup = BeautifulSoup(page.content, "html.parser")
        price = soup.find_all('div', {'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'})[0].find('span').text
        return price
while True:
        print('the current price: ' + str(parsePrice()))

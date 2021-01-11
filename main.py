import requests
import lxml
from popup import Popup
from bs4 import BeautifulSoup

product_name = ""
product_url = "https://www.amazon.ca/Mercer-Culinary-10-Inch-Forged-Chefs/dp/B000OOLD26/ref=sr_1_" \
              "50?crid=1793CMPNIW4YF&dchild=1&keywords=chef+knife&qid=1610117346&sprefix=chef+%2Caps%2C184&sr=8-50"
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate'
}

search_price = 60.99

response = requests.get(url=product_url, headers=headers).text

soup = BeautifulSoup(response, 'lxml')

product_name = soup.find(name='span', class_="a-size-large product-title-word-break").getText().strip("\n")
price = soup.find(name='span', class_='a-size-medium a-color-price priceBlockBuyingPriceString').getText()
price = float(price.strip('CDN$\xa0'))


if price <= search_price:
    _popup = Popup(product_name, price)

    _popup.window.mainloop()
else:
    print("No price adjustment.")

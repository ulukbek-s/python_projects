import requests
from bs4 import BeautifulSoup

#could not finish due to the error that I could not find a solution

URL = input('Insert the link of the product: ')

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text()
print(title)

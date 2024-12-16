import requests
from bs4 import BeautifulSoup
import json

url = "https://www.cbn.gov.ng/Documents/circulars.html"

get_data= requests.get(url.format(3))

soup = BeautifulSoup(get_data.content,"html.parser")

data = soup.find_all('table')

print(get_data.content)
print(data)
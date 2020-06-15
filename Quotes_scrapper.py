import requests 
from bs4 import BeautifulSoup 
import csv
   
URL = "https://thequotes.com/"
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html.parser')

quotes = soup.findAll('div',{"class":"grid-item quote-data-id"})

filename = "Quotes.csv"
f = open(filename, "w")
headers = "Life-Quotes"

f.write(headers)

for quote in quotes:
    for wrapper in quote.findAll("p",{"class":"grid-item__quote"}):
        print(wrapper.text)
        data = wrapper.text
        f.write(data)
    
f.close()

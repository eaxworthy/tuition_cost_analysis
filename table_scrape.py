from bs4 import BeautifulSoup as bs
import requests

url = 'https://nces.ed.gov/fastfacts/display.asp?id=76'
response = requests.get(url)

#html = response.read().decode('cp1252')
htmlsoup = bs(response.content, "html.parser")
table = htmlsoup.find_all('tr')

rows = [] 
for x in htmlsoup.find_all('table'):
    rows.extend(
         (i for i in x.find_all('tr'))
    )

for row in rows[0:5]:
    print(row)
from bs4 import BeautifulSoup as bs
import requests

url = 'https://nces.ed.gov/fastfacts/display.asp?id=76'
response = requests.get(url)

#html = response.read().decode('cp1252')
htmlsoup = bs(response.content, "html.parser")
table = htmlsoup.find_all('table')



print(table)
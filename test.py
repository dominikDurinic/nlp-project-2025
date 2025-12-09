from bs4 import BeautifulSoup
import requests

url = 'https://deseta-gimnazija.hr/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html')

print(soup.text)

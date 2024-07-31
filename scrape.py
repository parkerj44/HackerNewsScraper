import requests
from bs4 import BeautifulSoup


response = requests.get('https://news.ycombinator.com/news')
print(response.text)

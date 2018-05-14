# Exercise 17 - Decode a Web Page
# For exp with using 'request' library

# Python web libraries
# requests/urllib2 + BeautifulSoup
# Scrapy

import requests as req
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = req.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

for item in soup.find_all(name='h2', attrs={'class': 'story-heading'}):
    if item.a and item.a.contents[0]:
        try:
            print(item.a.contents[0].encode("utf8").strip())
        except IOError:
            print("IOError: " + str(item))
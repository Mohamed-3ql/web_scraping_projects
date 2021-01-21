# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:59:30 2021

@author: mohamed_akel
"""

import requests               # simple http library for python
import re                     # regexp python library
from bs4 import BeautifulSoup # Python library for pulling data out of HTML and XML files


# website url.
url = "https://news.ycombinator.com/news"

# list to keep scraped articles.
articles = []

# request object to get the website.
req_news = requests.get(url)

# fetched website
html_soup = BeautifulSoup(req_news,"html.parser")

# iterate to find the elements which you want.
for item in html_soup.find_all('tr',class_='athing'):
    
    # after we find all tags with athing class name,
    # finding "<a>" tag with class name "storylink".
    item_a = item.find("a", class_="storylink")
    
    # getting hyperlinks of "a" tag with class name "stroylink".
    item_links = item_a.get('href') if item_a else None
    
    # getting the text of "a" tag.
    item_txt = item_a.get_text(strip=True) if item_a else None
    
    
    

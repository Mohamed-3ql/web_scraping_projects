# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:19:26 2021

@author: mohamed_akel
"""

# package that collects several modules for working with URLs
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

# library to pull web data.
from bs4 import BeautifulSoup


def getNames(url):
    """ get authors names function.
    Input:
        url: string contains address of the page
    
    output:
        names: a list contains author names.
    
    """
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        print("Server could not be found")
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        names = bs.find_all('span',{'class':'green'})
    except AttributeError as e:
        return None
    return names
    
url = "http://www.pythonscraping.com/pages/warandpeace.html"

namesList = getNames(url)

print("List Content")
print(namesList)

# iterate through names
for name in namesList:
    
    # seprate the text from the tag
    print(name.get_text())
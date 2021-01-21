# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:52:03 2021

@author: mohamed_akel
"""

# URL handling modules
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

# Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup

# html page url.
url = "http://www.pythonscraping.com/pages/page1.html"

try:
    # pulled html document.
    html = urlopen(url)
    

except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found")
    
else:
    print("it worked!")
    
print("")
print("Function Output:")

def getTitle(url):
    """ Get Title Of The Page Function.
    Input:
        url: string contains address of the page.
        
    Output:
        title: string contains the title of the page.
    """
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.html.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle(url)

# if the title not exist.
if title == None:
    print("Could not be found")
else:
    print(title)
    
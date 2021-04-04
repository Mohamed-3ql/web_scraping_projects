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

# list all the names.
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
    
# get all levels of heading in the page.
def getAllHeadings(url):
    """ get all levels of heading in the page function.
    Input: 
        url: string contains URL of desired page.
    Output:
        headings:list of headings of each level.
    
    """
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        headings = bs.find_all(['h1','h2','h3','h4','h5','h6'])
    except AttributeError as e:
        return None
    return headings
    
# URL for simple html web page
url = "http://www.pythonscraping.com/pages/warandpeace.html"

namesList = getNames(url)

print("List Content")
print(namesList)

# iterate through names
for name in namesList:
    
    # seprate the text from the tag
    print(name.get_text())


def getAllText(url):
    ''' get every text written by each author.
    Input:
    url: a string contains source page url

    Output:
    text_list: a list contains all the text
    '''
    



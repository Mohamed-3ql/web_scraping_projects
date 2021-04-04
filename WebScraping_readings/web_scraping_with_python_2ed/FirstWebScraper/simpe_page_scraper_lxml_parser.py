# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:09:59 2021

@author: mohamed_akel
"""

# URL handling modules
from urllib.request import urlopen 

#  Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup

# page url
url = "http://pythonscraping.com/pages/page1.html"

# pulled html document
html = urlopen(url) 
   

# bs4 object
bs_ = BeautifulSoup(html.read(),'lxml')

# printing the whole page
print("The Entire Page")
print(bs_.html)
print("")

# printing the head section.
print("Heading Section")
print(bs_.head)
print("") 

# printing body section.
print("Body Section")
print(bs_.body)

# accessing elements in the entire html.
print("heading level 1 ")
print(bs_.html.body.h1)
print("")

print("div Section")
print(bs_.html.body.div)
print("")

# accessing each tag directly
print("Head section")
print(bs_.title)
print("")

print("body section")
print(bs_.h1)


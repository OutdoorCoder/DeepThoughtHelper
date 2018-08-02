#! python3 SearchWikiPages.py

# Search the wiki pages for sentences with the number 42 in them

import requests
import bs4
import re


# TODO: replace this base url with a passed in url from the main file
api_url_base = 'https://en.wikipedia.org/wiki/List_of_minor_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Deep_Thought'

res = requests.get(api_url_base)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

pElems = soup.select('p')

for i in range(len(pElems)):
    print(str(pElems[i]))


# (\..*?)42(.*?\.)
#(\..*?)??42(.*?\.)

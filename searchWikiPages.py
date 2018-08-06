#! python3 SearchWikiPages.py

# Search the wiki pages for sentences with the number 42 in them

import requests
import bs4
import re

# TODO: Make this all into a function that gets passed the wiki url
# TODO: Have the wikiurl put together somewhere else, maybe the main page
# TODO: replace this base url with a passed in url from the main file
api_url_base = 'https://en.wikipedia.org/wiki/List_of_minor_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Deep_Thought'

res = requests.get(api_url_base)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
pElems = soup.select('p')

# Match the number 42 and it's surrounding sentence
# The central group is options for the number
# The [^.?!\n]* and [^.?!]* match anything that isn't a the beginning or end of a sentence
# The \W's around 42 make sure that 42 isn't part of a larger number like 32442
fortyTwoRegex = re.compile(r'[^.?!\n]*(?:\W42\W|forty two|forty-two)[^.?!]*[!.?]', re.IGNORECASE)

# This regex removes any html links or other html bit's in the capture text
htmlRemovalRegex = re.compile(r'<.*?>')

matches = fortyTwoRegex.findall(str(pElems))
finalResult = []

for m in range(len(matches)):
    finalResult.append(htmlRemovalRegex.sub('', matches[m]))

print(finalResult)

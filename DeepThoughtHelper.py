#! python3 DeepThoughtHelper.py

# Main program for project

from getWikiPages import getWikiUrlAddresses
from searchWikiPages import searchWikiPages

#TODO: Get parameters for getWikiUrlAddresses
wiki_url_end_address = getWikiUrlAddresses()

# construct those url's above into actual url's
wiki_url_base = 'https://en.wikipedia.org/wiki/'

wiki_url = wiki_url_base + wiki_url_end_address['query']['allpages'][0]['title']

# Search through those wiki pages and find 42!
print(searchWikiPages(wiki_url))

#TODO: Save the results, if any, to the database

#! python3 DeepThoughtHelper.py

# Main program for project
import pymongo
from getWikiPages import getWikiUrlAddresses
from searchWikiPages import searchWikiPages

#TODO: Get parameters for getWikiUrlAddresses from some automated thing you're gonna make
wiki_url_end_address = getWikiUrlAddresses()

# construct those url's above into actual url's
wiki_url_base = 'https://en.wikipedia.org/wiki/'

wiki_url = wiki_url_base + wiki_url_end_address['query']['allpages'][0]['title']

# Search through those wiki pages and find 42!
results = searchWikiPages(wiki_url)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
collection = mydb['test-collection']


dbResult  = collection.insert_one({'text': results, 'url': wiki_url})

#TODO: Save the results, if any, to the database

#! python3 DeepThoughtHelper.py

# Main program for project
import pymongo
import logging

from getWikiPages import getWikiUrlAddresses
from searchWikiPages import searchWikiPages

WIKI_URL_BASE = 'https://en.wikipedia.org/wiki/'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
nextWikiPage = mydb['nextWikiPage']
sentencesWith42 = mydb['sentencesWith42']

def main():
    if nextWikiPage.count() == 0:
        apiFrom = 'aaaaaaa'
    else:
        apiFrom = nextWikiPage.find_one()['nextApiFrom']

    wiki_url_end_address_data = getWikiUrlAddresses(apiFrom)
    wiki_url_end_address = wiki_url_end_address_data['query']['allpages'][0]['title']

    wiki_url = WIKI_URL_BASE + wiki_url_end_address

    # Search through those wiki pages and find 42!
    results = searchWikiPages(wiki_url)

    # also check to make sure the list is populated
    if results:
        logging.info(wiki_url)
        logging.info(results)
        dbResult  = sentencesWith42.insert_one({'text': results, 'url': wiki_url})

    # remove the previous nextWikiPage and insert our new one
    # get our next wiki end address
    nextApiFrom = wiki_url_end_address_data['continue']['apcontinue']

    nextWikiPage.remove({})
    nextWikiPage.insert_one({'nextApiFrom': nextApiFrom})

if __name__ == "__main__":
    main()

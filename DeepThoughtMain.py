#! python3 DeepThoughtHelper.py

# Main program for project
import pymongo
import logging

from getWikiPages import getWikiUrlAddresses
from searchWikiPages import searchWikiPages

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

    #get our next wiki end address
    nextApiFrom = wiki_url_end_address_data['continue']['apcontinue']

    wiki_url_base = 'https://en.wikipedia.org/wiki/'
    wiki_url = wiki_url_base + wiki_url_end_address

    # if we haven't already searched this URL, then insert the row
    # probably don't need this check
    if sentencesWith42.find_one({'url': wiki_url}) == None:
        # Search through those wiki pages and find 42!
        results = searchWikiPages(wiki_url)
        logging.info(wiki_url)
        logging.info(results)
        # also check to make sure the list is populated
        if results:
            dbResult  = sentencesWith42.insert_one({'text': results, 'url': wiki_url})

    # remove the previous nextWikiPage and insert our new one
    nextWikiPage.remove({})
    nextWikiPage.insert_one({'nextApiFrom': nextApiFrom})

if __name__ == "__main__":
    main()

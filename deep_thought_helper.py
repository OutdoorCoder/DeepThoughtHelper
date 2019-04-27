#! python3 DeepThoughtHelper.py
# Main program for project

import pymongo
import logging

from get_wiki_pages import get_wiki_url_pages
from search_wiki_pages import search_wiki_pages

logging.basicConfig(filename='records.log',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

log = logging.getLogger(__name__)

WIKI_URL_BASE = 'https://en.wikipedia.org/wiki/'

#connect to database and setup collections

# test database
#my_client = pymongo.MongoClient("localhost", 27017)

my_client = pymongo.MongoClient("mongodb://OutdoorCoder:aaaaaa1@ds151753.mlab.com:51753/heroku_041hh0sv")
my_db = my_client["heroku_041hh0sv"]
next_wiki_page = my_db['nextwikipage']
sentences_with_42 = my_db['sentencesWith42']

log.info("")

# Get the next wiki pages end address and create the url using wikipedias
# allpages api function
# Then search this next wiki page for any sentences with the number 42l.
# From the results of the allpages call get and store the next wiki page.
def main():
    if next_wiki_page.count() == 0:
        # start at the beginning of the alphabet if we haven't searched anything
        api_from = 'aaaaaaa'
    else:
        api_from = next_wiki_page.find_one()['next_api_from']

    # construct the url
    wiki_url_end_address_data = get_wiki_url_pages(api_from)
    wiki_url_end_address = wiki_url_end_address_data['query']['allpages'][0]['title']

    wiki_url = WIKI_URL_BASE + wiki_url_end_address

    # Search through the wiki page and find 42
    results = search_wiki_pages(wiki_url)

    # if there are results enter them into the database
    if results:
        log.info(wiki_url)
        log.info(results)
        if sentences_with_42.find({'text': results}).count() == 0:
            dbResult  = sentences_with_42.insert_one({'text': results, 'url': wiki_url})

    # get our next wiki end address
    next_api_from = wiki_url_end_address_data['continue']['apcontinue']

    # remove the previous next_wiki_page and insert our new one
    next_wiki_page.remove({})
    next_wiki_page.insert_one({'next_api_from': next_api_from})

if __name__ == "__main__":
    main()

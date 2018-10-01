#! python3 DeepThoughtHelper.py
# Main program for project

import pymongo
import logging

from get_wiki_pages import get_wiki_url_pages
from search_wiki_pages import search_wiki_pages

WIKI_URL_BASE = 'https://en.wikipedia.org/wiki/'

logging.basicConfig(filename='records.log',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

log = logging.getLogger(__name__)


#connect to database and setup collections
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["mydatabase"]
next_wiki_page = my_db['nextwikipage']
sentences_with_42 = my_db['sentencesWith42']

def main():
    if next_wiki_page.count() == 0:
        api_from = 'aaaaaaa'
    else:
        api_from = next_wiki_page.find_one()['next_api_from']

    wiki_url_end_address_data = get_wiki_url_pages(api_from)
    wiki_url_end_address = wiki_url_end_address_data['query']['allpages'][0]['title']

    wiki_url = WIKI_URL_BASE + wiki_url_end_address

    # Search through those wiki pages and find 42!
    results = search_wiki_pages(wiki_url)

    # check to make sure the list is populated
    if results:
        log.info(wiki_url)
        log.info(results)
        dbResult  = sentences_with_42.insert_one({'text': results, 'url': wiki_url})

    # get our next wiki end address
    next_api_from = wiki_url_end_address_data['continue']['apcontinue']

    # remove the previous next_wiki_page and insert our new one
    next_wiki_page.remove({})
    next_wiki_page.insert_one({'next_api_from': next_api_from})

if __name__ == "__main__":
    main()

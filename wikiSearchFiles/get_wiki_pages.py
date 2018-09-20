#! python3 getWikiPages.py

#send html request to wiki Allpages api, then return extension.

import json
import requests
import logging

log = logging.getLogger(__name__)

api_token = ''
api_url_base = 'https://en.wikipedia.org/w/api.php?action=query&list=allpages&aplimit=1&format=json'

headers = {'Content-Type': 'application/json'}

def getWikiUrlAddresses(apiFrom):
    api_url = '{0}&apfrom={1}'.format(api_url_base, apiFrom)
    #print(api_url)
    response = requests.get(api_url, headers = headers)

    #TODO: finish walking through that demo and figure out better error handling/logging
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        log.ERROR('Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None


#wikiUrls = getWikiUrlAddresses()
#print(wikiUrls)
#print(wikiUrls['query']['allpages'][0]['title'])

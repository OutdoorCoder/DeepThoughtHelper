#! python3 getWikiPages.py

#send html request to wiki Allpages api, then return extensions.

#imports

import json
import requests

#https://en.wikipedia.org/w/api.php?action=query&list=allpages&apfrom=aaaa&aplimit=5&format=json

api_token = ''
api_url_base = 'https://en.wikipedia.org/w/api.php?action=query&list=allpages&aplimit=5&format=json'

#TODO: make it so this values is passed in. In the db we'll save the value of this we can iterate
#forward through the alphabet
apiFrom = 'aaaa'

headers = {'Content-Type': 'application/json'}

def getWikiUrlAddresses():
    api_url = '{0}&apfrom={1}'.format(api_url_base, apiFrom)
    print(api_url)
    response = requests.get(api_url, headers = headers)

    #TODO: finish walking through that demo and figure out better error handling/logging
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


wikiUrls = getWikiUrlAddresses()

#TODO: make it so other python files can call this and get back just those Url's
print(wikiUrls)

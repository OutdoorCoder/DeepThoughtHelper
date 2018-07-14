#! python3 getWikiPages.py

#send html request to wiki Allpages api, then return extensions.

#imports

import json
import requests

api_token = ''
api_url_base = 'https://en.wikipedia.org/w/'

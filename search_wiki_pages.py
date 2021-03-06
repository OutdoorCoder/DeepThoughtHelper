#! python3 search_wiki_pages.py
# Search the wiki pages for sentences with the number 42 in them
# Then format that result and return it

import requests
import bs4
import re
import logging

log = logging.getLogger(__name__)
# test url
#api_url_base = 'https://en.wikipedia.org/wiki/List_of_minor_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Deep_Thought'

def search_wiki_pages(url):

    # test url
    #url = "https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy"

    res = requests.get(url)
    if res.status_code == 404:
        log.info(str(res.status_code) + ', ' + url)
        return []

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    p_elements = soup.select('p')

    # Match the number 42 and it's surrounding sentence
    # The central group is options for the number
    # The [^.?!\n]* and [^.?!]* match anything that isn't a the beginning or end of a sentence
    # The negated \w's around 42 make sure that 42 isn't part of a larger number like 32442
    # The negated brackets around 42 make sure we don't get wikipedia footnotes, otherwise the results get flooded
    # with footnotes
    forty_two_regex = re.compile(r'[^.?!\n]*(?<!\d|\w)(?:42|forty two|forty-two)(?!\d|\w)[^.\]\?!]*[!.?]', re.IGNORECASE)
    # This regex removes any html links or other html bit's in the capture text
    html_removal_regex = re.compile(r'<.*?>')

    # get all text that has 42 using the regex
    matches = forty_two_regex.findall(str(p_elements))

    final_result = []
    #remove html from matched text, and then append to results
    for m in range(len(matches)):
        final_result.append(html_removal_regex.sub('', matches[m]))

    return final_result

#print(search_wiki_pages(api_url_base))

import requests
import random
from lxml import html

def webCrawl(url):
    headers = {'User-Agent': 'MyUserAgent/1.0'}
    response = requests.get(url, headers=headers)

    tree = html.fromstring(response.content)

    titles = tree.xpath('//h1[@*]//text()')
    links = tree.xpath('//a/@href')
    linkTitles = tree.xpath('//a/@title')

    return {
        "title": titles[0],
        "links": links,
        "linkTitles": linkTitles
        }

currentURL = 'https://en.wikipedia.org/wiki/Linux'
while True:
    pageData = webCrawl(currentURL)
    print(f'Currently at {pageData['title']}')
    wikiLinks = [l for l in pageData['links'] if l.startswith('/wiki/') and ':' not in l]
    if not wikiLinks:
        print("Reached a dead end..?")
        break
    randomIndex = random.randint(0, len(wikiLinks)-1)
    currentURL = 'https://en.wikipedia.org' + wikiLinks[randomIndex]


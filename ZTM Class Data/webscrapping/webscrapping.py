# Web Scrapping and APIs
import requests
from bs4 import BeautifulSoup
import pprint


response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def cch(links, subtext):
    hn =[]
    for idx, item in enumerate(links):
        title = item.get_text()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].get_text().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn
pprint.pprint(cch(links, subtext))


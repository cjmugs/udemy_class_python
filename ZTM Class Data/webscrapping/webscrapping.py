# Web Scrapping and APIs
import requests
from bs4 import BeautifulSoup


response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

def cch(links, votes):
    hn =[]
    for idx, item in enumerate(links):
        title = links[idx].get_text()
        href = links[idx].get('href', None)
        points = int(votes[idx].get_text().replace('points', ''))
        print(points)
        hn.append({'title': title, 'link': href})
    return hn

print(cch(links, votes))


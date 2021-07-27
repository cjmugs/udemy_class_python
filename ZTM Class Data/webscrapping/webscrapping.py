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
        title = links[idx].getText()
        hn.append(title)
        return hn

print(cch(links, votes))


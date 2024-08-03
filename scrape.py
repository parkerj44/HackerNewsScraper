import requests
from bs4 import BeautifulSoup
import pprint


response = requests.get('https://news.ycombinator.com/news')
html_object = BeautifulSoup(response.text, 'html.parser')
links = html_object.select('.storylink')
subtext = html_object.select('.subtext')


#sort stories
def sorted_stories(list):
    return sorted(list)

# Creates personal Hacker News if points > 100
def personal_hn(links, subtext):
    hacker_news = []

    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hacker_news.append({'title': title, 'link': href, 'votes': points})
    return sorted_stories(hacker_news)


pprint.pprint(personal_hn(links, subtext))

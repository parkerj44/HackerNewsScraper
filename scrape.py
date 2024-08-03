import requests
from bs4 import BeautifulSoup
import pprint


response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')
html_object = BeautifulSoup(response.text, 'html.parser')
html_object2 = BeautifulSoup(response2.text, 'html.parser')
links = html_object.select('.titleline')
links2 = html_object2.select('.titleline')
subtext = html_object.select('.subtext')
subtext2 = html_object2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


#sort stories
def sorted_stories(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

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


pprint.pprint(personal_hn(mega_links, mega_subtext))

from bs4 import BeautifulSoup
import requests


def Samakal(keyword):
    address = "https://samakal.com/search?category=&author=&tag=&date=&headline={}".format(keyword)

    getRequest = requests.get(address, headers = {
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}).text


    soup = BeautifulSoup(getRequest, 'html.parser')

    data = []

    results = soup.findAll('div', {"class": "col-md-12 col-sm-12 col-xs-12"})
    for result in results:
        img = result.find("img")['src']
        title = str(getattr(result.find('h4'), 'text', None)).replace(" ", " ")
        snippet = str(getattr(result.find('p'), 'text', None)).replace(" ", " ")
        link = result.find("a")['href']


        data.append({
            "thumbnail": img,
            "title": title,
            "snippet": snippet,
            "url": link,
        })

    return data


def Politico(keyword):
    address = "https://www.politico.com/search?s=&userInitiated=true&q={}".format(keyword)

    getRequest = requests.get(address, headers = {
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}).text

    soup = BeautifulSoup(getRequest, 'html.parser')

    data = []

    results = soup.findAll('article', {"class": "story-frag"})
    for result in results:
        img = result.find("img")['data-lazy-img']
        title = str(getattr(result.find('h3'), 'text', None))
        snippet = str(getattr(result.find('p'), 'text', None))
        link = result.find("a")['href']


        data.append({
            "thumbnail": img,
            "title": title,
            "snippet": snippet,
            "url": link,
        })

    return data


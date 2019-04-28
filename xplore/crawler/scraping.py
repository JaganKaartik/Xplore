"""

/* This is the main file that contains all the scrappers */

"""

#Google News RSS/XML Crawler

from bs4 import BeautifulSoup
import requests
import json

def glScrape(text):
    htmlurl = 'https://news.google.com/rss/search?q='+text
    url = requests.get(htmlurl)
    soup = BeautifulSoup(url.text,'xml')

    titles = soup.findAll('title')
    titles.pop(0)

    links = soup.findAll('link')
    links.pop(0)

    pubDates = soup.findAll('pubDate')
    pubDates.pop(0)

    descriptions = soup.findAll('description')
    descriptions.pop(0)

    #Dictionary to hold crawled information

    GfeedDict = {}
    te = []

    for i in titles:
        te.append(i.get_text())
        GfeedDict['title'] = te
    te = []
    for i in links:
        te.append(i.get_text())
        GfeedDict['link'] = te
    te = []
    for i in pubDates:
        te.append(i.get_text())
        GfeedDict['pubdate'] = te
    te = []
    for i in descriptions:
        string = i.get_text()
        string = string.split('<p>')[1]
        string = string[:-4]
        te.append(string+"Read More")
        GfeedDict['description'] = te

    return GfeedDict

   
#NewYork Times News RSS/XML Crawler 

def nyScrape(text):
    htmlurl = 'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/'+text+'/rss.xml'
    url = requests.get(htmlurl)
    soup = BeautifulSoup(url.text,'xml')
    
    titles = soup.findAll('title')
    titles.pop(0)
    
    links = soup.findAll('link')
    links.pop(0)
    
    pubDates = soup.findAll('pubDate')
    pubDates.pop(0)
    
    
    descriptions = soup.findAll('description')
    descriptions.pop(0)
    
    #Dictionary to hold crawled information
    
    NYTfeedDict = {}

    #Temporary Dictionary

    te = []

    for i in titles:
        te.append(i.get_text())
        NYTfeedDict['title'] = te
    te = []
    for i in links:
        te.append(i.get_text())
        NYTfeedDict['link'] = te
    te = []
    for i in pubDates:
        te.append(i.get_text())
        NYTfeedDict['pubdate'] = te
    te = []
    for i in descriptions:
        te.append(i.get_text())
        NYTfeedDict['description'] = te

    return NYTfeedDict


def guaScrape(text):
    htmlurl = 'https://www.theguardian.com/'+text+'/rss'
    url = requests.get(htmlurl)
    soup = BeautifulSoup(url.text,'xml')

    titles = soup.findAll('title')
    titles.pop(0)
    titles.pop(0)

    links = soup.findAll('link')
    links.pop(0)

    pubDates = soup.findAll('pubDate')
    pubDates.pop(0)

    descriptions = soup.findAll('description')
    descriptions.pop(0)

    #Dictionary to hold crawled information

    GAfeedDict = {}
    te = []

    for i in titles:
        te.append(i.get_text())
        GAfeedDict['title'] = te
    te = []
    for i in links:
        te.append(i.get_text())
        GAfeedDict['link'] = te
    te = []
    for i in pubDates:
        te.append(i.get_text())
        GAfeedDict['pubdate'] = te
    te = []
    for i in descriptions:
        string = i.get_text()
        string = string.split('<p>')[1]
        string = string[:-4]
        te.append(string+"Read More")
        GAfeedDict['description'] = te

    return GAfeedDict



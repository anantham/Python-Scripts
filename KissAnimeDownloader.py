# KISSANIME - http://kissanime.com/ ANIME DOWNLOADER
import urllib, urllib2, httplib
httplib.HTTPConnection.debuglevel = 1
from bs4 import BeautifulSoup
from selenium import webdriver

BASE_URL = "http://kissanime.com/Anime/"
# EDIT THIS AND ADD YOUR REQUIRED ANIME NAME
AnimeName = "Nodame-Cantabile"
URL = BASE_URL + AnimeName


episodeURLs = []
downloadURLs = []

def getDownloadURLs(url):
    print url
    driver = webdriver.Firefox()
    driver.get(url)
# because they block scrapers, we use "magic browser"! lol
req = urllib2.Request(URL, headers={'User-Agent' : "Magic Browser"})

con = urllib2.urlopen(req)

soup = BeautifulSoup(con)

# gets all the tables
tables = soup.findAll('td')

# we go through the tables
for table in tables:
    try:
        # whenever we get a 'a' tag we extract the 'href' attribute
        episodeURLs.append(table.findAll('a')[0].get('href'))
    # In every alternate line no 'a' exists trying to access the
    # first element ([0]) of an empty list results in this
    except IndexError:
        pass

for episodeURL in episodeURLs:
    downloadURLs = getDownloadURLs("http:/kissanime.com/Anime" + episodeURL)

# KISSANIME - http://kissanime.com/ ANIME DOWNLOADER

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

BASE_URL = "http://kissanime.com/Anime/"
DELAY = 10 # change it depending on your internet connectivity
episodeURLs = []
downloadURLs = []

#------------------------------- EDIT THIS AND ADD YOUR REQUIRED ANIME NAME
AnimeName = "Nodame-Cantabile"
#-------------------------------

URL = BASE_URL + AnimeName

print "Opening firefox Browser"
driver = webdriver.Firefox()

print "Navigating to Login Page"
driver.get("http://kissanime.com/Login")

print "DELAY start"
time.sleep(DELAY)
print "DELAY end"

print "Logging in"
user = driver.find_element_by_name("username")
passwd = driver.find_element_by_name("password")
user.send_keys("<ur username>")
passwd.send_keys("<ur password>")
passwd.send_keys(Keys.RETURN)

print "DELAY start"
time.sleep(DELAY)
print "DELAY end"

print "Navigating to anime episode page"
driver.get(URL)

print "DELAY start"
time.sleep(DELAY)
print "DELAY end"

html = driver.page_source
soup = BeautifulSoup(html)
epListTable = soup.find("table", {"class" : "listing"})

for row in epListTable.findAll('tr'):
    # each row is <td> tag enclosed
    try:
        episodeURLs.append("http://kissanime.com"+row.findAll('a')[0].get('href'))
    except IndexError:
        print "\n Obtaining episode URL's ....\n"

print "These are the episode URL's"
print episodeURLs

for url in episodeURLs:
    print "\n Navigating to get Video for the URL => "+url
    driver.get(url)

    print "DELAY start"
    time.sleep(DELAY)
    print "DELAY end"

    temp = []
    
    html = driver.page_source
    soup = BeautifulSoup(html)
    for div in soup.findAll('div', {"id" : "divDownload"}):
        links = div.findAll('a')
        for link in links:
            dummy = (url[url.find('?')-2:url.find('?')], link.text.strip(), link.attrs['href'])
            temp.append(dummy)
            print "\n\n Temp for"+link.text.strip()
            print temp
            
    downloadURLs.append(temp)
    
for link in downloadURLs:
    print link
    print "\n"


print "Copy paste the above links to a text file, use import from tezt file option in IDM to download all"


            
            
    
    




        

import urllib2
import urllib
from bs4 import BeautifulSoup
import os
import requests



def download(url, filepath):
    page=urllib2.urlopen(url)

    soup=BeautifulSoup(page)
    
    finalurl=soup.find("div", {"id": "comic"}).contents[1].get("src")

    image=urllib.urlopen(finalurl)

    if image.headers.maintype=="image":

        buf=image.read()

        print "Image stored to "+filepath

        download=file(filepath,"wb")

        download.write(buf)

        download.close()
        image.close()

base="https://xkcd.com/"
path='C:\\Users\\Aditya\\Desktop\\Work\\xkcd\\'

for i in range(191,1446):
    
    tempurl=base+str(i)+"/"
    temppath=path+str(i)+".png"
    download(tempurl,temppath)

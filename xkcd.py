import urllib2
import urllib
from bs4 import BeautifulSoup



print "Enter from which xkcd comic onwards should be downloaded"
start=int(raw_input())
print "Enter till which xkcd comic should be downloaded (latest is 1445)"
end=int(raw_input())

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
#change the path here, to whereever you want the directory to be
path='C:\\Users\\Aditya\\Desktop\\Work\\xkcd\\'

for i in range(start,end+1):
    
    tempurl=base+str(i)+"/"
    temppath=path+str(i)+".png"
    download(tempurl,temppath)

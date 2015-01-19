import urllib2
import urllib
from bs4 import BeautifulSoup


print "\nEnter from which xkcd comic onwards should be downloaded"
start=int(raw_input())
print "\nEnter till which xkcd comic should be downloaded \n(latest is somewhere around 1475)"
print "If you want till the latest one just enter a large value \nbut keep a eye on whether you see a lot of 404's cause that signifies the end."
end=int(raw_input())

def download(url, filepath):
    try:
        page = urllib2.urlopen(url)
    except urllib2.HTTPError:
        print "lol, not funny joke, No comic for 404 guys! "
        print "if u see this a lot, all available comics have been downloaded"
        return
    
    soup = BeautifulSoup(page)
    
    finalurl = soup.find("div", {"id": "comic"}).contents[1].get("src")

    try:
        check = "to check, the url ="+finalurl
    except TypeError:
        # Now as finalurl is not a string, we have not scraped the image url,
        # the tag in this page is 'href'!
        finalurl = soup.find("div", {"id": "comic"}).contents[1].get('href')
        print "rare image, we somehow got the URL -> "+soup.find("div", {"id": "comic"}).contents[1].get('href')
        
        # what if we didnt get a image!?
        if(finalurl[:4:-1][0:4] != 'gnp.'):
            print "Not a .png image!!"
            print "backup plan, we use this ->"+soup.find("div", {"id": "comic"}).contents[1].img.get("src")
            finalurl = soup.find("div", {"id": "comic"}).contents[1].img.get("src")
            
    try:
        image = urllib.urlopen(finalurl)
    except AttributeError:
        print "Anomaly - final url was not properly set"
        
    if image.headers.maintype=="image":

        buf = image.read()

        print "Image stored to "+filepath

        download = file(filepath,"wb")

        download.write(buf)

        download.close()
        image.close()
    print "\n"

base="http://xkcd.com/"

# Change the path here, to whereever you want the directory to be
path = "F:\\Work\\xkcd\\"

for i in range(start,end+1):
    tempurl=base+str(i)+"/"
    temppath=path+str(i)+".png"
    download(tempurl,temppath)

import urllib2
import urllib
from bs4 import BeautifulSoup
import os
import requests


def download(url, filename, path1):
     
        
        # open the page url and get the html shit into page
        page=urllib2.urlopen(url)
        
        #soupyfy it and store in soup
        soup=BeautifulSoup(page)
        
        # get the required images (a list with tag matching "img") with
        # ALL its attributes by looking for the tag "img"
        img=soup.findAll("img")
        
        # in the case of mutiple images matching the img tag condition then we are
        # taking each element of the list and getting its Source(src) url
        for imglink in img:
                # final url of the .jpg file
                finalurl=imglink.get("src")
                
        # using finalurl we get the whole image into image
        image=urllib.urlopen(finalurl)
        
        # check if its a image we are dealing with
        if image.headers.maintype=="image":
                
                # read the file into buf
                buf=image.read()
                
                # simply catenate the strings to get the file path
                # path1 is the path of the file's location
                filepath="%s%s" % (path1,filename)

                # print the message to show we have done it
                print filename+" stored to "+filepath

                # open a file handle to write with
                download=file(filepath,"wb")

                # WRITE file to location
                download.write(buf)

                #close both handles
                download.close()
                image.close()
                
                   



# url of the base wesite with which to work with
base="http://www.mangareader.net/beelzebub/"

for j in range(1,240):
        tempurl=base+str(j)+"/"
        #get desktop path (my default download path)
        path=os.getcwd()+"\\Manga\\"
        if not os.path.exists(path+str(j)+"\\"):
                os.makedirs(path+str(j)+"\\")
                path=path+str(j)+"\\"
        for i in range(20):
                url1=tempurl+str(i+1)
                name=str(i+1)+".jpg"
                #checks for 404 error
                check=requests.head(url1)
                if check.status_code==404:
                        break
                        
#call the function to start downloading!
                download(url1,name,path)
        

        


        
        


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
base="http://www.mangareader.net/388-26158-1/red-river/chapter-1.html"

# chapter number - ch_no ; the value will change for different manga its base[34:36]
ch_no=58

#set the storage path HERE (my default download path)
path='C:\\Users\\Aditya\\Desktop\\Work\\WallPapers\\Manga\\'

for j in range(97):
        # base[0:34] give the first 34 characters
        tempurl=base[0:34]+str(ch_no+j)+"-"
        #check if the folder for the 'i+1'th chapter exists
        if not os.path.exists(path+str(j+1)+"\\"):
                #if not make it
                os.makedirs(path+str(j+1)+"\\")
                #and store the pages of the chapter in the chapter folder by changing the path
                path=path+str(j+1)+"\\"
                
        # the loop over the pages
        for i in range(39):
                finalurl=tempurl+str(i+1)+base[38:]
                name=str(i+1)+".jpg"
                #checks for 404 error
                check=requests.head(finalurl)
                if check.status_code==404:
                        break
                        
#call the function to start downloading!
                download(finalurl,name,path)
        

        


        
        


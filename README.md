## Python-Scripts

**A _motley_ collection of python scripts. These are the different programs I wrote for fun.**

### Usage

I will be explaining for a user who works in the windows environment. If any issues come up, please
dont hesitate to contact me.

* Install python 2.7.9 in your system. You can find it [here][5].

* Just download any of the scripts to your computer OR copy the code into a text editor and save it as filename.py

* Check if the individual script prerequisites have been satisfied, they are given below.

* Double click on the file to run OR open the command line there and type 
	
	python filename.py
 

### Overview

* **Root.py**
	This is a program which takes a integer greater than or equal to one and 
	finds its root to the specified accuracy. It was made mainly to compute 
	an irrational number to a specified accuracy.

	No other prerequisites.

* **sonicwall_login.py**
	This is used for automating the whole process of logging into the Sonicwall
	firewall at my college. It is not of any use in my college anymore as logging into 
	sonicwall is not necessary for accessing the Internet.
	I answered a [question][1] in superuser with this code.

	Prerequisites:

	You need to have the selenium python library installed. 
	if you dont have that follow the instructions given at the end.
	Once you have confirmed succesfull installation of that library,

	Install Mozzila firefox, its possible to change the webdriver being used
	to that of chrome, but the existing code needs mozzila.Get it [here][7].

	Also edit the python code and replace <your username> and <your password> with
	your actual username and password.
	If you arent trying to use this for nit trichy, find out the actual url of the login 
	page (the url behind the frame) and replace https://192.168.20.1/auth1.html
	with your url. If you have any trouble finding it contact me.

* **xkcd.py**
	These xkcd comics are one of most favorite comics, so I actually modified the Manga Downloader,
	and made the xkcd comic downloader.

	Prerequisites:

	Replace this "F:\\Work\\xkcd\\" with the path to the folder to which you want to download. 
	Dont forget to add an extra backslash for every backslash (escape sequence)!

* **Manga Downloader.py**
	This was the first real usefull python script I wrote, It was just after I had heard about 
	BeautifulSoup and I wanted to make a program which downloads manga.

	Prerequisites:

	You need to have the selenium python library installed. 
	if you dont have that follow the instructions given at the end.
	Once you have confirmed succesfull installation of that library,

	Edit the script and change the 'base' and 'path' variables to the 
	url of the first page, first chapter of the manga you want to download AND
	the location to which you want to download it respectively.

* **Maximum_subarray.py**
	This is the solution to the problem of finding the subarray with maximum sum, 
	It has been solved in this script using both the dynamic programming approach (O(n)) as well 
	as the divide and conquer approach (O(nlog(n)). I have explained the whole thing in
	my [Blog][2]

* **Kruskal's.py**
	This is a script to find the [Minimal Spanning Tree][3] of a connected, undirected graph,
	using Kruskal's algorithm which is a greedy algorithm. I have also included the I/O of
	a test I conducted with a graph and the image of the graph and its only MST.
	These are the Kruskal\_test.txt and Kruskal\_test.jpg 
	I have used part of this code to answer [this question][4]

* **scrape_results**
	This is a script I had planned to write for some time now, After the second semester results came 
	the first semester results werent available in the site. So now as third semester results are approaching
	I thought of writing this script which just automates the result gathering process, and stores the result
	in my custom class, which is stored to disk as a .student file (ususally just 2KB).

	Prerequisites:

	Yeah just like a lot of the other scripts you need selenium, Set it up.

	Edit the START\_ROLL\_NUMBER and END\_ROLL\_NUMBER to set the range of students you want to save.
	For reference the roll numbers of my year students are given.

* **rename.py**
	This script was born out my requirement to mass rename files (anime, tv series, movies)
	so that Kodi (known as XBMC) would pick it up. I would recommend understanding the code 
	so that you can make the appropriate changes to it and run it.It will now just show what
	changes the script will make.

* **numerical_methods**
	When we got [Janaki Raman Sir](https://tnjanakiraman.wordpress.com/) as our numerical methods teacher
	in Sem IV, he placed great emphasis on the concepts behind the methods, so I decided to implement them
	in python. 
	I havent completed The Illinois method implementation, the regula falsi by itself fails in loads of cases. 



### Setting up Library's 

* Download the zip file [here][6]. 
  For selenium-2.44.0 this is the link, you can install all python library's in this way
  Extract it to a folder.
  Open command promt (or even windows power shell) inside the extracted folder.
  run the following command,

 	python setup.py install

  check whether the installtion was succesfull,
  enter 'python' into the command line. (Without the quotes ofcourse!)
  	python
  this should appear
  	
	PS C:\Users\Aditya\Documents\Projects\Python\Python-Scripts> python
	Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>>

  cool try importing the library you just installed, in our case try,

  	import selenium

  if you dont get a ImportError then you have got it up running.. I guess... :P

[1]: https://superuser.com/questions/330297/automate-logging-in-through-sonicwall/785792?noredirect=1#comment1023176_785792
[2]: http://relativetoaditya.blogspot.in/2014/12/maximum-subarray.html
[3]: https://en.wikipedia.org/wiki/Minimum_spanning_tree
[4]: https://stackoverflow.com/questions/14369739/creating-adjacency-lists-from-dicts-in-python/27380835#27380835
[5]: https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi
[6]: https://pypi.python.org/packages/source/s/selenium/selenium-2.44.0.tar.gz
[7]: https://www.mozilla.org/en-US/firefox/new/
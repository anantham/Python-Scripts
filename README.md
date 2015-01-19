## Python-Scripts

**A _motley_ collection of python scripts. These are the different programs I wrote for fun.**

### Usage

* Install python 2.7.9 in your system. You can find it [here][5].

* Just download this file to your computer OR copy the code into a text editor and save it as filename.py

* Double click on the file to run OR open the command line there and type 
	'python filename.py'

* **Root.py**
	This is a program which takes a integer greater than or equal to one and 
	finds its root to the specified accuracy. It was made mainly to compute 
	an irrational number to a specified accuracy.

* **sonicwall_login.py**
	This is used for automating the whole process of logging into the Sonicwall
	firewall at my college. It is not of any use in my college as logging into 
	sonicwall is not necessary for access the Internet.
	I answered a [question][1] in superuser with this code.

* **xkcd.py**
	These xkcd comics are one of most favorite comics, so I actually modified the Manga Downloader,
	and made the xkcd comic downloader.

* **Manga Downloader.py**
	This was the first real usefull python script I wrote, It was just after I had heard about 
	BeautifulSoup and I wanted to make a program which downloads manga.

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

[1]: https://superuser.com/questions/330297/automate-logging-in-through-sonicwall/785792?noredirect=1#comment1023176_785792
[2]: http://relativetoaditya.blogspot.in/2014/12/maximum-subarray.html
[3]: https://en.wikipedia.org/wiki/Minimum_spanning_tree
[4]: https://stackoverflow.com/questions/14369739/creating-adjacency-lists-from-dicts-in-python/27380835#27380835
[5]: https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi
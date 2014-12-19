from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("http://www.nitt.edu/prm/ShowResult.htm")

driver.get("javascript:(function(){document.getElementsByName('main')[0].contentWindow.document.getElementById('TextBox1').value=110113006;}());")


driver.get("javascript:(function(){document.getElementsByName('main')[0].contentWindow.document.getElementById('Button1').click();}());")

sleep(1)

driver.get("javascript:(function(){document.getElementsByName('main')[0].contentWindow.document.getElementById('Dt1').selectedIndex = 1;document.getElementsByName('main')[0].contentWindow.document.getElementById('Dt1').onchange();}());")

print "I have got the page to a specific student's result!!"

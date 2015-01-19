# -*- coding: cp1252 -*-
# The selenium.webdriver module provides all the WebDriver implementations. get it online, [I got the module from here][1]
from selenium import webdriver
# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

# here, a instance of Firefox WebDriver is created. You can do it for various browsers
driver = webdriver.Firefox()
# The driver.get method will navigate to a page given by the URL.
#WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired)
# before returning control to your test or script.
# It’s worth noting that if your page uses a lot of AJAX on load then WebDriver may not      know when it has completely loaded. so please be patient
driver.get("https://192.168.20.1/auth1.html")
# The next line is an assertion to confirm that title has “Sonic” word in it: (not really neccesary :p)
# This is used to confirm that the webpage is the right one
# some sites may not have it
# assert "Sonic" in driver.title
# we use the 'name' tag to get a handle to the username and password  this finds the appropriate box.
user = driver.find_element_by_name("userName")
passwd = driver.find_element_by_name("pwd")
# use the 'send_keys' function to set the "box's" values to your password and username
user.send_keys("<your username>")
passwd.send_keys("<your password>")
# we sumbit the form
passwd.send_keys(Keys.RETURN)
# we close the window after logging in, the popup which takes care of the 3 hour windows remains open.
driver.close()

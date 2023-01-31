"""
Author: Hai Nguyen
Date: 12th August 2020
Version: 01
Language: python 
Tasks: test scrape aliexpress popular
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
#Must Install bs4, pandas, selenium
# specify the url
urlpage = 'https://m.aliexpress.com/popular/baby.html' 
print(urlpage)
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(5)
#driver.quit()

elements=driver.find_elements("xpath","//p[@class='star-orders']/span[contains(text(),'Sold')]")
if not elements:
    print("No element found")  
else:
    element = elements[0]
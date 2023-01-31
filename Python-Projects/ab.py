from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

MAX_RETRIES = 20

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
session.mount('https://', adapter)
session.mount('http://', adapter)

"""
chOption = Options()
DRIVER_PATH = 'C:/Users/Harry/python-virtual-environments/env/chromedriver_win32/chromedriver.exe'
chOption.add_argument("user-data-dir=C:/Users/Harry/python-virtual-environments/User Data")
chOption.add_argument("--profile-directory=Profile 10");
#chOption.add_argument('headless')
driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=chOption)
"""

DRIVER_PATH = 'C:/Users/Harry/python-virtual-environments/env/geckodriver-v0.26.0-win64/geckodriver.exe'
driver = webdriver.Firefox(executable_path=DRIVER_PATH)

#launch url
url = "https://dictionary.cambridge.org/vi/dictionary/english-vietnamese/abandon"
#url = "https://shopee.vn"
#r = session.get(url)

#headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}

headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'DNT':'1',
'Host':'example.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
 }


req = requests.get("https://shopee.vn", headers)
 
#req = requests.get(url, headers)

#soup = BeautifulSoup(req.content, 'html.parser')
#print(soup.prettify())

"""
word = driver.find_element_by_xpath(".//div[@class = 'dpos-h di-head normal-entry']").text
example = driver.find_element_by_xpath(".//div[@class = 'di-body normal-entry-body']").text

print(word)
print(example)
#di-body normal-entry-body
#dpos-h di-head normal-entry
"""

#driver.quit()
"""
Author: Hai Nguyen
Date: 20th July 2020
Version: 01
Language: python 
Tasks: scrape Cambridge Dictionary words from a List
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
#Must install selenium and 
# download chromedriver according the the current chrome browser version on the running machine

defPath2 = './pics/content2/'
wordPath2 = './pics/words2/'
word_Path2 = 'wordList.txt'

def writeListOfStr(list,name="abcd"):
	f= open(name+ ".txt","a+", encoding = 'utf-8')
	for i in range(len(list)):
		f.write(list[i])
	f.close() 
#def readList(list,name="abcde"):
f= open(word_Path2,"r")
sList= f.readlines()
f.close() 

DRIVER_PATH = 'chromedriver.exe'
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)
#driver.get("https://dictionary.cambridge.org/vi/dictionary/english-vietnamese/abandon")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://www.google.com")

path = "https://dictionary.cambridge.org/vi/dictionary/english-vietnamese/"

#sList = ["abandon","academy","alternative","analyse","amend"]	#list contains words to scrape
jobList = []	#List to be used in scrapeDict method

#Method - set the number of words to scrape from the sList and Add them to jobList
def getSearchTerm(list,jList,count):
	for i in range(count):
		a = list.pop(i)
		jList.append(a)
		print(a)
	print("\n")
	


#Method to scrape words definition from a list
def scrapeDict(jList):
	i = 0
	list_02 = []
	list_01 = []	
	for i in range(len(jList)):
		url = path + jList[i]
		example_List = []
		driver.get(url)
		driver.implicitly_wait(100)
		skip = False
		try:
			#word = driver.find_element_by_xpath(".//div[@class = 'dpos-h di-head normal-entry']").text
			word_Type = driver.find_element("xpath", value=".//span[@class='dpos-h_hw di-title']").contents
			word_Mean = driver.find_element("xpath", value=".//span[@class='pron dpron']").contents
			list_02.append(" "+jList[i] + word_Type + " " + word_Mean+ "\n")
			list_02.append("**************************\n")
		except NoSuchElementException:
			skip = True
		if not skip:
			try:
				#example = driver.find_element_by_xpath(".//div[@class = 'pos-body']").text
				example_List1 = driver.find_elements_by_xpath("//div[@class='pos-body']/*//div[@class='def ddef_d db']")
				example_List2 = driver.find_elements_by_xpath("//div[@class='pos-body']/*//span[@class='eg deg']")
				example_Listvn = driver.find_elements_by_xpath("//div[@class='pos-body']/*//span[@class='trans dtrans']")
			
				#print("Term : " + jList[i] + "\n"+ word_Type + " " + word_Mean)
				#print("**************************\n")
				
				
				for j in range(len(example_List1)):
					list_01.append(example_Listvn[j].text+ " \n"+ " . " + example_List1[j].text)
					#if j < len(example_List2):
				for k in range(len(example_List2)):
					list_01.append("_ " +example_List2[k].text+"\n")
			except NoSuchElementException:
				print("missing something here!")
			try:	
				moreRef = driver.find_element_by_xpath("//div[@class='lcs']").text
				
				list_01.append("Xem Thêm: " + "\n" +moreRef+ "\n")
			except NoSuchElementException:
				print("No more!")
			
			list_01.append("**************************\n")
				#print(list_01[j])
		else:
			print("Skipped a Link: " + jList[i])
	writeListOfStr(list_01,"content02")
	writeListOfStr(list_02,"wordMean02")
	
	for l in list_02:
		print(l)
	for k in list_01:
		print(k)
	jList.clear()
	list_01.clear()
	list_02.clear()

	"""
		count = len(example_List1) - len(example_List2)
		if count == 0:
			for j in range(len(example_List1)):
				print(str(j)+ ": " +example_Listvn[j].text+ " \n"+ " . " +example_List1[j].text+ " \n"+ "_ " +example_List2[j].text + "\n")
		else:
			for j in range(len(example_List2)):
				print(str(j)+ ": " +example_Listvn[j].text+ " \n"+ " . " +example_List1[j].text+ " \n"+ "_ " +example_List2[j].text + "\n")
				print(example_List2[k].text + "\n")
		"""		
		#print("Xem Thêm: " + "\n" +moreRef+ "\n")

"""
#Call function getSearchTerm
getSearchTerm(sList,jobList,6)		

#Input a list of words to scrape for definitions
scrapeDict(jobList)
"""
def drainList(listBreak,listWork,count):
	for i in range(int(len(listBreak)/count)):
		getSearchTerm(listBreak,listWork,count)	
		scrapeDict(listWork)
		print("Round : " + str(i))
		print("Please Wait...")
drainList(sList,jobList,5)

driver.quit()
"""
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
"""
"""
Author: Harry Nguyen
Date: 17th July 2022
Version: 02
Language: python 
Tasks: scrape Ielts Dictionary words and write to 3 seperate text Lists
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#launch url
url = "https://www.examword.com/ielts-flashcard/500-vocabulary-1?la=en&nu=1"

page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
driver.get(url)
driver.implicitly_wait(200)

#content = driver.find_element_by_xpath(".//div[@class = 'cardExp']").text
## The Whole Definition + example

#One Element Each
w_Type = driver.find_element(By.XPATH, ".//*[contains(@class,'listWordType')]").text
w_Explain = driver.find_element(By.XPATH, ".//*[contains(@class,'listWordExplanation')]").text

#list of elements
w_TypeList = driver.find_elements(By.XPATH, ".//*[contains(@class,'listWordType')]")
w_ExplainList = driver.find_elements(By.XPATH, ".//*[contains(@class,'listWordExplanation')]")

#w_WordList = driver.find_elements_by_xpath(".//*[contains(@class,'cardWord')]")
w_WordList = driver.find_elements(By.XPATH, ".//*[contains(@class,'cardWord')]")
lines = []
storage = []
def getPrint(list,count):
	for i in range(len(list)):		# in this case both list have the same len()
		j = 0
		while j < count and j < len(list):
			lines.append(list[j].text)
			storage.append(list[j].text)
			del list[j]
			j+=1

a4Width, a4Height = int(11.7 * 300), int(8.27 * 300) # A4 at 300dpi landscape	
#a4Width, a4Height = int(8.27 * 300), int(11.7 * 300) # A4 at 300dpi portrait

path = './pics/content/'
wordPath = './pics/words/'

imageW = int(a4Width/5)
imageH = int(a4Height/5)
basicFont = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', size=34)
italicFont = ImageFont.truetype('C:/Windows/Fonts/arialni.ttf', size=34)
boldFont = ImageFont.truetype('C:/Windows/Fonts/arialnb.ttf', size=34)

def text_wrap(text, font, max_width):
	listA = []
        
	# If the text width is smaller than the image width, then no need to split
	# just add it to the line list and return
	if font.getsize(text)[0]  <= max_width:
		listA.append(text)
	else:
		#split the line by spaces to get words
		words = text.split(' ')
		i = 0
		# append every word to a line while its width is shorter than the image width
		while i < len(words):
			line = ''
			while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
				line = line + words[i]+ " "
				i += 1
			if not line:
				line = words[i]
				i += 1
			listA.append(line)
	return listA
	
def drawTextOnImage(list,path,type=None,plus=False):
	count = 0
	nextW = 0
	fill = "black"
	
	if type == "italic":
		font = italicFont
		fill = "blue"
	elif type == "bold":
		font = boldFont
		fill = "red"
	else:
		font = basicFont
	for i in list:
		if not plus:
			img = Image.new('RGB', (imageW, imageH), color=(255, 255, 255))
			nextH = 0
			# create the canvas
			canvas = ImageDraw.Draw(img)
			text_width, text_height = canvas.textsize(i, font=font)
			
			x_pos = int(imageW/5)
			y_pos = text_height*3 + int((imageH - text_height)/5)
			
			listB = text_wrap(i, font, 456)
			for index in listB:
				canvas.text((x_pos, y_pos+nextH), index, font=font, fill=fill, align = "right")
				nextH += text_height
				
			img.save(path + str(count) +".jpg")	
			count += 1
		else:
			img = Image.open(path + str(count) +".jpg")
			nextH = 0
			# create the canvas
			canvas = ImageDraw.Draw(img)
			text_width, text_height = canvas.textsize(i, font=font)
			
			x_pos = int(imageW/5)
			y_pos = int((imageH - text_height)/5)
			
			listB = text_wrap(i, font, 456)
			for index in listB:
				canvas.text((x_pos, y_pos+nextH), index, font=font, fill=fill, align = "right")
				nextH += text_height
				
			img.save(path + str(count) +".jpg")	
			count += 1
	list.clear()


		
def drainList(break_list,work_list,path,type= None,option=False):
	for i in range(int(len(break_list)/25)):
		getPrint(break_list,25)
		drawTextOnImage(work_list,path,type,option)

#drainList(w_ExplainList,lines,path, "italic")
#drainList(w_TypeList,lines,wordPath)
#drainList(w_WordList,lines,wordPath, "bold", True)

def writeList(list,name="abcd"):
	f= open(name+ ".txt","w+", encoding = 'utf-8')
	for i in range(len(list)):
		f.write(list[i].text+"\n")
	f.close() 

writeList(w_WordList,"wordList")
writeList(w_TypeList, "typeList")
writeList(w_ExplainList, "ExplainList")

driver.quit()
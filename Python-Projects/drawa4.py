"""
Author: Hai Nguyen
Date: 10th July 2020
Version: 01
Language: python 
Tasks: draw flash cards for IELTS
"""
from PIL import Image, ImageDraw, ImageFont
#Must install Pillow
	
a4Width, a4Height = int(11.7 * 300), int(8.27 * 300) # A4 at 300dpi landscape	
#a4Width, a4Height = int(8.27 * 300), int(11.7 * 300) # A4 at 300dpi portrait

printPath1 = './pics/print1/'
printPath2 = './pics/print2/'
contentPath = './pics/content/'
wordPath = './pics/words/'

album = []
top = []
def albumAdd(list,path):
	link_List = []
	for i in range(100):
		link_List.append(path+str(i)+".jpg")
		list.append(Image.open(link_List[i]).resize((int(a4Width/5), int(a4Height/5))))
		

albumAdd(album,contentPath)
albumAdd(top,wordPath)


# In order to print double-sided - list must be swapped
def swapList(list,p1,p2,cre):
	list_Swap = list
	pos1 = p1
	pos2 = cre-p1-1
	increment = cre 
	while pos1 in range(len(list)):
		#print(str(pos1) + " : " + str(pos2))
		if pos1 <= (len(list)-cre):
			list[pos1],list[pos2] = list[pos2],list[pos1]
		else:
			print("ignored")
		pos1+=5
		pos2+=5

#swap top list horizontally
swapList(top,0,4,5)
swapList(top,1,3,5)

def makeImGrid(path,list,count,name=""):
	left = 0
	right = 0
	dst = Image.new('RGB', (a4Width, a4Height))
	for k in range(25):
		if a4Width-left >= list[k].width:
			dst.paste(list[k], (left, right))
			left += list[k].width
		else:
			left = 0
			right+= list[k].height
			dst.paste(list[k], (left, right))
			left += list[k].width
			print("Jumped Down One Line")
	dst.save(path + name  +str(count)+".jpg")	
	del list[:25]

def makeIt(apath,list,name=""):
	count = int(len(list)/25)
	for i in range(count):
		makeImGrid(apath,list,i,name)
	
	
makeIt(printPath1,album,"word")
makeIt(printPath2,top,"content")
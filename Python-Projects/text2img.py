"""
Author: Harry Nguyen
Date: 8th July 2020
Version: 01
Language: python, PIL
Tasks: draw texts on images in pics folder
"""

from PIL import Image, ImageDraw, ImageFont

a4Width, a4Height = int(11.7 * 300), int(8.27 * 300) # A4 at 300dpi landscape	
#a4Width, a4Height = int(8.27 * 300), int(11.7 * 300) # A4 at 300dpi portrait

path = './pics/'

lines = ["abandon", "/ə'bændən/ n. Syn. relinquish lacking restraint or control; feeling of extreme emotional intensity; unbounded enthusiasm"]

imageW = int(a4Width/5)
imageH = int(a4Height/5)
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', size=34)

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
	
def drawTextOnImage(list):
	count = 0
	nextW = 0
	nextH = 0
	for i in list:
		img = Image.new('RGB', (imageW, imageH), color=(51, 144, 255))
		
		# create the canvas
		canvas = ImageDraw.Draw(img)
		text_width, text_height = canvas.textsize(i, font=font)
		
		x_pos = int(imageW/5)
		y_pos = int((imageH - text_height)/5)
		
		listB = text_wrap(i, font, 456)
		for index in listB:
			canvas.text((x_pos, y_pos+nextH), index, font=font, fill='#FFFFFF', align = "right")
			nextH += text_height
			
		img.save(path + str(count) +".jpg")	
		count += 1

drawTextOnImage(lines)


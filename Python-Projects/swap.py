"""
Author: Harry Nguyen
Date: 11th July 2020
Version: 01
Language: python 
Tasks: swap a list of words to print double-sided on A4 paper dimension
"""

list1 = [ 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
def swapList(list,p1,p2,cre):
	list_Swap = list
	pos1 = p1
	pos2 = cre-p1-1
	increment = cre 
	while pos1 in range(len(list)):
		print(str(pos1) + " : " + str(pos2))
		if pos1 <= (len(list)-cre):
			list[pos1],list[pos2] = list[pos2],list[pos1]
		else:
			print("ignored")
		pos1+=5
		pos2+=5

def printI(list):
	for i in list:
		print(i)
printI(list1)	
print("\n")
swapList(list1,0,4,5)
printI(list1)		
swapList(list1,1,3,5)
print("\n")
printI(list1)	
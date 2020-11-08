"""
	5.	Keyboard Row 
	Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
 
	Example:
		Input: ["Hello", "Alaska", "Dad", "Peace"]
		Output: ["Alaska", "Dad"]
"""

def typeWithOneRow(str):
	isRotTop = True
	isRowMiddle = True
	isRowButton = True
	rowTop = {'q','w','e','r','t','y','u','i','o','p'}
	rowMiddle = {'a','s','d','f','g','h',"j",'k','l'}
	rowButton = {'z','x','c','v','b','n','m'}
	strcp = []
	for i in str:
		for j in i:
			j = j.lower()
			if isRotTop and j in rowTop:
				pass
			else:
				isRotTop = False
			if isRowMiddle and j in rowMiddle:
				pass
			else:
				isRowMiddle = False
			if isRowButton and j in rowButton:
				pass
			else:
				isRowButton = False
			if not isRotTop and not isRowMiddle and not isRowButton:
				break
		if isRotTop or isRowMiddle or isRowButton:
			strcp.append(i)
		isRotTop, isRowMiddle, isRowButton = True, True, True
	return strcp

if __name__ == "__main__":
	str = ['Hello', 'Alaska', 'Dad', "Peace"]
	print("INPUT:\tstr =", str)
	print("OUTPUT:\t", typeWithOneRow(str))
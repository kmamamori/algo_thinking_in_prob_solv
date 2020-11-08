"""
	3.	Most Common Word
	Given a string of words separated by spaces, find the word that appears the most in the string
	Example:
		Given “hello world hello hello world hi”
		Return hello
"""


def mostStringAppearance(str):
	spltStr = str.split()
	tracker = {}
	for i in spltStr:
		if tracker.get(i)==None:
			tracker[i] = 1
		else:
			tracker[i] += 1
	max_num = 0
	max_str = ""
	for s, n in tracker.items():
		if n > max_num:
			max_str = s
			max_num = n
	return max_str

if __name__ == "__main__":
	str = "hello world hello hello world hi"
	print("INPUT:\t str =", str)
	print("OUTPUT:\t", mostStringAppearance(str))
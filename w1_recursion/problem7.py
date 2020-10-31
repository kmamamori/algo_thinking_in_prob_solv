"""
	Problem 7: Write a method called splitArray that receives an array of ints as input and determines whether it is possible to divide the ints into two groups, so that the sums of the two groups are the same.
	Every int must be in one group or the other.
	Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper from splitArray. (No loops needed.)
"""

import numpy as np

def findsubset(S, S2, last, g):
	if g==0:
		return True, []
	if g<0 or last<0:
		return False, []
	res, subset = findsubset(S, S2, last-1, g-S[last])
	if res:
		subset.append(S[last])
		S2.remove(S[last])
		return True, subset
	else:
		return findsubset(S, S2, last-1, g)

def partition(S):
	t = sum(S)
	if t%2==0:
		S2=[i for i in S]
		a, s = findsubset(S, S2, len(S)-1, t//2)
		if a:
			print("\nMain set:", S)
			print("Solution:", s, " & ", S2)
		else: 
			print("There is no solution")
	else:
		print("There is no solution")


arr = [1, 2, 3]
partition(arr)

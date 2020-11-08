"""
	4.	Single Number
	Given a non-empty array of integers, every element appears twice except for one. Find that single one.
		Example 1: Input: [2,2,1] Output: 1
		Example 2: Input: [4,1,2,1,2]Output: 4
"""


def findOne(arr):
	tracker = {}
	for i in arr:
		if tracker.get(i) == None:
			tracker[i] = 1
		else:
			tracker[i] += 1
	for s, n in tracker.items():
		if n%2==0:
			continue
		else:
			return s


if __name__ == "__main__":
	arr = [2, 2, 1]
	print("INPUT:\tarr =", arr)
	print("OUTPUT:\t", findOne(arr))
	arr = [4,1,2,1,2]
	print("INPUT:\tarr =", arr)
	print("OUTPUT:\t", findOne(arr))

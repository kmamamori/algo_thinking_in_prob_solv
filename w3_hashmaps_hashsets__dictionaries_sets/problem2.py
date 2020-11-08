"""2.	Repeated Number
	You are given an array of integers called nums. 
	The numbers stored in the array appear only once except for one.
	Write a method that finds this number
	Example:
		nums = [3, 4, 6, 1, 3, 10, -1] return 3
"""

def repatedNum(nums):
	arr = [[] for i in range(10)]
	for i in nums:
		appendingindex = i%10
		if i in arr[appendingindex]:
			return i
		else:
			arr[appendingindex].append(i)
	return None

if __name__ == "__main__":
	nums = [3,4,6,1,3, 10, -1]
	print("INPUT: nums =", nums)
	print("OUTPUT: ", repatedNum(nums))
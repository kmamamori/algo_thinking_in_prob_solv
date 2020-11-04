"""
	1.	TwoSum 
	Given an array of integers, return the indices of the two numbers that add up to a specific target.
	You may assume that each input would have exactly one solution, and you may not use the same element twice.
	Example:
		Given nums = [2, 7, 11, 15], target = 9,
		Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""

def adding2numbers(testingarray, target):
	additionarray = []
	for i in range(len(testingarray)-1, -1, -1):
		if target == 0 and len(additionarray) == 2:
			return additionarray
		if target > testingarray[i] and len(additionarray) == 0:
			target -= testingarray[i]
			additionarray.append(testingarray[i])
		elif testingarray[i] == target and len(additionarray) == 1:
			additionarray.append(testingarray[i])
			return additionarray

def main():
	target = 9
	nums = [2,7,11,15]
	print(adding2numbers(nums, target))
	

main()
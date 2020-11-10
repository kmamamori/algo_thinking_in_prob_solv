"""
	Problem 3: Rotate Array
		Given an array, rotate the array to the right by k steps, where k is non-negative.
		Example 1:
			Input: [1,2,3,4,5,6,7] and k = 3
			Output: [5,6,7,1,2,3,4]
			Explanation:
				rotate 1 steps to the right: [7,1,2,3,4,5,6]
				rotate 2 steps to the right: [6,7,1,2,3,4,5]
				rotate 3 steps to the right: [5,6,7,1,2,3,4]
		Example 2:
			Input: [-1,-100,3,99] and k = 2
			Output: [3,99,-1,-100]
			Explanation:
				rotate 1 steps to the right: [99,-1,-100,3]
				rotate 2 steps to the right: [3,99,-1,-100]
		Write two solutions to this problem:
			First solution: No constrains, just solve the problem
			Second solution: Solve the problem in-place – O(1) extra space
"""


def rotateArray(arr, tarkget):
    arr1 = [0 for i in range(len(arr))]
    index = 0
    for i in range(0, len(arr)):
        index = -len(arr) + k + i
        arr1[index] = arr[i]
    return arr1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("INPUT: k =", k)
    print("INPUT: arr =", arr)
    print("OUTPUT: ", rotateArray(arr, k))

    arr = [-1, -100, 3, 99]
    k = 2
    print("INPUT: k =", k)
    print("INPUT: arr =", arr)
    print("OUTPUT: ", rotateArray(arr, k))

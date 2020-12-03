"""
1.	Given two sorted arrays a1 and a2 of size m and n. Find the median of the two sorted arrays in O(log (m + n)).

Example:
	[1, 4, 5, 8], [2, 3, 6] -> 4
	[1, 4, 5], [2, 3, 6] -> 3.5

	Input: 2 arrays
	Output: double
"""

def  find_median(a1, a2):
    print("INPUT:\t", a1, a2)
    arr = []
    i, j = 0, 0
    lenarr = len(a1) + len(a2)
    while j+i < lenarr:
        if i == len(a1):
            arr = [a2[j]] + arr
            j += 1
            continue
        if  j == len(a2):
            arr = [a1[i]] + arr
            i += 1
            continue
        if a1[i] < a2[j]:
            arr = [a1[i]] + arr
            i += 1
        else:
            arr = [a2[j]] + arr
            j += 1
    print("Combined array:\t", arr)
    if lenarr%2 == 1:
        return arr[lenarr//2]
    else:
        return 0.5*(arr[lenarr//2] + arr[lenarr//2-1])

if __name__ == "__main__":
    a1, a2 = [1,4,5], [2,3,6]
    print("OUTPUT\t", find_median(a1, a2), "\n")
    a1, a2 = [1,4,5,8], [2,3,6]
    print("OUTPUT\t", find_median(a1, a2), "\n")
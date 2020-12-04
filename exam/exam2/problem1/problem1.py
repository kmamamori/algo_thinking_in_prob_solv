"""
1 - Minimum Falling Path Sum

Given a square array of integers A, we want the minimum sum of a falling path through A.
A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
•	[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
•	[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
•	[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.
 Note:
1.	1 <= A.length == A[0].length <= 100
2.	-100 <= A[i][j] <= 100

"""

def minimumFallingPathSum(arr):
    n1, n2, c = 0, 0, 0
    n = len(arr)
    for i in range(n-2, -1, -1):
        n1, n2 = 1000, 1000
        for j in range(0, n, 1):
            if arr[i+1][j] < n1:
                n2 = n1
                n1 = arr[i+1][j]
                c = j
            elif arr[i+1][j] < n2:
                n2 = arr[i+1][j]
        for j in range(0, n, 1):
            arr[i][j] += n2 if j == c else n1
        return min(arr[-2])

if __name__ == "__main__":
    print(minimumFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
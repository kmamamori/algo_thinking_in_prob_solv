"""
	Problem 4: DI String Match
		Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
		Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
			•	If S[i] == "I", then A[i] < A[i+1]
			•	If S[i] == "D", then A[i] > A[i+1]
			
		Example 1:
			Input: "IDID"
			Output: [0,4,1,3,2]
		Example 2:
			Input: "III"
			Output: [0,1,2,3]
		Example 3:
			Input: "DDI"
			Output: [3,2,0,1]
			
		Note:
			1.	1 <= S.length <= 10000
			2.	S only contains characters "I" or "D".
"""


def stringMatch(S):
    arr = [i for i in range(len(S) + 1)]
    arr2 = []
    for i in range(0, len(S)):
        if S[i] == "D":
            arr2.append(arr.pop(-1))
        else:
            arr2.append(arr.pop(0))
    arr2.append(arr.pop(0))
    return arr2


if __name__ == "__main__":
    S = "IDID"
    print("INPUT: ", S)
    print("OUTPUT:", stringMatch(S))

    S = "III"
    print("INPUT: ", S)
    print("OUTPUT:", stringMatch(S))

    S = "DDI"
    print("INPUT: ", S)
    print("OUTPUT:", stringMatch(S))

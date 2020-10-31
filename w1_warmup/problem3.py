"""
	Ken Amamori
	Problem 3: Write a function to return a copy of a list of strings with duplicates removed.
	Preserve order in the original list as much as possible (keep first occurrence).
	If you solve this quickly, reimplement the function, but only keep the strings that appear at least n times in the list (n is specified as a parameter).
	Example: [foo, bar, baz, foo, bar] -> [foo, bar, baz]
	Time: O(n), Space: O(n)
"""

testingarray = ["foo", "bar", "baz", "foo", "bar", "abc", "abc", "foo"]
outputarray = []

for v1 in testingarray:
	if v1 in outputarray:
		continue
	else:
		outputarray.append(v1)

print(outputarray)
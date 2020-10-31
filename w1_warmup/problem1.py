"""
	Ken Amamori
	Problem 1: Reverse all the words in a string of words and spaces / tabs while preserving the word order and spacing.
	Example: “moo cow bark dog” -> “oom woc krab god
    time: O(n), space: O(n)
"""


testingstring = "moo cow bark dog"

outputstring = ""
tempstring = ""

for v in testingstring:
    if v == " ":
        outputstring = outputstring + tempstring
        outputstring = outputstring + " "
        tempstring = ""
    else:
        tempstring = v + tempstring

outputstring = outputstring + tempstring

print(":"+outputstring+":")

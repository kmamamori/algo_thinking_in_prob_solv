"""
	Ken Amamori
	Problem 5: Return the longest contiguous substring of 2 distinct characters from an input string.
	Example
		input: abbaacab return: abbaa
		input: abcefabbabaabefghghfa return: abbabaab
		input: aabceddddcdccecabceftg  return: ddddcdcc
		input: acbabbcbca  return : bbcbc

	Tracing requried since used Google.
	Time: O(n^2), Space: O(n)
"""

#function which returns longest substring with two distinct characters
def repeatedString(strng):
	if len(strng)==0:
		return ""
	i=0
	max_len=0
	start=0
	end=-1
	dict={strng[0]:1}
	for j in range(1,len(strng)):
		if strng[j] in dict.keys():
			dict[strng[j]]+=1
		else:
			dict[strng[j]]=1
		while(len(dict)>2):
			dict[strng[i]]-=1
			if dict[strng[i]]==0:
				del dict[strng[i]]
			i+=1
		if len(dict)==2:
			if max_len<(j-i+1):
				max_len=j-i+1
				start=i
				end=j
	return strng[start:(end+1)]

strng=input()
print(repeatedString(strng))

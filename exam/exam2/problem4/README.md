### minimum ascii delete sum for two strings:
## Problem:
- Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

## Explain:
Creating an arrayin order to reach to the answer. If one side (string) is null (empty) the result is the other string's ascii sum. Whenever the characters in the stirng at the same index are the same, ignore it, if they are different, delete since theirs previos character. Repeat the above until everything is covered. At the end, the result will be stored in the last index from both col and row.
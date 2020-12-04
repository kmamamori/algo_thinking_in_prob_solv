### Integer Break
## Problem:
- Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

## Explain:
- Getting 5 as an input, we can come up with, (1,4) -> 4, (2,3)-> 6 and the answer should be 6. However, never reaching (3,2) nor (4,1) since it is not a needed computation. Note that, a character can be diveded into a addition for instance 3 -> (1,3) partition, which means that by using recursive method, partition in partition is needs to be accomplished. Stored the visited integer into the array of size+1, and repeating the partitioin, the last element on the array will be the resut. By comparing the array at i where i is [1, n+1], j*(i-j) where j is [1, i], m at (i-j) times j accomplishes the recusively computation which leads to the result.


## Example:
# Example 1:
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

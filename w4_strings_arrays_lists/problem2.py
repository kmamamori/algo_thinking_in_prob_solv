"""
	Problem 2: Convert Binary Number in a Linked List to Integer

	Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
	Return the decimal value of the number in the linked list.
	Example 1:
		Input: head = [1,0,1]
		Output: 5
		Explanation: (101) in base 2 = (5) in base 10
	Example 2:
		Input: head = [0]
		Output: 0
	Example 3:
		Input: head = [1]
		Output: 1
	Example 4:
		Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
		Output: 18880
	Example 5:
		Input: head = [0,0]
		Output: 0
 
	Constraints:
		•	The Linked List is not empty.
		•	Number of nodes will not exceed 30.
		•	Each node's value is either 0 or 1

"""

class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def helperFunction(head):
	if head == None:
		return 0, 0
	else:
		cur, sum = helperFunction(head.next)
		return cur+1, sum+(pow(2, cur)*head.val)

def convertToDecimal(head):
	return helperFunction(head)[1]

def createLL(arr):
	head = Node(arr[0])
	temp = head
	temp2 = None
	for i in range(1, len(arr)):
		temp2 = Node(arr[i])
		temp.next = temp2
		temp = temp.next
	return head


if __name__ == "__main__":
	arr1 = [1,0,1]
	print("INPUT:\t", arr1)
	print("OUTPUT:\t", convertToDecimal(createLL(arr1)))
	arr2 = [0]
	print("INPUT:\t", arr2)
	print("OUTPUT:\t", convertToDecimal(createLL(arr2)))
	arr3 = [1]
	print("INPUT:\t", arr3)
	print("OUTPUT:\t", convertToDecimal(createLL(arr3)))
	arr4 = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
	print("INPUT:\t", arr4)
	print("OUTPUT:\t", convertToDecimal(createLL(arr4)))
	arr5 = [0,0]
	print("INPUT:\t", arr5)
	print("OUTPUT:\t", convertToDecimal(createLL(arr5)))
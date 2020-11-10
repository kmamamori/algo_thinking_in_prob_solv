"""
	Problem 1: Middle of Linked List

	Given a non-empty, singly linked list with head node head, return a reference to the middle node of the linked list.
	If the list has an even number of nodes, return the node at index n/2, where n is the number of nodes. For example, if n =4, return a references to the node at position 4/2 = 2

	Write two solutions to this problem:
		First solution: No constrains, just solve the problem
		Second solution: Use one loop only

	Example 1:
		Input: 1 -> 2 -> 3 -> 4 -> 5
		Output: Node 3 from this list 
	Example 2:
		Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
		Output: Node 4 from this list 

"""


class Node:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = None


def getMiddle(head):
    temp = head
    len = 0
    while temp != None:
        len += 1
        temp = temp.next
    print(len)
    temp = head
    len = (len)//2
    while(len != 0):
        len -= 1
        temp = temp.next
    return temp


def oneloopGetMiddle(head):
    temp = head
    len = 0
    index_middle = 0
    n = n1
    while temp != None:
        len += 1
        if (len//2) > index_middle:
            index_middle = len//2
            n = n.next
        temp = temp.next
    return n


n1 = Node('n1')
n2 = Node('n2')
n3 = Node('n3')
n4 = Node('n4')
n5 = Node('n5')
n6 = Node('n6')

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

print("getMiddle", getMiddle(n1).val)
print("oneloopGetMiddle", oneloopGetMiddle(n1).val)

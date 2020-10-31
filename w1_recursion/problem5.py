"""
	Problem 5: Average of Levels in Binary Tree
	Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array. 
"""
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def averageOfLevels(root):
    q = Queue()
    q.put(root)
    while (not q.empty()):
        Sum = 0
        count = 0
        temp = Queue()
        while (not q.empty()):
            n = q.queue[0]
            q.get()
            Sum += n.val
            count += 1
            if (n.left != None):
                temp.put(n.left)
            if (n.right != None):
                temp.put(n.right)
        q = temp
        print((Sum * 1.0 / count), end=" ")


def Insert(T, newItem):
    if T == None:
        T = TreeNode(newItem)
    elif T.val > newItem:
        T.left = Insert(T.left, newItem)
    else:
        T.right = Insert(T.right, newItem)
    return T


def InOrder(T, space=' '):
    if T is not None:
        InOrder(T.left, space+'	')
        print(space, T.val)
        InOrder(T.right, space+'	')


T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100]
for a in A:
    T = Insert(T, a)
averageOfLevels(T)

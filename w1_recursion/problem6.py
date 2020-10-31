"""
	Problem 6: A full binary tree is a binary tree where each node has exactly 0 or 2 children.
	Write a function/method that, given the root of a binary tree, determines if it is full or not.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


def isFull(T):
    if T is None:
        return True
    if T.left is None and T.right is None:
        return True
    if T.left is not None and T.right is not None:
        return (isFull(T.left) and isFull(T.right))
    return False


T = None
A = [70, 50, 90, 130, 150, 40, 10, 45, 100, 80, 60]
for a in A:
    T = Insert(T, a)

InOrder(T)
print(isFull(T))

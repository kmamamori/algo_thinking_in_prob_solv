"""
	Problem 4: Same Tree: Given the roots of two binary trees, write a function to check if they are the same or not.
	Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
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

    # print a tree in inorder


def InOrder(T, space=' '):
    if T is not None:
        InOrder(T.left, space+'	')
        print(space, T.val)
        InOrder(T.right, space+'	')


def isIdentical(T1, T2):
    if T1 is None and T2 is None:
        return True
    if T1.val != T2.val:
        return False
    if T1.val == T2.val and isIdentical(T1.left, T2.left) and isIdentical(T1.right, T2.right):
        return True
    return False

T1 = None
T2 = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100]
for a in A:
    T1 = Insert(T1, a)
    T2 = Insert(T2, a)

# T2.right.val = 9
print(isIdentical(T1, T2))

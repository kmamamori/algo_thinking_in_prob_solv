"""
    Problem 2: Invert Binary Tree 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root):
    if root is None:
        return root
    elif root is not None:
        root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root


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


T = None
A = [4,7,2,9,6,3,1]
for a in A:
    T = Insert(T, a)

InOrder(T)
invertTree(T)
InOrder(T)

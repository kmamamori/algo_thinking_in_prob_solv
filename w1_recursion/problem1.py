"""
    Problem 1: Range Sum of BST 

    Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
    The binary search tree is guaranteed to have unique values.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

def Insert(T, newItem):
    if T == None:
        T = TreeNode(newItem)
    elif T.val > newItem:
        T.left = Insert(T.left, newItem)
    else:
        T.right = Insert(T.right, newItem)
    return T

        # print a tree in inorder


def InOrder(T, space):
    if T is not None:
        InOrder(T.left, space+'	')
        print(space, T.val)
        InOrder(T.right, space+'	')

def rangeSumBST(T, L, R):
    if T == None:
        return 0
    if T.val >= L and T.val <= R:
        return T.val + rangeSumBST(T.right, L, R) + rangeSumBST(T.left, L, R)
    else:
        return 0 + rangeSumBST(T.right, L, R) + rangeSumBST(T.left, L, R)

T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100]
for a in A:
    T = Insert(T, a)

InOrder(T, '  ')
print('newline\n')
print(rangeSumBST(T, 30, 130))


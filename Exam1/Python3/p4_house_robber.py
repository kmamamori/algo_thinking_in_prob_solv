from typing import ClassVar


def house_robber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    
    tree1 = TreeNode()
    for n in nums:
        tree1 = addval(tree1, n)
    # tree2 = createTree(nums[1:])
    # return result



class TreeNode:
    def __init__(self, x):
        # self.val = x
        self.val = x
        self.children = []


def addval(T, n):
    if T == None:
        T = TreeNode(n)
    if T.left == None:
      T.right = addval(T.right, n)
    else:
      T.left = addval(T.left, n)
    return T


def createTree(nums):
    t = Tree()

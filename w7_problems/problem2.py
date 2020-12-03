"""
    5.	Write a function that receives the root of a binary tree as input and inverts it. 
    Do not create a new tree, modify the one that was passed as input. 
    Feel free to write a helper (recursive) method.
"""



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invert(T):
    if T is None:
        return
    if T.left is None and T.right is not None:
        T.left, T.right = T.right, None
        return invert(T.right)
    T.right, T.left = T.left, T.right
    invert(T.left)
    invert(T.right)
    return

def addNode(i, T):
    if T == None:
        T = TreeNode(i)
    elif T.val > i:
        T.left = addNode(i, T.left)
    else:
        T.right = addNode(i, T.right)
    return T

def createTree(arr):
    T = None
    for i in arr:
        T = addNode(i, T)
    return T

def printTree(T, s):
    if T is not None:
        printTree(T.left, s+'	')
        print(s, T.val)
        printTree(T.right, s+'	')

if __name__ == "__main__":
    arr = [7,3,10,-1,5,9,12]
    T = createTree(arr)
    printTree(T, '	')
    invert(T)
    printTree(T, '	')
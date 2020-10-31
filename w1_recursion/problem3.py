"""
	Problem 3: A binary tree is univalued if every node in the tree has the same value.
	Return true if and only if the given tree is univalued.
"""
# Definition for a binary tree node.


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

	
#assume T is not Null
def isUnivalued(T):
	return isUnivaluedValue(T, T.val)

def isUnivaluedValue(T, val):
	return T == None or val == T.val and isUnivaluedValue(T.left, val) and isUnivaluedValue(T.right, val)
			


T = None
A = [4,7,2,9,6,3,1]
# A = [1, 1, 1, 1, 1, 1]
for a in A:
    T = Insert(T, a)

InOrder(T)
print(isUnivalued(T))
T.right.val = 1
T.right.right.val = 1
T.right.left.val = 1
T.left.val = 1
T.left.right.val = 1
T.left.left.val = 7
T.val=1
InOrder(T)
print(isUnivalued(T))

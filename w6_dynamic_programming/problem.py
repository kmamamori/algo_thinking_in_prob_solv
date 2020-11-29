class Node:
    def __init__(self, left=None, right=None, item=None):
        self.left = left
        self.right = right
        self.item = item


def max_sum(root):
    if root.left == None and root.right == None:
        return root.item
    elif root.left == None:
        sr, sl = max_sum(root.right), 0
    elif root.right == None:
        sl, sr = max_sum(root.left), 0
    else:
        sl, sr = max_sum(root.left), max_sum(root.right)
    root.item += sr if sl<sr else sl
    root.left, root.right = None, None
    return root.item
        
def printAll(t):
    print("t", t.item)
    print("t.left",t.left.item)
    print("t.right", t.right.item)
    
    print("t.left.left", t.left.left.item)
    print("t.left.right", t.left.right.item)
    print("t.right.left", t.right.left.item)
    print("t.right.right", t.right.right.item)
    
    print("t.left.left.left", t.left.left.left.item)
    print("t.left.left.right", t.left.left.right.item)
    print("t.left.right.left", t.left.right.left.item)
    print("t.left.right.right", t.left.right.right.item)
    print("t.right.right.left", t.right.right.left.item)
    print("t.right.left.right", t.right.left.right.item)
    print("t.right.right.right", t.right.right.right.item)
    
    
if __name__ == "__main__":
    t_arr = [3,10,6,-5,-70,-4,-1,2,50,-8]
    t = Node()
    t.item = t_arr[0]
    t.left = Node()
    t.right = Node()
    t.left.item = t_arr[1]
    t.right.item = t_arr[2]
    t.left.right = Node()
    t.left.left = Node()
    t.left.left.item = t_arr[3]
    t.left.right.item = t_arr[4]
    t.right.left = t.left.right
    t.right.right = Node(None,None,t_arr[5])
    t.left.left.left = Node(None,None,t_arr[6])
    t.left.left.right = Node(None,None,t_arr[7])
    t.left.right.left = t.left.left.right
    t.left.right.right = Node(None,None,t_arr[8])
    t.right.right.left = t.left.right.right
    t.right.right.right = Node(None,None,t_arr[9])
    
    print("OUTPUT:", max_sum(t))
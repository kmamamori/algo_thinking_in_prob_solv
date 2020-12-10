class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def union(S,i,j):
            ri = find(S,i)
            rj = find(S,j)
            if ri!=rj: # Do nothing if i and j belong to the same set
                S[rj] = ri  # Make j's root point to i's root
                return True #return true since i and j joined
            return False
        
        # Returns root of tree that i belongs to
        def find(S,i):
            if S[i]<0:
                return i
            return find(S,S[i])
        
        S = [-1 for i in range(2*len(edges))]
        for i in edges:
            if not union(S, i[0], i[1]):
                return i

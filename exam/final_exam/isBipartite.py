class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = [0]
        v = [-1 for i in range(len(graph))]
        v[0] = 1
        color = [-1 for i in range(len(graph))]
        color[0] = 0
        for c in range(len(graph)):
            while q != []:
                u = q.pop(0)
                for i in graph[u]:
                    if v[i] == -1:
                        q.append(i)
                        v[i] = 1
                        color[i] = 1-color[u]
                        if color[i] == color[u]:
                            return False
                    if color[i] == color[u]:
                        return False
            return True

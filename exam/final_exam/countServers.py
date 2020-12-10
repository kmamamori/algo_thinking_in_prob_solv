class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        server = 0
        s = set()
        for i in range(r):
            for  j in range(c):
                if i == r-1:
                    if j != c-1:
                        if grid[i][j]==1 and grid[i][j+1]:
                            s, server = checkSet(s, i, j, server, grid)
                            s, server = checkSet(s, i, j+1, server, grid)
                else:
                    if j == c-1:
                        if grid[i][j] == 1 == grid[i+1][j]:
                            s, server = checkSet(s, i, j, server, grid)
                            s, server = checkSet(s, i+1, j, server, grid)
                    else:
                        if grid[i][j] == 1 and grid[i][j+1]==1:
                            s, server = checkSet(s, i, j, server, grid)
                            s, server = checkSet(s, i, j+1, server, grid)
                        if grid[i+1][j]==1 and grid[i][j]==1:
                            s, server = checkSet(s, i+1, j, server, grid)
                            s, server = checkSet(s, i, j, server, grid)
               
        return server
    
    def checkSet(s, i, j, server, grid):
        if [[i][j]] not in s:
            server += 1
            s.add([[i][j]])
        return s, server

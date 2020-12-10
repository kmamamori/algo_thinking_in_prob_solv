class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, prev = [False for b in range(len(rooms))], [-1 for a in range(len(rooms))] #visited var and previous state
        s = []
        s.append(0) #stack
        visited[0] = True
        while s!=[]: #as long as stack has something
            u = s.pop() #pop the newest value
            for t in rooms[u]:
                if not visited[t]: #non checked
                    visited[t] = True
                    prev[t] = u
                    s.append(t) #push
        if False in visited:
            return False
        return True

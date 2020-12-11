class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 0:
            return True
        visited = [False for i in range(len(rooms))] #visited
        s = []
        s.append(0) #stack
        visited[0] = True
        while s!=[]: #as long as stack has something
            u = s.pop() #pop the newest value
            for room in rooms[u]:
                if room > len(rooms)-1:
                    return False
                if not visited[room]: #non checked
                    visited[room] = True
                    s.append(room) #push
        return not False in visited

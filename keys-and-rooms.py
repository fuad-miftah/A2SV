class Solution:
    def bfs(self,node,visited,rooms):
        visited.add(node)
        for neighbour in rooms[node]:
            if neighbour not in visited:
                self.bfs(neighbour,visited,rooms)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.bfs(0,visited,rooms)
        if len(visited) == len(rooms):
            return True
        return False
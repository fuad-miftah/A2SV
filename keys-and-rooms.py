class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])
        visited.add(0)
        while queue:
            node = queue.popleft()
            for neigbour in rooms[node]:
                if neigbour not in visited:
                    queue.append(neigbour)
                    visited.add(neigbour)

        if len(visited) == len(rooms):
            return True
        return False
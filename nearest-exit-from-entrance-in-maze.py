class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance[0],entrance[1])])
        visited = set([(entrance[0],entrance[1])])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        level = 0
        while queue:
            level += 1
            length = len(queue)
            for i in range(length):
                cp = queue.popleft()
                for r,c in directions:
                    nr = r + cp[0]
                    nc = c + cp[1]
                    if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and (nr,nc) not in visited and maze[nr][nc] == ".":
                        if nr == 0 or nr == len(maze)-1 or nc == 0 or nc == len(maze[0])-1:
                            return level
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                 
        return -1
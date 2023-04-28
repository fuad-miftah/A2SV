class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        queue = deque()
        res = [ [0 for _ in range(len(mat[0]))] for i in range((len(mat))) ]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        count = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while queue:
            count += 1
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                for r,c in directions:
                    newr = node[0] + r
                    newc = node[1] + c
                    if 0 <= newr < len(mat) and 0 <= newc < len(mat[0]) and (newr,newc) not in visited:
                        res[newr][newc] = count
                        mat[newr][newc] = 0
                        queue.append((newr,newc))
                        visited.add((newr,newc))
                    
        return res
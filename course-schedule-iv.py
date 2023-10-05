class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses

        dist = [[False for _ in range(n)] for _ in range(n) ]
        for r,t in prerequisites:
            dist[r][t] = True 
        
        for k in range(n):
            for j in range(n):
                for i in range(n):
                    dist[i][j] |= (dist[i][k] and  dist[k][j])
        res = []
        for x,y in queries:
            res.append(dist[x][y])
        
        return res
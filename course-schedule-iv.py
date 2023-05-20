class Solution:
    def bfs(self,i,dic,v):
        queue = deque()
        queue.append(i)
        visited = set()
        visited.add(i)
        while queue:
            node = queue.popleft()
            for child in dic[node]:
                if child == v:
                    return True
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        return False
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        dic = defaultdict(list)
        for c,p in prerequisites:
            dic[c].append(p)

        res = []

        for u,v in queries:
            p = self.bfs(u,dic,v)
            if p:
                res.append(True)
            else:
                res.append(False)
                
        return res
class Solution:
    def bfs(self,i,dic):
        path = []
        queue = deque()
        queue.append(i)
        visited = set()
        visited.add(i)
        while queue:
            node = queue.popleft()
            for child in dic[node]:
                if child not in visited:
                    path.append(child)
                    queue.append(child)
                    visited.add(child)
        return path
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for a,b in edges:
            dic[b].append(a)
        res = []
        for i in range(n):
            ancestor = self.bfs(i,dic)
            ancestor.sort()
            res.append(ancestor)
        return res
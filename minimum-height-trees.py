class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        dic = defaultdict(list)
        incoming = defaultdict(int)
        for u, v in edges:
            dic[u].append(v)
            dic[v].append(u)
            incoming[u] += 1
            incoming[v] += 1
        res = []
        queue = deque()
        visited = set()
        for key in dic.keys():
            if len(dic[key]) == 1:
                queue.append(key)
                res.append(key)
                visited.add(key)

        while queue:
            temp = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                for child in dic[node]:
                    if child not in visited:
                        if incoming[child] == 2:
                            temp.append(child)
                            visited.add(child)
                            queue.append(child)
                            incoming[child] -= 1
                        else:
                            incoming[child] -= 1
            if temp != []:
                res = temp

        return res
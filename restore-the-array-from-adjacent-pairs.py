class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)

        for u, v in adjacentPairs:
            dic[u].append(v)
            dic[v].append(u)
        
        queue = deque()
        for key in dic:
            if len(dic[key]) == 1:
                queue.append(key)
                break

        nums = []
        visited = set()

        while queue:
            curr = queue.popleft()
            nums.append(curr)
            for adj in dic[curr]:
                dic[curr].remove(adj)
                dic[adj].remove(curr)
                queue.append(adj)
        
        return nums
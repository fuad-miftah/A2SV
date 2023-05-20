class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        dic = defaultdict(list)
        incoming = defaultdict(int)
        for u,v in edges:
            dic[u].append(v)
            incoming[v] += 1
            
        queue = deque() 
        visited = set()
        for key in dic:
            if incoming[key] == 0:
                queue.append(key)
                visited.add(key)
        

        path = [str(1)] * n
        
        level = 1
        while queue:
            level += 1
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                for child in dic[node]:
                    if child not in visited:
                        if incoming[child] == 1:
                            path[child-1] = str(level)
                            queue.append(child)
                            visited.add(child)
                        else:
                            incoming[child] -= 1
            
        return " ".join(path)
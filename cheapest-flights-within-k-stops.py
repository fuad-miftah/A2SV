class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        graph = defaultdict(list)
        
        for f,t,p in flights:
            graph[f].append((t,p))

        que = deque()
        que.append((src,0,0)) 
        result = float("inf")
        dist = [float("inf")] * n
        while que:
            node,stopes,pr = que.popleft()
            if node == dst:
                result = min(result,pr)
                continue

            if stopes > k:
                continue
            for child,p in graph[node]:
                if pr + p < dist[child]:
                    dist[child] = pr + p
                    data = (child,stopes + 1,pr + p)
                    que.append(data)
        
        
        return result if result != float("inf") else -1
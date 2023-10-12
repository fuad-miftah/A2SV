class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        dist = [float("inf") for _ in range(n+1)]
        dist[k] = 0
        dist[0] = 0
        pqueue = []
        pqueue.append((0,k))
        visited = set()
        while pqueue:

            d , node = heappop(pqueue)
            if node in visited:
                continue 
            visited.add(node)
            
            for ch, wg in graph[node]:
                val = d + wg 
                if dist[ch] > val:
                    dist[ch] = val 
                    heappush(pqueue,(val,ch))
        
        return max(dist) if max(dist) != float("inf") else -1
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dic = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            dic[u].append([v, succProb[i]])
            dic[v].append([u, succProb[i]])
            
        max_prob = [0.0] * n    
        max_prob[start] = 1.0
        
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbour, weight in dic[node]:

                if max_prob[node] * weight > max_prob[neighbour]:
                    max_prob[neighbour] = max_prob[node] * weight
                    queue.append(neighbour)
                    
        return max_prob[end]
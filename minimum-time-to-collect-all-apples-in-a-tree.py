class Solution:
    def dfs(self,node,dic,hasApple,visited):
            visited.add(node)    
            ans = 0
            for child in dic[node]:
                if child not in visited:
                    ans += self.dfs(child,dic,hasApple,visited)
 
            if not ans and not hasApple[node]: 
                return 0

            return ans + 1   
            
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        dic = defaultdict(list)
        for u,v in edges:
            dic[u].append(v)
            dic[v].append(u)
        res = self.dfs(0,dic,hasApple,set())
        
        return (res - 1) * 2 if res > 0 else 0
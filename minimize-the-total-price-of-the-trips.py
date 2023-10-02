class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        freq = [0]*n 
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(a,par,b):
            if a == b:
                freq[b] += 1 
                return True 
            for nb in graph[a]:
                if nb != par:
                    if dfs(nb,a,b):
                        freq[a] += 1
                        return True
        for x,y in trips:
            dfs(x,-1,y)
        tot = 0
        for i in range(n):
           tot += freq[i] * price[i]

        lookup = {}
        def dp(a,par,used):
            
            res = price[a]//2 * freq[a] if used else 0 
            if (a,used) in lookup:
                return lookup[(a,used)]

            for nb in graph[a]:

                if nb != par:
                        if used:
                            res += dp(nb,a,not used)
                        else:
                            ifused = dp(nb,a,not used)
                            ifnotused = dp(nb,a,used)
                            res += max(ifused , ifnotused)
            lookup[(a,used)] = res
            return res

        return tot - max(dp(0,-1,False),dp(0,-1,True))
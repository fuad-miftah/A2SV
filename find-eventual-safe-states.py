class Solution:
    def dfs(self,node,res,color,graph):
        if color[node] == 1:
            return False
        if color[node] == 2:
            return True

        color[node] = 1
        for child in graph[node]:
            
            if not self.dfs(child,res,color,graph):
                return False
        
        color[node] = 2
        return True
        

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        res = []
        for i in range(len(graph)):
            if self.dfs(i,res,color,graph):
                res.append(i)

        return res
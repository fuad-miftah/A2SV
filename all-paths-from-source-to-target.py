class Solution:
    def dfs(self,node,target,graph,path,res):

        if node == target:
            res.append(path[:])
            return res

        for i in graph[node]:
            path.append(i)
            self.dfs(i,target,graph,path[:],res)
            path.remove(i)
        return res
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.dfs(0,len(graph)-1,graph,[0],[])
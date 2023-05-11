from typing import List

class Solution:
    #Function to detect cycle in an undirected graph.
    def dfs(self,i,adj,parent,visited):

        visited.add(i)
        
        for child in adj[i]:
            if child not in visited:
                if not self.dfs(child,adj,i,visited):
                    return False
            elif parent != child:
                return False
        return True
        
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = set()
        
		for i in range(V):
		    if i not in visited and not self.dfs(i,adj,-1,visited):
		        return 1
		return 0
		
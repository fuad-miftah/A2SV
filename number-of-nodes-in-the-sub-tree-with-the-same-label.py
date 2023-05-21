class Solution:
    def dfs(self,node,dic,visited,labels,res,alphabet):
        whenEnter = alphabet[labels[node]]
        visited.add(node)
        
        for child in dic[node]:
            if child not in visited:
                self.dfs(child,dic,visited,labels,res,alphabet)
                
        alphabet[labels[node]] += 1
        res[node] = alphabet[labels[node]] - whenEnter
        

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        dic = defaultdict(list)
        for u,v in edges:
            dic[u].append(v)
            dic[v].append(u)
        res = [0] * n
        self.dfs(0,dic,set(),labels,res,Counter())
        return res
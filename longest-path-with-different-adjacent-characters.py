class Solution:
    def dfs(self,node,dic,visited,s):
        if node not in dic:
            return 1

        count = 1
        for child in dic[node]:
            coun = self.dfs(child,dic,visited,s)
            if s[child] != s[node]:
                self.res = max(self.res, count+coun)
                count = max(count,coun + 1)
        
        return count

    def longestPath(self, parent: List[int], s: str) -> int:

        dic = defaultdict(list)
        for i in range(1, len(parent)):
            dic[parent[i]].append(i)
            
        self.res = 1
        count = self.dfs(0,dic,set(),s)
        return self.res
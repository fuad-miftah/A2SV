class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dic = defaultdict(list)
        for u,v in richer:
            dic[v].append(u)
        res = [-1] * len(quiet)
        visited = set()
        for i in range(len(quiet)):
            if i not in visited:
                self.dfs(i,visited,dic,res,quiet)
        
        return res
    def dfs(self,i,visited,dic,res,quite):
        visited.add(i)
        if dic[i] == []:
            res[i] = i
            return i
        ans = i
        for child in dic[i]:
            if child not in visited:
                cur = self.dfs(child,visited,dic,res,quite)
                if quite[cur] < quite[ans]:
                    ans = cur
            else:
                if quite[res[child]] < quite[ans]:
                    ans = res[child]
        res[i] = ans
        return ans
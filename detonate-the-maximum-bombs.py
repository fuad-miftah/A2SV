class Solution:
    def dfs(self,node,visited,adl):
        visited.add(node)
        for neighbour in adl[node]:
            if neighbour not in visited:
                self.count += 1
                self.dfs(neighbour,visited,adl)
        return
    def canReach(self,bomb,tobereached):

        hypotnes = sqrt((tobereached[0]-bomb[0]) ** 2 + (tobereached[1] - bomb[1]) ** 2)
        if hypotnes <= bomb[2]:
            return True
        else:
            return False 

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adl = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and self.canReach(bombs[i],bombs[j]):
                    adl[i].append(j)
        res = 1
        for bomb in range(len(bombs)):
            self.count = 1
            self.dfs(bomb,set(),adl)
            res = max(res, self.count)

        return res
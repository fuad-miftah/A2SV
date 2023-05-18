class Solution:
    def init(self, n):
        self.size = defaultdict(lambda: 1)
        self.rep = {i : i for i in range(1, n + 1)}

    def find(self,x):
        if self.rep[x] == x:
            return self.rep[x]

        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self,x,y):
            
        repx = self.find(x)
        repy = self.find(y)

        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.size[repx] += self.size[repy]
                self.rep[repy] = self.rep[repx]
            else:
                self.size[repy] += self.size[repx]
                self.rep[repy] = self.rep[repx]
        

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.init(n)
        res = float("inf")
        for u,v,d in roads:
            self.union(u,v)

        for u,v,d in roads:
            if self.find(1) == self.find(u):
                res = min(res, d)
            
        return res
class Solution:
    def init(self, stones):
        self.size = defaultdict()
        self.rep = {}
        for i,j in stones:
            self.rep[(i,j)] = (i,j)
            self.size[(i,j)] = 1

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

    def removeStones(self, stones: List[List[int]]) -> int:
        self.init(stones)
        
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union((stones[i][0], stones[i][1]), (stones[j][0], stones[j][1]))

        
        parents = set()
        for u,v in stones:
            par = self.find((u,v))
            parents.add(par)

        return len(stones) - len(parents)
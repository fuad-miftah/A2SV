class Solution:
    def init(self,s):
        self.size = [1] * len(s)
        self.rep = [ i for i in range(len(s))]

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

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.init(s)
        for u ,v in pairs:
            self.union(u,v)

        res = list(s)
        dic = defaultdict(list)
        for i,par in enumerate(self.rep):
            grandPar = self.find(par)
            dic[grandPar].append(i)

        for key in dic:
            indxs = dic[key]
            chars = []
            for i in range(len(indxs)):
                chars.append(s[indxs[i]])
            chars.sort()
            indxs.sort()
            j = 0
            for indx in indxs:
                res[indx] = chars[j]
                j += 1
        
        return "".join(res)
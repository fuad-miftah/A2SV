class Solution:
    def init(self, grid):
        self.size = defaultdict(lambda : 1)
        self.rep = {}
        for i in range(97,123):
            self.rep[chr(i)] = chr(i)
        

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

    def equationsPossible(self, equations: List[str]) -> bool:
        self.init(equations)
        notEqual = set()
        for s in equations:
            s1 = s[0]
            s2 = s[3]
            eq = s[1] + s[2]
            if eq == "==":
                if (s1,s2) not in notEqual and (s2,s1) not in notEqual:
                    self.union(s1,s2)
                else:
                    return False
            else:
                notEqual.add((s1,s2))
                if self.find(s1) == self.find(s2):
                    return False

        for u,v in notEqual:
            if self.find(u) == self.find(v):
                return False
        return True
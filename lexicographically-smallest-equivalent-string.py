class Solution:
    def find(self,x):
        if self.rep[ord(x)-97] == x:
            return self.rep[ord(x)-97]

        self.rep[ord(x) - 97] = self.find(self.rep[ord(x)-97])
        return self.rep[ord(x)-97]

    def union(self,x,y):
            
        repx = self.find(x)
        repy = self.find(y)

        if repx != repy:
            if repx < repy:
                self.rep[ord(repy) - 97] = self.rep[ord(repx) - 97]
            else:
                self.rep[ord(repx) -97] = self.rep[ord(repy) -97]

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.rep = list(ascii_lowercase)
        for i in range(len(s1)):
            self.union(s1[i], s2[i])
        res = ""
        for i in range(len(baseStr)):
            res += self.find(baseStr[i])
        
        return res
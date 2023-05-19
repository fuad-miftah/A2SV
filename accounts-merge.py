class Solution:
    def init(self, accounts):
        self.size = [1 for i in range(len(accounts))]
        self.rep = [i for i in range(len(accounts))]
 
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

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.init(accounts)
        emailsFound = {}
        for i in range(len(accounts)):
            for k in range(1,len(accounts[i])):
                if accounts[i][k] in emailsFound:
                    self.union(i,emailsFound[accounts[i][k]])
                emailsFound[accounts[i][k]] = i

        keys = defaultdict(list)
        for i in range(len(self.rep)):
            keys[self.find(self.rep[i])].append(i)

        res = []
        for key in keys:
            temp = set()
            for indx in keys[key]:
                for k in range(1,len(accounts[indx])):
                    temp.add(accounts[indx][k])
            l = list(temp)
            l.sort()
            l.insert(0, accounts[key][0])
            res.append(l)
        return res
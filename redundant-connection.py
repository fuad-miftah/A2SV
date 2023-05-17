class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = [1] * len(edges)
        rep = [ i for i in range(len(edges))]
        res = []
        def find(x):
            if rep[x] == x:
                return rep[x]

            rep[x] = find(rep[x])
            return rep[x]
        def union(x,y):
            
            repx = find(x)
            repy = find(y)

            if repx != repy:
                if size[repx] > size[repy]:
                    size[repx] += size[repy]
                    rep[repy] = rep[repx]
                else:
                    size[repy] += size[repx]
                    rep[repy] = rep[repx]
            else:
                res.append([x+1,y+1])

        for u,v in edges:
            union(u-1,v-1)
        
        return res[-1]
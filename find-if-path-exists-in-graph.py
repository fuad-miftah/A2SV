class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        size = [1] * n
        rep = [ i for i in range(n)]

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

        for u,v in edges:
            union(u,v)
        
        return find(source) == find(destination)
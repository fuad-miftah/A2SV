class Solution:
    def init(self, grid):
        self.size = defaultdict()
        self.rep = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
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

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.init(grid)
        dic = {1:[(0,-1),(0,1)] , 2:[(-1,0),(1,0)], 3:[(0,-1),(1,0)], 4:[(0,1),(1,0)],5:[(-1,0),(0,-1)], 6:[(-1,0),(0,1)]}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for r,c in dic[grid[i][j]]:
                    nr = r + i
                    nc = c + j
                    inbound = 0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                    if inbound and (-r,-c) in dic[grid[nr][nc]]:
                        self.union((i,j),(nr,nc))
        
        return self.find((0,0)) == self.find( (len(grid)-1,len(grid[0])-1) )
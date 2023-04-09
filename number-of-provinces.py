class Solution:
    def mark(self,i,visited,isConnected):
        if i < 0 or i > len(isConnected) or i in visited:
            return
        visited.add(i)

        for j in range(len(isConnected[0])):
            if j != i and isConnected[i][j] != 0:
                self.mark(j,visited,isConnected)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                self.mark(i,visited,isConnected)
        return provinces
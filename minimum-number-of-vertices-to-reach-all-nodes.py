class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        indeg = [True] * n
        for i in range(len(edges)):
            indeg[edges[i][1]] = False

        res = []
        for i in range(n):
            if indeg[i] == True:
                res.append(i)
            

        return res
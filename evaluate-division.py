class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        index = defaultdict(int)

        x = 0
        for a,b in equations:
            if a not in index:
                index[a] = x
                x += 1 
            if b not in index:
                index[b] = x
                x += 1
        
        n = len(index)

        mat = [[-1]*n for _ in range(n)]

        for i in range(n):
            mat[i][i] = 1

        for i , (a ,b) in enumerate(equations):
            mat[index[a]][index[b]] = values[i]
            mat[index[b]][index[a]] = 1/values[i]
        
        
        for k in range(n):
            for j in range(n):
                for i in range(n):
                    if mat[i][k] != -1 and  mat[j][k] != -1:
                        mat[i][j] = mat[i][k] / mat[j][k]
                        mat[j][i] = mat[j][k] / mat[i][k]
        
        ans = []
        for a,b in queries:
            if a not in index or b not in index:
                ans.append(-1)
            else:
                ans.append(mat[index[a]][index[b]])
        
        return ans
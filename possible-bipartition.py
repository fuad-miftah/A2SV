class Solution:
    def dfs(self,node,adl,color):
        if color[node] == -1:
            color[node] = 1
        for neighbour in adl[node]:
            if color[neighbour] == -1:
                color[neighbour] = 1 - color[node]
                if not self.dfs(neighbour,adl,color):
                    return False
            else:
                if color[neighbour] == color[node]:
                    return False
        return True
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n + 1)
        adl = defaultdict(list)
        for i in range(len(dislikes)):
            adl[dislikes[i][0]].append(dislikes[i][1])
            adl[dislikes[i][1]].append(dislikes[i][0])

        for i in range(n):
            if color[i] == -1:
                if not self.dfs(i,adl,color):
                    return False
        return True
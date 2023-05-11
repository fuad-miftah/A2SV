class Solution:
    def dfs(self,i,dic,color):
        if color[i] == 1:
            return False
        if color[i] == 2:
            return True
        color[i] = 1
        for child in dic[i]:
            if not self.dfs(child,dic,color):
                return False
        color[i] = 2
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0] * numCourses
        dic = defaultdict(list)
        for c,p in prerequisites:
            dic[c].append(p)

        res = []

        for i in range(numCourses):
            if self.dfs(i,dic,color):
                res.append(i)
                
        if len(res) == numCourses:
            return True
        else:
            return False
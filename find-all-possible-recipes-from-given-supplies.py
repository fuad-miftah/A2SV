class Solution:
    def dfs(self,i,rec,ing,sup,color):
        if color[i] == 1:
            return False
        if color[i] == 2:
            return True
        color[i] = 1
        for needed in ing[i]:
            if needed not in sup:
                if needed in rec:
                    indx = rec.index(needed)
                    if not self.dfs(indx,rec,ing,sup,color):
                        return False
                else:
                    return False

        color[i] = 2
        return True
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        color = [0] * len(recipes)
        res = []
        for i in range(len(recipes)):
            if self.dfs(i,recipes,ingredients,supplies,color):
                res.append(recipes[i])
        return res
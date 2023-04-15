class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = []
        l = 0
        r = len(skill) - 1
        skill.sort()
        skills = skill[l] + skill[r]
        res.append( [skill[l] , skill[r]] )
        l += 1
        r -= 1
        while l <= r:
            if skill[l] + skill[r] != skills:
                return -1
            else:
                res.append( [skill[l], skill[r]] )
                l += 1
                r -= 1
        output = 0
        for i in range(len(res)):
            output += res[i][0] * res[i][1]
        return output
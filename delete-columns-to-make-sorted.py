class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            maxx = strs[0][i]
            for j in range(1,len(strs)):
                if maxx > strs[j][i]:
                    res+=1
                    break
                maxx = max(maxx,strs[j][i]) 
        return res
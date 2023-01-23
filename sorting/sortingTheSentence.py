class Solution(object):
    def sortSentence(self, s):
        res = ""
        splitedArr = s.split()
        dic = {}
        for i in splitedArr:
            dic[i[-1]] = i[:-1]
        
        for i in sorted(dic):
            res = res + dic[i] + " "

        return res.rstrip(" ")    
            

sol = Solution()
sol.sortSentence("Myself2 Me1 I4 and3")


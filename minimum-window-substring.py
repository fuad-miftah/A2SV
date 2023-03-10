class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        count1 = Counter(t) 
        count2 = {}
        l = 0
        r = 0
        def isValid(c1,c2):
            if len(c1) != len(c2):
                return False
            for i in c2:
                if c1[i] > c2[i]:
                    return False
            return True
        while r < len(s):
            if s[r] in count1:
                if s[r] in count2:
                    count2[s[r]]+=1
                else:
                    count2[s[r]] = 1

            while isValid(count1,count2):
                if r-l+1 < len(res) or res == "":
                    res = s[l:r+1]

                if s[l] in count2:
                    count2[s[l]]-=1
                l+=1            
            r+=1
        return res
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) < k : return 0
        left = 0
        curVow = 0
        res = 0
        for i in range(k):
            if s[i] in "aeiou":
                curVow+=1
        res = max(res, curVow)
        right = k-1
        while right < len(s)-1:
            right+=1
            if s[right] in "aeiou":
                curVow+=1
            if s[left] in "aeiou":
                curVow-=1
            left+=1
            res = max(res, curVow)
        return res

        

        


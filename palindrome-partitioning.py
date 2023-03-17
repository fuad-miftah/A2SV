class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPalindrome(s):
            l = 0
            r = len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtrack(indx,curr):
            if indx >= len(s):
                ans.append(curr.copy())
                return
            for i in range(indx,len(s)):
                val = s[indx:i+1]
                if isPalindrome(val):
                    curr.append(val)
                    backtrack(i+1,curr)
                    curr.pop()
            return
        backtrack(0,[])
        return ans
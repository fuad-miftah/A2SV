class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        def backtrack(indx):
            if indx >= len(s):
                return len(ans) >= 2
            for i in range(indx,len(s)):
                val = int(s[indx:i+1])
                if ans == [] or ans[-1] - 1 == val:
                    ans.append(val)
                    if backtrack(i+1):
                        return True
                    ans.pop()
            return False
        return backtrack(0)
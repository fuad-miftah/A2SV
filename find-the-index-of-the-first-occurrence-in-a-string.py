class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        
        for r in range(len(haystack)):
            if haystack[r] == needle[0]:
                l = 0
                while l < len(needle) and r < len(haystack) and haystack[r] == needle[l]:
                    r+=1
                    l+=1
                if l == len(needle):
                    res = r - l
                    return res

        return res
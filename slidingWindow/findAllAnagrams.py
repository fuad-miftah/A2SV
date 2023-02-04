class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = Counter(p)
        countS = Counter(s[:len(p)])
        res = []
        if countP == countS: res.append(0)
        left = 0
        for right in range(len(p),len(s)):
            countS[s[right]]+=1
            countS[s[left]]-=1
            
            if countS[s[left]] == 0:
                del countS[s[left]]
            left+=1
            if countP == countS: res.append(left)
            
        return res
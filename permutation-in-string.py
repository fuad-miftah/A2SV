class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = Counter(s2[:len(s1)])
        
        if count1 == count2:
            return True
        l = 0
        
        for r in range(len(s1), len(s2)):
            
            if s2[r] in count2:
                count2[s2[r]]+=1
            else:
                count2[s2[r]] = 1
            count2[s2[l]] -= 1
            l+=1
            #count2 = Counter(s2[l:r+1])
            if count1 == count2:
                return True
        return False
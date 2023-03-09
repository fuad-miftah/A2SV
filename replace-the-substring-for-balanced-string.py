class Solution:
    def balancedString(self, s: str) -> int:
        res = sys.maxsize
        cont = Counter(s)
        av = int(sum(cont.values()) / 4)
        maxx = {}

        if cont["Q"] > av:
            maxx["Q"] = cont["Q"] - av
        if cont["R"] > av:
            maxx["R"] = cont["R"] - av
        if cont["W"] > av:
            maxx["W"] = cont["W"] - av
        if cont["E"] > av:
            maxx["E"] = cont["E"] - av
        # print(cont)
        # print(maxx)
        l = 0
        maxx2 = maxx
        if maxx:
            for r in range(len(s)):
                if s[r] in maxx2:
                    maxx2[s[r]] -= 1
                
                allz = True
                for d in maxx2:
                    if maxx2[d] > 0:
                        allz = False
                        break
                if allz == True:
                    res = min(res, r-l+1)
                    while l < r and allz == True:
                        if s[l] in maxx2:
                            maxx2[s[l]]+=1
                        res = min(res, r-l+1)
                        l+=1
                        for e in maxx2:
                            if maxx2[e] > 0:
                                allz = False
                                break
                        
                                     
        else:
            res = 0

        return res
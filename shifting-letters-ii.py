class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        prefix = [0]*len(s)
        for i in range(len(shifts)):
            start,end,drxn = shifts[i]
            if drxn == 0:
                prefix[start]-=1
                if end+1 < len(prefix):
                    prefix[end+1]+=1
            else:
                prefix[start]+=1
                if end+1 < len(prefix):
                    prefix[end+1]-=1
        if prefix:
            for i in range(1,len(prefix)):
                prefix[i] = prefix[i-1]+prefix[i]

        #print(ord("a"))
        res = ""
        for i in range(len(s)):
            cha = (ord(s[i]) + prefix[i] - 97)%26 + 97
            res+=chr(cha)
        return res
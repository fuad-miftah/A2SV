class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        j = 0
        while num != 0:
            if num & 1 == 0:
                res += (2**j)
            num >>= 1
            j += 1
        
        return res
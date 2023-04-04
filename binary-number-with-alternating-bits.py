class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = 0
        if n % 2 == 0:
            temp = 0
        else:
            temp = 1
        n >>= 1
        while n > 0:
            if n & 1:
                if temp == 1:
                    return False
                temp = 1
            else:
                if temp == 0:
                    return False
                temp = 0
            n >>= 1
        return True
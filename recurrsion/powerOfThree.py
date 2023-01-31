class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: 
            return True
        if n <= 0 : 
            return False
        if n % 3 == 0:
            n = int(n/3)
            return self.isPowerOfThree(n)
        else:
            return False
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 1: 
            return True
        if n <= 0 : 
            return False
        if n % 4 == 0:
            n = int(n/4)
            return self.isPowerOfFour(n)
        else:
            return False
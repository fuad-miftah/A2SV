class Solution:
    def findPrimes(self,n):
        res = set()      
        i = 2
        while i * i <= n:
            while n % i == 0:
                res.add(i)
                n //= i
            i += 1
        
        if n > 1:
            res.add(n)
        return res

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        for num in nums:
            res.update(self.findPrimes(num))
    
        return len(res)
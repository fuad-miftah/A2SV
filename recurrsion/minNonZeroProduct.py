class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        def power(a,b):
    
            if b==0:
                return 1
            
            out_ = power(a,b//2)
            out_ = out_ * out_
            
            if b%2 !=0 :
                out_ = out_ * a
            
            return out_%(1000000007)
        
        return (power(2**p -2, 2**(p-1) - 1) * (2**p - 1)) % (10**9 + 7)
        
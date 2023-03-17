class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        return self.helper(n,k)
        
    def helper(self,n,k):
        if n == 2:
            if k == 1:
                return 0
            else:
                return 1
        mid = (2**(n-1)) / 2
        if k > mid:
            ans = self.helper(n-1,k-mid)
            if ans == 0:
                return 1
            else:
                return 0
        else:
            return self.helper(n-1,k)
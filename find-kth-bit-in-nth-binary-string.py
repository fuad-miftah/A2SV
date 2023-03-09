class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1: return "0"
        def find(n,k):
            if n == 1: return "0"
            count = (1 << n) - 1
            if k == (count//2): return "1"
            if k > (count//2):
                s = find(n-1,count-k-1)
                if s == "0":
                    return "1"
                else:
                    return "0"
            return find(n-1,k)
        return find(n, k-1)
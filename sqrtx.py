class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        l = 0
        r = x

        while l <= r:
            mid  = (r + l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
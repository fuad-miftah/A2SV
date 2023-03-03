# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            mid = (r+l) // 2
            res = isBadVersion(mid)
            if res == True:
                if mid == 1: return 1
                if not isBadVersion(mid-1):
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1
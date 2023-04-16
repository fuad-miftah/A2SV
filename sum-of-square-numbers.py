class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        while l <= r:
            if (l * l) + (r * r) == c:
                return True
            elif (l * l) + (r * r) > c:
                r -= 1
            else:
                l += 1
        return False
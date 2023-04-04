class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        res = 0
        for i in range(1,smallest+1):
            if smallest % i == 0 and largest % i == 0:
                res = i
        return res
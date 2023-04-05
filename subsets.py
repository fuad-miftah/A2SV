class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = 2 ** len(nums)
        for i in range(n):
            temp = []
            j = i
            indx = 0
            while j > 0:
                if j & 1:
                    temp.append(nums[indx])
                j >>= 1
                indx += 1
            res.append(temp)
        return res
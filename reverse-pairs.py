class Solution:
    def __init__(self):
        self.res = 0
    def reversePairs(self, nums: List[int]) -> int:
        self.divide(nums)
        return self.res

    def divide(self,nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2

        l = self.divide(nums[ : mid])
        r = self.divide(nums[mid : ])

        return self.merge(l,r)

    def merge(self,l,r):
            j = 0
            for i in range(len(l)):
                while j < len(r) and l[i] > 2 * r[j]:
                    j+=1
                if j != 0 and l[i]  > 2 * r[j-1]:
                    self.res += j
            mergedArr = []
            p1 = 0
            p2 = 0
            while p1 < len(l) and p2 < len(r):
                if l[p1] < r[p2]:
                    mergedArr.append(l[p1])
                    p1+=1
                else:
                    mergedArr.append(r[p2])
                    p2+=1

            while p1 < len(l):
                mergedArr.append(l[p1])
                p1+=1
            while p2 < len(r):
                mergedArr.append(r[p2])
                p2+=1

            return mergedArr
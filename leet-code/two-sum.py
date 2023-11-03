class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newArr = []
        for i,num in enumerate(nums):
            newArr.append((num,i))
        newArr.sort()
        res = []
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            s = newArr[p1][0] + newArr[p2][0]
            if s == target:
                res.append(newArr[p1][1])
                res.append(newArr[p2][1])
                break
            elif s > target:
                p2 -= 1
            else:
                p1 += 1
        return res
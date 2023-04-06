class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
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
        ors = []
        for i in range(len(res)):
            if res[i] != []:
                cur_or = 0
                for j in range(len(res[i])):
                    cur_or |= res[i][j]
                ors.append(cur_or)
        count = Counter(ors)
        return count[max(ors)]
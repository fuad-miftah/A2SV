class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int,{0:1})
        prefix = 0
        res = 0
        for i in range(len(nums)):
            prefix += nums[i]
            #print(dic)
            if prefix%k in dic:
                res+=dic[prefix%k]
            dic[prefix%k]+=1
        return res
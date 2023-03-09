class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixsum = [0]
        ans = 0
        for i,num in enumerate(nums):
            prefixsum.append(prefixsum[i]+num)
        print(prefixsum)
        hashmap = {0:1}
        for i in range(1,len(prefixsum)):
            if prefixsum[i] >= goal:
                if prefixsum[i]-goal in hashmap:
                    ans+=hashmap[prefixsum[i]-goal]
            
            hashmap[prefixsum[i]] = 1 + hashmap.get(prefixsum[i],0)
        return ans
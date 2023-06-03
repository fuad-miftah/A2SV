class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = defaultdict(int)
        
        def dfs(index, total):          
            key = (index, total)
            
            if (index, total) not in dic:
                if index == len(nums):                    
                    return 1 if total == target else 0
                else:
                    dic[(index, total)] = dfs(index+1, total + nums[index]) + dfs(index+1, total - nums[index])                    
                        
            return dic[(index, total)]                                                             
                
        return dfs(0,0)
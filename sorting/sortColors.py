class Solution(object):
    def sortColors(self,nums):
        # for i in range(1,len(nums)):
        #     j = i
        #     while j > 0 and nums[j-1] > nums[j]:
        #         nums[j-1],nums[j] = nums[j],nums[j-1]
        #         j-=1
        # print(nums)

        arr = [0]*3
        for i in nums:
            arr[i]+=1
        for i in range(len(nums)-1,-1,-1):
            nums[i] = len(arr)-1
            arr[-1]-=1
            if arr[-1] == 0:
                arr.pop()
        print(nums)

nums = [2,0,2,1,1,0]
sol = Solution()
sol.sortColors(nums)
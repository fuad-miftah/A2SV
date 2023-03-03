class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        def findLeft(m):
            l = 0
            r = m
            while l <= r:
                mid = (r+l) // 2
                if nums[mid] == target:
                    if mid == 0: return 0
                    if nums[mid-1] != target:
                        return mid
                    else:
                        r = mid - 1
                else: 
                    l = mid + 1
                    
        def findRight(m):
            l = m
            r = len(nums)-1
            while l <= r:
                mid = (r+l) // 2
                if nums[mid] == target:
                    if mid == len(nums)-1: return len(nums)-1
                    if nums[mid+1] != target:
                        return mid
                    else:
                        l = mid + 1
                else: 
                    r = mid - 1
        while l<=r:
            mid = (r + l) // 2
            if nums[mid] == target:
                left = findLeft(mid)
                right = findRight(mid)
                return [left,right]
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1,-1]
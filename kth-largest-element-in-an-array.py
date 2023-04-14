class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       
        target = len(nums) - k

        def partition(nums,low,high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
        
                    i = i + 1
        
                    (nums[i], nums[j]) = (nums[j], nums[i])
        
            (nums[i + 1], nums[high]) = (nums[high], nums[i + 1])
        
            return i + 1

        def quickSort(nums,low,high):
            if low < high:
                pivot = partition(nums,low,high)

                if pivot == target:
                    return nums[pivot]
                elif pivot > target:
                    return quickSort(nums,low,pivot-1)
                else:
                    return quickSort(nums,pivot+1,high)
            else:
                return nums[low]

        return quickSort(nums,0,len(nums)-1)
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left = 0
        res = 0
        while left < len(arr):
            while left < len(arr) - 1 and arr[left] >= arr[left+1]:
                left+=1
            right = left+1
            while right < len(arr) - 1 and arr[right] < arr[right+1]:
                right+=1
            while right < len(arr)- 1 and arr[right] > arr[right+1]:
                right+=1
                res = max(res, right-left+1)
            
            left = right
        return res
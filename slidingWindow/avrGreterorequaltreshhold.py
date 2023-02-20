class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k : return 0
        avr = k * threshold
        curSum = sum(arr[:k])
        left = 0
        right = k-1
        res = 0
        if curSum >= avr: res+=1
        while right < len(arr)-1:
            right+=1
            curSum+=arr[right]
            curSum-=arr[left]
            left+=1
            if curSum >= avr : res+=1
        return res

            
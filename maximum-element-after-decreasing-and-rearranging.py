class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(len(arr)):
            if i == 0:
                arr[0] = 1
            else:
                prev = arr[i-1]
                if arr[i] > prev + 1:
                    arr[i] = prev + 1
        return arr[-1]
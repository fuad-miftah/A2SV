class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) >= 3:
            cur = arr[0]
            if arr[0] >= arr[1]: return False
            j = 0
            while j < len(arr) - 1 and arr[j+1] > cur:
                j += 1
                cur = arr[j]
            
            if j != len(arr)-1:
                if arr[j] == arr[j+1]: return False
                cur = arr[j+1]
                for k in range(j+2,len(arr)):
                    if arr[k] >= cur:
                        return False
                    cur = arr[k]
                return True
        return False
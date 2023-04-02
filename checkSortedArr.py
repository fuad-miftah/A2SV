class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        if n == 1:
            return True
        l = 0
        r = 1
        while r < n:
            if arr[l] <= arr[r]:
                l+=1
                r+=1
            else:
                return False
        return True
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        l = 0
        if len(arr) == 1 : return 1
        prev = ""
        if arr[1] > arr[0]:
            prev = ">"
            res = 2
        elif arr[1] < arr[0]:
            prev = "<"
            res = 2
        else:
            prev = "="
            l = 1
        for r in range(2,len(arr)):
            if prev == ">":
                if arr[r] > arr[r-1]:
                    l = r - 1
                elif arr[r] == arr[r-1]:
                    prev = "="
                    l = r
                else:
                    prev = "<"
            elif prev == "<":
                if arr[r] < arr[r-1]:
                    l = r - 1
                elif arr[r] == arr[r-1]:
                    prev = "="
                    l = r
                else:
                    prev = ">"
            else:
                if arr[r] < arr[r-1]:
                    prev = "<"
                elif arr[r] > arr[r-1]:
                    prev = ">"
                else:
                    l = r
            res = max(res, r-l+1)
            
        return res
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        for a,b in costs:
            arr.append((b-a,a,b))
        arr = sorted(arr, reverse = True)
        res = 0
        for i in range(len(arr)//2):
            res += arr[i][1]
        for i in range(len(arr)//2,len(arr)):
            res += arr[i][2]
        return res
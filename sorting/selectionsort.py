class Solution: 
    def select(self, arr, i):
        min = arr[i]
        for j in range(i, len(arr)):
            if min > arr[j]:
                arr[j] , min = min , arr[j]
                
        return min


    def selectionSort(self, arr, n):
        sortedArr = []
        for i in range(n):
            selected = self.select(arr, i)
            arr[i] = selected


arr = [4 , 1, 3, 9, 7]
sol = Solution()
sol.selectionSort(arr, 5)
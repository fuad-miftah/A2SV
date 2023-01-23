class Solution: 
    def select(self, arr, i):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
                
        return min


    def selectionSort(self, arr, n):
        
        for i in range(n):
            selected = self.select(arr, i)
            if i != selected:
                arr[i], arr[selected] = arr[selected], arr[i]
        print(arr)

arr = [4 , 1, 3, 9, 7]
sol = Solution()
sol.selectionSort(arr, 5)
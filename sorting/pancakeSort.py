class Solution(object):
    def pancakeSort(self, arr)
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sortedArr = sorted(arr)
        sortedby = []
        while arr != sortedArr:
            
            mini = min(arr)
            print(mini)
            sortedby.append(index(mini))
            sliced = arr[:index(mini):-1]
            print(sliced)
            notSliced = arr[index(mini):]
            print(notSliced)
            arr = sliced + notSliced
            print(arr)
        print(sortedby)
        return sortedby

        




arr = [3,2,4,1]
sol = Solution()
sol.pancakeSort(arr)
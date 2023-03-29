class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        x = len(arr)
        output = []
        for i in range(x):
            max_ = max(arr[:x-i])
            indMax = arr.index(max_) + 1
            arr[:indMax] = reversed(arr[:indMax])
            output.append(indMax)

            arr[:x-i] = reversed(arr[:x-i])
            output.append(x-i)
        return output
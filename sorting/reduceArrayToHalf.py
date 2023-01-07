import collections
import math
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counts = collections.Counter(arr)
        result = sorted(arr, key=lambda x: (counts[x], x), reverse=True)
        half = int(math.ceil(len(arr) / 2)) 
        result = result[:half]
        result = list(set(result))
            
        return len(result)

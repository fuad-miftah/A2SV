class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l+r)//2
            count = 0
            csum = 0

            for i in range(len(weights)):
                csum+=weights[i]
                if csum > mid:
                    count+=1
                    csum = weights[i]
            if csum > 0:
                count+=1

            if count > days:
                l = mid + 1
            else:
                r = mid - 1
        return r+1
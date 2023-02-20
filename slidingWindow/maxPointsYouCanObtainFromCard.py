class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = len(cardPoints) - k
        totalSum = sum(cardPoints)
        windowSum = sum(cardPoints[:window])
        left = 0
        res = totalSum - windowSum
        for right in range(window, len(cardPoints)):
            windowSum+=cardPoints[right]
            windowSum-=cardPoints[left]
            res = max(res, totalSum - windowSum)
            left+=1
        return res


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for stone in stones:
            temp = set()
            for i in dp:
                temp.add(abs(i + stone))
                temp.add(abs(i - stone))
            dp = temp
        return min(dp) if len(dp) > 0 else 0
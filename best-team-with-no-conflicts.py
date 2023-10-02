class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = []
        arr = []
        for i in range(len(scores)):
            arr.append((ages[i],scores[i]))
        arr.sort()
        for i in range(len(scores)):
            maxi = arr[i][1]
            for j in range(i-1,-1,-1):
                if arr[j][1] <= arr[i][1]:
                    maxi = max(maxi, arr[i][1] + dp[j])
            dp.append(maxi)
        return max(dp)
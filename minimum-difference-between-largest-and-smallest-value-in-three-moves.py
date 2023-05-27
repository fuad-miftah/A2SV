class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        ans = []
        temp = nums[::]
        i = 0
        while i < 3:
            maxi = max(temp)
            temp.remove(maxi)
            i += 1
        ans.append(max(temp) - min(temp))

        temp = nums[::]
        i = 0
        while i < 3:
            mini = min(temp)
            temp.remove(mini)
            i += 1
        ans.append(max(temp) - min(temp))

        temp = nums[::]
        mini1 = min(temp)
        temp.remove(mini1)
        mini2 = min(temp)
        temp.remove(mini2)
        maxi = max(temp)
        temp.remove(maxi)
        ans.append(max(temp) - min(temp))

        temp = nums[::]
        maxi1 = max(temp)
        temp.remove(maxi1)
        maxi2 = max(temp)
        temp.remove(maxi2)
        mini = min(temp)
        temp.remove(mini)
        ans.append(max(temp) - min(temp))

        return min(ans)
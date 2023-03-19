class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        prevSmall = [-1]*N
        nextSmall = [N]*N
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                nextSmall[stack.pop()] = i
            if stack and arr[stack[-1]] <= arr[i]:
                prevSmall[i] = stack[-1]
            stack.append(i)
        res = 0

        for i in range(N):
            n = nextSmall[i] - i - 1
            m = i - prevSmall[i] - 1
            res+=((n+1) * (m+1)) * arr[i]
        return res % (10**9 + 7)
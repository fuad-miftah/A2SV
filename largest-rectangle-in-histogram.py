class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        leftMin = [-1]*N
        rightMin = [N]*N
        stack = []
        for i in range(N):
            while stack and heights[stack[-1]] > heights[i]:
                rightMin[stack.pop()] = i
            if stack:
                leftMin[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(N):
            w = rightMin[i]-leftMin[i]-1
            h = heights[i]
            res = max(res, w * h)
        return res
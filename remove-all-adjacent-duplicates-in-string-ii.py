class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                if stack[-1][1] + 1 == k:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([s[i],1])
        res = ""
        for ch, count in stack:
            for i in range(count):
                res += ch
        return res
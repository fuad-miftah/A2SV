class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        for i in range(len(s)):
            count[s[i]]-=1
            while stack and stack[-1] > s[i] and count[stack[-1]] > 0 and s[i] not in stack:
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
        res = ""
        for i in stack:
            res+=i
        return res
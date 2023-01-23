class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        if size == k: return '0'
        stack = []
        for n in num:
            while stack and k and stack[-1] > int(n):
                stack.pop()
                k -= 1
            if len(stack) == 1 and stack[-1] == 0:
                stack.pop()
            stack.append(int(n))
        while k and stack:
            stack.pop()
            k -= 1
        return ''.join(map(str,stack))  if stack else "0"



num = "1432219"
sol = Solution()
print(sol.maxOperations(num,3))
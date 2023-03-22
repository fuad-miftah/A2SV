class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
    
        for i in range(len(s)):
        
            if s[i] == "(":
                stack.append(s[i])
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    temp = 0
                    while stack and stack[-1] != "(":
                        temp+=2*(stack.pop())
                    if stack:
                        stack.pop()
                    stack.append(temp)
        ans = 0
        while stack:
            ans+=stack.pop()
        return ans
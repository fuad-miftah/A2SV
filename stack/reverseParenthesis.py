class Solution:
    def reverseParenthesis(self , s):
        stack = []
        top = -1
        string = ''
        for i in range(len(s)):
  
            if s[i] == ')':
                current = stack[top]
                while current != '(':
                    string += stack.pop()
                    top -= 1
                    current = stack[top]
                if current == '(' and i != len(s) - 1:
                    stack.pop()
                    top -= 1
                if i == len(s) - 1:
                    for j in range(len(stack)-1,1,-1):
                        string += stack[j]
                    return string
                else:
                    for j in string:
                        stack.append(j)
                        top += 1
                    string = ''
                    
            else:
                stack.append(s[i])
                top += 1
        

s = "(u(love)i)"
s = "(abcd)"
s = "(ed(et(oc))el)"
"a(bcdefghijkl(mno)p)q"
sol = Solution()
print(sol.reverseParenthesis(s))
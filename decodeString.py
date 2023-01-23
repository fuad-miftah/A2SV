class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        def decoder(n,s):
            if stack[n] == '[':
                return s
            popped = stack.pop(n)
            s = s + popped[::-1]

            return decoder(n-1,s)
        
        for word in s:
            if word != ']':
                if word.isdigit():
                    num = word
                    while stack!= [] and stack[-1].isdigit():
                        num = stack.pop() + num
                    stack.append(num)

                else:
                    stack.append(word)
            
            else:
                s = decoder(len(stack) - 1,'')
                s = s[::-1]
                stack.pop()
                multi = int(stack.pop())
                for i in range(multi):
                    stack.append(s)
        
        res = ''.join(stack)
        #print(res)
        return res
        

s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "3[acb]"
s = "100[leetcode]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
#"zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
sol = Solution()
sol.decodeString(s)
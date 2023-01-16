class Solution(object):
    def maxOperations(self, num, k):
        stack = []
        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        stack = stack[:len(num)-k]
        res = ''.join(stack)

        if res == str(int(res)):
            return res
        else:
            return "0"

        #return str(int(res)) if res else "0"




num = "1432219"
sol = Solution()
print(sol.maxOperations(num,3))
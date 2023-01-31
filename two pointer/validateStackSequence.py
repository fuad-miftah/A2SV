class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        N = len(popped)
        j = 0
        for i in pushed:
            stack.append(i)
            while stack and j < N and stack[-1] == popped[j]:
                j+=1
                stack.pop()
        print(stack == [])
        return stack == []
pushed = [1,2,3,4,5]  
popped = [4,5,3,2,1]
sol = Solution()
sol.validateStackSequences(pushed,popped)
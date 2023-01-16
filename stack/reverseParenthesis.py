class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        lastWord = []
        stack = []
        output = ''
        for i in range(len(s)):
            if s[i] != ')':
                lastWord.append(s[i])
            else:
                while lastWord[len(lastWord)-1] != '(':
                    stack.append(lastWord.pop())
                lastWord.pop()
                for i in stack:
                    lastWord.append(i)
                stack = []
        for i in lastWord:
            output += i
        return output
            
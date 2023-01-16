class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        result = 0
        for i in tokens: 
            if i == '+' or i == '-' or i == '*' or i == '/':
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if i == '+':
                    result = op1 + op2
                    stack.append(result)
                elif i == '-':
                    result = op1 - op2
                    stack.append(result)
                elif i == '*':
                    result = op1 * op2
                    stack.append(result)
                else:
                    if op1 * op2 > 0:
                        result = int(op1 / op2)
                    else:
                        result = (op1 +(-op1 % op2)) // op2
                    stack.append(result)
            else:
                stack.append(i)
        if stack == []:
            return result
        else:
            return int(stack[0])
        
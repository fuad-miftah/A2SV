class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        top = -1
        temp = []
        isValid = True
       
        for i in s:
            if i == '(' or i == '[' or i == '{':
                temp.append(i)
                top += 1
            else:
                if temp != []:
                    if i == ')':
                        if temp[top] == '(':
                            temp.pop()
                            top -= 1
                        else:
                            isValid = False
                            break
                    if i == ']':
                        if temp[top] == '[':
                            temp.pop()
                            top -= 1
                        else:
                            isValid = False
                            break
                    if i == '}':
                        if temp[top] == '{':
                            temp.pop()
                            top -= 1
                        else:
                            isValid = False
                            break
                else:
                    isValid = False
                    break
        if isValid == True and top == -1:
            return True
        else:
            return False
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.topp = -1
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.topp += 1
        return None
        

    def pop(self):
        """
        :rtype: None
        """
        self.topp -= 1
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.topp]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
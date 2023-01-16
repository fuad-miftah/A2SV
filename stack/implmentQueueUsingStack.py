class MyQueue(object):
    #addStack = []
    #top = -1

    def __init__(self):
        self.addStack = []
        self.top = -1
        self.x = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.addStack.append(x)
        self.top += 1
        return None
        

    def pop(self):
        """
        :rtype: int
        """
        
        element = self.addStack.pop(0)
        self.top -=1
        return element
         
        

    def peek(self):
        """
        :rtype: int
        """
        return self.addStack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.top == -1:
            return True
        else:
            return False
        
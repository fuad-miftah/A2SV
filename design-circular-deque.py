class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.deque = []
        self.k = k
        self.front = -1
        self.rear = -1
        self.contain = 0
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.contain == 0:
            self.deque.append(value)
            self.front+=1
            self.rear+=1
            self.contain+=1
        elif self.contain != self.k:
            self.deque.insert(0,value)
            self.rear+=1
            self.contain+=1
        else:
            return False
        return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.contain == 0:
            self.deque.append(value)
            self.front+=1
            self.rear+=1
            self.contain+=1
        elif self.contain != self.k:
            self.deque.append(value)
            self.rear+=1
            self.contain+=1
        else:
            return False
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.contain == 0:
            return False
        else:
            self.deque.pop(0)
            self.rear-=1
            self.contain-=1
            return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.contain == 0:
            return False
        else:
            self.deque.pop()
            self.rear-=1
            self.contain-=1
            return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.contain != 0:
            return self.deque[0]
        else:
            return -1
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.contain != 0:
            return self.deque[self.rear]
        else:
            return -1
        
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.contain == 0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.contain == self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
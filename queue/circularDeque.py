class MyCircularDeque(object):
    def __init__(self, k):
        self.k = k
        self.front = -1
        self.rear = -1
        self.deque = []
        self.contain = 0

    def insertFront(self, value):
        if self.deque != []:
            if self.contain != self.k:
                

    


sol = MyCircularDeque(3)
print(sol.insertFront(1))

        
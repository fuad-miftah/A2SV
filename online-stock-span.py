class StockSpanner:

    def __init__(self):
        self.stack = []
        self.indx = -1
        

    def next(self, price: int) -> int:
        self.indx += 1
        count = 1
        lastr = -1
        while self.stack and self.stack[-1][0] <= price:
            lastr = self.stack[-1][1]
            self.stack.pop()
        if self.stack and lastr != -1:
            count = self.indx - self.stack[-1][1]
        elif self.stack == [] and lastr != -1:
            count = self.indx - (-1)
        self.stack.append([price,self.indx])

        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
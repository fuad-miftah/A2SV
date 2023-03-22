class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.queue = []
        self.check = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.check[num] += 1
        if len(self.queue) < self.k:
            return False
        else:
            if len(self.queue) > self.k:
                v = self.queue.pop(0)
                self.check[v] -= 1
                if self.check[v] == 0:
                    del self.check[v]
            if len(self.check) > 1 or self.value not in self.check:
                return False
            else:
                return True
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity 
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        val = self.dic.pop(key)
        self.dic[key] = val   
        return val  

    def put(self, key: int, value: int) -> None:
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if len(self.dic) == self.capacity:
                del self.dic[next(iter(self.dic))]         
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
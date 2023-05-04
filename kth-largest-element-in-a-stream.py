class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)
        self.nums = nlargest(self.k,self.nums)
        heapify(self.nums)
        
    def add(self, val: int) -> int:
        if self.nums and len(self.nums) >= self.k:
            if val > self.nums[0]:
                heappop(self.nums)
                heappush(self.nums, val)
                return self.nums[0]
            return self.nums[0]
        else:
            heappush(self.nums,val)
            return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
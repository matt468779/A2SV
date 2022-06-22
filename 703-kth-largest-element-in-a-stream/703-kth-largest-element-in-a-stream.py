class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        self.nums, self.k = [], k
        i = 0
        l = len(nums)
        while i < k and i < l:
            heapq.heappush(self.nums, -heapq.heappop(nums))
            i += 1
            
    def add(self, val: int) -> int:
        if len(self.nums) >= self.k:
            heapq.heappushpop(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
        return self.nums[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
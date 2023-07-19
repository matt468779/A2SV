class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, heapq.heappop(nums)+1)
        
        mod = 10**9 + 7
        res = 1
        for num in nums:
            res = (res * num) % mod
        
        return res
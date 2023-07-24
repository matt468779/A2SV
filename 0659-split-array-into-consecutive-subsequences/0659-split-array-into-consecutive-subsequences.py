class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        last_num = defaultdict(list)
        for num in nums:
            if last_num[num-1]:
                heapq.heappush(last_num[num], heapq.heappop(last_num[num-1]) + 1)
            else:
                heapq.heappush(last_num[num], 1)
        
        for num in last_num:
            for length in last_num[num]:
                if length < 3:
                    return False
        
        return True
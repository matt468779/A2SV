class Solution:
    def findScore(self, nums: List[int]) -> int:
        hp = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(hp)
        marked = set()
        score = 0
        while hp:
            val, idx = heapq.heappop(hp)
            if idx not in marked:
                score += val
                marked.add(idx+1)
                marked.add(idx-1)
        
        return score
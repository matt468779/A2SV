class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = []
        for i in range(len(mat)):
            heapq.heappush(strength, (sum(mat[i]), i))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(strength)[1])
        
        return res
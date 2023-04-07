class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:            
        hp1 = costs[:candidates]
        secondHalf = max(len(costs)-candidates, candidates)
        hp2 = costs[secondHalf:]
        heapq.heapify(hp1)
        heapq.heapify(hp2)
        idx1 = candidates
        idx2 = secondHalf-1
        res = 0
        for i in range(k):
            if (hp1 and not hp2) or (hp1 and hp2 and hp1[0] <= hp2[0]):
                res += heapq.heappop(hp1)
                if idx1 <= idx2:
                    heapq.heappush(hp1, costs[idx1])
                    idx1 += 1
            else:
                res += heapq.heappop(hp2)
                if idx1 <= idx2:
                    heapq.heappush(hp2, costs[idx2])
                    idx2 -= 1
        
        return res
                
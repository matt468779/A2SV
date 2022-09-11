class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        effSpe = list(zip(efficiency, speed))
        effSpe.sort(reverse=True)
        
        sumSpe, perf = 0, 0
        minSpe = []
        for i in range(n):
            if i < k:
                heapq.heappush(minSpe, effSpe[i][1])
                sumSpe += effSpe[i][1]
            else:
                pop = heapq.heappushpop(minSpe, effSpe[i][1])
                sumSpe += effSpe[i][1] - pop
            perf = max(perf, sumSpe*effSpe[i][0])

        return perf % 1000000007
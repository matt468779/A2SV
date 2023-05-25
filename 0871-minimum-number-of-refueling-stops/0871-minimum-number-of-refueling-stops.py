class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        hp = []
        distance = startFuel
        res = 0
        for station in stations:
            while hp and distance < station[0]:
                distance -= heapq.heappop(hp)
                res += 1
                
            if distance < station[0]:
                return -1
            
            heapq.heappush(hp, -station[1])
            
        while hp and distance < target:
            distance -= heapq.heappop(hp)
            res += 1
        
        return res if distance >= target else -1
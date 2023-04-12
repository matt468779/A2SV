class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        passengers = 0
        hp = []
        for i in range(len(trips)):
            while hp and hp[0][0] <= trips[i][1]:
                passengers -= heapq.heappop(hp)[1]
                
            passengers += trips[i][0]
            heapq.heappush(hp, (trips[i][2], trips[i][0]))
            
            if passengers > capacity:
                return False
        
        return True
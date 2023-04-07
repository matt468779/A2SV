class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hp = []
        i = 1
        while i < len(heights):
            diff = heights[i] - heights[i-1]
            if diff <= 0:
                i += 1
                continue
            
            if diff <= bricks:
                bricks -= diff
                heapq.heappush(hp, -diff)
                i += 1
            elif ladders:
                if hp:
                    long_so_far = -hp[0]
                else:
                    long_so_far = 0
                    
                if long_so_far > diff:
                    heapq.heappop(hp)
                    bricks += long_so_far
                else:
                    i += 1
                ladders -= 1
            else:
                break
                
        return i-1
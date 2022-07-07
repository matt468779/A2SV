class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        i = 0
        while i < len(heights)-1:
            if heights[i+1] - heights[i] <= 0:
                i += 1
                continue

            if bricks >= heights[i+1] - heights[i]:
                heapq.heappush(heap, heights[i]-heights[i+1])
                bricks -= heights[i+1]-heights[i]
                i += 1

            elif ladders > 0:
                ladders -= 1
                if len(heap) == 0 or heights[i+1] - heights[i] >= -heap[0]:
                    i += 1
                else:
                    bricks -= heapq.heappop(heap)
            else:
                break
        return i

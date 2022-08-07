class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo = 1
        hi = min(time)*totalTrips
        while lo <= hi:
            mid = (lo+hi)//2
            s = 0
            for t in time:
                s += mid//t
            if s < totalTrips:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi+1
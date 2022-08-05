class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        while lo < hi:
            mid = (lo+hi)//2
            s = 0
            daysTaken = 0
            for i in range(len(weights)):
                if s+weights[i] < mid:
                    s += weights[i]
                elif s+weights[i] > mid:
                    daysTaken += 1
                    s = weights[i]
                else:
                    daysTaken += 1
                    s = 0
            if s > 0:
                daysTaken += 1

            if daysTaken <= days:
                hi = mid
            else:
                lo = mid+1
            
        return hi
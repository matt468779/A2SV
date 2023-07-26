class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def time_taken(speed):
            if speed == 0:
                return float('inf')
            
            time = 0
            for i in range(len(dist)-1):
                time += ceil(dist[i]/speed)
            
            return time + dist[-1]/speed
                
        l = 1
        r = 10**7
        while l <= r:
            mid = (l+r)//2
            time = time_taken(mid)    
            
            if time > hour:
                l = mid+1
            else:
                r = mid-1
        
        if time_taken(l) > hour:
            return -1
        return l
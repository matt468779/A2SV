class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rg = sorted([[i - r, i + r] for i, r in enumerate(ranges)])
        ans = start = end = i = 0
        while start < n:
            while i <= n and rg[i][0] <= start:
                end = max(end, rg[i][1])
                i += 1   
                
            if start == end:
                return -1
            
            start = end
            ans += 1
            
        return ans
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        def bin_search(l, key):
            r = len(events) - 1
            while l <= r:
                mid = (l+r)//2
                if events[mid][0] >= key:
                    r = mid-1
                else:
                    l = mid+1
            
            return l
        
        dp = {}
        def solve(i, count):
            if count >= k or i >= len(events):
                return 0
            
            state = (i, count)
            if state in dp:
                return dp[state]
            
            choose = events[i][2] + solve(bin_search(i+1, events[i][1]+1), count + 1)
            no_choose = solve(i+1, count)
            dp[state] = max(choose, no_choose)
            return dp[state]
        
        return solve(0, 0)
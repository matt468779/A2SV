class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def solve(i, coveredDays):
            state = (i, coveredDays)
            if state in dp:
                return dp[state]
            
            if i >= len(days):
                return 0
            if days[i] <= coveredDays:
                return solve(i+1, coveredDays)
            
            res = float('inf')
            costTicket1 = costs[0] + solve(i+1, days[i])
            costTicket2 = costs[1] + solve(i+1, days[i]+6)
            costTicket3 = costs[2] + solve(i+1, days[i]+29)
            
            dp[state] = min(costTicket1, costTicket2, costTicket3)
            return dp[state]
        
        return solve(0, 0)
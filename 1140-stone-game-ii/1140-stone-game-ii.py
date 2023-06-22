class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        pre_sum = [0] * (len(piles)+1)
        for i in range(len(piles)):
            pre_sum[i+1] = piles[i] + pre_sum[i]
            
        dp = {}
        def solve(i, m):
            if i + 2*m >= len(piles):
                return pre_sum[-1] - pre_sum[i]
            if (i,m) in dp:
                return dp[(i,m)]
            
            res = float('-inf')
            for j in range(i, min(i+2*m, len(piles))):
                res = max(res, pre_sum[j+1] - pre_sum[i] + pre_sum[-1] - pre_sum[j+1] - solve(j+1, max(m, j-i+1)))
            
            dp[(i,m)] = res
            return dp[(i,m)]
        
        return solve(0, 1)
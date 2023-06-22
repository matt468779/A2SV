class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        pre_sum = [0] * (len(piles)+1)
        for i in range(len(piles)):
            pre_sum[i+1] = piles[i] + pre_sum[i]
            
        def solve(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            left = piles[i] + pre_sum[j+1] - pre_sum[i+1] - solve(i+1, j)
            right = piles[j] + pre_sum[j] - pre_sum[i] - solve(i, j-1)
            
            dp[(i, j)] = max(left, right)
            return dp[(i, j)]
        
        alice = solve(0, len(piles)-1)
        return True if alice > pre_sum[len(piles)] / 2 else False
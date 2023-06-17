class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        dp = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        dp[0] = list(grid[0])
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                for k in range(len(grid[0])):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + moveCost[grid[i-1][k]][j])
                dp[i][j] += grid[i][j]
                
        return min(dp[-1])
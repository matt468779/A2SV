class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[-1][-1] = int(not obstacleGrid[-1][-1])
        
        def getValue(i, j):
            if i < m and j < n:
                return dp[i][j]
            return 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] += getValue(i+1, j) + getValue(i, j+1)
                    
        return dp[0][0]
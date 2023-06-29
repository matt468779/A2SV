class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = [0, 0]

        def solve(i, j, is_top):
            if j < 0 or j >= len(grid[0]):
                return -1
            if i >= len(grid):
                return j
            if dp[i][j][is_top] != 0:
                return dp[i][j]
            
            res = 0
            if is_top:
                
                if j+1 < len(grid[0]) and grid[i][j] == 1 and grid[i][j+1] == -1:
                    res = -1
                elif j-1 >= 0 and grid[i][j] == -1 and grid[i][j-1] == 1:
                    res = -1
                
                elif grid[i][j] == 1:
                    res = solve(i, j+1, False)
                else:
                    res = solve(i, j-1, False)

            else:
                res = solve(i+1, j, True)
                
            dp[i][j][is_top] = res
            return res
        
        res = [0] * len(grid[0])
        
        for i in range(len(grid[0])):
            res[i] = solve(0, i, True)
        
        return res
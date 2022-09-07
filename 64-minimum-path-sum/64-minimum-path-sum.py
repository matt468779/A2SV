class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def traverse(i, j):
            if self.dp[i][j] != -1:
                return self.dp[i][j]
            self.dp[i][j] = grid[i][j] + min(traverse(i+1, j), traverse(i, j+1))
            return self.dp[i][j]
        
        self.dp = []
        for i in range(len(grid)):
            self.dp.append([-1]*len(grid[0]))
            
        self.dp[-1][-1] = grid[-1][-1]
        for i in range(len(grid)-2, -1, -1):
            self.dp[i][-1] = grid[i][-1] + self.dp[i+1][-1]
        
        for i in range(len(grid[0])-2, -1, -1):
            self.dp[-1][i] = grid[-1][i] + self.dp[-1][i+1]
        
        return traverse(0, 0)
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                grid[row][col] = 0
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row, col+1)
                
        for i in range(len(grid)):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][-1] == 1:
                dfs(i, len(grid[0])-1)
        
        for i in range(1, len(grid[0])-1):
            if grid[0][i] == 1:
                dfs(0, i)
            if grid[-1][i] == 1:
                dfs(len(grid)-1, i)
                
        count = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 1:
                    count += 1
        
        return count
                
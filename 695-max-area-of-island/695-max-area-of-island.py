class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.area = 0
        self.maxArea = 0
        def calculateArea(row: int, col: int):
            if row >= 0 and row < len(self.grid) and col >= 0 and col < len(self.grid[0]) and self.grid[row][col]:
                self.area += 1
                self.grid[row][col] = 0
                calculateArea(row+1, col)
                calculateArea(row, col+1)
                calculateArea(row-1, col)
                calculateArea(row, col-1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j]:
                    calculateArea(i, j)
                    self.maxArea = max(self.maxArea, self.area)
                    self.area = 0
        
        return self.maxArea
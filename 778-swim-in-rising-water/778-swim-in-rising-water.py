class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.reached = []
        for i in range(len(grid)):
            self.reached.append([])
            for j in range(len(grid)):
                self.reached[-1].append([float('inf'), False])
        self.reached[0][0][0] = 0

        def visit(row, col, elev):
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid) and not self.reached[row][col][1]:
                if self.reached[row][col][0] == float('inf') and elev >= grid[row][col]:
                    self.reached[row][col][0] = elev
                elif self.reached[row][col][0] == float('inf') and elev < grid[row][col]:
                    self.reached[row][col][0] = grid[row][col]
                elif self.reached[row][col][0] != float('inf') and elev > grid[row][col]:
                    self.reached[row][col][0] = min(elev, self.reached[row][col][0])
                heapq.heappush(self.q, (self.reached[row][col][0], row, col))

        self.q = [(grid[0][0],0,0)]
        while self.q and not self.reached[len(grid)-1][len(grid)-1][1]:
            p = heapq.heappop(self.q)
            if not self.reached[p[1]][p[2]][1]:
                visit(p[1]+1, p[2], p[0])
                visit(p[1], p[2]+1, p[0])
                visit(p[1], p[2]-1, p[0])
                visit(p[1]-1, p[2], p[0])

                self.reached[p[1]][p[2]][1] = True
            
        return self.reached[len(grid)-1][len(grid)-1][0]
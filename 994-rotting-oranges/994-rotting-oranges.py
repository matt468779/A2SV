class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = 0
        self.q  = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.q.append((i, j))
                    oranges += 1
                elif grid[i][j] == 1:
                    oranges += 1
        
        self.rotten = len(self.q)
        if oranges == self.rotten:
            return 0
        
        def rot(row, col):
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                self.q.append((row, col))
                self.rotten += 1
                grid[row][col] = 2
    
        minutes = -1
        res = 0
        while self.q:
            l = len(self.q)
            for _ in range(l):
                p = self.q.popleft()
                rot(p[0]+1, p[1])
                rot(p[0]-1, p[1])
                rot(p[0], p[1]+1)
                rot(p[0], p[1]-1)
            minutes += 1
        
        if oranges == self.rotten:
            return minutes
        return -1
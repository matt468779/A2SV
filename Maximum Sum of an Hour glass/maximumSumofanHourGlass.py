class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hourglass = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                s = 0
                for k in range(3):
                    for l in range(3):
                        s += grid[i+k][j+l]*hourglass[k][l]
                
                res = max(res, s)

        return res

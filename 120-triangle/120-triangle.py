class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def traverse(i, j, dist):
            if self.dp[i][j] != 'x':
                return self.dp[i][j]
            self.dp[i][j] = triangle[i][j] + min(traverse(i+1, j, dist+triangle[i][j]), traverse(i+1, j+1, dist+triangle[i][j]))
            return self.dp[i][j]
        
        self.dp = []
        for i in range(len(triangle)):
            self.dp.append([])
            for j in range(i+1):
                self.dp[-1].append('x')
        self.dp[-1] = triangle[-1]
    
        return traverse(0, 0, triangle[0][0])
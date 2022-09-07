class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
#         def traverse(i, j, dist):
#             if self.dp[i][j] != 'x':
#                 return self.dp[i][j]
#             self.dp[i][j] = triangle[i][j] + min(traverse(i+1, j, dist+triangle[i][j]), traverse(i+1, j+1, dist+triangle[i][j]))
#             return self.dp[i][j]
        
#         self.dp = []
#         for i in range(len(triangle)):
#             self.dp.append([])
#             for j in range(i+1):
#                 self.dp[-1].append('x')
#         self.dp[-1] = triangle[-1]
    
#         return traverse(0, 0, triangle[0][0])
    
        dp = [triangle[0][0]] * len(triangle)
        for i in range(1, len(triangle)):
            triangle[i][i] += triangle[i-1][i-1]
            triangle[i][0] += triangle[i-1][0]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        
        return min(triangle[-1])
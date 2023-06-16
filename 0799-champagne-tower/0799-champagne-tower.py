class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #bottom up approach
        m,n = query_row, query_glass
        dp = [[0 for _ in range(i+1)] for i in range(m+1)] #choose the DS for the answer
        
        dp[0][0]= poured
        for i in range(1,m+1):
            for j in range(i+1):
                if j<len(dp[i-1]) and dp[i-1][j]>1:
                    dp[i][j] += (dp[i-1][j] -1)/2   
                  
                if j-1>=0 and dp[i-1][j-1]>1:
                    dp[i][j] +=(dp[i-1][j-1]-1)/2
               
        return dp[m][n] if dp[m][n]<=1 else 1
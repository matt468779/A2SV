class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * (n+2) for _ in range(n+2)]
        for query in queries:
            mat[query[0]+1][query[1]+1] += 1
            mat[query[0]+1][query[3]+2] -= 1
            mat[query[2]+2][query[1]+1] -= 1
            mat[query[2]+2][query[3]+2] += 1
        
        res = [[0] * (n) for _ in range(n)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                mat[i][j] = mat[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
                res[i-1][j-1] = mat[i][j]
                
        return res
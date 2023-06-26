class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns = set()
        rows = set()
        r, c = len(matrix), len(matrix[0])
        def set_row(row):
            for i in range(c):
                matrix[row][i] = 0
        
        def set_column(col):
            for i in range(r):
                matrix[i][col] = 0
                
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    columns.add(j)
                    rows.add(i)
        
        for row in rows:
            set_row(row)
        
        for col in columns:
            set_column(col)
        
    
                
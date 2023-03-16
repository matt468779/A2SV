class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        col = set()
        left_diag = set()
        right_diag = set()
        def solve(row):
            if row == n:
                res.append([''.join(board[i][:]) for i in range(n)])
                return

            for i in range(n):
                if i not in col and row+i not in left_diag and row-i not in right_diag:
                    col.add(i)
                    left_diag.add(row + i)
                    right_diag.add(row - i)                    
                    board[row][i] = 'Q'
                    solve(row+1)
                    board[row][i] = '.'
                    col.remove(i)
                    left_diag.remove(row + i)
                    right_diag.remove(row - i)  
        
        solve(0)
        return res
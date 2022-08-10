class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def connected(row: int, col: int):
            if row >= 0 and col >= 0 and row < len(board) and col < len(board[0]) and board[row][col] == 'O':
                board[row][col] = 'A'
                connected(row-1, col)
                connected(row+1, col)
                connected(row, col-1)
                connected(row, col+1)
                
        for i in range(len(board)):
            if board[i][0] == 'O':
                connected(i, 0)
            if board[i][-1] == 'O':
                connected(i, len(board[0])-1)
        
        for i in range(1, len(board[0])-1):
            if board[0][i] == 'O':
                connected(0, i)
            if board[-1][i] == 'O':
                connected(len(board)-1, i)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
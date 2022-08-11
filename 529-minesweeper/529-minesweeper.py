class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def update(row, col):
            if inBound(row, col) and board[row][col] == 'E':
                adjMines = checkAdjacent(row, col)
                if adjMines > 0:
                    board[row][col] = str(adjMines)
                else:
                    board[row][col] = 'B'
                    update(row+1, col)
                    update(row-1, col)
                    update(row, col+1)
                    update(row, col-1)
                    update(row+1, col+1)
                    update(row+1, col-1)
                    update(row-1, col+1)
                    update(row-1, col-1)
                    
        def checkAdjacent(row, col):
            count = 0
            if inBound(row+1, col) and board[row+1][col] == 'M':
                count += 1
            if inBound(row-1, col) and board[row-1][col] == 'M':
                count += 1
            if inBound(row, col-1) and board[row][col-1] == 'M':
                count += 1
            if inBound(row, col+1) and board[row][col+1] == 'M':
                count += 1
            if inBound(row+1, col+1) and board[row+1][col+1] == 'M':
                count += 1
            if inBound(row+1, col-1) and board[row+1][col-1] == 'M':
                count += 1
            if inBound(row-1, col+1) and board[row-1][col+1] == 'M':
                count += 1
            if inBound(row-1, col-1) and board[row-1][col-1] == 'M':
                count += 1
            return count
                
        def inBound(row, col):
            return row >= 0 and col >= 0 and row < len(board) and col < len(board[0])
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            update(click[0], click[1])
        return board
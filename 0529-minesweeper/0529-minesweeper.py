class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        adj_direction = [(1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
        def adjacent_mines(clickR, clickC):
            res = 0
            for x, y in adj_direction:
                if 0 <= x+clickR < rows and 0 <= y+clickC < cols and board[x+clickR][y+clickC] == 'M':
                    res += 1
                    
            return res
        
        def solve(clickR, clickC):
            if not(0 <= clickR < rows and 0 <= clickC < cols) or board[clickR][clickC] != 'E' :
                return
            no_adj_mines = adjacent_mines(clickR, clickC)
            if no_adj_mines == 0:
                board[clickR][clickC] = 'B'
                for x, y in adj_direction:
                    if 0 <= x+clickR < rows and 0 <= y+clickC <= cols:
                        solve(x+clickR, y+clickC)
            else:
                board[clickR][clickC] = str(no_adj_mines)
                
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            solve(click[0], click[1])
            
        return board
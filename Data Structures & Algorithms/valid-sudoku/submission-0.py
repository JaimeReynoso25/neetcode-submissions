class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # validates rows
        for row in board:
            rowSet = set()
            for col in row:
                if col.isnumeric():
                    if col in rowSet:
                        return False
                    rowSet.add(col)
        
        # validates columns
        for row in range(9):
            colSet = set()
            for col in range(9):
                if board[col][row].isnumeric():
                    if board[col][row] in colSet:
                        return False
                    colSet.add(board[col][row])

        # validate squares
        def squareValidator(squareRow, squareCol):
            squareSet = set()
            for i in range(3):
                for j in range(3):
                    if board[i+squareRow][j+squareCol].isnumeric():
                        if board[i+squareRow][j+squareCol] in squareSet:
                            return False
                        squareSet.add(board[i+squareRow][j+squareCol])
            return True


        startRow = 0
        for row in range(3):
            startCol = 0
            for col in range(3):
                if squareValidator(startRow, startCol) == False:
                    return False
                startCol += 3
            startRow += 3
        
        return True

        

        






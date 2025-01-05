class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain 1-9, no repetition
        # Each column must contain 1-9, no repetition
        # Each of the 3x3 boxes must contain 1-9 without repetition
        rows,cols = len(board[0]), len(board)
        rowSet, colSet = set(), set()
        for row in range(9):
            rowSet = set()
            for col in range(9): # check rows
                if board[row][col] in rowSet and board[row][col] != ".":
                    return False
                else:
                    rowSet.add(board[row][col])                    

        for row in range(9):
            colSet = set()
            for col in range(9):  
                cur = board[col][row]
                if cur != ".":
                    if cur in colSet:
                        return False
                    colSet.add(cur)           

        # Check 3x3 board
        for row in range(0,9,3):
            for col in range(0,9,3):
                gridSet = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] in gridSet and board[r][c] != ".":
                            return False
                        else:
                            gridSet.add(board[r][c])   

        return True
              
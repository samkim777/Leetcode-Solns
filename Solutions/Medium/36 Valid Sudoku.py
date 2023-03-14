class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = r / 3, c / 3

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                    # Check if duplicate in col/row or 3x3 square
                if (board[r][c] in cols[c] or
                    board[r][c] in rows[r] or
                    # Check if key '1' has this board value, then '2'
                    board[r][c] in squares[(r//3,c//3)]): # Key at r/3,c/3
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True                



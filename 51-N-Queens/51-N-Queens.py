# Last updated: 5/22/2025, 6:26:09 PM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # When a queen is placed, all the horizontal, dialgonal, and vertical
        # grids cannot have a queen
        # so when we place a queen, we know which grids are not availiable
        # For example, placing a queen on the first row col in a 4x4,
        # our closest next queen is (2,1)
        # and once we have a queen here, then we again know which grids
        # are not avaliable
        # We can use backtracking to try all grids and form different
        # ways to place the queen on the board
        # Time complexity O(8^n*n^2) where n is size of board
        # Space complexity O(n)
        res = []
        cols = set()
        diagR = set()
        diagL = set()

        grid = [["." for _ in range(n)] for _ in range(n)]
        def backtrack(rows):
            # base case, we find board with non overlapping queens
            if rows == n:
                board = ["".join(r) for r in grid]
                res.append(board)
                return
            # Go through this column of this row
            for col in range(n):
                if col in cols or (rows+col) in diagR or (rows-col) in diagL:
                    # Cannot place queen here
                    continue
                # else we can place queen
                grid[rows][col] = "Q"
                cols.add(col)
                diagR.add(rows+col)
                diagL.add(rows-col)
                backtrack(rows+1)

                grid[rows][col] = "."
                cols.remove(col)
                diagR.remove(rows+col)
                diagL.remove(rows-col)
        backtrack(0)
        return res
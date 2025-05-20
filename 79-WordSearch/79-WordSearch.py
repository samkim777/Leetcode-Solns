# Last updated: 5/19/2025, 11:11:56 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def backtrack(r,c,i):
            # base case when we find the char
            if i == len(word):
                return True
            # base case for when if out of bounds or not correct char
            if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c]:
                return False
            # Mark the visited cells
            temp = board[r][c]
            board[r][c] = "X"
            res = backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1)
            board[r][c] = temp
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False
# Last updated: 5/15/2025, 11:32:27 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        if len(word) > rows * cols:
            return False

        def dfs(r,c,i):
            # base case
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c]:
                return False
            # To keep track of the grid that we visited, we mark it as X
            tmp = board[r][c]
            board[r][c] = "X"

            cur = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c] = tmp
            return cur
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False